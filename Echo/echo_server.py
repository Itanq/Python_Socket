#!/usr/bin/python
#-*- coding:utf-8 -*-

import socket
import sys
import argparse


host = 'localhost'
data_payload = 2048

class ECHO_SERVER():
    '''
        简单的回显应用的服务端类
    '''
    def echo_server(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_address = (host, port)
        print u"开始启动回显应用服务器在 %s:%s\n" % server_address
        sock.bind(server_address)
        sock.listen(5)
        while True:
            print u"等待接收客服端的信息..."
            client, address = sock.accept()
            data = client.recv(data_payload)
            if data:
                print "Data: %s" %data
                client.send(data)
                print u"%s bytes 数据返回到 %s" %(data, address)
            client.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    tmp = ECHO_SERVER()
    tmp.echo_server(port)

