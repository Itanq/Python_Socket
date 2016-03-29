#!/usr/bin/python
#-*- coding:utf-8 -*-

import socket, sys
import argparse


host = 'localhost'

class ECHO_CLIENT():
    '''
        简单的回显应用的客服端类
    '''
    def echo_client(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (host, port)
        print u"正在连接到 %s:%s" %server_address
        sock.connect(server_address)

        try:
            message = raw_input('Please input your message: ')
            print u"正在发送中..."
            sock.sendall(message)
            amount_received = 0
            amount_expected = len(message)
            while amount_received < amount_expected:
                data = sock.recv(16)
                amount_received += len(data)
                print u"收到: %s" %data
        except socket.error, e:
            print u"socket异常: %s" %str(e)
        except Exception, e:
            print u"其他异常.."
        finally:
            print u"关闭与服务器的连接..."
            sock.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Socket Server Example")
    parser.add_argument('--port', action="store", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    tmp = ECHO_CLIENT()
    tmp.echo_client(port)
