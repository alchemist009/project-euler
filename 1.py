#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    p = (n-1) // 3
    q = (n-1) // 5
    r = (n-1) // 15
    
    sum = (3 * p * (p+1) // 2) + (5 * q * (q+1) // 2) - (15 * r * (r+1) // 2)
        
    print(sum)