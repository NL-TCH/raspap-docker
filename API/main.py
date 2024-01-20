from fastapi import FastAPI
from fastapi.security.api_key import APIKey

import json

import system
import networking
import ap
import dns
import restart

app = FastAPI()

@app.get("/system")
async def get_system():
    return{
'hostname': system.hostname(),
'uptime': system.uptime(),
'systime': system.systime(),
'usedMemory': system.usedMemory(),
'processorCount': system.processorCount(),
'LoadAvg1Min': system.LoadAvg1Min(),
'systemLoadPercentage': system.systemLoadPercentage(),
'systemTemperature': system.systemTemperature(),
'hostapdStatus': system.hostapdStatus(),
'operatingSystem': system.operatingSystem(),
'kernelVersion': system.kernelVersion(),
'rpiRevision': system.rpiRevision()
}

@app.get("/ap")
async def get_ap():
    return{
'driver': ap.driver(),
'ctrl_interface': ap.ctrl_interface(),
'ctrl_interface_group': ap.ctrl_interface_group(),
'auth_algs': ap.auth_algs(),
'wpa_key_mgmt': ap.wpa_key_mgmt(),
'beacon_int': ap.beacon_int(),
'ssid': ap.ssid(),
'channel': ap.channel(),
'hw_mode': ap.hw_mode(),
'ieee80211n': ap.ieee80211n(),
'wpa_passphrase': ap.wpa_passphrase(),
'interface': ap.interface(),
'wpa': ap.wpa(),
'wpa_pairwise': ap.wpa_pairwise(),
'country_code': ap.country_code(),
'ignore_broadcast_ssid': ap.ignore_broadcast_ssid()
}

@app.get("/networking")
async def get_networking():
    return{
'interfaces': json.loads(networking.interfaces()),
'throughput': json.loads(networking.throughput())
}

@app.get("/dns/domains")
async def getdomains():
    return{
'domains': json.loads(dns.adblockdomains())
}

@app.get("/dns/hostnames")
async def gethostnames():
    return{
'hostnames': json.loads(dns.adblockhostnames())
}

@app.post("/restart/webgui")
async def restart():
    restart.webgui()

@app.post("/restart/adblock")
async def restart():
    restart.adblock()