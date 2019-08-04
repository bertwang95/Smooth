'''
@author: Guanqi Wang
@summary: use the nearest neighbour to increase resolution in 2D
'''

import numpy as np
import open_pgm as op

# t is the number of times to increase resolution
def increase_resolution (name,t):
    data=op.read_pgm(name)
    [row, column] = data[1]
    array = data[0]
    image=array.reshape(row,column)

    new_image=np.zeros((row*t,column*t))
    # the nearest neighbour
    for i in range(0,row):
        for j in range (0,column):

            for m in range (i*t,i*t+t):
                for n in range (j*t,j*t+t):
                    new_image[m][n]=image[i][j]

    return (new_image)