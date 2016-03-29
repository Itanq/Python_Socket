#!/usr/bin/python
# -*- coding:utf-8 -*-

import socket, os
import threading
import SocketServer

server_host = 'localhost'
server_port = 0
buf_size = 1024

echo_msg = raw_input('输入你要发送的消息')

class ForkClient():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connet((ip, port))

    def run(self):
        current_pid = os.getpid()
        print u"PID %s 发送消息给服务器..." % current_pid
        sent_data_length = self.sock.send(echo_msg)
