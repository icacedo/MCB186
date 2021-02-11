# use a dictionary
# use .count()
# use only one loop

import seqlib
import random

random.seed(1)

seq = seqlib.random_dna(20, 0.3, 0.2, 0.4, 0.1)
w = 10

for i in range(len(seq)-w+1):
	wn = seq[i:w+i]
	counts = {}
	counts['A'] = wn.count('A')
	counts['C'] = wn.count('C')
	counts['G'] = wn.count('G')
	counts['T'] = wn.count('T')
	AT = counts['A'] + counts['T']
	GC = counts['G'] + counts['C']
	print(wn, counts, GC/(AT+GC))

	








