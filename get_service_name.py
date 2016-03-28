#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

class Server():
'''
    根据端口号来获取服务的名称类
'''
    def find_service_name(self, port):
        service_name = socket.getservbyport(port)
        print "Port: %s => Service Name: %s\n" %(port, service_name)


if __name__ == '__main__':
    tmp = Server()
    tmp.find_service_name(80)
    tmp.find_service_name(25)
    tmp.find_service_name(53)
    tmp.find_service_name(11)
