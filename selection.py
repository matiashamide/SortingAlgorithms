
from ctypes import sizeof
from random import Random, random
from typing import List, Sized
import time

array = [8,5,4,6,1,2,9,0,3]
arrayOrdenado = [1,2,3,4,5,6,7,8]

#for i in range (1 , 1000):
#    arrayOrdenado.append(i)
#    array.append(array[i])


print("----------------")

def selection(array : List):

    for i in range (0,len(array)):
        pos = i
        print(array)
        for j in range (i + 1, len(array)):
            
            if(array[j] < array[pos]):
                pos = j
        aux = array[i]
        array[i] = array[pos]
        array[pos] = aux
    return array

start = time.time()
selection(array)
end = time.time()

print("time elapsed: " , end - start)
