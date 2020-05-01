#!/usr/bin/env python3


import socket
import json
from classes.protocol import net_protocol
from classes.json_p import *
from classes.login import *
from classes.create import *


serverip = "127.0.0.1"
#host = "192.168.2.210"
port = 5555

host = socket.gethostbyname(socket.gethostname())

send_data = net_protocol
send_data["src"] = host
send_data["dest"] = serverip

cmnd = input(
    "Welcome \n Type /login or /create to get started\nAnything to end Application.\n> ")

if cmnd == "/create":
    send_data = create_account(send_data)
elif cmnd == "/login":
    send_data = login_account(send_data)
    clientname = send_data['user']
else:
    exit()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((serverip, port))

send_data = format_data(send_data)
s.sendall(send_data)
send_data = deformat_data(send_data)


send_data["type"] = "null"


while True:
    data = s.recv(1024)
    recv_data = deformat_data(data)
    if recv_data["type"] == "notification":
        print(recv_data["msg"])
    else:
        print("Unknown Protocol Command")
        break
    send_data["msg"] = input(f"{clientname}> ")
    send_data["type"] = "msg"
    send_data = format_data(send_data)
    s.sendall(send_data)


data = s.recv(1024)
recv_data = json.loads(data.decode('utf-8'))
print(recv_data)
s.sendall(b'establishing Connection')
data = s.recv(1024)
print('Recieved: ', repr(data))
data = input("> ")
data = data.encode('utf-8')
s.sendall(data)
