#!/bin/python3

import os

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  
    left = [x for x in arr if x < pivot]      
    middle = [x for x in arr if x == pivot]   
    right = [x for x in arr if x > pivot]    
    
    return quickSort(left) + middle + quickSort(right)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    
    result = quickSort(arr)
    
    fptr.write(' '.join(map(str, result)) + '\n')
    
    fptr.close()
