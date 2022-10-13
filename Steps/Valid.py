import re 
import os 
import sys
import subprocess
import time
from traceback import print_tb
from cherrypy import url
from colorama import Fore,init
from responses import target
import socket



#Error Function 
def error(err,target):
    if err == 1 :
        e = Fore.LIGHTRED_EX + "\n[+] " +"Error --- Check Your "+Fore.LIGHTGREEN_EX +"Connection "+Fore.LIGHTRED_EX +"OR Enter a valid Target :" + Fore.LIGHTGREEN_EX + " '{}'".format(target) + Fore.LIGHTRED_EX + " format : \n " + " "*3 + Fore.LIGHTRED_EX + "IP  : " + Fore.LIGHTGREEN_EX + "x.x.x.x \n" + " "*4 + Fore.LIGHTRED_EX +  "URL :" + Fore.LIGHTGREEN_EX + """ ------.-- ( Without : "www" at the beginning and "/" at the end ) """
        time.sleep(0.6)
        print(e)
        sys.exit(1)
    elif err == 0 : 
        e = Fore.LIGHTGREEN_EX + "\n[+] " + Fore.LIGHTYELLOW_EX +"Checking the format of : "+ Fore.LIGHTGREEN_EX + target
        ee = Fore.LIGHTGREEN_EX +"    Done"  
        print(e)
        time.sleep(0.6) 
        print(ee)
        time.sleep(0.2) 



#Error Function : ping test
def error_ping(err2,target):
    if err2 == 0 :
        e = Fore.LIGHTGREEN_EX +"    Done"
        print(e)
    else :
        e = Fore.LIGHTRED_EX + "    Error connection : " + Fore.LIGHTYELLOW_EX + "Verify your "+Fore.LIGHTGREEN_EX +"connection"+Fore.LIGHTYELLOW_EX+" OR Check"+Fore.LIGHTGREEN_EX +" {}  ".format(target)
        print(e)
        sys.exit(1)



#Test target up / down
def ping_test (ntarget,target) : 
    proc = subprocess.Popen(
        # Let it ping more times to run longer.
        ["ping", "-c", "1", ntarget],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True )
    time.sleep(0.2)
    print(Fore.LIGHTGREEN_EX + "[+] " + Fore.LIGHTYELLOW_EX + "Checking " + Fore.LIGHTGREEN_EX + "Network "+ Fore.LIGHTYELLOW_EX +"and "+ Fore.LIGHTGREEN_EX + target + Fore.LIGHTYELLOW_EX +" Connectivity :")
    while proc.poll() is None:
        time.sleep(0.1)
    return proc.poll()
        


#Check if : ip   or   url 
def split_target(target) : 
    itip = re.match(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",target)
    if itip:
        ip = 0
        return ip
    else: 
        url = 1
        return url


def convert(target):
    ipp = socket.gethostbyname(str(target))
    return ipp