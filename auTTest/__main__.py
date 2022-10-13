#!/usr/bin/python3
#import requir library
from ast import Break
from cProfile import label
from gc import callbacks
import imp
from multiprocessing.reduction import DupFd
import tarfile
from traceback import print_tb
from turtle import goto
import click
import datetime
import pyfiglet
from pyfiglet import Figlet
import time
import progressbar
from colorama import Fore,init
from pathlib import Path
import socket
from responses import target
from sqlalchemy import except_, false
import subprocess


#import function --- 
from Steps.Valid import split_target , ping_test , error , error_ping , convert
from Steps.Front import animated_marker , name 
from Steps.Recon import domain_list3r,dnsrecon
from Steps.Check import ssll , waf 
from Steps.Bruteforce import testhttps , ffufcommon , ffufsmall 
from Steps.autoenum import whatweb , webtech 
from Steps.autoscan import nikto , nuclei , checknnn 
from Steps.Portscan import nmapport  
from Steps.Openvas import openvas , makecopy
from Steps.Result import reportip,reporturl

#Global variable --- 
global err 


#Print name of Tools using pyfiglet 
name()
#call prog   ress bar function
animated_marker(6)


#For Option : using click library 
time.sleep(0.4)
@click.command()
@click.option("--target", prompt=Fore.LIGHTGREEN_EX + "[+] " + Fore.LIGHTYELLOW_EX + """Please enter the target IP/URL """)


#main function
def main(target):
        #check if the input is valid or not 
        time.sleep(0.2)
        try:
                ntarget = socket.gethostbyname(str(target))
                err=0   
        except: 
                err=1


        #Print error input
        error(err,target)


        #Ping test and Print error for ping test
        error_ping(ping_test(ntarget,target),target)
        time.sleep(0.2)

        #copy old report to new folder : old_report
        makecopy()

        #Run script based on target type : ip or url 
        ##################### this is an url  
        if split_target(target) == 1 :

                print(Fore.LIGHTGREEN_EX + "\n--> " + Fore.LIGHTYELLOW_EX + "Your target "+ Fore.LIGHTGREEN_EX + target + Fore.LIGHTYELLOW_EX +" is an URL !!!\n")
                time.sleep(0.2)
                print(Fore.LIGHTCYAN_EX + "="*8 + Fore.LIGHTCYAN_EX + " Start URL Recon " + Fore.LIGHTCYAN_EX + "="*10 +"\n" )
                time.sleep(0.2)

#<-------------------- Domain and sub-domains ------------------------>
                print(Fore.LIGHTGREEN_EX + "[+] " + Fore.LIGHTYELLOW_EX + "Finding domain and sub-domain :")
                #domain_list3r(target)
                time.sleep(0.2)

#<-------------------- dns-recon ------------------------>
                print(Fore.LIGHTGREEN_EX + "[+] " + Fore.LIGHTYELLOW_EX + "Finding DNS records :")
                #dnsrecon(target)
                time.sleep(0.2)

#<-------------------- Check waf ------------------------>
                print(Fore.LIGHTGREEN_EX + "[+] " + Fore.LIGHTYELLOW_EX + "Checking for 'WAF' :")
                #waf(target)
                time.sleep(0.2)

#<-------------------- Check ssl------------------------>
                print(Fore.LIGHTGREEN_EX + "[+] " + Fore.LIGHTYELLOW_EX + "Checking for 'SSL/TLS' :")
                #ssll(target)
                time.sleep(0.2)

#<-------------------- Hidden Content usin ffuf ------------------------>
                print(Fore.LIGHTGREEN_EX + "[+] " + Fore.LIGHTYELLOW_EX + "Checking for Hidden Content : ")
                time.sleep(0.2)        
                # < ---- small ----- >
                print(Fore.LIGHTCYAN_EX + "    --> " + Fore.LIGHTCYAN_EX + "Running "+ Fore.LIGHTGREEN_EX +"ffuf " + Fore.LIGHTCYAN_EX + " ... " )
                #ffufcommon(testhttps(target))
                time.sleep(0.2)        

                # < ---- medium ----- >
                #print(Fore.LIGHTCYAN_EX + "    --> " + Fore.LIGHTCYAN_EX + "Medium research ( slower and medium worldlist ) for more accuracy : ")
                #ffufsmall(testhttps(target))

                time.sleep(0.2)

