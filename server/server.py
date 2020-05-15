#!/usr/bin/env python3
import socket
import json
import sys
from termcolor import colored, cprint
from tinydb import *
from classes.db_handler import *
from classes.user import user
from classes.protocol import net_protocol
from classes.json_p import *
from classes.create import *
from classes.login import *
from classes.msg import *

db_filepath = 'database/db.json'

db = db_handler(db_filepath)


host_ip = "127.0.0.1"
# host = "192.168.2.210"
port = 5555
hostname = "SecureChat"

db.define_server_parameters(hostname, host_ip, port)


server_entry = db.get_server_info()

cprint("*********************************", 'cyan')
cprint(f"* Server Name: {server_entry.get('name')}\t*", 'cyan')
cprint(f"* Server IP: {server_entry.get('ip')}\t\t*", 'cyan')
cprint("*********************************", 'cyan')
cprint("Server Status: Online", 'green', attrs=['blink'])

send_data = net_protocol
recv_data = net_protocol

# Prepare sending protocol
send_data["src"] = server_entry.get('ip')
send_data["user"] = server_entry.get('name')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Reuse Addr if not closed properly
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((host_ip, port))

s.listen()

conn, addr = s.accept()

data_init = conn.recv(1024)

recv_data = deformat_data(data_init)
# user_entry = db.get_user_info(recv_data['user'])
if recv_data["type"] == "init_create":
    cprint(
        f">Create User Request, from Client {recv_data['src']}", 'blue')
    db.insert_new_user(recv_data, 1)
    user_entry = db.get_user_info(recv_data['user'])
    send_data = msg_welcome(server_entry, user_entry)
elif recv_data["type"] == "init_login":  # todo
    code = db.user_login(recv_data)
    if code == "wrong_user":
        recv_data = msg_invalid_user(recv_data)
    elif code == "wrong_password":
        recv_data = msg_invalid_password(recv_data)
        conn.close()
    else:
        user_entry = db.get_user_info(recv_data['user'])
        recv_data = msg_welcome(server_entry, user_entry)

else:
    print("Recieved false INIT-Package, closing connection")
    conn.close()

send_data = format_data(send_data)
conn.sendall(send_data)

while True:
    print("hello")
    recv_data = conn.recv(1024)
    recv_data = deformat_data(recv_data)

    if not recv_data:
        break
    elif recv_data["type"] == "msg":
        print(f" Recieved Message: ")
        print(recv_data["msg"])


s.close()
