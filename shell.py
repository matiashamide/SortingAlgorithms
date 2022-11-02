
from ctypes import sizeof
from random import Random, randint, random
from typing import List, Sized
import time

array = []
arrayOrdenado = []

for i in range (1 , 1000):
    arrayOrdenado.append(i)
    array.append(randint(0,999))


print("----------------")

def shell(array : List, n = len(array)):

    if n%2 == 0:
        intervalo = int(n/2)
    else:
        intervalo = int((n - 1)/2)
    
    print(n)
    print(intervalo)
    flag = True
    i = 0 
    while( i + intervalo < len(array) ):
        
        j = i
        k = i + intervalo
        
        while(array[j] > array[k] and j >= 0):
            #print(array)
            aux = array[j]
            
            array[j] = array[k]
            array[k] = aux

            k = k - intervalo
            j = j - intervalo
            
            flag = False    
                  
        i = i + 1

    if flag:
        return array
    
    return shell(array, intervalo)

start = time.time()
print(shell(array) )
end = time.time()

print("time elapsed: " , end - start)
