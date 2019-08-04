'''
@author: Guanqi Wang
@summary: slice the 3D array
'''
import numpy as py
import matplotlib.pyplot as plt
import three_d_median_filter as tdmf
import three_d_array as tda

def get_slice(a,b,t,n,axis):
    A=[]
    # a=int(input('the begin pgm file:'))
    # b=int(input('the last ogm file:'))
    # t= int(input('the number of times to increase the width and height：'))
    # n=int(input('the size of filter:'))
    # axis=str(input('the constant axis you choose is:'))
    A=tda.three_d(a,b,t,n)
    AA=A[0]
    XX1=AA[2]
    YY1=AA[1]
    ZZ1=AA[0]
    B=A[1]
    E=A[2]
    print(XX1,YY1,ZZ1)
    C=tdmf.three_d_median_filter(a,b,t,n)
    CC=C[0]
    XX2=CC[2]
    YY2=CC[1]
    ZZ2=CC[0]
    D=C[1]
    print(XX2,YY2,ZZ2)

    if axis=='x' :
        i = int(input('you want to slice from x='))
        if i <= XX1:
            c = int((n - 1) / 2)
            m = int((i - c) / 2)
            xbeforeir = E[:, :, m]
            xconstantbefore = B[:, :, i]
            xconstantafter = D[:, :, i]
            print(xconstantbefore, xconstantbefore.shape)
            print(xconstantafter,xconstantafter.shape)

            plt.title('before increase resolution')
            plt.imshow(xbeforeir)
            plt.show()
            plt.title('before smooth')
            plt.imshow(xconstantbefore)
            plt.show()
            plt.title('after smooth')
            plt.imshow(xconstantafter)
            plt.show()
            # save as pgm files
            file = open('test\\xBeforeIncreaseResolution.pgm', 'w')
            [m, n] = xbeforeir.shape
            max = 85
            file.write('P2\n' + str(n) + ' ' + str(m) + '\n' + str(max) + '\n')
            for i in range(0, m):
                for j in range(0, n):
                    file.write(str(int(xbeforeir[i][j])) + '\n')
            file.close()
            file = open('test\\xBeforeSmooth.pgm', 'w')
            [m, n] = xconstantbefore.shape
            max = 85
            file.write('P2\n' + str(n) + ' ' + str(m) + '\n' + str(max) + '\n')
            for i in range(0, m):
                for j in range(0, n):
                    file.write(str(int(xconstantbefore[i][j])) + '\n')
            file.close()

            file = open('test\\xAfterSmooth.pgm', 'w')
            [m, n] = xconstantafter.shape
            max = 85
            file.write('P2\n' + str(n) + ' ' + str(m) + '\n' + str(max) + '\n')
            for i in range(0, m):
                for j in range(0, n):
                    file.write(str(int(xconstantafter[i][j])) + '\n')
            file.close()

        else:
            print('out of range')

    elif axis=='y' :
        i = int(input('you want to slice from y='))
        if i <= YY1:
            c = int((n - 1) / 2)
            m = int((i - c) / 2)
            ybeforeir = E[::, m]
            yconstantbefore = B[::, i]
            yconstantafter = D[::, i]
            print(yconstantbefore, yconstantbefore.shape)
            print(yconstantafter, yconstantafter.shape)

            plt.title('before increase resolution')
            plt.imshow(ybeforeir)
            plt.show()
            plt.title('before smooth')
            plt.imshow(yconstantbefore)
            plt.show()
            plt.title('after smooth')
            plt.imshow(yconstantafter)
            plt.show()
            # save as pgm files
            file = open('test\\yBeforeIncreaseResolution.pgm', 'w')
            [m, n] = ybeforeir.shape
            max = 85
            file.write('P2\n' + str(n) + ' ' + str(m) + '\n' + str(max) + '\n')
            for i in range(0, m):
                for j in range(0, n):
                    file.write(str(int(ybeforeir[i][j])) + '\n')
            file.close()

            file = open('test\\yBeforeSmooth.pgm', 'w')
            [m, n] = yconstantbefore.shape
            max = 85
            file.write('P2\n' + str(n) + ' ' + str(m) + '\n' + str(max) + '\n')
            for i in range(0, m):
                for j in range(0, n):
                    file.write(str(int(yconstantbefore[i][j])) + '\n')
            file.close()

            file = open('test\\yAfterSmooth.pgm', 'w')
            [m, n] = yconstantafter.shape
            max = 85
            file.write('P2\n' + str(n) + ' ' + str(m) + '\n' + str(max) + '\n')
            for i in range(0, m):
                for j in range(0, n):
                    file.write(str(int(yconstantafter[i][j])) + '\n')
            file.close()
        else:
            print('out of range')


    elif axis=='z' :
        i=int(input('you want to slice from z='))
        if i<=ZZ1:
            c = int((n - 1)/2)
            m = int((i - c)/2)
            zbeforeir = E[m,::]
            zconstantbefore = B[i,::]
            zconstantafter = D[i,::]
            print(zconstantbefore, zconstantbefore.shape)
            print(zconstantafter, zconstantafter.shape)

            plt.title('before increase resolution')
            plt.imshow(zbeforeir)
            plt.show()
            plt.title('before smooth')
            plt.imshow(zconstantbefore)
            plt.show()
            plt.title('after smooth')
            plt.imshow(zconstantafter)
            plt.show()
            # save as pgm files
            file = open('test\\zBeforeIncreaseResolution.pgm', 'w')
            [m, n] = zbeforeir.shape
            max = 85
            file.write('P2\n' + str(n) + ' ' + str(m) + '\n' + str(max) + '\n')
            for i in range(0, m):
                for j in range(0, n):
                    file.write(str(int(zbeforeir[i][j])) + '\n')
            file.close()

            file = open('test\\zBeforeSmooth.pgm', 'w')
            [m, n] = zconstantbefore.shape
            max = 85
            file.write('P2\n' + str(n) + ' ' + str(m) + '\n' + str(max) + '\n')
            for i in range(0, m):
                for j in range(0, n):
                    file.write(str(int(zconstantbefore[i][j])) + '\n')
            file.close()

            file = open('test\\zAfterSmooth.pgm', 'w')
            [m, n] = zconstantafter.shape
            max = 85
            file.write('P2\n' + str(n) + ' ' + str(m) + '\n' + str(max) + '\n')
            for i in range(0, m):
                for j in range(0, n):
                    file.write(str(int(zconstantafter[i][j])) + '\n')
            file.close()
        else:
            print('out of range')

    else:
        print('the axis you choose is wrong')
