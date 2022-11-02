
from ctypes import sizeof
from random import Random, random
from typing import List, Sized
import time

array = [8,5,4,6,1,2,9,0,3]
#[5,8,4,6,1,2,9,0,3]
#[5,4,8,6,1,2,9,0,3]
#[4,5,8,6,1,2,9,0,3]
arrayOrdenado = [1,2,3,4,5,6,7,8]

#for i in range (1 , 1000):
#    arrayOrdenado.append(i)
#    array.append(array[i])


print("----------------")

def insertion(array : List):

    for i in range(0, len(array) - 1):
        
        if(array[i] > array[i+1]):
            aux = array[i]
            array[i] = array[i+1]
            array[i+1] = aux
            
            for j in range (i, 0, -1):
                if(array[j] < array[j - 1]):
                    aux = array[j]
                    array[j] = array[j-1]
                    array[j-1] = aux
                else:
                    break

    return array

start = time.time()
insertion(array)
end = time.time()

print("time elapsed: " , end - start)
