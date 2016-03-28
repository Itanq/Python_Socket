#!/usr/bin/python
#! -*- coding: utf-8 -*-

import socket

'''
    获取设备信息的类:
        可获取本地设备的名及IP地址
        可获取远程设备的IP地址
'''
class Machin_Info():

    def get_machin_info(self):
        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)
        print "Host Name: ", host_name
        print "IP Address: ", ip_address

    def get_remote_machin_info(self, remote_host):
        try:
            print remote_host," IP Address: ", socket.gethostbyname(remote_host)
        except socket.error, err_msg:
            print "%s: %s" % (remote_host, err_msg)


if __name__ == '__main__':

    machin_info = Machin_Info()
    remote_machin_info = Machin_Info()

    machin_info.get_machin_info()
    remote_machin_info.get_remote_machin_info('www.baidu.com')
