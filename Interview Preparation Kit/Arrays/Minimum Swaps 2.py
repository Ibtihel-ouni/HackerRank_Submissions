#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    ref_arr = sorted(arr)
    index_dict = { v : i for i ,v in enumerate(arr)}

    swaps = 0
    
    for i , v in enumerate (arr):
        #correct the value in i if necessary
        correct_value = ref_arr[i]
        if v != correct_value:
            #search for the index of the correct value
            swap_to_index = index_dict[correct_value]
            #switch the values in swap_to_index and i
            arr[swap_to_index] , arr[i] = arr[i] , arr[swap_to_index]
            index_dict[correct_value] = i
            index_dict[v] = swap_to_index
            #increase the swap counter 
            swaps += 1
        
    return swaps    
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
