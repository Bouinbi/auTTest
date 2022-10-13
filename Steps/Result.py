from asyncore import read
from dataclasses import dataclass
import imp
import subprocess
import time 
from colorama import Fore
from fpdf import FPDF
import datetime
from datetime import date
from pathlib import Path


def reporturl(target) :
    home = str(Path.home())
    #Creat pdf
    pdf = FPDF()

    #First page : title ...
    pdf.add_page()
    pdf.set_font('Times', 'B', 24)
    pdf.cell(0, 220, 'Scan Report for target', 0, 1, align = 'C')
    pdf.set_font('Times', '', 22)
    pdf.cell(0, -195, target, 0, 1, align = 'C')


    #summary page
    pdf.add_page()
    pdf.set_font('Times', 'B', 22)
    pdf.cell(0, 30, 'Summary', 0, 1, align = 'C')
    pdf.set_font('Arial', '', 14)
    pdf.cell(0, 9, "Domain and Sub-domain", 0, 1, align = 'L',link=1)
    pdf.cell(0, 9, "DNSrecon", 0, 1, align = 'L',link=2)
    pdf.cell(0, 9, "Checking for 'WAF'", 0, 1, align = 'L',link=3)
    pdf.cell(0, 9, "Checking for 'SSL/TLS'", 0, 1, align = 'L',link=4)
    pdf.cell(0, 9, "Checking for Hidden Content", 0, 1, align = 'L',link=5)
    pdf.cell(0, 9, "whatweb", 0, 1, align = 'L',link=6)
    pdf.cell(0, 9, "webtech", 0, 1, align = 'L',link=7)
    pdf.cell(0, 9, "Nikto", 0, 1, align = 'L',link=8)
    pdf.cell(0, 9, "nuclei", 0, 1, align = 'L',link=9)
    pdf.cell(0, 9, "Nmap", 0, 1, align = 'L',link=10)

    #Recon : Subdomains ...
    pdf.add_page()
    pdf.set_font('Times', 'B', 22)
    pdf.ln(h = 5)
    pdf.set_link(1, y = 0.0, page = -1)
    pdf.cell(0, 18, 'Domain and Sub-domain', 0, 1, align = 'L')
    #Read file 
    file = open("{}/auTTest/Output/Recon/domain_sublist3r.txt".format(home), "r") 
    pdf.set_font('Arial', '', 12)
    for g in file: 
        pdf.cell(60, 5, txt = g, ln = 1, align = 'L') 



    #Recon : DNSrecon ...
    pdf.add_page()
    pdf.set_font('Times', 'B', 22)
    pdf.ln(h = 5)
    pdf.set_link(2, y = 0.0, page = -1)
    pdf.cell(0, 18, 'DNSrecon', 0, 1, align = 'L')
    #Read file 
    file = open("{}/auTTest/Output/Recon/dnsrecon.csv".format(home), "r") 
    pdf.set_font('Arial', '', 12)
    for g in file: 
        pdf.cell(60, 5, txt = g, ln = 1, align = 'L') 


    #Checking for 'WAF'
    pdf.add_page()
    pdf.set_font('Times', 'B', 22)
    pdf.ln(h = 5)
    pdf.set_link(3, y = 0.0, page = -1)
    pdf.cell(0, 18, 'Checking for "WAF"', 0, 1, align = 'L')
    #Read file 
    file = open("{}/auTTest/Output/Check/waf.txt".format(home), "r") 
    pdf.set_font('Arial', '', 12)
    for g in file: 
        pdf.cell(60, 5, txt = g, ln = 1, align = 'L') 
    #Checking for SSL/TLS
    pdf.set_font('Times', 'B', 22)
    pdf.ln(h = 10)
    pdf.set_link(4, y = 0.0, page = -1)
    pdf.cell(0, 18, 'Checking for "SSL/TLS"', 0, 1, align = 'L')
    #Read file 
    file = open("{}/auTTest/Output/Check/ssl.txt".format(home), "r") 
    pdf.set_font('Arial', '', 12)
    for g in file: 
        pdf.cell(60, 5, txt = g, ln = 1, align = 'L') 


    #Checking for Hidden Content
    #Common list
    pdf.add_page()
    pdf.set_font('Times', 'B', 22)
    pdf.ln(h = 8)
    pdf.cell(0, 8, 'Hidden Content', 0, 1, align = 'L')
    pdf.set_font('Times', 'B', 14)
    pdf.set_link(5, y = 0.0, page = -1)
    pdf.cell(0, 12, 'Using Common list ...', 0, 1, align = 'L')
    #Read file 
    file = open("{}/auTTest/Output/Bruteforce/ffcommon.txt".format(home), "r") 
    pdf.set_font('Arial', '', 12)
    for g in file: 
        pdf.cell(60, 6, txt = g, ln = 1, align = 'L') 
    #Small list
    pdf.ln(h = 10)
    pdf.set_font('Times', 'B', 14)
    pdf.cell(0, 12, 'Using Medium list ...', 0, 1, align = 'L')
    #Read file 
    file = open("{}/auTTest/Output/Bruteforce/ffsmall.txt".format(home), "r") 
    pdf.set_font('Arial', '', 12)
    for g in file: 
        pdf.cell(60, 6, txt = g, ln = 1, align = 'L') 


    #whatweb
    pdf.add_page()
    pdf.set_font('Times', 'B', 22)
    pdf.ln(h = 5)
    pdf.set_link(6, y = 0.0, page = -1)
    pdf.cell(0, 18, 'whatweb', 0, 1, align = 'L')
    #Read file 
    file = open("{}/auTTest/Output/Autoenum/whatweb.txt".format(home), "r") 
    pdf.set_font('Arial', '', 12)
    for g in file: 
        pdf.multi_cell(190, 7, txt = g,align = 'L') 


    #webtech
    pdf.set_font('Times', 'B', 22)
    pdf.ln(h = 5)
    pdf.set_link(7, y = 0.0, page = -1)
    pdf.cell(0, 18, 'webtech', 0, 1, align = 'L')
    #Read file 
    file = open("{}/auTTest/Output/Autoenum/webtech.txt".format(home), "r") 
    pdf.set_font('Arial', '', 12)
    for g in file: 
        pdf.cell(60, 5, txt = g, ln = 1, align = 'L') 



    #Nikto
    pdf.add_page()
    pdf.set_font('Times', 'B', 22)
    pdf.ln(h = 5)
    pdf.set_link(8, y = 0.0, page = -1)
    pdf.cell(0, 18, 'Nikto', 0, 1, align = 'L')
    #Read file 
    file = open("{}/auTTest/Output/Autoscan/nikto.txt".format(home), "r") 
    pdf.set_font('Arial', '', 12)
    for g in file: 
        pdf.multi_cell(190, 7, txt = g, border=1,align = 'L') 


    #nuclei
    pdf.add_page()
    pdf.set_font('Times', 'B', 22)
    pdf.ln(h = 5)
    pdf.set_link(9, y = 0.0, page = -1)
    pdf.cell(0, 18, 'nuclei', 0, 1, align = 'L')
    #Read file 
    file = open("{}/auTTest/Output/Autoscan/nuclei.txt".format(home), "r") 
    pdf.set_font('Arial', '', 12)
    for g in file: 
        pdf.multi_cell(190, 7, txt = g, border=1,align = 'L') 


    #nmap
    pdf.add_page()
    pdf.set_font('Times', 'B', 22)
    pdf.ln(h = 5)
    pdf.set_link(10, y = 0.0, page = -1)
    pdf.cell(0, 18, 'nmap', 0, 1, align = 'L')
    #Read file 
    file = open("{}/auTTest/Output/Portscan/nmapport.txt".format(home), "r") 
    pdf.set_font('Arial', '', 12)
    for g in file: 
        pdf.multi_cell(190, 6, txt = g,align = 'L')


    #Fin
    dat = date.today()
    pdf.output('{}/auTTest/Report/report-{}-{}.pdf'.format(home,target,dat), 'F')


