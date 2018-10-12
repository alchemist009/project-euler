#!/bin/python3

import sys
import math


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    maxPrime = -1

    while n % 2 == 0:
        n = n / 2
        maxPrime = 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n = n / i
    
    if n > 2: 
        maxPrime = n
    
    print(int(maxPrime))