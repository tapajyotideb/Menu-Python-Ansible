import os

rpm_pkg = os.system("rpm -q httpd")
if rpm_pkg == 0:
	print("\nRestarting web service...\n")
	os.system("sleep 3")
	os.system("systemctl restart httpd")
else:
	os.system("yum install httpd")
	print("\nStarting the service..\n")
	os.system("systemctl start httpd")
	os.system("iptables -F")

