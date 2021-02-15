#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    c=0
    
    for i in range (len(q)-1,0,-1):
        if (q[i] != i + 1):
            if(q[i-1] == i + 1):
                c += 1
                q[i-1], q[i] = q[i], q[i-1]
            elif (q[i-2]== i + 1) :
                c+=2
                q[i-2], q[i-1] = q[i-1], q[i-2]
                q[i-1], q[i] = q[i], q[i-1]
            else :
                print("Too chaotic")
                return
                
    print(c)
    
