# Meshing your body
---
## Introduction:
The program is aim to increase the spatial resolution of the given DHP figure in 3D, then use filter to smooth pgm figure in 3D, meanwhile metain a truthful representation of the human body. Finally slice the 3D figure to the 2D pgm figure.

## Flow Chart
```
graph TB
A[open ogm file]-->B[make 3D array]
B-->C[3D median filter]
C-->D[choose the constant axis and slice]
D-->E[before increase resolution pgm figure]
D-->F[before smooth pgm figure]
D-->G[after smooth pgm figure]
F-->H[check pixel]
G-->H
H-->I[miss the pixel?]
I-->|YES|J[the pgm figure only have miss value]
I-->|NO|K[exist big difference in frequency of  occurrence?]
J-->K
K-->|YES|L[the pgm figure only have the difference value]
K-->|NO|N
L-->M[weighted median filter]
M-->P[after smooth figure]
P-->N[combine]
J-->N
G-->N
N-->O[final after smooth figure]
```
## Running
Open the main_program.py, and run the code, first you can see:
>the begin pgm file:  
>the last pgm file:  
>the number of times to increase the width and height：  
>the size of filter:  
>the constant axis you choose is:  

For the first input and second innput is the begin pgm file and end pgm file, you need to enter the nuber between 1 to 399, and the begin pgm file's number should smaller than the last pgm file's.  

For the third input is the time of the increase resolution, you need to enter the number a positive integer.  

For the fouth input is the size of filter you choose, you need to enter the odd number greater than 3.  

For the fifth input, you should choose the axis you want to, you can choose x, y or z.  
Then you will see:
>you want to slice from x= or y= or z=

You can enter the integer between the szie of x, y or z.  

And you will get three figure: before increase resolution, before smooth and after smooth.   
Then the program will check if after smooth pgm figure miss some pixels and if there exist a huge difference of frequency of value's occurence.    
- if some pixels are missed, you will get the pgm figure that pixels are missed and the improve smooth pgm figure that combine after smooth pgm figureand missed pixels figure.
- if there exist huge difference between frequency of occurrence of before smooth figure and frequency of occurrence of after smooth figure you will get the pgm figure only have that value and 0 from before smooth figure, and the pgm figure which is smoothed by weighted median filter, and the weight is calculated by using genetic method.
- Finally, combine the improve smooth pgm figure and the pgm figure which is smoothhed by weighted median filter, and get the final after smooth figure.<br>

All the figure are saved in the test file.

## Module introduction
- open_pgm.py: is used to open the pgm figure.
- increase_reaolution.py: use nearest neighbour to increase resolution in 2D
- border.py: pad the edge of the 2D array
- three_d_array.py: build 3D array according to the 2D pgm figure, and use nearest neighbour to increase resolution, and pad the 3D array edge according to the size of the filter.
- three_d_median_filter.py: use 3D improve median filter to smooth the 3D array.
   - find_median.py: use heap sort method to find the median values form the filter list.
   - find_most_frequency.py: use histogram to skip smoe voxels to speed up the smoothing.
- get_slice.py: is used to slice the 3D array, and get the before increase resolution, before smooth and after smooth pgm figure of x constant, y constant or z constant.
- weight_median_filter.py: use the weighted median filter to smooth the 2D figure
  - weight.py: use genetic method to find the best weight
    - crossover_mutation.py: used to make parents to crossover and mutation
    - fitness.py: used to check the score of the weighted median filter
-main_program.py: used to combine all the steps and get the final after smooth pgm figure