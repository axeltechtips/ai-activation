import random
import string
import subprocess
import os

def generate_activation_key():
  random_string = ""
  for _ in range(25):
    random_char = random.choice(string.ascii_uppercase + string.digits)
    random_string += random_char
  return "-".join(random_string[i:i+5] for i in range(0, len(random_string), 5))

def main():
  working_keys = []
  for _ in range(100):
    key = generate_activation_key()
    print(f"Trying to activate Windows with key {key}...")
    result = subprocess.run(["cscript", "slmgr.vbs", "/ato", "/ipr", key], capture_output=True, text=True)
    if result.returncode == 0:
      print("Windows activated successfully!")
      working_keys.append(key)
      with open("working_keys.txt", "w") as f:
        for key in working_keys:
          f.write(key + "\n")
      break
    else:
      print(f"Invalid key: {key}")

if __name__ == "__main__":
  main()
