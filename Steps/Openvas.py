from asyncore import read
import subprocess
import time 
from colorama import Fore
import datetime
from datetime import date
from pathlib import Path


# Openvass
def openvas(ip,targ) :
    home = str(Path.home())
    #Start openvass 
    cmd1 = "sudo gvm-start"
    proc = subprocess.Popen(cmd1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True )
    while proc.poll() is None:
        time.sleep(0.1)


    #Giving Permission to gvm socket file  
    cmd1 = "sudo chmod 662 /var/run/gvmd/gvmd.sock"
    subprocess.Popen(cmd1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True )
    time.sleep(1)


    #Creat Target
    cmd1 = "<create_target><name>Target</name><hosts>{}</hosts><port_range>T:1-65535</port_range></create_target>".format(ip)
    cmd11 =  "gvm-cli --gmp-username admin --gmp-password admin123 socket --socketpath /var/run/gvmd/gvmd.sock --xml "+ '\" {} \"'.format(cmd1) + """ | cut -d '"' -f 6 > ~/auTTest/targetid.txt"""
    subprocess.Popen(cmd11, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True )
    #if target if already exist 
    cmd1 = """gvm-cli --gmp-username admin --gmp-password admin123 socket --socketpath /var/run/gvmd/gvmd.sock --xml "<get_targets/>" | cut -d '"' -f 6 > ~/auTTest/targetid.txt"""
    subprocess.Popen(cmd1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True )
    time.sleep(1)
    print(Fore.LIGHTCYAN_EX + "    --> " + Fore.LIGHTGREEN_EX + "Traget "+ Fore.LIGHTCYAN_EX +"Created " + Fore.LIGHTCYAN_EX + " ... " )

    

    #Read target id
    with open("{}/auTTest/targetid.txt".format(home), "r") as file:
        readline = file.read().splitlines()
        id1 = "\'" + readline[0] + "\'"
    #Creat Task
    cmd1 = "<create_task><name>Target</name><target id={}>".format(id1)+"</target><config id='daba56c8-73ec-11df-a475-002264764cea'></config></create_task>"
    cmd11 = "gvm-cli --gmp-username admin --gmp-password admin123 socket --socketpath /var/run/gvmd/gvmd.sock --xml "+ '\" {} \"'.format(cmd1) + """ | cut -d '"' -f 6 > ~/auTTest/taskid.txt"""
    subprocess.Popen(cmd11, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True )
    time.sleep(1)
    print(Fore.LIGHTCYAN_EX + "    --> " + Fore.LIGHTGREEN_EX + "Task "+ Fore.LIGHTCYAN_EX +"Created " + Fore.LIGHTCYAN_EX + " ... " )



    #Read task id 
    with open("{}/auTTest/taskid.txt".format(home), "r") as file:
        readline=file.read().splitlines()
        id1 = "\'" + readline[0] + "\'"    
    #start Task
    cmd1 = "<start_task task_id={}/>".format(id1)
    cmd11 = "gvm-cli --gmp-username admin --gmp-password admin123 socket --socketpath /var/run/gvmd/gvmd.sock --xml "+ '\" {} \"'.format(cmd1) + """ | cut -d '>' -f 3 | cut -d '<' -f 1 > ~/auTTest/rapport.txt """
    subprocess.Popen(cmd11, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True )
    time.sleep(1)
    print(Fore.LIGHTCYAN_EX + "    --> " + Fore.LIGHTGREEN_EX + "Task "+ Fore.LIGHTCYAN_EX +"Started " + Fore.LIGHTCYAN_EX + " ... " )
    time.sleep(2)
    print(Fore.LIGHTCYAN_EX + "    --> " + Fore.LIGHTCYAN_EX + "Wait Task to"+ Fore.LIGHTGREEN_EX +" finish " + Fore.LIGHTCYAN_EX + " ..." )




    #Check if task is finished
    finish = 0
    with open("{}/auTTest/taskid.txt".format(home), "r") as file:
        readline=file.read().splitlines()
        id1 = "\'" + readline[0] + "\'"    
    while finish == 0 :
        cmd1 = "<get_tasks task_id={} details='1' />".format(id1)
        cmd11 = "gvm-cli --gmp-username admin --gmp-password admin123 socket --socketpath /var/run/gvmd/gvmd.sock --xml "+ '\" {} \"'.format(cmd1) + """ > ~/auTTest/finish.txt"""
        subprocess.Popen(cmd11, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True )
        time.sleep(2)
        with open("{}/auTTest/finish.txt".format(home), "r") as file:
                ff = file.read()
        if "<status>Done</status>" in ff :
            finish = 1
        else : 
            finish = 0
        time.sleep(20)



    #Read report id 
    with open("{}/auTTest/rapport.txt".format(home), "r") as file:
        readline=file.read().splitlines()
        id1 = "\'" + readline[0] + "\'"    
    #Get report 
    cmd1 = "<get_reports report_id={} format_id='c1645568-627a-11e3-a660-406186ea4fc5' details='True' />".format(id1)
    cmd11 = "gvm-cli --gmp-username admin --gmp-password admin123 socket --socketpath /var/run/gvmd/gvmd.sock --xml "+ '\" {} \"'.format(cmd1) + """ | grep -oP "(?<=</report_format>)[^<]+" | base64 -d > ~/auTTest/Report/report-openvass.csv"""
    subprocess.Popen(cmd11, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True )
    time.sleep(1)
    #change name report
    dat = date.today()
    cmd11 = "mv ~/auTTest/Report/report-openvass.csv ~/auTTest/Report/openvas-report-{}-{}.csv".format(targ,dat)
    subprocess.Popen(cmd11, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True )
    print(Fore.LIGHTCYAN_EX + "        Done")


def makecopy() : 
    cmd1 = "mv ~/auTTest/Report/* ~/auTTest/Old_Report/"
    subprocess.Popen(cmd1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True )
