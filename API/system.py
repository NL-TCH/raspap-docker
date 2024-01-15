import subprocess

def hostname():
    return subprocess.run("hostname -f", shell=True, capture_output=True, text=True).stdout.strip()

def uptime():
    return subprocess.run("uptime -p", shell=True, capture_output=True, text=True).stdout.strip()

def systime():
    return subprocess.run("date", shell=True, capture_output=True, text=True).stdout.strip()

def usedMemory():
    return subprocess.run("free -m | awk 'NR==2{total=$2 ; used=$3 } END { print used/total*100}'", shell=True, capture_output=True, text=True).stdout.strip()

def processorCount():
    return subprocess.run("nproc --all", shell=True, capture_output=True, text=True).stdout.strip()

def LoadAvg1Min():
    return subprocess.run("awk '{print $1}' /proc/loadavg", shell=True, capture_output=True, text=True).stdout.strip()

def systemLoadPercentage():
    return round((float(LoadAvg1Min())*100)/float(processorCount()),2)

def systemTemperature():
    try:
        output = subprocess.run("cat /sys/class/thermal/thermal_zone0/temp", shell=True, capture_output=True, text=True).stdout.strip()
        return float(output)/1000
    except ValueError:
        return 0
    

def hostapdStatus():
    return subprocess.run("pidof hostapd | wc -l", shell=True, capture_output=True, text=True).stdout.strip()

def operatingSystem():
    return subprocess.run('''lsb_release -sd | sed 's/"//g' ''', shell=True, capture_output=True, text=True).stdout.strip()

def kernelVersion():
    return subprocess.run("uname -r", shell=True, capture_output=True, text=True).stdout.strip()

#def rpiRevision():
#    return subprocess.run("cat /proc/cpuinfo | grep Revision", shell=True, capture_output=True, text=True).stdout.strip()

