from fastapi import FastAPI
from fastapi.security.api_key import APIKey

import json

import modules.system as system
import modules.ap as ap
import modules.client as client
import modules.dns as dns
import modules.dhcp as dhcp
import modules.ddns as ddns
import modules.firewall as firewall
import modules.networking as networking
import modules.openvpn as openvpn
import modules.wireguard as wireguard
import modules.restart as restart


tags_metadata = [
    {
        "name": "system",
        "description": "All information regarding the underlying system."
    },
    {
        "name": "accesspoint/hostpost",
        "description": "Get and change all information regarding the hotspot"
    }
]
app = FastAPI(
    title="API for Raspap",
    openapi_tags=tags_metadata,
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

@app.post("/ap/driver", tags=["accesspoint/hostpost"])
async def post_ap_driver(driver: str):
    ap.set_driver(driver)
    return {'driver': driver}

@app.post("/ap/ctrl_interface", tags=["accesspoint/hostpost"])
async def post_ap_ctrl_interface(ctrl_interface: str):
    ap.set_ctrl_interface(ctrl_interface)
    return {'ctrl_interface': ctrl_interface}

@app.post("/ap/ctrl_interface_group", tags=["accesspoint/hostpost"])
async def post_ap_ctrl_interface_group(ctrl_interface_group: str):
    ap.set_ctrl_interface_group(ctrl_interface_group)
    return {'ctrl_interface_group': ctrl_interface_group}

@app.post("/ap/auth_algs", tags=["accesspoint/hostpost"])
async def post_ap_auth_algs(auth_algs: str):
    ap.set_auth_algs(auth_algs)
    return {'auth_algs': auth_algs}

@app.post("/ap/wpa_key_mgmt", tags=["accesspoint/hostpost"])
async def post_ap_wpa_key_mgmt(wpa_key_mgmt: str):
    ap.set_wpa_key_mgmt(wpa_key_mgmt)
    return {'wpa_key_mgmt': wpa_key_mgmt}

@app.post("/ap/beacon_int", tags=["accesspoint/hostpost"])
async def post_ap_beacon_int(beacon_int: str):
    ap.set_beacon_int(beacon_int)
    return {'beacon_int': beacon_int}

@app.post("/ap/ssid", tags=["accesspoint/hostpost"])
async def post_ap_ssid(ssid: str):
    ap.set_ssid(ssid)
    return {'ssid': ssid}

@app.post("/ap/channel", tags=["accesspoint/hostpost"])
async def post_ap_channel(channel: str):
    ap.set_channel(channel)
    return {'channel': channel}

@app.post("/ap/hw_mode", tags=["accesspoint/hostpost"])
async def post_ap_hw_mode(hw_mode: str):
    ap.set_hw_mode(hw_mode)
    return {'hw_mode': hw_mode}

@app.post("/ap/ieee80211n", tags=["accesspoint/hostpost"])
async def post_ap_ieee80211n(ieee80211n: str):
    ap.set_ieee80211n(ieee80211n)
    return {'ieee80211n': ieee80211n}

@app.post("/ap/wpa_passphrase", tags=["accesspoint/hostpost"])
async def post_ap_wpa_passphrase(wpa_passphrase: str):
    ap.set_wpa_passphrase(wpa_passphrase)
    return {'wpa_passphrase': wpa_passphrase}

@app.post("/ap/interface", tags=["accesspoint/hostpost"])
async def post_ap_interface(interface: str):
    ap.set_interface(interface)
    return {'interface': interface}

@app.post("/ap/wpa", tags=["accesspoint/hostpost"])
async def post_ap_wpa(wpa: str):
    ap.set_wpa(wpa)
    return {'wpa': wpa}

@app.post("/ap/wpa_pairwise", tags=["accesspoint/hostpost"])
async def post_ap_wpa_pairwise(wpa_pairwise: str):
    ap.set_wpa_pairwise(wpa_pairwise)
    return {'wpa_pairwise': wpa_pairwise}

@app.post("/ap/country_code", tags=["accesspoint/hostpost"])
async def post_ap_country_code(country_code: str):
    ap.set_country_code(country_code)
    return {'country_code': country_code}

@app.post("/ap/ignore_broadcast_ssid", tags=["accesspoint/hostpost"])
async def post_ap_ignore_broadcast_ssid(ignore_broadcast_ssid: str):
    ap.set_ignore_broadcast_ssid(ignore_broadcast_ssid)
    return {'ignore_broadcast_ssid': ignore_broadcast_ssid}

@app.get("/clients/{wireless_interface}", tags=["Clients"])
async def get_clients(wireless_interface):
    return{
'active_clients_amount': client.get_active_clients_amount(wireless_interface),
'active_clients': json.loads(client.get_active_clients(wireless_interface))
}

@app.get("/dhcp", tags=["DHCP"])
async def get_dhcp():
    return{
'range_start': dhcp.range_start(),
'range_end': dhcp.range_end(),
'range_subnet_mask': dhcp.range_subnet_mask(),
'range_lease_time': dhcp.range_lease_time(),
'range_gateway': dhcp.range_gateway(),
'range_nameservers': dhcp.range_nameservers()
}

@app.get("/dns/domains", tags=["DNS"])
async def get_domains():
    return{
'domains': json.loads(dns.adblockdomains())
}

@app.get("/dns/hostnames", tags=["DNS"])
async def get_hostnames():
    return{
'hostnames': json.loads(dns.adblockhostnames())
}

@app.get("/dns/upstream", tags=["DNS"])
async def get_upstream():
    return{
'upstream_nameserver': dns.upstream_nameserver()
}

@app.get("/dns/logs", tags=["DNS"])
async def get_dnsmasq_logs():
    return(dns.dnsmasq_logs())


@app.get("/ddns", tags=["DDNS"])
async def get_ddns():
    return{
'use': ddns.use(),
'method': ddns.method(),
'protocol': ddns.protocol(),
'server': ddns.server(),
'login': ddns.login(),
'password': ddns.password(),
'domain': ddns.domain()
}

@app.get("/firewall", tags=["Firewall"])
async def get_firewall():
    return json.loads(firewall.firewall_rules())

@app.get("/networking", tags=["Networking"])
async def get_networking():
    return{
'interfaces': json.loads(networking.interfaces()),
'throughput': json.loads(networking.throughput())
}

@app.get("/openvpn", tags=["OpenVPN"])
async def get_openvpn():
    return{
'client_configs': openvpn.client_configs(),
'client_config_names': openvpn.client_config_names(),
'client_config_active': openvpn.client_config_active(),
'client_login_names': openvpn.client_login_names(),
'client_login_active': openvpn.client_login_active()
}

@app.get("/openvpn/{config}", tags=["OpenVPN"])
async def client_config_list(config):
    return{
'client_config': openvpn.client_config_list(config)
}

@app.get("/wireguard", tags=["WireGuard"])
async def get_wireguard():
    return{
'client_configs': wireguard.configs(),
'client_config_names': wireguard.client_config_names(),
'client_config_active': wireguard.client_config_active()
}

@app.get("/wireguard/{config}", tags=["WireGuard"])
async def client_config_list(config):
    return{
'client_config': wireguard.client_config_list(config)
}

@app.post("/restart/webgui")
async def restart_webgui():
    restart.webgui()

@app.post("/restart/adblock")
async def restart_adblock():
    restart.adblock()