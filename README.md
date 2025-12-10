# Hydrone LLM Motion Scripts

## Description

This repository contains the code and prompt templates used to generate and run **LLM-driven motion scripts** for the Hydrone aquatic social robot. Instead of relying on pre-programmed schedules (PPS), we use a large language model (LLM, e.g., GPT) to generate Python control scripts that express the personality of well-known characters


1. **Offline stage:** A PC-side script sends structured prompts (robot constraints, character, user actions, example output format) to the LLM, and saves the generated motion scripts as Python files.
2. **Online stage:** An operator connects to the Hydrone over Wi-Fi, selects one of the saved scripts, and runs it on the robot to produce character-specific motion behaviour.

---

## Repository Structure

The core components are:

- `1_Generate_LLMscript_for_Hydrone.py`  
  CLI tool that:
  - Lists available prompt templates in `prompts_water_drone/`
  - Sends selected prompts to the OpenAI API
  - Extracts the generated Python code
  - Saves each result as a runnable motion script in `LLM_Generated_Scripts/`

- `Run_LLM_Scripts_on_Hydrone.py`  
  TCP client that:
  - Connects to the ESP32/M5 controller on the Hydrone via Wi-Fi
  - Lists available LLM-generated scripts in `LLM_Generated_Scripts/`
  - Lets the operator select a script by number
  - Executes the script, which calls `send_command(...)` to drive the robot

- `prompts_water_drone/`  
  Folder of **pre-prepared prompt files** (`.txt`).  
  Each file typically encodes:
  - Robot constraints (thrusters, pump, safety limits)
  - The target character (e.g., “Winnie the Pooh”, “Tigger”, “Eeyore”)
  - A description of user actions / scenario
  - Example output / function signatures expected in the generated Python code

  Filenames ending with **`(prompt)`** are treated specially when naming the generated scripts (see below).

- `LLM_Generated_Scripts/`  
  Folder where all **LLM-generated motion scripts** are stored as `.py` files.  
  The generator script:
  - Takes the prompt filename (without extension)
  - Removes a trailing `(prompt)` if present
  - Produces files named:

    ```text
    <PromptBaseName> (LLM_Generated_Script).py
    ```

  All generated scripts are kept flat in this single folder so the runner UI can easily list them.

- `config.example.json`  
  Template for your API configuration:

  ```json
  {
    "OPENAI_API_KEY": "YOUR_API_KEY_HERE"
  }
