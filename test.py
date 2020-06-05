num = input("\nEnter the number of datanodes to be setup: ")
print("\nPlease enter the IP(s):")
for i in range(0, int(num)):
	ip = str(input())
        with open('/etc/ansible/hosts', 'r') as file:
        	data = file.read()
        begin = '[slaves]'
        end = '[master]'
        start = data.find(begin) + len(begin)
        stop = data.find(end)
        new_str = data[:start] + "\n" + ip + " ansible_user=root ansible_password=redhat\n" + data[start+1:]
