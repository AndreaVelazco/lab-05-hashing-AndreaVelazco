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
        index = self.hash_function(x)
        if self.table[index] is None:
            self.table[index] = [x]
        else:
            self.table[index].append(x)

    def delete(self, x):
        index = self.hash_function(x)
        if self.table[index] is not None and x in self.table[index]:
            self.table[index].remove(x)

    def find(self, x):
        index = self.hash_function(x)
        if self.table[index] is not None and x in self.table[index]:
            return True
        else:
            return False

def mi_Mod(x, n=10):
    return x % n

def randomFn(x, n=10):
    return choice(range(n))

def RandomHashFun(M, n=10):
    fnTable = [None] * M
    for x in range(M):
        fnTable[x] = choice(range(n))

    def randomFnTake2(x):
        return fnTable[x]

    return randomFnTake2

randomFn2 = RandomHashFun(1000, 10)

HT = HashTable(mi_Mod, 10)

x = 1234567
y = 76554334234
HT.insert(x)

print(HT.find(x))  # True
print(HT.find(y))  # False

HT.delete(x)
print(HT.find(x))  # False

HT = HashTable(randomFn, 10)

x = 1234567
y = 76554334234
HT.insert(x)

print(HT.find(x))  # True
print(HT.find(y))  # False

HT = HashTable(randomFn2, 1000)

x = 123
y = 76
HT.insert(x)

print(HT.find(x))  # True
print(HT.find(y))  # False

