#!/bin/env python3

import socket as sk

# valore dei campi nel protocollo IP
IP_PROTOCOL = 1

# valori dei campi nel protocollo ICMP
ICMP_TYPE = 8
ICMP_CODE = 0

# indirizzo del server a cui inviare il ping
IP_ADDR = '8.8.8.8'


def carry_around_add(a, b):
    c = a + b
    return (c & 0xffff) + (c >> 16)


def checksum(msg):
    s = 0
    for i in range(0, len(msg), 2):
        w = ord(msg[i]) + (ord(msg[i+1]) << 8)
        s = carry_around_add(s, w)
    return ~s & 0xffff


def build_ping():
    header = bytes([ICMP_TYPE, ICMP_CODE, 0, 0])
    chksum = checksum(header)
    chksum1 = chksum & 0xffff0000
    chksum2 = chksum & 0x0000ffff
    header = bytes([ICMP_TYPE, ICMP_CODE, chksum1, chksum2])


with sk.socket(sk.AF_INET, sk.SOCK_RAW, IP_PROTOCOL) as ipsocket:
    # il valore della porta viene ignorato!
    ipsocket.sendto(build_ping(), (IP_ADDR, 50000))
