import openai
import os
import json
import datetime

# ---- Load OpenAI API Key ----
with open("config.json", "r") as f:
    config = json.load(f)

openai.api_key = config["OPENAI_API_KEY"]

# ---- Folders ----
PROMPTS_DIR = "prompts_water_drone"          # where your .txt prompt files live
OUTPUT_ROOT = "LLM_Generated_Scripts"        # root folder for LLM-generated scripts
os.makedirs(OUTPUT_ROOT, exist_ok=True)


# ---- Extract Python Code Block ----
def extract_code_from_markdown(text: str) -> str:
    """
    Extracts the first Python code block from a markdown string.
    Falls back to the first ``` block, then to the raw text.
    """
    if "```python" in text:
        return text.split("```python", 1)[1].split("```", 1)[0].strip()
    elif "```" in text:
        return text.split("```", 1)[1].split("```", 1)[0].strip()
    return text.strip()


# ---- Discover Pre-Prepared Prompt Files ----
def discover_prompts():
    """
    Scan PROMPTS_DIR for .txt files and return a mapping:
    {
        "1": {"name": "Hydrone_prompt_basic", "path": "prompts_water_drone/Hydrone_prompt_basic.txt"},
        "2": {"name": "Some_other_prompt",   "path": "prompts_water_drone/Some_other_prompt.txt"},
        ...
    }
    """
    prompts = {}

    if not os.path.isdir(PROMPTS_DIR):
        return prompts

    txt_files = sorted(
        f for f in os.listdir(PROMPTS_DIR)
        if f.lower().endswith(".txt")
    )

    for idx, filename in enumerate(txt_files, start=1):
        name = os.path.splitext(filename)[0]
        path = os.path.join(PROMPTS_DIR, filename)
        prompts[str(idx)] = {"name": name, "path": path}

    return prompts


# ---- Generate Code from a Single Prompt File ----
def generate_from_prompt_file(prompt_info: dict):
    """
    Given a prompt info dict with keys 'name' and 'path',
    send its content to GPT and save the resulting code
    in a single shared folder, with a name derived from the prompt.
    """
    prompt_name = prompt_info["name"]
    prompt_path = prompt_info["path"]

    # Load prompt text
    try:
        with open(prompt_path, "r", encoding="utf-8") as f:
            prompt_text = f.read().strip()
    except Exception as e:
        print(f"❌ Could not read prompt file '{prompt_path}': {e}")
        return

    print(f"\n🧠 Generating response for prompt: {prompt_name}")

    try:
        response = openai.chat.completions.create(
            model="gpt-5",  # keep your model selection
            messages=[
                {
                    "role": "system",
                    "content": "You generate Python scripts to control a water drone via movement-based emotional scenarios."
                },
                {
                    "role": "user",
                    "content": prompt_text
                }
            ]
            # , temperature=0.4  # can be used for lower version models of GPT
        )

        content = response.choices[0].message.content
        code = extract_code_from_markdown(content)

        # ---- Build output filename based on prompt name ----
        base_name = prompt_name.strip()

        # Remove trailing "(prompt)" if present (case-insensitive)
        suffix = "(prompt)"
        if base_name.lower().endswith(suffix.lower()):
            base_name = base_name[:-len(suffix)].rstrip()

        # Replace characters that are invalid in Windows filenames
        invalid_chars = '<>:"/\\|?*'
        safe_base = "".join("_" if c in invalid_chars else c for c in base_name)

        output_filename = f"{safe_base} (LLM_Generated_Script).py"
        filepath = os.path.join(OUTPUT_ROOT, output_filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# Generated from prompt: {prompt_name}\n")
            f.write(f"# Source prompt file: {prompt_path}\n")
            f.write(f"# Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(code)

        print(f"✅ Saved to {filepath}")

    except Exception as e:
        print(f"❌ Error generating for prompt '{prompt_name}':\n{e}\n")


# ---- Main Menu Loop ----
def run_main_loop():
    while True:
        prompts = discover_prompts()
        if not prompts:
            print("There is no prompt in the prompt folder.")
            return

        # Sort keys numerically so order is stable
        prompt_keys = sorted(prompts.keys(), key=int)
        max_index = int(prompt_keys[-1])

        # "All" option will be max_index + 1
        all_choice = max_index + 1

        print("\n🎭 Pre-Prepared Prompt List")
        for key in prompt_keys:
            info = prompts[key]
            print(f"{key}. {info['name']}")

        print(f"{all_choice}. All prompts")
        print("0. Exit")

        choice_raw = input("\nEnter a number: ").strip()

        if not choice_raw.isdigit():
            print("❌ Invalid input. Please enter a number.")
            continue

        choice = int(choice_raw)

        if choice == 0:
            print("👋 Exiting.")
            break
        elif choice == all_choice:
            # Run all prompts
            selected_keys = prompt_keys
        else:
            key_str = str(choice)
            if key_str not in prompts:
                print("❌ Invalid number. Try again.")
                continue
            selected_keys = [key_str]

        # Run selected prompts one after the other
        for key in selected_keys:
            info = prompts[key]
            generate_from_prompt_file(info)


# ---- Run It ----
if __name__ == "__main__":
    run_main_loop()
