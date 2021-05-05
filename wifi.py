import subprocess

print("wifi password")

data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split("\n")
profiles = [i.split(":")[l][l:-l] for i in data if "All User Profile" in l]

for i in profiles:
    results = subprocess.check_output
