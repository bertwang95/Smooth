'''
@author: Guanqi Wang
@summary: use the padding to extend the edge of the figure in 2D
'''
import numpy as np
import open_pgm as op
import increase_resolution as ir
import matplotlib.pyplot as plt

# n is size of filter, t is the number of times to increase resolution
def border(name,n,t):
    image=ir.increase_resolution(name,t)

    [row,column]=image.shape
    add_row=add_column=int((n-1)/2)  #the number of row and column increase
    new_row=int(row)+int(add_row)*2
    new_column=int(column)+int(add_column)*2
    newimage=np.zeros([new_row,new_column]) #new matrix

    # extend the edge of figure, the edge value are 0
    for i in range (add_row,row+add_row):
        for j in range (add_column,column+add_column):
            newimage[i][j]=image[i-add_row][j-add_column]

    # give the value of original  figure edge to the nearest pixel after extend the edge of figure
    for i in range (add_row,row+add_row):
        for j in range (0,add_row):
            newimage[i][j]=image[i-add_row][0]
    for i in range (0,add_row):
        for j in range(add_column,column+add_column):
            newimage[i][j]=image[0][j-add_column]
    for i in range (add_row,row+add_row):
        for j in range (column+add_column,new_column):
            newimage[i][j]=image[i-add_row][column-1]
    for i in range (row+add_row,new_row):
        for j in range (add_column,column+add_column):
            newimage[i][j]=image[row-1][j-add_column]

    return (newimage)