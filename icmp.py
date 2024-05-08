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
    a = (a[0] << 8) | a[1]
    print(a, b)
    c = a + b
    return (c & 0xff) + (c >> 8)


def checksum(msg):
    s = 0
    for i in range(0, len(msg), 2):
        s = carry_around_add(msg[i:i+2], s)
    res = ~s & 0xffff
    return bytes([(res & 0xff00) >> 8, res & 0xff])


def build_ping():
    header = bytes([ICMP_TYPE, ICMP_CODE, 0, 0])
    header = header[0:2] + checksum(header)
    print(header.hex())
    return header


with sk.socket(sk.AF_INET, sk.SOCK_RAW, IP_PROTOCOL) as ipsocket:
    # il valore della porta viene ignorato!
    ipsocket.sendto(build_ping(), (IP_ADDR, 50000))
