## A simple socket example written by
# Gauravjeet Singh
# gaurav.ishwerdas@gmail.com

import socket
import sys

## s1, s2
# They both act as client sockets in this example
# s1 sends a string to server socket core
# s2 recieve string of data from server socket core

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s1.connect(('localhost',8084))
	data = raw_input('enter your message: ')
	
	s1.send(data)
	s1.close()
	
	s2.connect(('localhost', 8084))
	data2 = s2.recv(1024)
	print data2
	s2.close()
except Exception:
	print 'Error occured while connecting to core'
	sys.exit()
