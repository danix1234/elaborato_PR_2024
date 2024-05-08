#!/bin/env python3
# -*- coding: utf-8 -*-

import random


def randbyte() -> int:
    """
    return random value of lenght 1 byte
    """
    return random.randint(0, 0xff)


def add_carry(x: bytes, y: int) -> int:
    x_int = int.from_bytes(x, 'big')
    sum = x_int + y
    return (sum & 0xff_ff) + (sum & 0x1_00_00)


def checksum(raw_msg: bytes) -> bytes:
    """
    compute internet checksum on a sequence of bytes,
    and return two bytes representing the checksum
    """
    chksum = 0
    for i in range(0, len(raw_msg), 2):
        elem = raw_msg[i:i+2]
        chksum += add_carry(elem, chksum)
    return ~chksum
