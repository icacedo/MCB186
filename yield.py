def spam(seq, x):
	for nt in seq:
		yield nt, x
		
for nt, extra in spam('ACTG', 'UGAC'):
	print(nt, extra)

