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
	print('Med:', lengths[len(lengths)/2 - 1] + lengths[len(lengths)/2])
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
		

