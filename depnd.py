line1 = "export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/"
line2 = "export PATH=/usr/java/jdk1.8.0_171-amd64/bin/:$PATH"

with open('/root/.bashrc', 'r+') as file:
	for line in file:
		if line1 == line:
			print("JAVA_HOME variable already set")
		else:
			print >> file, line1
		if line2 == line:
			print("PATH variable already set")
		else:
			print >> file, line2
			
