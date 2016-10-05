#!/usr/bin/env python

import socket

def get_remote_machine_info():
    remote_host = 'www.python.org'
    remoteDomainName = socket.getfqdn(remote_host)
    try:
        print("ip address: {}".format(socket.gethostbyname(remote_host)))
        print("Domain Name: {}".format(remoteDomainName))
    except socket.error as error_msg:
        print ("{}: {}".format(remote_host, error_msg))

if __name__ == '__main__':
    get_remote_machine_info()
