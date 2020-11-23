# MACchangerGUI

Written by Khuong Dinh

Date: Nov 18 2020

Usage: Using GUI to change MAC addresses linux, Mac OS and Windows System, restore default Windows MAC addresses

Description:
The MACchanger source code is designed to run from MACchangerMain.py with SystemAdmin/sudo privilege.

The MACchangerGUI.py is translated from MACchangerGUI.ui using pyuic5-tool designer tool, this .py file is kept separated with the rest in case GUI need to be adjusted. Try the best to keep GUI class variables' name the same for they are used in main program.

The MACchangerModular has the core functions which is used to change MAC addresses


Libraries from pip needed to compiled this program: PyQT5, netifaces

 
Further	work:
	+The adjusted MAC address in Mac OS and Linux will automatically restore to its' origin after machine reboot but still a function to restore them at-will should also be implemented.
	+Need turn the code to be more object oriented to expand development or to be intergrated into bigger project 
	+Work on MAC addess randomizer, log
