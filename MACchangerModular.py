import os
import winreg
import re
def change_macMAC(interface, new_mac):
    os.system('sudo ifconfig ' + interface + ' ether ' + new_mac)

def change_linuxMAC(interface, new_mac):
    os.system('sudo ifconfig ' + interface + ' down')
    os.system('sudo ifconfig ' + interface + ' ether hw ' + new_mac)
    os.system('sudo ifconfig ' + interface + ' up')

def change_windowsMAC(interface, new_mac):
    for i in ['00','01','02','03','04','05','06','07','08','09','10','11']:
            keypath = 'SYSTEM\CurrentControlSet\Control\Class\{4d36e972-e325-11ce-bfc1-08002be10318}\\00'+ i
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,keypath, 0, winreg.KEY_ALL_ACCESS) as regkey:
                    if interface == winreg.QueryValueEx(regkey,'NetCfgInstanceId')[0]:
                        os.system('reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4D36E972-E325-11CE-BFC1-08002BE10318}\\00' + i +' /v NetworkAddress /d ' + new_mac + ' /f')
            except OSError:
                return None
def reset_windowsMAC(interface, new_mac):
    for i in ['00','01','02','03','04','05','06','07','08','09','10','11']:
            keypath = 'SYSTEM\CurrentControlSet\Control\Class\{4d36e972-e325-11ce-bfc1-08002be10318}\\00'+ i
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,keypath, 0, winreg.KEY_ALL_ACCESS) as regkey:
                    if interface == winreg.QueryValueEx(regkey,'NetCfgInstanceId')[0]:
                        os.system('reg delete HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4D36E972-E325-11CE-BFC1-08002BE10318}\\00'+ i +' /v NetworkAddress /f')
            except OSError:
                return None            
def isValidMACAddress(str): 
    regex = ("^([0-9A-Fa-f]{2}[:.-])" + "{5}([0-9A-Fa-f]{2})$|" +"([0-9a-fA-F]{12})$")
    p = re.compile(regex)
    if (str == None):
        return False
    if(re.search(p, str)):
        return True
    else:
        return False
