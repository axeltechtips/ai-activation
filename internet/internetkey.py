import random
import string
import subprocess
import requests
import os

def generate_activation_key():
  random_string = ""
  for _ in range(25):
    random_char = random.choice(string.ascii_uppercase + string.digits)
    random_string += random_char
  return "-".join(random_string[i:i+5] for i in range(0, len(random_string), 5))

def get_activation_keys_from_web():
  response = requests.get("https://api.kinguin.net/v1/keys/windows/10/pro/")
  if response.status_code == 200:
    return response.json()
  else:
    return []

def main():
  working_keys = []
  keys_from_web = get_activation_keys_from_web()
  for key in keys_from_web:
    print(f"Trying to activate Windows with key {key}...")
    result = subprocess.run(["cscript", "slmgr.vbs", "/ato", "/ipr", key], capture_output=True, text=True)
    if result.returncode == 0:
      print("Windows activated successfully!")
      working_keys.append(key)
    else:
      print(f"Invalid key: {key}")

if __name__ == "__main__":
  main()
