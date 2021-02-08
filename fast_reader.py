import seqlib
import statistics 
import sys

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
	qual = qual.rstrip()
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
# this loop is for the total number of sequences


'''
avgs = []
for q1 in range(len(all_probs)):
	# this loop is for number of positions in each sequence
	total_p = 0
	seq_avg = []
	for q2 in all_probs[q1]:
		total_p += q2
		seq_avg.append(total_p / len(all_probs[q1]))
		print(q2)
		sys.exit()
	avgs.append(seq_avg)
print(len(all_probs))
print(len(avgs))
print(len(seq_avg))
'''


for i in range(len(probs)):
	column = []
	for row in all_probs:
		column.append(row[i])
	print(i, statistics.mean(column))
	
	













