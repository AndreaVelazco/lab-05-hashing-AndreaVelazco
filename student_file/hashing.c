#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define TABLE_SIZE 10

typedef struct HashTable {
    int size;
    int* table;
    int (*hash_function)(int);
} HashTable;

int mi_Mod(int x, int n) {
    return x % n;
}

int randomFn(int x, int n) {
    return rand() % n;
}

void initHashTable(HashTable* ht, int (*hash_function)(int)) {
    ht->size = TABLE_SIZE;
    ht->table = (int*)malloc(TABLE_SIZE * sizeof(int));
    ht->hash_function = hash_function;

    for (int i = 0; i < TABLE_SIZE; i++) {
        ht->table[i] = -1;  
    }
}
