# Explanation: O(n^2)
'''
Start at the beginning of the array and swap the first two elements
if the first is greater than the second. Then we compare the next particular
and so on. Continue making swaps until the list is sorted
'''

def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]

    return alist
A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
print(bubbleSort(A))


# Explanation: O(n^2)
'''
Simple but inefficient, find the smallest element using a linear san
and move it to the front(swap it iwth the front element). Then find the
second smallest, and then third.. until all elements sorted
'''

def selectionSort(alist):
    for fillslot in range(len(alist)-1, 0, -1):
        posOfMax = 0
        for location in range(1, fillslot+1):
            if alist[location] > alist[posOfMax]:
                posOfMax = location

        tmp = alist[fillslot]
        alist[fillslot] = alist[posOfMax]
        alist[posOfMax] = tmp

    return alist

A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
print(selectionSort(A))


# Explanation: O(n^2)
''' Insert Into A Assumed Sorted Sublist
it always maintains a sorted sublist in the lower positions of the list.
Each new item is then inserted back into the previous subist such that the
sroted sublist is item larger
Assume a list with one item (position 0) is already sorted.
Make n - 1 passes to sort n elements
'''

def insertionSort(alist):
    for index in range(1, len(alist)):
        currentValue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentValue:
            alist[position] = alist[position - 1]
            position =  position - 1

        alist[position] = currentValue

    return alist

A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
print(insertionSort(A))
