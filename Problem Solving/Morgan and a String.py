#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the morganAndString function below.
def morganAndString(a, b):

    a_list = list(a)
    b_list = list(b)
    a_list.append('|')
    b_list.append('|')
    answer_list = list()
    answer_size = len(a_list) + len(b_list)
    counter, a_pointer, b_pointer = 0, 0, 0
    skip = False
    storage_counters = []
    a_previous, b_previous = '',''
    while len(answer_list) < answer_size:
        if not skip:
            if a_pointer == len(a_list):
                answer_list.extend(b_list[b_pointer:])
                break
            if b_pointer == len(b_list):
                answer_list.extend(a_list[a_pointer:])
                break

            a_letter = a_list[a_pointer + counter]
            b_letter = b_list[b_pointer + counter] 
            
            if ord(a_letter) == ord(b_letter):
                if counter == 0:
                    a_previous = a_letter
                    b_previous = b_letter 
                else:
                    a_previous = a_list[a_pointer + counter -1]
                    b_previous = b_list[b_pointer + counter -1]
                if(a_letter != a_previous or b_letter != b_previous):
                    storage_counters.append(counter)

                if a_pointer + counter == len(a_list) -1 or b_pointer + counter == len(b_list) -1 :
                    skip = True
                    a_letter = "A"
                    b_letter = "B"
                    continue
                counter += 1
                continue
        skip = False
        counter = 0
        if ord(a_letter) < ord(b_letter):
            if(len(storage_counters) !=0) :
                       # print(storage_counters)
                breakpoint = storage_counters[0]
                       # print("Breakpoint: ",breakpoint," a_list[a_pointer : a_pointer + breakpoint])",a_list[a_pointer : a_pointer + breakpoint])
                answer_list.extend(a_list[a_pointer : a_pointer + breakpoint])
                a_pointer += breakpoint
                storage_counters.clear()
                       # print("a_list: ",a_list[a_pointer:])
            else:
                answer_list.append(a_list[a_pointer])
                a_pointer += 1
        else:
            if(len(storage_counters) !=0) :
                        #print(storage_counters)
                breakpoint = storage_counters[0]
                       # print("Breakpoint: ",breakpoint," b_list[b_pointer : b_pointer + breakpoint]",b_list[b_pointer : b_pointer + breakpoint])
                answer_list.extend(b_list[b_pointer : b_pointer + breakpoint])
                b_pointer += breakpoint
                storage_counters.clear()
                        #print("b_list: ",b_list[b_pointer:])
            else:
                answer_list.append(b_list[b_pointer])
                b_pointer += 1
    answer_list.pop()
    answer_list.pop()
    return ''.join(answer_list)
