#!/usr/bin/env python3
import socket
import json
import sys
from tinydb import *
from classes.user import user
from classes.protocol import net_protocol
from classes.json_p import *
from classes.create import *
from classes.login import *
from classes.msg import *

db = TinyDB('server/database/db.json')


host = "127.0.0.1"
# host = "192.168.2.210"
port = 5555
servername = "SecureChat"

server_query = Query()

if not db.search(server_query.id == 0):
    db.insert({'id': 0, 'name': servername, 'ip': host, 'port': port})
else:
    db.update({'ip': host}, server_query.id == 0)
    db.update({'name': servername}, server_query.id == 0)


server_entry = db.get(server_query.id == 0)
print(f"Server Name: {server_entry.get('name')}")
print(f"Server ID: {server_entry.get('id')}")
print(f"Server IP: {server_entry.get('ip')}")

data = net_protocol
recv_data = net_protocol

data["src"] = server_entry.get('ip')
data["user"] = server_entry.get('name')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Reuse Addr if not closed properly
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((host, port))

s.listen()

conn, addr = s.accept()

data_init = conn.recv(1024)

recv_data = deformat_data(data_init)
if recv_data["type"] == "init_create":
    print(
        f"Successfully recieved INIT-Create-Package from Client {recv_data['src']}")
    create(recv_data, db)
    user_entry = db.get(server_query.name == recv_data['user'])
    data = msg_welcome(server_entry, user_entry, data)
    print("finished")
elif recv_data["type"] == "init_login":
    code = login(recv_data, db)
    if code == "wrong_user":
        data = msg_invalid_user(data, recv_data['ip'])
    elif code == "wrong_password":
        data = msg_invalid_password(data, recv_data['user'])
    else:
        user_entry = db.get(server_query.name == recv_data['user'])
        data = msg_welcome(server_entry, user_entry, data)

else:
    print("Recieved false INIT-Package, closing connection")
    conn.close()

send_data = format_data(data)
conn.sendall(send_data)

while True:
    print("hello")
    data = conn.recv(1024)
    recv_data = deformat_data(data)

    if not recv_data:
        break
    elif recv_data["type"] == "msg":
        print(f" Recieved Message: ")
        print(recv_data["msg"])


s.close()
