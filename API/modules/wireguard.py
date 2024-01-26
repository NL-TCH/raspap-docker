import subprocess

def configs():
    return subprocess.run("ls /etc/wireguard/ | wc -l", shell=True, capture_output=True, text=True).stdout.strip()

