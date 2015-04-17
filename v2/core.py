import socket
import sys

core = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	core.bind(('localhost', 8084))

	core.listen(2)

	s1,addr = core.accept()

	data = s1.recv(1024)

	data = '[tested message] ' + data

	s2, addr2 = core.accept()

	s2.send(str(data))

	sys.exit()
except KeyboardInterrupt:
	print "Good bye"
	sys.exit()
