
from ctypes import sizeof
from random import randint
import sys
from typing import List, Sized
import time
import numpy as np
#[5,8,4,6,1,2,9,0,3]
#[5,4,8,6,1,2,9,0,3]
#[4,5,8,6,1,2,9,0,3]
arrayOrdenado = [1,2,3,4,5,6,7,8,9,10,11,12]
array = [9,6,5,4,1,2,10,0,3,1,2,7]
sys.setrecursionlimit(10**6)
for i in range (1 , 10000):
    arrayOrdenado.append(i)
    array.append(randint(0,1000))


print("----------------")

def quick(array : List, first = 0, last = len(array) - 1 ):
    
    if(last - first <= 0): # base case
        return array


    pivot = array[last]
    j = first
    i = first
    while i in range(first , last + 1) and j <= i:
        if(array[i] < pivot):
            aux = array[j]
            array[j] = array[i]
            array[i] = aux
            j = j + 1

        i = i + 1    

    pivotPos = j
    
    array[last] = array[pivotPos]
    array[pivotPos] = pivot

    quick(array, first, pivotPos - 1)                                                       
    quick(array, pivotPos + 1, last )                                                       

    return array 

start = time.time()
quick(arrayOrdenado)
end = time.time()

print("time elapsed: " , end - start)
