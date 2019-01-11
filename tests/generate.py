#!/usr/bin/env python3
import sys
import random
def generate_maze():
    ''' Write NxN matrix of random bits into file '''
    name = sys.argv[1]
    size = int(sys.argv[2])
    f = open(name, 'w')
    
    for i in range(0, size):
        for j in range(0, size):
            seed = random.randint(1, 10000)
            b = seed % 2
            f.write(str(b))
        f.write('\n')
    f.close

generate_maze()
