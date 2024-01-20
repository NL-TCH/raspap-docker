import subprocess
import json

def adblockdomains():
    output = subprocess.run("cat /etc/raspap/adblock/domains.txt", shell=True, capture_output=True, text=True).stdout.strip()
    domains =output.split('\n')
    domainlist=[]
    for domain in domains:
        if domain.startswith('#') or domain=="":
            continue
        domainlist.append(domain.split('=/')[1])
    return domainlist

def adblockhostnames():
    output = subprocess.run("cat /etc/raspap/adblock/hostnames.txt", shell=True, capture_output=True, text=True).stdout.strip()
    hostnames = output.split('\n')
    hostnamelist=[]
    for hostname in hostnames:
        if hostname.startswith('#') or hostname=="":
            continue
        hostnamelist.append(hostname.replace('0.0.0.0 ',''))
    return hostnamelist

print(adblockhostnames())