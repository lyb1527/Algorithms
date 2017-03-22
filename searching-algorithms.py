'''
Types of Searching:
1. unorderred linear search
2. orderred linear search
3. binary search
4. interpolation search
5. symbol tables and hashing
6. string searching algorithm: tries, Ternary search, suffix trees.

'''



# 1. unordered Linary Search

def unorderedLinearSearch(nums, value):
    for i in range(len(nums)):
        if nums[i] == value:
            return i
    return -1

A = [1534,246,933, 127,277,321,454,565,2201]
print(unorderedLinearSearch(A,277))


# 2. ordered Linear Search
# we dont have to scan the complete array to see if the
#element is there. If the value at A[i] is greater than the data
# to be searched, then we return -1 without searchign the
#remaining array

def orderedLinearSearch(nums, value):
    for i in range(len(nums)):
        if nums[i] == value:
            return i
        elif nums[i] > value:
            return -1
    return -1


A = [127,277,321,454,565,2201]
print(orderedLinearSearch(A,400))

#3. binary search
# the list has to be sorted

def binarySearch(nums, value):
    low  = 0
    high = len(nums) - 1
    while low + 1 <= high:
        mid = (low+high) // 2
        if nums[mid] > value:
            high = mid
        elif nums[mid] < value:
            low = mid
        else:
            return mid
    return -1
A = [127, 246, 277, 321, 454, 565,933, 1534, 2201 ]
print(binarySearch(A,277))


#4. Interpolation Search
'''
Interpolation search tries to improve the binary search, the
find a value k index that is closer to the searched item

    mid = (low + ((value - nums[low]) * (high  - low)) / (nums[high] - nums[low]))

constant K is used to narrow down the search space
for binary search , K is (low + high) / 2

This new K ensure we are closer to the searched value. On average interpolation search make
about log(logn) comparisons(if elements are uniformly distributed)

In interpolation search, interpolation is used to find an item near the one being searched for, then
linear search is used to find the exact item.

For this algo to give best results, data set should be ordered and uniformly distributed
\
List has to be SORTED
'''

def interpolationSearch(nums, value):
    low = 0
    high = len(nums) - 1
    while nums[low] <= value and nums[high] >= value:
        mid = (low + ((value - nums[low]) * (high  - low))
              / (nums[high] - nums[low]))
        if nums[mid] < value:
            low = mid + 1
        elif nums[mid] > value:
            high = mid - 1
        else:
            return mid
    if nums[low] == value:
        return low
    return -1

a = [127, 246, 277, 321, 454, 565,933, 1534, 2201 ]
#A = [1534,246,933, 127,277,321,454,565,2201]
print(interpolationSearch(a,1534))
