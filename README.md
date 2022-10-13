# auTTest
kali linux tools to automate pentest.


## Tools needed 
Most be already installed : 
```bash
sublis3r
dnsrecon
wafw00f
sslscan
ffuf :
	- /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt 
	- /usr/share/seclists/Discovery/Web-Content/common.txt
whatweb
webtech
Nikto
nuclei
nmap 
OpenVas : 
	- usernmae=admin , password=admin123
	- --socketpath=/var/run/gvmd/gvmd.sock

```

## Modules Installation  


Use the package manager [pip](https://pip.pypa.io/en/stable/) to install modules/tool :

```bash
sudo pip3 install <Module_Name>
```

## Installation

Before the instalation , you must install : :

- Go to auTTest Folder and run :

```bash
sudo Python3 Install_Requir.py
```

- In auTTest Folder run :

```bash
pip install -r requirements.txt
```

- Install auTTest ( in auTTest folder run) :

```bash
sudo pip3 install -e .
```


## Usage
- Just type auTTest in terminal and press enter :
```bash
auTTest
```
- After type your IP/URL.


## Report
- You will find the report of scan in your home dire under   :   ~/auTTest/Report


## Uninstall 

```bash
sudo pip3 uninstall auTTest
```
