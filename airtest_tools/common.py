from airtest.core.api import *
from airtest.core.api import G
from airtest.core.api import connect_device


def deviceConnect(uuid=None):
    if uuid == None:
        uuid = "1576457605007R5"
    device = connect_device("Android://127.0.0.1:5037/%s?cap_method=minicap&touch_method=adb" % (uuid))

    return device

def deviceRemoteConnect(ip=None):
    if ip == None:
        ip = "10.200.8.110:5555"
    device = connect_device("Android:///%s?cap_method=minicap&touch_method=adb" % (ip))

    return device

def phoneResolution():
    phone_resolution = {}
    phone_resolution["height"] = G.DEVICE.display_info["height"]
    phone_resolution["width"] = G.DEVICE.display_info["width"]

    return phone_resolution