def reportip(target) :

    #Creat pdf
    pdf = FPDF()
    home = str(Path.home())
    #First page : title ...
    pdf.add_page()
    pdf.set_font('Times', 'B', 24)
    pdf.cell(0, 220, 'Scan Report for target', 0, 1, align = 'C')
    pdf.set_font('Times', '', 22)
    pdf.cell(0, -195, target, 0, 1, align = 'C')


    #summary page
    pdf.add_page()
    pdf.set_font('Times', 'B', 22)
    pdf.cell(0, 30, 'Summary', 0, 1, align = 'C')
    pdf.set_font('Arial', '', 14)
    pdf.cell(0, 9, "Nikto", 0, 1, align = 'L',link=8)
    pdf.cell(0, 9, "nuclei", 0, 1, align = 'L',link=9)
    pdf.cell(0, 9, "Nmap", 0, 1, align = 'L',link=10)

    #Nikto
    pdf.add_page()
    pdf.set_font('Times', 'B', 22)
    pdf.ln(h = 5)
    pdf.set_link(8, y = 0.0, page = -1)
    pdf.cell(0, 18, 'Nikto', 0, 1, align = 'L')
    #Read file 
    file = open("{}/auTTest/Output/Autoscan/nikto.txt".format(home), "r") 
    pdf.set_font('Arial', '', 12)
    for g in file: 
        pdf.multi_cell(190, 7, txt = g, border=1,align = 'L') 


    #nuclei
    pdf.add_page()
    pdf.set_font('Times', 'B', 22)
    pdf.ln(h = 5)
    pdf.set_link(9, y = 0.0, page = -1)
    pdf.cell(0, 18, 'nuclei', 0, 1, align = 'L')
    #Read file 
    file = open("{}/auTTest/Output/Autoscan/nuclei.txt".format(home), "r") 
    pdf.set_font('Arial', '', 12)
    for g in file: 
        pdf.multi_cell(190, 7, txt = g, border=1,align = 'L') 


    #nmap
    pdf.add_page()
    pdf.set_font('Times', 'B', 22)
    pdf.ln(h = 5)
    pdf.set_link(10, y = 0.0, page = -1)
    pdf.cell(0, 18, 'nmap', 0, 1, align = 'L')
    #Read file 
    file = open("{}/auTTest/Output/Portscan/nmapport.txt".format(home), "r") 
    pdf.set_font('Arial', '', 12)
    for g in file: 
        pdf.multi_cell(190, 6, txt = g,align = 'L')


    #Fin
    dat = date.today()
    pdf.output('{}/auTTest/Report/report-{}-{}.pdf'.format(home,target,dat), 'F')


