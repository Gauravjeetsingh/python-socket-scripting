import socket
import sys

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ipaddr = raw_input("Enter ip address of your system: ")
host = ipaddr

port = 8080

serversocket.bind((host, port))

serversocket.listen(5)

clientsocket,addr = serversocket.accept()
print("Got a connection from %s" % str(addr))
print('Message Board')

while True:
	message = raw_input(':')
	clientsocket.send(str(message))

	if message == 'quit':
		serversocket.shutdown(1)
		serversocket.close()
		sys.exit()		
