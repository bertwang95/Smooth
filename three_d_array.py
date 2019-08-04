'''
@author: Guanqi Wang
@summary: build 3D array
'''
import numpy as np
import os
import open_pgm as op
import increase_resolution as ir


# a is the begin pgm file, b is the last pgm file, t is the number of times to increase resolution, n is size of filter
def three_d(a, b, t, n):
    L = 0
    three_d_list = []
    head = 'data\\v1_00'
    tail = '.pgm'
    image_length = L
    k = 0
    m = 0
    # buile 3D array
    for x in range(a, int(b + 1)):
        if x < 10:
            path = head + '00' + str(x) + tail  # the pgm path when small than 10
            if os.path.exists(path):
                data = op.read_pgm(path)
                image = data[0]
                [image_height, image_width] = data[1]
                map = image.reshape(image_height, image_width)
                three_d_list.append(map)

        elif x >= 10 and x < 100:
            path = head + '0' + str(x) + tail  # the pgm path when small than 100 but bigger and equal to 10
            if os.path.exists(path):
                data = op.read_pgm(path)
                image = data[0]
                [image_height, image_width] = data[1]
                map = image.reshape(image_height, image_width)
                three_d_list.append(map)

        else:
            path = head + str(x) + tail  # the pgm path when bigger than 100
            if os.path.exists(path):
                data = op.read_pgm(path)
                image = data[0]
                [image_height, image_width] = data[1]
                map = image.reshape(image_height, image_width)
                three_d_list.append(map)

    three_d_array = np.array(three_d_list)
    [z,y,x] = three_d_array.shape

    # increase resolution in 3D
    Z = z * t
    Y = y * t
    X = x * t
    increase_resolution_array = np.zeros(((Z,Y,X)))
    for i in range (0,z):
        for j in range (0,y):
            for m in range (0,x):

                for p in range (i * t,i * t  + t):
                    for q in range (j * t,j * t + t):
                        for o in range (m * t,m * t + t):
                            increase_resolution_array[p][q][o] = three_d_array[i][j][m]

    # use the padding to extend the edge of the array in 3D
    c = int((n - 1) / 2)
    new_three_d_array = np.zeros([Z + 2 * c, Y + 2 * c, X + 2 * c])
    for i in range(c, Z + c):
        for j in range(c, Y + c):
            for m in range(c, X + c):
                new_three_d_array[i][j][m] = increase_resolution_array[i - c][j - c][m - c]

    for m in range (c, X + c):
        for i in range(c, Z + c):
            for j in range(0, c):
                new_three_d_array[i][j][m] = increase_resolution_array[i - c][0][m - c]
    for m in range (c, X + c):
        for i in range(c, Z + c):
            for j in range(Y + c, Y + 2 * c):
                new_three_d_array[i][j][m] = increase_resolution_array[i - c][Y - 1][m - c]
    for m in range (c, Y + c):
        for i in range(c, Z + c):
            for j in range(0,c):
                new_three_d_array[i][m][j] = increase_resolution_array[i - c][m - c][0]
    for m in range (c, Y + c):
        for i in range(c, Z + c):
            for j in range(X + c, X + 2 * c):
                new_three_d_array[i][m][j] = increase_resolution_array[i - c][m - c][X - 1]
    for m in range (c, X + c):
        for i in range(c, Y + c):
            for j in range(0, c):
                new_three_d_array[j][i][m] = increase_resolution_array[0][i - c][m - c]
    for m in range (c, X + c):
        for i in range(c, Y + c):
            for j in range(Z + c, Z + 2 * c):
                new_three_d_array[j][i][m] = increase_resolution_array[Z - 1][i - c][m - c]

    return (new_three_d_array.shape, new_three_d_array, three_d_array)

