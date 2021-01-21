import argparse
import sys
import statistics
import seqlib

parser = argparse.ArgumentParser(
	description='Genome assembly statistics')
	
parser.add_argument('--fasta',  required=True, type=str,
	metavar='<path>', help='path to a fasta file, may be compressed')
parser.add_argument('--verbose', action='store_true',
	help='print some diagnostic messages to stderr')
# this stores the input if the verbose function was chose
# for use by the subsequent if statement
# anything with a -- is stored as an arg.parse
arg = parser.parse_args()

print(arg.fasta)

# stores stderr if the verbose argument was used
# stderr is made available by the sys library 
if arg.verbose:
	sys.stderr.write(f'Reading {arg.fasta}\n')
	
# from the function defined in seqlib.py
# 'arg' is replaced with the name of the fasta file
# from the '--fasta' argument
# seqlib is a name and must be defined?
# name and seq are defined in seqlib.py
# name and seq are stored as variables
lengths = []
counter = 0
letters = 0
for name, seq in seqlib.read_fasta(arg.fasta):
	counter += 1
	letters += len(seq)
	lengths.append(len(seq))

print('##############################')
print('Mean:', statistics.mean(lengths))
print('Median:', statistics.median(lengths))
print('Number of sequences:', counter)
print('Number of nucleotides:', letters)
print('##############################')

# mean
print('#####~mean~###################')
print(letters / len(lengths))
mean = letters / len(lengths)

# median
print('#####~median~#################')
lengths = sorted(lengths, reverse = True)
if (counter % 2) == 0:
	print((lengths[int(counter / 2) - 1] + lengths[int(counter / 2)]) / 2)
else:
	print(lengths[int(counter / 2)])

# standard deviation
print('#####~standard~deviation~#####')
var = 0
for l in lengths:
	var += ((l - mean) ** 2) / (counter - 1)
print(var ** 0.5)
print(statistics.stdev(lengths))

# N50
print('#####~N50~###################')
# need total number of contigs
# then half of total number
# add contigs
fifty = 0
stop = letters / 2
index = 0
for l in lengths:
	if fifty <= stop:
		fifty += l
		index += 1
	else:
		print(lengths[index - 1])
		break
		

		

	





































	

