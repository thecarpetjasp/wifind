#!/usr/bin/env python3 
import os
import colorama
from colorama import Fore, Style
print ("\nFetching info on all connected hosts...\n\n")
ip_gate = os.popen("ip r | sed -n '2p' | grep -oP '\K[^ ]*' | sed -n '1p'").read()
ip_gate = ip_gate.replace("\n", "")
os.system("nmap -sn " + ip_gate + " -Pn 2>&1 | grep '(' > temp.txt")
wifi_list = open("temp.txt").readlines()
if wifi_list[2] == ("Nmap done: 0 IP addresses (0 hosts up) scanned in 0.00 seconds"):
	print ("NO RESULTS! TRY RECONNECTING TO YOUR NETWORK!")
	exit()
ip_list = []
host_list = []
for a in range(2, len(wifi_list) - 1):
	temp_line = (wifi_list[a])
	temp_line = temp_line.replace("\n", "")
	temp_line = os.popen("echo '" + temp_line + "' | grep -oP '[^(]*\K[^)]*' | sed -n 's/(//p'").read()
	temp_line = temp_line.replace("\n", "")
	ip_list.append(temp_line)
for a in range(2, len(wifi_list) - 1):
	temp_line = (wifi_list[a])
	temp_line = temp_line.replace("\n", "")
	temp_line = os.popen("echo '" + temp_line + "' | grep -oP 'Nmap scan report for \K[^ (]*'").read()
	temp_line = temp_line.replace("\n", "")
	host_list.append(temp_line)
for a in range(0 , len(host_list)):
	print (Fore.BLUE + "[" + Fore.RED + str(a + 1) + Fore.BLUE + "] " + Fore.YELLOW + host_list[a] + Style.RESET_ALL + " : " + ip_list[a])
os.system("rm temp.txt")
