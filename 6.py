#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    sumSquares = n * (n+1) * (2 * n + 1) // 6
    
    squareSums = (n * (n+1) // 2) ** 2
    
    print(abs(sumSquares - squareSums))