#<-------------------- Auto Enumeration ------------------------>
                print(Fore.LIGHTGREEN_EX + "[+] " + Fore.LIGHTYELLOW_EX + "Auto Enumeration : ")
                time.sleep(0.2)
                # < ---- whatweb ----- >
                print(Fore.LIGHTCYAN_EX + "    --> " + Fore.LIGHTCYAN_EX + "Running "+ Fore.LIGHTGREEN_EX +"whatweb " + Fore.LIGHTCYAN_EX + " ... " )
                #whatweb(testhttps(target))
                time.sleep(0.2)
                # < ---- webtech ----- >
                print(Fore.LIGHTCYAN_EX + "    --> " + Fore.LIGHTCYAN_EX + "Running "+ Fore.LIGHTGREEN_EX +"webtech " + Fore.LIGHTCYAN_EX + " ... " )
                #webtech(testhttps(target))
                time.sleep(0.2)


#<-------------------- Auto scanning ------------------------>
                print(Fore.LIGHTGREEN_EX + "[+] " + Fore.LIGHTYELLOW_EX + "Auto Scanning : ")
                time.sleep(0.2)
                # < ---- nikto ----- >
                print(Fore.LIGHTCYAN_EX + "    --> " + Fore.LIGHTCYAN_EX + "Running "+ Fore.LIGHTGREEN_EX +"Nikto " + Fore.LIGHTCYAN_EX + " ... " )
                #       nikto(testhttps(target))
                time.sleep(0.2)
                # < ---- nuclei ----- >
                print(Fore.LIGHTCYAN_EX + "    --> " + Fore.LIGHTCYAN_EX + "Running "+ Fore.LIGHTGREEN_EX +"nuclei " + Fore.LIGHTCYAN_EX + " ... " )
                #nuclei(testhttps(target))
                time.sleep(0.2)




        ##################### this is an ip  
        #Convert to ip
        print("\n" + Fore.LIGHTCYAN_EX + "="*8 + Fore.LIGHTCYAN_EX + " Start IP Scanning " + Fore.LIGHTCYAN_EX + "="*10 +"\n" )
        time.sleep(0.2)
        ippp = convert(target)

        #Check if nikto nuclei used ..
        f = checknnn()
        if f != 1 :
                #<-------------------- Auto scanning ------------------------>
                print(Fore.LIGHTGREEN_EX + "[+] " + Fore.LIGHTYELLOW_EX + "Auto Scanning : ")
                time.sleep(0.2)
                # < ---- nikto ----- > 
                print(Fore.LIGHTCYAN_EX + "    --> " + Fore.LIGHTCYAN_EX + "Running "+ Fore.LIGHTGREEN_EX +"Nikto " + Fore.LIGHTCYAN_EX + " ... " )
                #nikto(testhttps(target))
                time.sleep(0.2)
                # < ---- nuclei ----- >
                print(Fore.LIGHTCYAN_EX + "    --> " + Fore.LIGHTCYAN_EX + "Running "+ Fore.LIGHTGREEN_EX +"nuclei " + Fore.LIGHTCYAN_EX + " ... " )
                #nuclei(testhttps(target))
                time.sleep(0.2)

        # < ---- nmap-Port ----- >
        print(Fore.LIGHTGREEN_EX + "[+] " + Fore.LIGHTYELLOW_EX + "Checking open Port and Services/OS version available : ")
        time.sleep(0.2)
        #nmapport(ippp)
        time.sleep(0.2)

        # < ---- Openvass ----- >
        print(Fore.LIGHTGREEN_EX + "[+] " + Fore.LIGHTYELLOW_EX + "Running auto vuln scanner : " +Fore.LIGHTGREEN_EX + "OpenVas")
        time.sleep(0.2)
        #openvas(ippp,target)
        time.sleep(0.2)




        ##################### Report
        print(Fore.LIGHTGREEN_EX + "[+] " + Fore.LIGHTYELLOW_EX + "Generating report ...")
        if split_target(target) != 1 :
                reportip(target)
        else : 
                reporturl(target)
        time.sleep(1)
        print(Fore.LIGHTGREEN_EX +"    Done")
