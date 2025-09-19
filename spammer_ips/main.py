#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getSpammerIPs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ip
#  2. INTEGER_ARRAY timestamp
#  3. INTEGER k
#  4. INTEGER t
#

def getSpammerIPs(ip, timestamp, k, t):
    # Write your code here
    ip_list = {}
    spam_ips = []
    print("k:", k, "t:", t)

    for x in range(len(ip)):
        current_ip = ip[x]
        current_time = timestamp[x]

        if current_ip not in ip_list:
            ip_list[current_ip] = []

        ip_list[current_ip].append(current_time)

    print(ip_list)

    for ips, times in ip_list.items():
        times.sort()
        counter = 1
        for y in range(len(times)-1):
            current = times[y]
            #print(current)
            next_time = times[y+1]
            #print("current - next = ", abs(current - next_time))
            if abs(current - next_time) <= t:
                counter+=1
                print("count for ip", ips, "is: ", counter)
                if counter >= k:
                    spam_ips.append(ips)
                    break
    
    return spam_ips


if __name__ == '__main__':
    #fptr = open(os.environ['out.txt'], 'w')

    ip_count = int(input().strip())

    ip = []

    for _ in range(ip_count):
        ip_item = int(input().strip())
        ip.append(ip_item)

    timestamp_count = int(input().strip())

    timestamp = []

    for _ in range(timestamp_count):
        timestamp_item = int(input().strip())
        timestamp.append(timestamp_item)

    k = int(input().strip())

    t = int(input().strip())

    result = getSpammerIPs(ip, timestamp, k, t)

    print(result)
