'''
@author: Guanqi Wang
@summary: Use the heap sort to find the median value
'''

import numpy as np
from collections import deque

# switch two value
def swap_param(L, i, j):
    L[i], L[j] = L[j], L[i]
    return L

# adjusted to a large root heap
def heap_adjust(L, start, end):
    temp = L[start]

    i = start
    j = 2 * i

    while j <= end:
        if (j < end) and (L[j] < L[j + 1]):
            j += 1
        if temp < L[j]:
            L[i] = L[j]
            i = j
            j = 2 * i
        else:
            break
    L[i] = temp

def heap_sort(L):
    L_length = len(L) - 1

    first_sort_count = L_length // 2
    # adjust to a large root heap
    for i in range(first_sort_count):
        heap_adjust(L, first_sort_count - i, L_length)
    # pop out the max value and the adjust to a large root heap
    for i in range(L_length - 1):
        L = swap_param(L, 1, L_length - i)
        heap_adjust(L, 1, L_length - i - 1)

    return [L[i] for i in range(1, len(L))]

# find the median value
def find_median(array):
    L=deque(array)
    L.appendleft(0)
    A=heap_sort(L) #sort A from max value to min value
    k=int(len(array))
    i=int((k-1)/2) #get the median value
    med=int(A[i])

    return (med)
