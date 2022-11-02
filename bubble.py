

from ctypes import sizeof
from random import Random, randint, random
from typing import List, Sized
import time
import sys
array = [8,5,4,6,1,2,9,0,3]
arrayOrdenado = [1,2,3,4,5,6,7,8]

for i in range (1 , 100000):
    arrayOrdenado.append(i)
    array.append(randint(0,1000))

print("----------------")
sys.setrecursionlimit(10**7)

def bubble(array : List, iteration = 0):
    ordenado = True

    for i in range (0 , len(array) - iteration -  1):
        print("e")
        if(array[i] > array[i + 1]):
            aux = array[i + 1]
            array[i + 1] = array[i]
            array[i] = aux
            ordenado = False
    
    if ordenado:
        return array
    else:
        return bubble(array , iteration + 1)

start = time.time()
bubble(array)
end = time.time()

print("time elapsed: " , end - start)