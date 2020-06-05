with open('/tmp/ip.txt', 'r') as file:
	ip = file.read().rstrip('\n')


#Configuring hdfs-site.xml file

x = """<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>
<name>dfs.data.dir</name>
<value>/data</value>
</property>

</configuration>"""

#Writing modified contents to hdfs-site.xml
with open('/etc/hadoop/hdfs-site.xml', 'w') as file:
	file.write(x)

#Configuring core-site.xml file


y = """<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>
<name>fs.default.name</name>
<value>hdfs://{}:9001</value>
</property>

</configuration>""".format(ip)

#Writing modified contents to core-site.xml
with open('/etc/hadoop/core-site.xml', 'w') as file:
        file.write(y)
