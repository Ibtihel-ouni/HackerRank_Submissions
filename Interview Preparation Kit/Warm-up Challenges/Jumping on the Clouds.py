#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    curr = 0
    while curr < len(c):
        if (curr + 2) < len(c) and (c[curr + 2] == 0):
            jumps += 1
            curr += 2
        elif (curr + 1) < len(c) and (c[curr + 1] == 0):
            jumps += 1
            curr += 1
        else :
            curr += 1
    return jumps
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
