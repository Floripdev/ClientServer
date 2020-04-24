#!/usr/bin/env python3
import socket
from classes.user import user


host = "127.0.0.1"
port = 5555

clientname = "server"

newUser = user(clientname, 0, host)
print(newUser.getName())
print(newUser.getId())
print(newUser.getIp())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

s.listen()

conn, addr = s.accept()

data = f"Welcome to the chat Server! :) connected to {host} on Port: {port}"
data = data.encode('utf-8')
conn.sendall(data)

while True:
    data = conn.recv(1024)
    if not data:
        break
    print(f"Recieved Data: ${data}")
    conn.sendall(b'Connection established!')

s.close()
