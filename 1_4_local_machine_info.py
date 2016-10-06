#!/usr/bin/env python

import socket
import time
import ntplib


def get_remote_machine_info():
    remote_host = 'ie.pool.ntp.org'
    remoteDomainName = socket.getfqdn(remote_host)
    try:
        print("ip address: {}".format(socket.gethostbyname(remote_host)))
        print("Domain Name: {}".format(remoteDomainName))
    except socket.error as error_msg:
        print ("{}: {}".format(remote_host, error_msg))


def print_time():
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request('ie.pool.ntp.org') #student.litdom.lit.ie
    timedelta = time.time() - response.tx_time
    System_time = (time.ctime())
    NTP_time = (time.ctime(response.tx_time))

    print ("Current system time : ", System_time)
    print ("NTP server time : ", NTP_time)
    print ("Time Delta : ", timedelta)
    
if __name__ == '__main__':
    get_remote_machine_info()
    print_time()
    
        
