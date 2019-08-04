'''
@author: Guanqi Wang
@summary: the main program of the smooth program
'''
import numpy as np
import get_slice as gs
import open_pgm as op
import weight as we
import matplotlib.pyplot as plt
import find_median as fd
import weight_median_filter as wmf
import combine as cb
def main():
    a = int(input('the begin pgm file:'))
    b = int(input('the last pgm file:'))
    t = int(input('the number of times to increase the width and height：'))
    n = int(input('the size of filter:'))
    axis = str(input('the constant axis you choose is:'))

    # gs.get_slice(a,b,t,n,axis)

    head = 'test\\'
    name1 = head + str(axis) + 'AfterSmooth.pgm'
    name2 = head + str(axis) + 'BeforeSmooth.pgm'
    name5 = head + str(axis) + 'add the miss pixel'
    data1 = op.read_pgm(name1)
    data2 = op.read_pgm(name2)
    array1 = data1[0]
    list1 = array1.tolist()
    array2 = data2[0]
    [row, column] = data2[1]
    image2 = array2.reshape(row, column)
    list2 = array2.tolist()
    #get the pixels' value and the frequency of pixels occurence
    d1 = {}
    for i in list1:
        if i not in d1.keys():
            d1[i] = list1.count(i)
    print(d1)

    d2 = {}
    for i in list2:
        if i not in d2.keys():
            d2[i] = list2.count(i)
    print(d2)
    # check pixels
    # if some pixels' value are missed, then put the missed pixel in the before smooth figure into the after smooth figure
    if len(d1) < len(d2):
      for i in d1.keys():
          a = d1[i] - d2[i]
          b = d2[i]
          if a / b > 0.1 or i == 51:
              print('the pixel value need to improve is: ', i)
              B = np.zeros([row, column])
              for p in range(row):
                  for q in range(column):
                      if image2[p][q] == i:
                          B[p][q] = i
              plt.title('the pixel value need to improve is: ' + str(i))
              plt.imshow(B)
              plt.show()

              name = 'test\\' + str(i) + '.pgm'
              file = open(name, 'w')
              [m, k] = B.shape
              max = 85
              file.write('P2\n' + str(k) + ' ' + str(m) + '\n' + str(max) + '\n')
              for p in range(0, m):
                  for q in range(0, k):
                      file.write(str(int(B[p][q])) + '\n')
              file.close()

              # calculate the weight
              G = we.gentic_weight(n, name)

              # smooth the missing pixels by using weight median filter
              name3 = wmf.weight_median_filter(n, G, name, i)

              # combine two figure
              final_image2 = cb.improve(name1, name3, i)

              plt.title('improve smooth figure')
              plt.imshow(final_image2)
              plt.show()

              file = open('test\\improve smooth figure.pgm', 'w')
              [m, k] = final_image2.shape
              max = 85
              file.write('P2\n' + str(k) + ' ' + str(m) + '\n' + str(max) + '\n')
              for p in range(0, m):
                  for q in range(0, k):
                      file.write(str(int(final_image2[p][q])) + '\n')
              file.close()
      for j in d2.keys():
          if j not in d1.keys():
              A = np.zeros([row, column])
              for p in range(row):
                  for q in range(column):
                      if image2[p][q] == j:
                          A[p][q] = j
              plt.title('the missing pixel: ' + str(j))
              plt.imshow(A)
              plt.show()

              name4 = 'test\\' + str(j) + '.pgm'
              file = open(name4, 'w')
              [m, k] = image2.shape
              max = 85
              file.write('P2\n' + str(k) + ' ' + str(m) + '\n' + str(max) + '\n')
              for p in range(0, m):
                  for q in range(0, k):
                      file.write(str(int(A[p][q])) + '\n')
              file.close()
              # combine two figure
              final_image2 = cb.improve('test\\improve smooth figure.pgm', name4, j)

              plt.title('the final after smooth figure')
              plt.imshow(final_image2)
              plt.show()

              file = open('test\\final after smooth figure.pgm', 'w')
              [m, k] = final_image2.shape
              max = 85
              file.write('P2\n' + str(k) + ' ' + str(m) + '\n' + str(max) + '\n')
              for p in range(0, m):
                  for q in range(0, k):
                      file.write(str(int(final_image2[p][q])) + '\n')
              file.close()
    else:
        # if the value's frequency of occurence exist large differences between before smooth figure and after smooth figure
        for i in d1.keys():
            a = d1[i] - d2[i]
            b = d2[i]
            if a / b > 0.1 or i == 51:
                print('the pixel value need to improve is: ', i)
                B = np.zeros([row, column])
                for p in range(row):
                    for q in range(column):
                        if image2[p][q] == i:
                            B[p][q] = i
                plt.title('the pixel value need to improve is: ' + str(i))
                plt.imshow(B)
                plt.show()

                name = 'test\\' + str(i) + '.pgm'
                file = open(name, 'w')
                [m, k] = B.shape
                max = 85
                file.write('P2\n' + str(k) + ' ' + str(m) + '\n' + str(max) + '\n')
                for p in range(0, m):
                    for q in range(0, k):
                        file.write(str(int(B[p][q])) + '\n')
                file.close()

                # calculate the weight
                G = we.gentic_weight(n, name)

                # smooth the missing pixels by using weight median filter
                name3 = wmf.weight_median_filter(n, G, name, i)

                # combine two figure
                final_image2 = cb.improve(name1, name3, i)

                plt.title('the final after smooth figure')
                plt.imshow(final_image2)
                plt.show()

                file = open('test\\final after smooth figure.pgm', 'w')
                [m, k] = final_image2.shape
                max = 85
                file.write('P2\n' + str(k) + ' ' + str(m) + '\n' + str(max) + '\n')
                for p in range(0, m):
                    for q in range(0, k):
                        file.write(str(int(final_image2[p][q])) + '\n')
                file.close()




main()
