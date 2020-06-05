import subprocess as sp

with open('/tmp/ip.txt', 'r') as file:
	ip = file.read().rstrip('\n')

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
        
jt_ip = sp.getoutput("ifconfig | grep inet | cut -d: -f2 | awk {'print $2'} | head -1")

x = """<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>
<name>mapred.job.tracker</name>
<value>{}:9002</value>
</property>

</configuration>""".format(jt_ip)

with open('/etc/hadoop/mapred-site.xml', 'w') as file:
        file.write(x)

