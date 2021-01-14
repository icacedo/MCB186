# 

import random
genome = []
size = 1000000
x = 100

for i in range(size):
	genome.append(0)

for i in range(size*x):
	r = random.randint(0, size-1)
	genome[r] += 1

print((genome.count(0)/size)*100)



