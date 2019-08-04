'''
@author: Guanqi Wang
@summary: use the weight median filter to smooth the missing pixel
'''
import numpy as np
import open_pgm as op
import find_median as fd
import matplotlib.pyplot as plt
import find_most_frequency as fmf

def weight_median_filter(n,G,name,i):
    data = op.read_pgm(name)
    [row, column] = data[1]
    array = data[0]
    image = array.reshape(row, column)
    after_smooth = np.zeros([row, column])
    C = np.zeros(n * n)
    c = int((n-1)/2)
    for m in range(row - n):
        for k in range(column - n):
            q = 0
            filter_array = np.zeros([n * n])
            for e in range(m, m + n):
                for j in range(k, k + n):
                    filter_array[q] = int(image[e][j])
                    q += 1
            filter_list = filter_array.tolist()
            #find the median value of the weighted value
            for x in range(len(filter_list)):
                C[x] = G[x] * filter_list[x]
            Q = C.tolist()
            K = fmf.find_most_frequency(Q)
            if K[0] == 0 and K[1] > (n * n - 1)/2:
                M = 0
            else:
                med = fd.find_median(C)
                for y in range(n * n):
                    if C[y] == med:
                        M = filter_list[y]
            after_smooth[m + c][k + c] = M

    plt.title('the missing pixel' + str(i) + 'after smooth')
    plt.imshow(after_smooth)
    plt.show()

    name3 = 'test\\' + str(i) + 'after_smooth.pgm'
    file = open(name3, 'w')
    [m, n] = after_smooth.shape
    max = 85
    file.write('P2\n' + str(n) + ' ' + str(m) + '\n' + str(max) + '\n')
    for p in range(0, m):
        for q in range(0, n):
            file.write(str(int(after_smooth[p][q])) + '\n')
    file.close()

    return (name3)
