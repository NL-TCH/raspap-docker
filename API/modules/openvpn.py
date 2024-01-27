import subprocess

def client_configs():
    return subprocess.run("find /etc/openvpn/client/ -type f | wc -l", shell=True, capture_output=True, text=True).stdout.strip()

def client_config_names():
    config_names_list = []
    output = subprocess.run('''ls /etc/openvpn/client/ | grep -v "^client.conf$"''', shell=True, capture_output=True, text=True).stdout.strip()
    lines = output.split("\n")
    for client in lines:
        config_names_dict ={'config':client}
        config_names_list.append(config_names_dict)
    return config_names_list

def client_config_active():
    output = subprocess.run('''ls -al  /etc/openvpn/client/ | grep "client.conf -"''', shell=True, capture_output=True, text=True).stdout.strip()
    active_config = output.split("/etc/openvpn/client/")
    return(active_config[1])

def client_config_list(client_config):
    output = subprocess.run(f"cat /etc/openvpn/client/{client_config}", shell=True, capture_output=True, text=True).stdout.strip()
    return output