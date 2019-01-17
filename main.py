#!/usr/bin/env python3
import socket
from datetime import datetime

remote_host = input('Remote host: ')
ports_from = input("Ports from: ")
ports_to = input("Ports to: ")

t1 = datetime.now()

remote_ip = socket.gethostbyname(remote_host)

try:
	for port in range(int(ports_from), int(ports_to)+1):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = s.connect_ex((remote_host, port))
		if result == 0:
			print(str(port) + ' is opened.')
		s.close()
except socket.error:
	print('Couldn\'nt connect to remote host')

t2 = datetime.now()
print('Scan completed in ' + str(t2 - t1) + ' .')