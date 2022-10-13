import subprocess
import time 
from colorama import Fore
import requests


######## ------------------------ http or https :
def testhttps(url) : 
    test = "http://{}".format(url)
    r = requests.get(test) # first we try http
    nurl = r.url #the reel url 
    return nurl


#whatweb
def whatweb(url) :
    cmd1 = "whatweb -a 3 {} > ~/auTTest/Output/Autoenum/whatweb.txt".format(url)
    proc = subprocess.Popen(
            # Let it ping more times to run longer.
            cmd1,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True )
    time.sleep(0.4)
    while proc.poll() is None:
        time.sleep(0.1)
    print(Fore.LIGHTGREEN_EX +"    Done")



#webtech
def webtech(url) :
    cmd1 = "webtech -u {} > ~/auTTest/Output/Autoenum/webtech.txt".format(url)
    proc = subprocess.Popen(
            # Let it ping more times to run longer.
            cmd1,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True )
    time.sleep(0.4)
    while proc.poll() is None:
        time.sleep(0.1)
    print(Fore.LIGHTGREEN_EX +"    Done")


    