#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    
    n = len(c)
    if k >= n :
        return sum(c)
    c.sort(reverse = True)
    cost = 0
    quo = 0
    rem = n
    while rem >= k :
        cost += (quo+1) * sum(c[quo*k:(quo+1)*k])
        quo += 1
        rem -= k
    if rem > 0 :
        cost += (quo + 1) * sum(c[quo * k:])
    return cost
