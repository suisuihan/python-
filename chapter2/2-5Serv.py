#!/home/zhaoyf/anaconda2/bin/python
# -*- coding:utf-8 -*-
import socket
import time
import os

HOST = ''                 
PORT = 50007         
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
s.bind((HOST, PORT))
s.listen(1)
while True:
    conn, addr = s.accept()
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        print data
        if not data: break
        if data == 'ls':
            data = str(os.listdir(os.path.abspath(os.curdir)))
        elif data == 'date':
            data = str(time.time())
        elif data == 'os':
            data = os.name
        print data
        conn.sendall(data)
    conn.close()
s.close()