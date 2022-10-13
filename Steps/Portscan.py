import subprocess
import time 
from colorama import Fore


# nmap for port scanner 
def nmapport(url) :
    cmd1 = "nmap -A -p0- -Pn {} -oN ~/auTTest/Output/Portscan/nmapport.txt".format(url)
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
# nmap for Services 
def nmapport(url) :
    cmd1 = "nmap -T4 -A -p0- -Pn -v {} -oN ~/auTTest/Output/Portscan/nmapport.txt".format(url)
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