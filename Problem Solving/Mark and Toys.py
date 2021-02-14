#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    i = 0
    sum = 0
    prices.sort()
    while sum < k:
        sum = sum + prices[i]
        i += 1
    return i - 1
