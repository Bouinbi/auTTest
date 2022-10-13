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



######## ------------------------ root domain : 
#ffuf-Common wordlist 
def ffufcommon(url) :
    cmd1 = "ffuf -w /usr/share/seclists/Discovery/Web-Content/common.txt -u {}FUZZ -of csv -o ~/auTTest/Output/Bruteforce/ffcommon.csv ".format(url)
    proc = subprocess.Popen(
            # Let it ping more times to run longer.
            cmd1,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True )
    time.sleep(0.4)
    while proc.poll() is None:
        time.sleep(0.1)
    
    cmd2="cat ~/auTTest/Output/Bruteforce/ffcommon.csv | cut -d ',' -f 1,2 > ~/auTTest/Output/Bruteforce/ffcommon.txt"
    proc = subprocess.Popen(
            # Let it ping more times to run longer.
            cmd2,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True )
    time.sleep(0.4)
    while proc.poll() is None:
        time.sleep(0.1)
    print(Fore.LIGHTGREEN_EX +"    Done")








#ffuf-2.3-small.txt wordlist 
def ffufsmall(url) :
    cmd1 = "ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -u {}FUZZ -of csv -o ~/auTTest/Output/Bruteforce/ffsmall.csv ".format(url)
    proc = subprocess.Popen(
            # Let it ping more times to run longer.
            cmd1,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True )
    time.sleep(0.4)
    while proc.poll() is None:
        time.sleep(0.1)
    
    cmd2="cat ~/auTTest/Output/Bruteforce/ffsmall.csv | cut -d ',' -f 1,2 | cut -d '#' -f 7 | awk 'NF > 0' > ~/auTTest/Output/Bruteforce/ffsmall.txt"
    proc = subprocess.Popen(
            # Let it ping more times to run longer.
            cmd2,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True )
    time.sleep(0.4)
    while proc.poll() is None:
        time.sleep(0.1)
    print(Fore.LIGHTGREEN_EX +"    Done")





