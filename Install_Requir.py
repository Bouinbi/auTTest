import subprocess

####################### Requir

#install progressbar
net = "sudo pip install progressbar" 
subprocess.run(net,shell=True)
print("#"*77)


#install gnome-terminal
net = "sudo apt-get install gnome-terminal" 
subprocess.run(net,shell=True)
print("#"*77)


cmd1 = "mkdir -p ~/auTTest/Output/Autoenum ~/auTTest/Output/Autoscan ~/auTTest/Output/Bruteforce ~/auTTest/Output/Check ~/auTTest/Output/Openvass ~/auTTest/Output/Portscan ~/auTTest/Output/Recon ~/auTTest/Report ~/auTTest/Old_Report "
subprocess.run(cmd1,shell=True)
print("#"*77)

