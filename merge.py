
from ctypes import sizeof
from random import randint
from typing import List, Sized
import time
import numpy as np
array = [9,6,5,4,1,2,10,0,3,1,2,7]
#[5,8,4,6,1,2,9,0,3]
#[5,4,8,6,1,2,9,0,3]
#[4,5,8,6,1,2,9,0,3]
arrayOrdenado = [1,2,3,4,5,6,7,8]

for i in range (1 , 10000):
    arrayOrdenado.append(i)
    array.append(randint(0,1000))

[1,2,3]
print("----------------")

def merge(array : List):
    
    if(len(array) == 1): # base case
        return array

    if(len(array)%2 == 0):
        n = int(len(array) / 2)
    else:
        n = int((len(array) + 1) / 2)
    arrayOneBeforeMerge = array[:n]
    arrayTwoBeforeMerge = array[n:]
    
    arrayOne = merge(arrayOneBeforeMerge)
    arrayTwo = merge(arrayTwoBeforeMerge)

    array = sort(array, arrayOne, arrayTwo)
    return array

def sort(originalArray, arrayone , arraytwo):
    i = 0
    j = 0
    while( i < len(arrayone) and j < len(arraytwo)):
        if arrayone[i] < arraytwo[j]:
            originalArray[i + j] = arrayone[i]
            i += 1
        else: 
            originalArray[i + j] = arraytwo[j]
            j += 1

    if i + j < len(originalArray):
        if(i < j ):
            for i in range(i , len(originalArray) - j ):
                originalArray[i + j] =  arrayone[i]
        elif(i > j):
            for j in range(j ,  len(originalArray) - i ):
                originalArray[i + j] =  arraytwo[j]
        elif(j == i):
            if(len(arrayone) > len(arraytwo)):
                for i in range(i , len(originalArray) - j ):
                    originalArray[i + j] =  arrayone[i]
            elif(len(arrayone) < len(arraytwo)):
                for i in range(j , len(originalArray) - i ):
                    originalArray[i + j] =  arraytwo[j]
    return originalArray        

start = time.time()
merge(arrayOrdenado)
end = time.time()

print("time elapsed: " , end - start)
