#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    res = 2
    a = []
    a.append(1)
    a.append(2)

    i = 1
    
    while a[i] < n:
        i += 1
        a.append(a[i-1] + a[i-2])
        if a[i] > n:
            a.pop()
            break
        if a[i] % 2 == 0:
            res += a[i]
    #print(a)
    print(res)