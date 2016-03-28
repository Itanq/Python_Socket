#/usr/bin/python
#-*- coding:utf-8 -*-

import socket

SEND_BUFF_SIZE = 4096
RECV_BUFF_SIZE = 4096

class Buffer():
    '''
        修改套接字发送和接收缓冲区大小类
    '''
    def modify_buff_size(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
        print "Buffer size [Before]: ", bufsize

        sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
        # 修改发送套接字的缓冲区大小
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUFF_SIZE)
        # 修改接收套接字的缓冲区大小
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUFF_SIZE)
        
        bufsize = sock.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
        print "Buffer size [After]: ", bufsize

if __name__ == '__main__':
    buf = Buffer()
    buf.modify_buff_size()

