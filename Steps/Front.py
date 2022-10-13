from ast import Break
from cProfile import label
from gc import callbacks
import imp
from multiprocessing.reduction import DupFd
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
import sys
import os
from responses import target
import re
from sqlalchemy import except_, false
import subprocess



#Print name of Tools using pyfiglet 
def name() :
    print(Fore.LIGHTGREEN_EX  + '\n')
    f = Figlet(font='big')
    init(autoreset=True)
    print(f.renderText("auT - Test  \t"))
    print(Fore.LIGHTGREEN_EX + "[*] " + Fore.LIGHTYELLOW_EX  + 'v1.1')
    time.sleep(0.1)
    init(autoreset=True)
    print(Fore.LIGHTGREEN_EX + "[*] " + Fore.LIGHTYELLOW_EX + 'https://github.com/Bouinbi')
    time.sleep(0.1)
    print(Fore.LIGHTGREEN_EX + "[*] " + Fore.LIGHTYELLOW_EX + str(datetime.datetime.now()) + "\n")
    time.sleep(0.3)



#Function to Print Progress Bar :
def animated_marker(x):
    widgets = [Fore.LIGHTGREEN_EX + "[+] " + Fore.LIGHTYELLOW_EX +'Loading :  ', progressbar.AnimatedMarker()]
    init(autoreset=True )
    bar = progressbar.ProgressBar(widgets=widgets).start()
    for i in range(x):
        time.sleep(0.1)
        bar.update(i)   
    print("")

"""
def install() : 
    cmd1 = "mkdir -p ~/auTTest/Output/Autoenum ~/auTTest/Output/Autoscan ~/auTTest/Output/Bruteforce ~/auTTest/Output/Check ~/auTTest/Output/Openvass ~/auTTest/Output/Portscan ~/auTTest/Output/Recon  "
    proc = subprocess.Popen(
            # Let it ping more times to run longer.
            cmd1,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True )
    time.sleep(0.4)
    while proc.poll() is None:
        time.sleep(0.1)
"""