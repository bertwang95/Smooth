'''
@author: Guanqi Wang
@summary: apply 3D filter to the 3D array
'''
import numpy as np
import three_d_array as tda
import find_median as fd
import find_most_frequency as fmf
import time as time

# a is the begin pgm file, b is the last pgm file, t is the number of times to increase resolution, n is size of filter
def three_d_median_filter(a,b,t,n):
    data=tda.three_d(a,b,t,n)
    three_d_array=data[1]
    [z,y,x]=data[0]

    start = time.time()
    filter_three_d_array = np.zeros([n * n * n])
    c = int(((n - 1) / 2))
    three_d_after_smooth = np.zeros([z,y,x])
    for d in range(z - n):
        for e in range(y - n):
            for f in range(x - n):
                q = 0
                # build the filter
                filter_three_d_array = np.zeros([n * n * n])
                for m in range(d, d + n):
                    for j in range(e, e + n):
                        for i in range(f, f + n):
                            filter_three_d_array[q] = three_d_array[m][j][i]
                            q += 1
                filter_three_d_list = filter_three_d_array.tolist()
                Z = fmf.find_most_frequency(filter_three_d_list)
                z = Z[1]
                # if the more than half pixels have the same value, the median is equal to the highest frequency of occurrence value
                if z > (n * n * n - 1) / 2:
                    med = Z[0]
                else:
                    med = fd.find_median(filter_three_d_array)

                med = int(med)
                three_d_after_smooth[d + c - 1][e + c - 1][f + c - 1] = med

    elapsed = (time.time() - start)
    print('time used', elapsed)

    return (three_d_after_smooth.shape,three_d_after_smooth)
