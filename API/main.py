from fastapi import FastAPI
from fastapi.security.api_key import APIKey

import json

import modules.system as system
import modules.networking as networking
import modules.ap as ap
import modules.dns as dns
import modules.dhcp as dhcp
import modules.restart as restart


tags_metadata = [
    {
        "name": "system",
        "description": "All information regarding the underlying system.",
    },
    {
        "name": "accesspoint/hostpost",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]
app = FastAPI(
    title="API for Raspap",
    tags_metadata=tags_metadata,
    version="0.0.1",
    license_info={
    "name": "Apache 2.0",
    "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
}
)

@app.get("/system", tags=["system"])
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

@app.get("/system/hostname", tags=["system"])
async def get_system_hostname():
    return{'hostname': system.hostname()}

@app.get("/system/systime", tags=["system"])
async def get_system_systime():
    return{'systime': system.systime()}

@app.get("/system/usedMemory", tags=["system"])
async def get_system_usedMemory():
    return{'usedMemory': system.usedMemory()}

@app.get("/system/processorCount", tags=["system"])
async def get_system_processorCount():
    return{'processorCount': system.processorCount()}

@app.get("/system/LoadAvg1Min", tags=["system"])
async def get_system_LoadAvg1Min():
    return{'LoadAvg1Min': system.LoadAvg1Min()}

@app.get("/system/systemLoadPercentage", tags=["system"])
async def get_system_systemLoadPercentage():
    return{'systemLoadPercentage': system.systemLoadPercentage()}

@app.get("/system/systemTemperature", tags=["system"])
async def get_system_systemTemperature():
    return{'systemTemperature': system.systemTemperature()}

@app.get("/system/hostapdStatus", tags=["system"])
async def get_system_hostapdStatus():
    return{'hostapdStatus': system.hostapdStatus()}

@app.get("/system/operatingSystem", tags=["system"])
async def get_system_operatingSystem():
    return{'operatingSystem': system.operatingSystem()}

@app.get("/system/kernelVersion", tags=["system"])
async def get_system_kernelVersion():
    return{'kernelVersion': system.kernelVersion()}

@app.get("/system/rpiRevision", tags=["system"])
async def get_system_rpiRevision():
    return{'rpiRevision': system.rpiRevision()}

@app.get("/ap", tags=["accesspoint/hostpost"])
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

@app.get("/ap/driver", tags=["accesspoint/hostpost"])
async def get_ap_driver():
    return {'driver': ap.driver()}

@app.post("/ap/driver", tags=["accesspoint/hostpost"])
async def post_ap_driver(driver: str):
    ap.set_driver(driver)
    return {'driver': driver}

@app.get("/ap/ctrl_interface", tags=["accesspoint/hostpost"])
async def get_ap_ctrl_interface():
    return {'ctrl_interface': ap.ctrl_interface()}

@app.post("/ap/ctrl_interface", tags=["accesspoint/hostpost"])
async def post_ap_ctrl_interface(ctrl_interface: str):
    ap.set_ctrl_interface(ctrl_interface)
    return {'ctrl_interface': ctrl_interface}

@app.get("/ap/ctrl_interface_group", tags=["accesspoint/hostpost"])
async def get_ap_ctrl_interface_group():
    return {'ctrl_interface_group': ap.ctrl_interface_group()}

@app.post("/ap/ctrl_interface_group", tags=["accesspoint/hostpost"])
async def post_ap_ctrl_interface_group(ctrl_interface_group: str):
    ap.set_ctrl_interface_group(ctrl_interface_group)
    return {'ctrl_interface_group': ctrl_interface_group}

@app.get("/ap/auth_algs", tags=["accesspoint/hostpost"])
async def get_ap_auth_algs():
    return {'auth_algs': ap.auth_algs()}

@app.post("/ap/auth_algs", tags=["accesspoint/hostpost"])
async def post_ap_auth_algs(auth_algs: str):
    ap.set_auth_algs(auth_algs)
    return {'auth_algs': auth_algs}

@app.get("/ap/wpa_key_mgmt", tags=["accesspoint/hostpost"])
async def get_ap_wpa_key_mgmt():
    return {'wpa_key_mgmt': ap.wpa_key_mgmt()}

@app.post("/ap/wpa_key_mgmt", tags=["accesspoint/hostpost"])
async def post_ap_wpa_key_mgmt(wpa_key_mgmt: str):
    ap.set_wpa_key_mgmt(wpa_key_mgmt)
    return {'wpa_key_mgmt': wpa_key_mgmt}

@app.get("/ap/beacon_int", tags=["accesspoint/hostpost"])
async def get_ap_beacon_int():
    return {'beacon_int': ap.beacon_int()}

@app.post("/ap/beacon_int", tags=["accesspoint/hostpost"])
async def post_ap_beacon_int(beacon_int: str):
    ap.set_beacon_int(beacon_int)
    return {'beacon_int': beacon_int}

@app.get("/ap/ssid", tags=["accesspoint/hostpost"])
async def get_ap_ssid():
    return {'ssid': ap.ssid()}

@app.post("/ap/ssid", tags=["accesspoint/hostpost"])
async def post_ap_ssid(ssid: str):
    ap.set_ssid(ssid)
    return {'ssid': ssid}

@app.get("/ap/channel", tags=["accesspoint/hostpost"])
async def get_ap_channel():
    return {'channel': ap.channel()}

@app.post("/ap/channel", tags=["accesspoint/hostpost"])
async def post_ap_channel(channel: str):
    ap.set_channel(channel)
    return {'channel': channel}

@app.get("/ap/hw_mode", tags=["accesspoint/hostpost"])
async def get_ap_hw_mode():
    return {'hw_mode': ap.hw_mode()}

@app.post("/ap/hw_mode", tags=["accesspoint/hostpost"])
async def post_ap_hw_mode(hw_mode: str):
    ap.set_hw_mode(hw_mode)
    return {'hw_mode': hw_mode}

@app.get("/ap/ieee80211n", tags=["accesspoint/hostpost"])
async def get_ap_ieee80211n():
    return {'ieee80211n': ap.ieee80211n()}

@app.post("/ap/ieee80211n", tags=["accesspoint/hostpost"])
async def post_ap_ieee80211n(ieee80211n: str):
    ap.set_ieee80211n(ieee80211n)
    return {'ieee80211n': ieee80211n}

@app.get("/ap/wpa_passphrase", tags=["accesspoint/hostpost"])
async def get_ap_wpa_passphrase():
    return {'wpa_passphrase': ap.wpa_passphrase()}

@app.post("/ap/wpa_passphrase", tags=["accesspoint/hostpost"])
async def post_ap_wpa_passphrase(wpa_passphrase: str):
    ap.set_wpa_passphrase(wpa_passphrase)
    return {'wpa_passphrase': wpa_passphrase}

@app.get("/ap/interface", tags=["accesspoint/hostpost"])
async def get_ap_interface():
    return {'interface': ap.interface()}

@app.post("/ap/interface", tags=["accesspoint/hostpost"])
async def post_ap_interface(interface: str):
    ap.set_interface(interface)
    return {'interface': interface}

@app.get("/ap/wpa", tags=["accesspoint/hostpost"])
async def get_ap_wpa():
    return {'wpa': ap.wpa()}

@app.post("/ap/wpa", tags=["accesspoint/hostpost"])
async def post_ap_wpa(wpa: str):
    ap.set_wpa(wpa)
    return {'wpa': wpa}

@app.get("/ap/wpa_pairwise", tags=["accesspoint/hostpost"])
async def get_ap_wpa_pairwise():
    return {'wpa_pairwise': ap.wpa_pairwise()}

@app.post("/ap/wpa_pairwise", tags=["accesspoint/hostpost"])
async def post_ap_wpa_pairwise(wpa_pairwise: str):
    ap.set_wpa_pairwise(wpa_pairwise)
    return {'wpa_pairwise': wpa_pairwise}

@app.get("/ap/country_code", tags=["accesspoint/hostpost"])
async def get_ap_country_code():
    return {'country_code': ap.country_code()}

@app.post("/ap/country_code", tags=["accesspoint/hostpost"])
async def post_ap_country_code(country_code: str):
    ap.set_country_code(country_code)
    return {'country_code': country_code}

@app.get("/ap/ignore_broadcast_ssid", tags=["accesspoint/hostpost"])
async def get_ap_ignore_broadcast_ssid():
    return {'ignore_broadcast_ssid': ap.ignore_broadcast_ssid()}

@app.post("/ap/ignore_broadcast_ssid", tags=["accesspoint/hostpost"])
async def post_ap_ignore_broadcast_ssid(ignore_broadcast_ssid: str):
    ap.set_ignore_broadcast_ssid(ignore_broadcast_ssid)
    return {'ignore_broadcast_ssid': ignore_broadcast_ssid}









@app.get("/dhcp")
async def get_dhcp():
    return{
'range_start': dhcp.range_start(),
'range_end': dhcp.range_end(),
'range_subnet_mask': dhcp.range_subnet_mask(),
'range_lease_time': dhcp.range_lease_time()
}

@app.get("/networking")
async def get_networking():
    return{
'interfaces': json.loads(networking.interfaces()),
'throughput': json.loads(networking.throughput())
}

@app.get("/dns/domains")
async def get_domains():
    return{
'domains': json.loads(dns.adblockdomains())
}

@app.get("/dns/hostnames")
async def get_hostnames():
    return{
'hostnames': json.loads(dns.adblockhostnames())
}

@app.get("/dns/logs")
async def get_dnsmasq_logs():
    return(dns.dnsmasq_logs())

@app.post("/restart/webgui")
async def restart_webgui():
    restart.webgui()

@app.post("/restart/adblock")
async def restart_adblock():
    restart.adblock()