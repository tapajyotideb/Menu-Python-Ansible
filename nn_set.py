import subprocess

#Configuring hdfs-site.xml file
with open('/etc/hadoop/hdfs-site.xml', 'r') as file:
	data = file.read()
begin = '<configuration>'
end = '</configuration>'
replace = "\n\n<property>\n<name>dfs.name.dir</name>\n<value>/nn</value>\n</property>\n\n"
start = data.find(begin) + len(begin)
stop = data.find(end)
new_str = data[:start] + replace + data[stop:]

#Writing modified contents to hdfs-site.xml
with open('/etc/hadoop/hdfs-site.xml', 'w') as file:
	file.write(new_str)

#Capturing IP from the system
nn_ip = subprocess.getoutput("ifconfig | grep inet | cut -d: -f2 | awk {'print $2'} | head -1")

#Configuring core-site.xml file
with open('/etc/hadoop/core-site.xml', 'r') as file:
        data = file.read()
replace = f"\n\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{nn_ip}:9001</value>\n</property>\n\n"
start = data.find(begin) + len(begin)
stop = data.find(end)
new_str = data[:start] + replace + data[stop:]

#Writing modified contents to core-site.xml
with open('/etc/hadoop/core-site.xml', 'w') as file:
        file.write(new_str)
