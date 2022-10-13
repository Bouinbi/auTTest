import subprocess
import time 
from colorama import Fore


#sub-domain using sublist3r
def domain_list3r(url) :
    cmd1 = "sublist3r -d {} -o ~/auTTest/Output/Recon/domain_sublist3r.txt".format(url)
    #cmd1 = "echo 'hello world 2 ' > ~/auTTest/Output/Recon/domain_sublist3r.txt"
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



#dns-recon 
def dnsrecon(url) :
    cmd1 = "dnsrecon -d {} -c ~/auTTest/Output/Recon/dnsrecon.csv".format(url)
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