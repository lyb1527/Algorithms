# Bucket sort: O(n)

# in this implementation, the Insertion sort is used to sort each bucket.
#This means that bucket sort algorithm does NOT specify
#which sorting algorithm to use on the buekcts.

import math

def insertionSort(A):
    for i in range(1, len(A)):
        tmp = A[i]
        k = i
        while k > 0 and tmp < A[k - 1]:
            A[k] = A[k-1]
            k -= 1
        A[k] = tmp

    #return A
#A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
#print(insertionSort(A))

def bucketSort(A):
    code = hashing(A)
    buckets = [list() for _ in range(code[1])]
    for i in A:
        x = rehashing(i, code)
        bucket = buckets[x]
        bucket.append(i)

    for bucket in buckets:
        insertionSort(bucket)

    ndx = 0
    for b in range(len(buckets)):
        for v in buckets[b]:
            A[ndx] = v
            ndx += 1
    return A

def hashing(A):
    m = A[0]
    for i in range(1, len(A)):
        if (m < A[i]):
            m = A[i]
        result = [m, int(math.sqrt(len(A)))]
        return result

def rehashing(i, code):
    return int(i / code[0] * (code[1] - 1))


A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
print(bucketSort(A))
