#!/bin/env python3
# -*- coding: utf-8 -*-

import socket as sk
from utilities import randbyte, checksum


def ping(ip_addr: str) -> bytes | str:
    """
    send ping request to ip address specified, using ICMP protocol (type 8)

    ICMP protocol is specified as follows (for ping requests):
    ------------------------------------------
    | type (1B) | code (1B) | checksum (2B)  |
    | identifier (2B) | sequence number (2B) |
             payload data (4B*n)
    ------------------------------------------
    - type and code specify the type of ICMP
    - checksum is the internet checksum on the entire ICMP packet
    - identifier and sequence are used to know what a ICMP answers to
    - payload data is optional data of len multiple of 4B
    """
    # initialize ICMP raw message
    type = bytes([8])
    code = bytes([0])
    chksum = bytes([0, 0])  # will be calculated later on
    id = bytes([randbyte(), randbyte()])
    seq = bytes([randbyte(), randbyte()])
    chksum = checksum(type + code + chksum + id + seq)
    ICMP_msg = type + code + chksum + id + seq

    # create a ipv4 socket, which uses ICMP protocol
    with sk.socket(sk.AF_INET, sk.SOCK_RAW, sk.IPPROTO_ICMP) as ipsocket:
        ipsocket.sendto(ICMP_msg, (ip_addr, 55_555))
        ipsocket.recvfrom(2048)[0].hex()

    return None


ping('8.8.8.8')
