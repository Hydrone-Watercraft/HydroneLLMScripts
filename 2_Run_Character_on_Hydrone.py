import os
import socket
import json
import time

# ---- Drone TCP Setup ----
HOST = "Copy_Drones_IP_Address_Here"     # Address of the TCP server on the microcontroller (ESP32/M5) on the watercraft
PORT = 5000         # Port for TCP communication
LEFT_CORRECTION = 1  # Factor to adjust left motor

# Connect to drone
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
print(f"✅ Connected to drone at {HOST}:{PORT}")

# ---- Drone Control Functions ----
def send_command(left, right, pump=0, duration=1.0, stop_after=True):
    corrected_left = int(left * LEFT_CORRECTION)
    corrected_right = int(right)

    corrected_left = corrected_left if abs(corrected_left) >= 1 else 0
    corrected_right = corrected_right if abs(corrected_right) >= 1 else 0

    cmd = {"left": corrected_left, "right": corrected_right, "pump": pump}
    sock.sendall((json.dumps(cmd) + "\n").encode())
    time.sleep(duration)

    if stop_after:
        stop_cmd = {"left": 0, "right": 0, "pump": 0}
        sock.sendall((json.dumps(stop_cmd) + "\n").encode())

def close():
    sock.close()
    print("❌ Disconnected from drone.")

# ---- Load and Run Scripts ----
def list_scripts(folder):
    return sorted([
        f for f in os.listdir(folder)
        if f.endswith(".py") and "_" in f
    ])

def run_script(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()
    try:
        exec(code, globals())
    except Exception as e:
        print(f"❌ Error during execution: {e}")

# ---- UI Loop ----
def main():
    folder = "LLM_Generated_Scripts"
    scripts = list_scripts(folder)

    if not scripts:
        print("⚠️ No scripts found in LLM_Generated_Scripts/")
        return

    while True:
        print("\n🎭 Available LLM-generated Scripts:")
        for idx, filename in enumerate(scripts, start=1):
            name = filename.replace(".py", "").replace("_", " ").title()
            print(f"{idx}. {name}")
        print("0. Exit")

        try:
            choice = int(input("\nSelect a script to run (0–{}): ".format(len(scripts))))
            if choice == 0:
                print("👋 Exiting...")
                break
            elif 1 <= choice <= len(scripts):
                selected = scripts[choice - 1]
                print(f"\n▶️ Running {selected}...\n")
                run_script(os.path.join(folder, selected))
            else:
                print("❌ Invalid choice.")
        except ValueError:
            print("❌ Please enter a valid number.")

    close()

if __name__ == "__main__":
    main()