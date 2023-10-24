import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from random import choice


class HashTable:
    def __init__(self, hash_function, size):
        self.size = size
        self.table = [None] * size
        self.hash_function = hash_function

    def insert(self, x):
        index = self.hash_function(x) % self.size
        if self.table[index] is None:
            self.table[index] = [x]
        else:
            self.table[index].append(x)

    def delete(self, x):
        index = self.hash_function(x) % self.size
        if self.table[index] is not None and x in self.table[index]:
            self.table[index].remove(x)

    def find(self, x):
        index = self.hash_function(x) % self.size
        if self.table[index] is not None and x in self.table[index]:
            return True
        return False
 
def mi_Mod(x, n=10):
    return x % n

def RandomHashFun(M, n=10):
        fnTable = [ None for i in range(M) ]
        for x in range(M):
            fnTable[x] = choice(range(n))
        def randomFn(x):
         return fnTable[x]
        return randomFn

randomFn2 = RandomHashFun(1000, 10)
print(randomFn2(52))
print(randomFn2(324))

HT = HashTable(randomFnTake2, 10)

x = 123
y = 76
HT.insert(x)

## verificar que la tabla hash funciona
