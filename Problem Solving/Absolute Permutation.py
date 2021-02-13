#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    
    a = list(range(n+1))
    
    if k == 0:
        return a[1:]
    if n % 2 == 1:
        return [-1]
    
    for i in range(1 , n-k+1):
        if a[i] == a[i+k] - k:
            #swap
            a[i] , a[i+k] = a[i+k] , a[i]
        elif abs(a[i] - i) != k:
            return [-1]
    
            
    for i in range(n - k + 1 ,n + 1):
        if abs(a[i] - i) != k:
            return [-1]
        
    return a[1:]
        
