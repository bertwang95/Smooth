'''
@author: Guanqi Wang
@summary: Open the pgm files.
'''
import numpy as np

# read the PGM figure
def read_pgm(name):
    with open(name) as f:
        lines = f.readlines()

# remove commented lines
    for l in list(lines):
        if l[0] == '#':
            lines.remove(l)

# Makes sure it is ASCII format (P2)
    assert lines[0].strip() == 'P2'

# Converts data to a list of integers
    data = []
    for line in lines[1:]:
        data.extend([int(c) for c in line.split()])   # read the data from the line

    return (np.array(data[3:]),(data[1],data[0]),data[2]) #data[0] is P2, data[1] is height and width, data[2] is maximum of pixel value
