#QuickSort
#1. choose any element to the pivotList
#2. divide all the other elements into 2 partitions, > pivot and < pivot
#3. use recursion to sort both partitions
#4. finally join the two sorted lists with the pivot

def quickSort(alist):
    less = []
    pivotList = []
    more = []
    if len(alist) <= 1:
        return alist
    else:
        pivot = alist[0]
        for i in alist:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)

        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more

A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
print(quickSort(A))
