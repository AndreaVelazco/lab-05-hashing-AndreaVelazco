#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define TABLE_SIZE 10

typedef struct HashTable {
    int size;
    int* table;
    int (*hash_function)(int);
} HashTable;
