import subprocess

def range_start():
    return subprocess.run("cat /etc/dnsmasq.d/090_wlan0.conf |grep dhcp-range= |cut -d'=' -f2| cut -d',' -f1", shell=True, capture_output=True, text=True).stdout.strip()

def range_end():
    return subprocess.run("cat /etc/dnsmasq.d/090_wlan0.conf |grep dhcp-range= |cut -d'=' -f2| cut -d',' -f2", shell=True, capture_output=True, text=True).stdout.strip()

def range_subnet_mask():
    return subprocess.run("cat /etc/dnsmasq.d/090_wlan0.conf |grep dhcp-range= |cut -d'=' -f2| cut -d',' -f3", shell=True, capture_output=True, text=True).stdout.strip()

def range_lease_time():
    return subprocess.run("cat /etc/dnsmasq.d/090_wlan0.conf |grep dhcp-range= |cut -d'=' -f2| cut -d',' -f4", shell=True, capture_output=True, text=True).stdout.strip()
