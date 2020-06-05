#! /usr/bin/python3

import subprocess as sp
import os 
import pyfiglet as pf
from pygame import mixer

def ip_input():
	ip1 = input()
	ssh_key = sp.getstatusoutput("ssh-copy-id {}".format(ip1))
	if "WARNING: All keys were skipped" in ssh_key[1]:
		pass
	if sp.getstatusoutput("ping -c 2 {}".format(ip1))[0] == 0:
		return ip1
	else:
		print("IP is down. I repeat, IP is down!!")	

def docker_ip():
	ip = input("Enter ip: ")
	with open('/etc/ansible/hosts', 'r') as file:
		data = file.read()
	begin = '[docker]'
	end = '[end]'
	start = data.find(begin) + len(begin)
	stop = data.find(end)
	new_str = data[:start] + "\n" + ip + " ansible_user=root ansible_password=redhat\n" + data[stop:]
					
	#Writing modified contents to ansible hosts file
	with open('/etc/ansible/hosts', 'w') as file:
		file.write(new_str)

condition = True

try:
	mixer.init()
	mixer.music.load("/root/hello.mp3")
	mixer.music.play()
	while condition:
		os.system("clear")
		print("\n\n")
		#print("\n\t\t\tWelcome to Menu", end = '')
		_fig = pf.Figlet(font='graffiti')
		print(_fig.renderText("Automated Configurator!!"))
		#print("\n\t\t=================================\n\n")
		#mixer.init()
		
		print("""\t\tPress 1: To Capture Photo
		Press 2: To Start a Live Video Stream( with some lag :P)
		Press 3: To Configure a Web Server
		Press 4: To Configure Hadoop Setup
		Press 5: To Configure Docker
		Press 6: Exit\n""")

		ch = input("Enter input: ")
	
		if int(ch) == 1:
			print("Enter ip: ", end='')
			ip = ip_input()
			
			sp.getoutput("scp /root/code/lol.py root@{}:/tmp".format(ip))
			sp.getoutput("ssh root@{} python36 /tmp/lol.py".format(ip))
			sp.getoutput("scp {}:/root/Desktop/abc.png /root/Desktop/".format(ip))
		
		elif int(ch) == 2:
			print("Enter ip: ", end='')
			ip = ip_input()
			
			sp.getoutput("scp /root/video.py root@{}:/tmp".format(ip))
			sp.getoutput("ssh -X root@{} python36 /tmp/video.py".format(ip))
		
		elif int(ch) == 3:
			print("Enter ip: ", end='')
			ip = ip_input()
			
			ssh_key = sp.getoutput("ssh-copy-id {}".format(ip))
			sp.getoutput("scp /root/server.py root@{}:/tmp".format(ip))
			sp.getoutput("ssh root@{} python36 /tmp/server.py".format(ip))
	
		elif int(ch) == 4:
			condition_inside = True
			while condition_inside:
				os.system("clear")
				print("\n\n----------------------Welcome to hadoop installion----------------------------\n\n\n")
				print("""\t\tPress 1: to create namenode
		Press 2: to create datanode
		Press 3: to create client
		Press 4: to create jobtracker
		Press 5: to exit\n""")
				ch1 = input("Enter input: ")
				if int(ch1) == 1:
					print("Enter namenode ip: ", end='')
					ip = str(input())
					
					#Configuring ansible inventory
					with open('/etc/ansible/hosts', 'r') as file:
						data = file.read()
					begin = '[master]'
					end = '[docker]'
					start = data.find(begin) + len(begin)
					stop = data.find(end)
					new_str = data[:start] + "\n" + ip + " ansible_user=root ansible_password=redhat\n" + data[stop:]
					
					#Writing modified contents to ansible hosts file
					with open('/etc/ansible/hosts', 'w') as file:
						file.write(new_str)
					
					os.system("ansible-playbook /root/dependency.yml")
					os.system("ansible-playbook /root/master_node.yml")

				if int(ch1) == 2: 
					num = input("\nEnter the number of datanodes to be setup: ")
					print("\nPlease enter the IP(s):")
					with open("/root/test.txt", "w") as file:
					        file.write('\n')
					for i in range(0, int(num)):
					        ip = str(input())
					        with open("/root/test.txt", "a") as file:
					                file.write(ip + ' ansible_user=root ansible_password=redhat\n')
					with open("/root/test.txt", "r") as file:
					        string = file.read()
					with open('/etc/ansible/hosts', 'r') as file:
					        data = file.read()
					begin = '[slaves]'
					end = '[master]'
					start = data.find(begin) + len(begin)
					stop = data.find(end)
					new_str = data[:start] + string +'\n'  + data[stop:]

					#Writing modified contents to ansible hosts file
					with open('/etc/ansible/hosts', 'w') as file:
					        file.write(new_str)
					
					os.system("ansible-playbook /root/dependency.yml")
					os.system("ansible-playbook /root/slaves.yml")
				if int(ch1) == 3:
					#Configuring ansible inventory
					with open('/etc/ansible/hosts', 'r') as file:
						data = file.read()
					begin = '[client]'
					end = '[end]'
					start = data.find(begin) + len(begin)
					stop = data.find(end)
					new_str = data[:start] + "\n" + ip + " ansible_user=root ansible_password=redhat\n" + data[stop:]
					
					#Writing modified contents to ansible hosts file
					with open('/etc/ansible/hosts', 'w') as file:
						file.write(new_str)
				
					os.system("ansible-playbook /root/dependency.yml")
					os.system("ansible-playbook /root/client.yml")
				if int(ch1) == 4:
					print("Enter jobtracker ip: ", end='')
					ip = str(input())
					
					#Configuring ansible inventory
					with open('/etc/ansible/hosts', 'r') as file:
						data = file.read()
					begin = '[jobtracker]'
					end = '[slaves]'
					start = data.find(begin) + len(begin)
					stop = data.find(end)
					new_str = data[:start] + "\n" + ip + " ansible_user=root ansible_password=redhat\n" + data[stop:]
					
					#Writing modified contents to ansible hosts file
					with open('/etc/ansible/hosts', 'w') as file:
						file.write(new_str)
					os.system("ansible-playbook /root/dependency.yml")
					os.system("ansible-playbook /root/jobtracker.yml")
					
				if int(ch1) == 5:
					condition_inside = False
		elif int(ch) == 5:
			os.system("clear")
			print("\n\n----------------------Welcome to docker installion----------------------------\n\n\n")
			print("""\t\tPress 1: to install Ubuntu-latest
		Press 2: to install centos-latest
		Press 3: to install ubuntu-14.04\n""")
			ch1 = input("Enter your choice: ")
			if int(ch1) == 1:
				docker_ip()
				os.system("ansible-playbook /root/Desktop/docker_ubuntu_latest.yml")
			if int(ch1) == 2:
				docker_ip()
				os.system("ansible-playbook /root/Desktop/docker_centos.yml")
			if int(ch1) == 3:
				docker_ip()
				os.system("ansible-playbook /root/Desktop/docker_ubuntu.yml")
				
		elif int(ch) == 6:
			print("\nOkie Bbye\n")
			condition = False

except (ValueError, EOFError) as e:
	print("\n\n******************Please provide correct input next time!**********************\n")
except KeyboardInterrupt:
	print("\n\nprogram terminated by user\n")

