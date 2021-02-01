import seqlib

# testing a list of lists
#list1 = ['se', 'qu', 'en', 'ce']
#list2 = ['SE', 'QU', 'EN', 'CE']
#list3 = [list1, list2]
# the first [] is the position in the list of lists
# the second [] is the position in the sublist 
#print(list3[1][2])
#sys.exit()

all_probs = []
for name, seq, qual in seqlib.read_fastq('mini.fastq.gz'):
	probs = []
	# this loop goes by each position in a single string of quality...
	# ...values for one sequence
	for qv in qual:
		# using the Sanger equation
		p = 10 ** ((ord(qv) - 33) / -10)
		probs.append(p)
	all_probs.append(probs)

# sum and get the averages for the values in all_probs
# sum each 'column' corresponding to the same position in each sequence
# there are 100000 sequences
for q1 in range(len(all_probs)):
	print(all_probs[q1])
	sys.exit()
	#for q2 in all_probs[q1]:
	# there are 152 positions in each sequence
		#print(all_probs[q2])











