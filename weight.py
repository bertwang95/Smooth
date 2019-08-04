'''
@author: Guanqi Wang
@summary: use the genetic method to find the weight of the median filter
'''

import numpy as np
import random
import fitness as ft
import crossover_mutation as cm
import time

def gentic_weight(n,name):

    population = 2
    pm = 0.5  #probability of mutation
    pc = 1 #probability of crossover
    genetic_length = n * n
    goal_fitness = 0.96
    max_value = n * n
    generation_length = 5 #the length of the generation
    initinal_weight = [[]]
    D = {x:0 for x in range (2)}

    start = time.time()
    # first generation
    for i in range (population):
        G = []
        for j in range (genetic_length):
            G.append(random.randint(0,max_value))
        initinal_weight.append(G)
        D[i] = ft.fitness_test(G,n,name)
    A = sorted(D.items(),key=lambda item:item[1],reverse=True)
    a = A[0][0]
    b = A[1][0]
    initinal_weight_array = np.array(initinal_weight)
    parentA = initinal_weight_array[a + 1]
    ParentA = parentA
    ParentA_fitness = A[0][1]
    print('parent A fitness is:',ParentA_fitness)
    print('parent A is: ',ParentA)
    parentB = initinal_weight_array[b + 1]
    ParentB = parentB
    ParentB_fitness = A[1][1]
    print('parent B fitness is:', ParentB_fitness)
    print('parent B is: ',ParentB)
    elapsed = (time.time() - start)
    print('time used', elapsed)

    # find the best weight according to the fitness score
    for generation in range (generation_length):
        generation += 1
        C = cm.crossover(ParentB,ParentA,pc)
        Child = cm.mutation(C,pm,max_value)
        Child_fitness = ft.fitness_test(Child,n,name)

        # parentA always has the highest fitness
        if Child_fitness > ParentB_fitness:
            if Child_fitness > ParentA_fitness:
                ParentB_fitness = ParentA_fitness
                ParentB = ParentA
                ParentA_fitness = Child_fitness
                ParentA = Child
            else:
                ParentB_fitness = Child_fitness
                ParentB = Child
        else:
            ParentA_fitness = ParentA_fitness
            ParentA = ParentA
            ParentB_fitness = ParentB_fitness
            ParentB = ParentB

        print(ParentA_fitness)
    filter_weight = ParentA
    print(filter_weight)

    return (filter_weight)

# gentic_weight(n=5,name='test\\51.pgm')