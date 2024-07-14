#!/bin/python3

import math
import os
import random
import re
import sys

def stringConstruction(s):
    unique_chars = set()
    
    for char in s:
        unique_chars.add(char)
    
    return len(unique_chars)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    n = int(input().strip())
    
    for _ in range(n):
        s = input().strip()
        result = stringConstruction(s)
        fptr.write(str(result) + '\n')
    
    fptr.close()
