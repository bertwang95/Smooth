'''
@author: Guanqi Wang
@summary: crossover and mutation
'''

import random

def crossover(pop1,pop2,pc):
    length = len(pop1)

    if random.random() < pc:
        cstart = random.randint(0,length-2)
        cstop = random.randint(cstart+1,length-1)
        temp1 = []
        temp2 = []
        temp3 = []
        temp1 = pop2[cstart:cstop]
        if cstart == 0:
            if cstop == length:
                pop1 = pop2
            else:
                temp2 = pop1[cstop:length]
                temp1.extend(temp2)
                pop1 = temp1
        else:
            if cstop == length:
                temp2 = pop1[0:cstart]
                temp2.extend(temp1)
                pop1 = temp2
            else:
                temp2 = pop1[0:cstart]
                temp3 = pop1[cstop:length]
                temp2.extend(temp1)
                temp2.extend(temp3)
                pop1 = temp2
    return (pop1)

def mutation(pop,pm,max_value):
    length = len(pop)
    if random.random() < pm:
         mpoint = random.randint(0,length - 1)
         change_value = random.randint(0,max_value)
         pop[mpoint] = change_value

    return (pop)