#!/usr/bin/python
# -*- coding:utf-8 -*-

import socket

class Block():
    def test_socket_modes(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 0设置为非阻塞模式
        # 1设置为阻塞模式
        s.setblocking(1)
        s.settimeout(0.5)
        s.bind(('127.0.0.1', 0))
        socket_address = s.getsockname()
        print "Triaval Server launched on socket: %s" %str(socket_address)
        while True:
            s.listen(1)


if __name__ == '__main__':
    tmp = Block()
    tmp.test_socket_modes()

