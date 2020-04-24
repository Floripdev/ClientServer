#!/usr/bin/env python3

import socket

sys.path.append('../help_classes')

host = "127.0.0.1"
port = 5555

clientname = input("Insert Name: ")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))
data = s.recv(1024)
print(data)
s.sendall(b'establishing Connection')
data = s.recv(1024)
print('Recieved: ', repr(data))
data = input("> ")
data = data.encode('utf-8')
s.sendall(data)
