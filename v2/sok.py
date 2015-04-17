import socket
import sys

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s1.connect(('localhost',8084))

data = raw_input('enter your message: ')

s1.send(data)
s1.close()

s2.connect(('localhost', 8084))
data2 = s2.recv(1024)
print data2
s2.close()
