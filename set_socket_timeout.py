#!/usr/bin/python
# -*- coding:utf-8 -*-

import socket

class Test_Socket_Timeout():
'''
    获取并设定默认的socket超时时间
'''
    def Timeout(self, time=100):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print "Default socket timeout: ", s.gettimeout()
        s.settimeout(time)
        print "Set socket timeout ", s.gettimeout()

if __name__ == '__main__':
    tmp = Test_Socket_Timeout()
    tmp.Timeout()
