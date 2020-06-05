with open('/tmp/jip.txt', 'r') as file:
	ip = file.read().rstrip('\n')

x = """<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>
<name>mapred.job.tracker</name>
<value>{}:9002</value>
</property>

</configuration>""".format(ip)

with open('/etc/hadoop/mapred-site.xml', 'w') as file:
        file.write(x)

