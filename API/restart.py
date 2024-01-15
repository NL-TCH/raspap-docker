import subprocess

def restart():
    return subprocess.run("sudo /etc/raspap/lighttpd/configport.sh --restart", shell=True, capture_output=True, text=True).stdout.strip()