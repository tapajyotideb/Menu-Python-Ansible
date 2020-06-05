string = "\nexport JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/\nexport PATH=/usr/java/jdk1.8.0_171-amd64/bin/:$PATH" 
with open("/root/.bashrc", "r") as file:
	content = file.read()
if string not in content:
	with open("/root/.bashrc", "a") as file:
		file.write(string)
else:
	pass
