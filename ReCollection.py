#coding=utf-8

import re

def isValidIp(ip):
    if re.match(r"^\s*\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s*$", ip):
        return True
    return False

def isValidMac(mac):
    if re.match(r"^\s*([0-9a-fA-F]{2,2}:){5,5}[0-9a-fA-F]{2,2}\s*$", mac):
        return True
    return False
