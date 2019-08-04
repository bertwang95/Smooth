'''
@author: Guanqi Wang
@summary: the score of the different weight median filter
'''

import open_pgm as op
import numpy as np
import find_median as fd
import find_most_frequency as fmf

def fitness_test(G,n,name):
    data1 = op.read_pgm(name)
    [row, column] = data1[1]
    array1 = data1[0]
    image1 = array1.reshape(row, column)

    data2 = op.read_pgm(name)
    [row, column] = data2[1]
    array2 = data2[0]
    image2 = array2.reshape(row, column)
    after_smooth = np.zeros([row,column])
    C = np.zeros(n * n)
    c = int((n-1)/2)
    for m in range (row-n):
        for k in range (column-n):
            q=0
            filter_array = np.zeros([n * n])
            for i in range(m,m+n):
                for j in range (k,k+n):
                    filter_array[q] = int(image2[i][j])
                    q += 1
            filter_list = filter_array.tolist()
            for x in range(len(filter_list)):
                C[x] = G[x] * filter_list[x]
            Q = C.tolist()
            K = fmf.find_most_frequency(Q)
            if K[0] == 0 and K[1] > (n * n - 1) / 2:
                M = 0
            else:
                med = fd.find_median(C)
                for y in range(n * n):
                    if C[y] == med:
                        M = filter_list[y]
            after_smooth[m + c][k + c] = M

    total = row * column
    same = 0
    for a in range (row):
        for b in range (column):
            if after_smooth[a][b] == image1[a][b]:
                same +=1

    fitness = float(same/total)

    return (fitness)