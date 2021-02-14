#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    current_level = 0
    count = 0
    for i in range(steps):
        if path[i] == 'U':
            current_level += 1
        elif path[i] == 'D':
            current_level -= 1
            if current_level == -1:
                count += 1
    return count
