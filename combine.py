'''
@author: Guanqi Wang
@summary: combine the after smooth figure and the after smooth missing pixel
'''
import open_pgm as op
import matplotlib.pyplot as plt

def improve(name1,name2,i):
    data1 = op.read_pgm(name1)
    [row, column] = data1[1]
    array1 = data1[0]
    image1 = array1.reshape(row, column)

    data2 = op.read_pgm(name2)
    [row, column] = data2[1]
    array2 = data2[0]
    image2 = array2.reshape(row, column)

    for a in range (row):
        for b in range (column):
            if image2[a][b] ==i:
                image1[a][b] == i

    return (image1)