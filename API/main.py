from fastapi import FastAPI
from fastapi.security.api_key import APIKey

import system
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

@app.post("/restart/webgui")
async def restart():
    restart.webgui()

@app.post("/restart/adblock")
async def restart():
    restart.adblock()