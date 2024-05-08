#!/bin/env python3

import socket
import socket as sk
import random

# valore dei campi nel protocollo IP
IP_PROTOCOL = 1

# valori dei campi nel protocollo ICMP
ICMP_TYPE = 8
ICMP_CODE = 0

# indirizzo del server a cui inviare il ping
IP_ADDR = '8.8.8.8'


def randbyte():
    return random.randint(0, 0xff)


def checksum(msg: bytes) -> (int, int):
    return 0, 0


def build_ping():
    header_nochksum = bytes([ICMP_TYPE, ICMP_CODE])
    data = bytes([randbyte(), randbyte(), randbyte(), randbyte()])
    chksum = checksum(header_nochksum + bytes([0, 0]) + data)
    return header_nochksum + chksum + data


# with sk.socket(sk.AF_INET, sk.SOCK_RAW, IP_PROTOCOL) as ipsocket:
#     # il valore della porta viene ignorato!
#     ipsocket.sendto(build_ping(), (IP_ADDR, 50000))
#     print(ipsocket.recvfrom(2048)[0].hex())

print(sk.IPPROTO_IP)
print(sk.IPPROTO_ICMP)
