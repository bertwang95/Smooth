'''
@author: Guanqi Wang
@summary: Use the dictionary to find the value which has the highest frequency of occurrence
'''

import operator
import find_median as fm

def find_most_frequency(L):
    d={}
    for i in L:
        if i not in d.keys():
            d[i]=L.count(i) # create a dictionary to store all the value
    A=sorted(d.items(),key=operator.itemgetter(1),reverse=True) # sort the value from max to min according to the frequency of occurrence

    if len(A)==1:
        max=A[0][0]
        fre=A[0][1]
    # if two maximum value's frequency of occurrence is equal, then use the median value to replace the maximum value
    elif A[0][1]==A[1][1]:
        max=fm.find_median(L)
        fre=A[0][1]
    else:
        max=A[0][0]
        fre=A[0][1]

    return (max,fre)