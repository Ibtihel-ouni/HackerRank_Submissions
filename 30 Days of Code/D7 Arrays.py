#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    rev_a=[]
    rev_a = arr[::-1]
    s=''

    for i in range(len(rev_a)):
        s += str(rev_a[i])
        s += ' '

    print(s)
