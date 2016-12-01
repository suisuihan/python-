#!/home/zhaoyf/anaconda2/bin/python
# -*- coding:utf-8 -*-
import socket

port = socket.getservbyname('daytime', 'udp')
print port

# 看不懂题目什么意思 --