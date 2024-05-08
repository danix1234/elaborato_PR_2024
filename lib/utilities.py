#!/bin/env python3
# -*- coding: utf-8 -*-

import random


def randbyte():
    """
    return random value of lenght 1 byte
    """
    return random.randint(0, 0xff)


def add_carry(x, y):
    """
    sum variable of two bytes with an integer
    """
    x_int = int.from_bytes(x, 'big')
    sum = x_int + y
    return sum


def checksum(raw_msg):
    """
    compute internet checksum on a sequence of bytes,
    and return two bytes representing the checksum
    """
    chksum = 0
    for i in range(0, len(raw_msg), 2):
        elem = raw_msg[i:i+2]
        chksum = add_carry(elem, chksum)
    sum = chksum & 0xffff
    carry = chksum >> 16
    chksum = sum + carry
    chkr = chksum & 0xff
    chkl = (chksum & 0xff00) >> 8
    return bytes([abs(0xff - chkl), abs(0xff-chkr)])
