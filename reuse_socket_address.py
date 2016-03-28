#!/usr/bin/python
# -*- coding:utf-8 -*-

import socket
import sys

class ReuseSocketAddress():
    def reuse_socket_address(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        old_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
        print "Old socket state: ", old_state

        # 激活套接字重用
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        new_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
        print "New socket state: ", new_state


        local_port = 8282
        srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind(('', local_port))
        srv.listen(1)
        print "Listen On Port: ", local_port
        while True:
            try:
                connection, addr = srv.accept()
                print "Connect by %s:%s"%(addr[0],addr[1])
            except KeyboardInterrupt:
                break
            except socket.error, msg:
                print '%s' % msg

if __name__ == '__main__':
    tmp = ReuseSocketAddress()
    tmp.reuse_socket_address()
