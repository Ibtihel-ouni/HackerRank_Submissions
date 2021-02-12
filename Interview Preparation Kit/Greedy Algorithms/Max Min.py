#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    
    n = len(arr)
    arr.sort()
    ans = arr[k-1] - arr[0]
    for i in range(1,n-k+1):
        ans = min(ans , arr[k-1+i] - arr[i])
        
    return ans
