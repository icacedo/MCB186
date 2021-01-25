import argparse
import sys
import seqlib

parser = argparse.ArgumentParser(description='read in a fasta file')
parser.add_argument('--fasta', required=True, type=str)
arg = parser.parse_args()

# prints the name of the file used as an argument input
print(arg.fasta)

# in what other ways can i read the output of read_fasta()?
print('##### Total size ##########################')
total_size = 0
num_contigs = 0
lengths = []
for name, seq in seqlib.read_fasta(arg.fasta):
	total_size += len(seq)
	num_contigs += 1
	lengths.append(len(seq))
print(total_size)

print('##### Number of contigs ###################')
print(num_contigs)

print('##### Shortest and longest contigs ########')
lengths = sorted(lengths, reverse=True)
print('longest:', lengths[0])
print('shortest:', lengths[len(lengths) - 1])

print('##### Average and median contig sizes #####')
print('Avg:', sum(lengths)/len(lengths))
if len(lengths)%2 == 0:
	print('Med:', lengths[len(lengths)//2 - 1] + lengths[len(lengths)//2])
else:
	print('Med:', lengths[(len(lengths) - 1)//2])

print('##### N50 #################################')
half = sum(lengths)/2
n = 0
contig = 0
for l in lengths:
	if n <= half:
		n += l
		contig += 1
	else:
		print(lengths[contig - 1])
		break
		
print('##### GC fraction #########################')
# if i leave it as 'for seq in', it prints both the name and the seq
ind = []
for name, seq in seqlib.read_fasta(arg.fasta):
	for p in range(len(seq)):
		ind.append(seq[p])
# same amount of nts here as in lengths
# print(ind)
# print(len(ind))
	
GC = 0
notACTG = 0
for nt in ind:
	if nt == 'G' or nt == 'g' or nt == 'C' or nt == 'c':
		GC += 1
	elif nt == 'A' or nt == 'a' or nt == 'T' or nt == 't':
		GC += 0
	else:	
		notACTG += 1
print(GC/(total_size - notACTG))


# using count() is MUCH faster

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		

