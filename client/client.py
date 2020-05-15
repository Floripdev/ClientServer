#!/usr/bin/env python3


import socket
import json
import random
import string
from termcolor import colored, cprint
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

autoform = net_protocol
autoform["user"] = ''.join(random.choice(
    string.ascii_letters) for i in range(8))
autoform["passwd"] = ''.join(random.choice(
    string.ascii_letters) for i in range(8))
autoform["src"] = host
autoform["dest"] = serverip
autoform["type"] = "init_create"
autoform["msg"] = "null"


cmnd = input(
    "****Welcome**** \nType 1: login or\nType 2: create to get started\nType 3: login autoform\nAnything to end Application/debug create user.\n> ")

if cmnd == "1":
    send_data = login_account(send_data)
elif cmnd == "2":
    send_data = create_account(send_data)
elif cmnd == "3":
    send_data = autoform
else:
    exit()


clientname = send_data['user']

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
        cprint(recv_data["msg"], 'blue')
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
