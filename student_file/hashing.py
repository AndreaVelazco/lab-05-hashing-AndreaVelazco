import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from random import choice


class HashTable:
  ## code
  ## code
  ## def insert(self, x)
  ## def delete(self, x)
  ## def find(self, x)
 

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