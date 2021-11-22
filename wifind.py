#!/usr/bin/env python3 
import os
import time
import colorama
from colorama import Fore, Style
print ("\nFETCHING ALL CONNECTED HOSTS...\n")
ip_gate = os.popen("ip r | sed -n '2p' | grep -oP '\K[^ ]*' | sed -n '1p'").read()
ip_gate = ip_gate.replace("\n", "")
os.system("nmap -sn " + ip_gate + " -Pn 2>&1 | grep '(' > temp.txt")
wifi_list = open("temp.txt").readlines()
wifi_error = (wifi_list[2])
wifi_error = wifi_error.replace("\n", "")
if (wifi_error) == ("Nmap done: 0 IP addresses (0 hosts up) scanned in 0.00 seconds"):
	print ("NO RESULTS! TRY RECONNECTING TO YOUR NETWORK!")
	os.system("rm temp.txt")
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
def split(word):
	return [char for char in word]
for a in range(0 , len(host_list)):
	len_check = split(host_list[a])
	if len(len_check) < 13:
		space = ("		:	")
	else:
		space = ("	:	")
	print (Fore.BLUE + "[" + Fore.RED + str(a + 1) + Fore.BLUE + "] " + Fore.YELLOW + host_list[a] + Style.RESET_ALL + space + ip_list[a])
print("\nFETCHING ALL OPEN PORTS...\n")
time.sleep(1)
for a in range(0, len(host_list)):
	print (Fore.BLUE + "[" + Fore.RED + str(a + 1) + Fore.BLUE + "] " + Fore.YELLOW + host_list[a] + Style.RESET_ALL + " : " + ip_list[a])
	os.system("nmap " + ip_list[a] + " | grep 'open'")
os.system("rm temp.txt")
