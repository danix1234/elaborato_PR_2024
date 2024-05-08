#!/bin/env python3
# -*- coding: utf-8 -*-

import sys
from lib.ping import check_status


ip_addr = sys.argv[1:]

# quit if no ip are passed from command line
if len(ip_addr) == 0:
    print('no ip address where passed')
    exit(0)

# check all ip statuses
for i in range(len(ip_addr)):
    ip_status = check_status(ip_addr[i])
    if ip_status is None:
        print(ip_addr[i] + ': is online')
    else:
        print(ip_addr[i] + ': is offline ---> ' + ip_status)
