#!/bin/env python3
# -*- coding: utf-8 -*-

import random


def randbyte() -> int:
    """
    return random value of lenght 1 byte
    """
    return random.randint(0, 0xff)


def checksum(raw_msg: bytes) -> bytes:
    """
    compute internet checksum on a sequence of bytes,
    and return two bytes representing the checksum
    """
    return
