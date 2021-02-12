#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    row = [0] * n
    col = [0] * n
    
    for i in range(n):
        for j in range(n):
            row[i] += container[i][j]
            col[i] += container[j][i]
    
    if sorted(col) == sorted(row) :
        return 'Possible'
    else : 
        return 'Impossible'
    
