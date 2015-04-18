## A simple socket example written by
# Gauravjeet Singh
# gaurav.ishwerdas@gmail.com

import socket
import sys

##Core
#
## A socket which acts as a server socket for this example
## Clients s1 and s2 gets connected to it
## Receive a string from s1 and send the same but modified string to s2

core = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	core.bind(('localhost', 8084))

	core.listen(2)
	s1,addr = core.accept()
	data = s1.recv(1024)
	data = '[tested message] ' + data

	s2, addr2 = core.accept()

	s2.send(str(data))

except KeyboardInterrupt:
	print "Good bye"
	sys.exit()
