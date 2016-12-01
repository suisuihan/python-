#!/home/zhaoyf/anaconda2/bin/python
# -*- coding:utf-8 -*-

import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    data = raw_input('>')
    if not data:
        break
    s.sendall(data)
    data = s.recv(1024)
    print('Received', repr(data))
s.close
