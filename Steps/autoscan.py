import subprocess
from tabnanny import check
import time 
from colorama import Fore
import requests


######## ------------------------ http or https :
def testhttps(url) : 
    test = "http://{}".format(url)
    r = requests.get(test) # first we try http
    nurl = r.url #the reel url 
    return nurl

"""
# wapiti
def wapiti(url) :
    cmd1 = "wapiti -u {} -f txt -o ~/auTTest/Output/Autoscan/wapiti.txt".format(url)
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

"""

global checknn
checknn = 0

# nuclei
def nuclei(url) :
    """
    nurl = url[:-1]
    cmd1 = "nuclei -u {} -o ~/auTTest/Output/Autoscan/nuclei.txt".format(nurl)
    cmd2 = " gnome-terminal -- bash -c " + '\" {} \"'.format(cmd1)
    #Run in new terminal
    print(Fore.LIGHTGREEN_EX +"    "+Fore.LIGHTGREEN_EX +"    Running in new terminal ( Will be closed auto after terminate ) ")
    subprocess.Popen(cmd2 ,shell=True) """

    nurl = url[:-1]
    cmd1 = "nuclei -u {} -o ~/auTTest/Output/Autoscan/nuclei.txt".format(nurl)
    proc = subprocess.Popen(
            cmd1,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True )
    time.sleep(0.4)
    while proc.poll() is None:
        time.sleep(0.1)
    print(Fore.LIGHTGREEN_EX +"    Done")
    checknn = 1



# Nikto
def nikto(url) :
    """
    cmd1 = " nikto -o ~/auTTest/Output/Autoscan/nikto.txt -Format txt -h {} ".format(url)
    cmd2 = " gnome-terminal -- bash -c " + '\" {} \"'.format(cmd1)
    #Run in new terminal
    print(Fore.LIGHTGREEN_EX +"    "+Fore.LIGHTGREEN_EX +"    Running in new terminal ( Will be closed auto after terminate ) ")
    subprocess.Popen(cmd2 ,shell=True)
    """

    cmd1 = " nikto -o ~/auTTest/Output/Autoscan/nikto.txt -Format txt -h {} ".format(url)
    proc = subprocess.Popen(
            cmd1,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True )
    time.sleep(0.4)
    while proc.poll() is None:
        time.sleep(0.1)
    print(Fore.LIGHTGREEN_EX +"    Done")
    checknn = 1


def checknnn():
    return checknn
