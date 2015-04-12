import socket
import sys

clientsok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ipaddr = raw_input("Enter ip address of message server: ")
host = ipaddr

port = 8080

try:
	clientsok.connect((host, port))

	while True:
		tm = clientsok.recv(1024)
		if tm != 'quit':
			print tm
		else:
			clientsok.shutdown(1)
			clientsok.close()
			sys.exit()

except Exception as error:
	e = sys.exc_info()[0]
	print('Error occured while connecting')
