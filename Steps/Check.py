import subprocess
import time 
from colorama import Fore



#Check for waf
def waf(url) :
    cmd1 = "wafw00f {} -o ~/auTTest/Output/Check/waf.txt".format(url)
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



#Check for ssl
def ssll(url) :
    cmd1 = "sslscan --no-cipher-details --no-ciphersuites --no-groups {}:443 > ~/auTTest/Output/Check/ssl.txt".format(url)
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