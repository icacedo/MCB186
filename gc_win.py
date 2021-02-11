def output(count):
	GC = count['G']+count['C']
	AT = count['A']+count['T']
	if GC + AT == 0:
		return None
	else:
		return GC/(GC+AT)

dna = 'ATTGTTTCAAATTTTTGTATACCAACGNNNNNNNNNNNNAGTCCGTTTCTCTTTCGGATTTTT'
w = 10

wn = dna[0:w]
count = {}
count['A'] = wn.count('A')
count['C'] = wn.count('C')
count['G'] = wn.count('G')
count['T'] = wn.count('T')
count['N'] = wn.count('N')
print(output(count))

for i in range(len(dna)-w):
	off = dna[i]
	on = dna[i+w]
	count[off] -= 1
	count[on] += 1
	print(output(count))

