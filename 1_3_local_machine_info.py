#!/usr/bin/env python

import socket
def find_service_name():
    protocolname = 'tcp'

    for port in range(1,1024):
        try:  
            print ("port: {} => service name: {}".format(port,socket.getservbyport(port, protocolname))  )
            print ("port: {} => service name : {}".format(53,socket.getservbyport('udp')) )
        except:
            pass
if __name__=='__main__':
    find_service_name()
    

        
