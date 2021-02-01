import seqlib
import sys

# count + or - strand?
# count upper or lowercase?
# skip all kmers with n's?
# command line arguments
strand = "="
# arg.strand()
k = 42
kcount = {}
limit = 10

for name, seq in seqlib.read_fasta(sys.argv[1]):
	seq = seq.upper()
	rvc = seqlib.rev_comp(seq)
	if strand == "+" or strand == "=":
		for i in range(len(seq) - k + 1):
			kmer = seq[i:i + k]
			if "N" in kmer: continue
			if kmer not in kcount: kcount[kmer] = 1
			else: kcount[kmer] += 1
	if strand == "-" or strand == "=":
		for i in range(len(rvc) - k + 1):
			kmer = rvc[i:i + k]
			if "N" in kmer: continue
			if kmer not in kcount: kcount[kmer] = 1
			else: kcount[kmer] += 1
lim = 0
for kmer, count in sorted(kcount.items(), key=lambda item: item[1], reverse=True):
	lim += 1
	print(kmer, count)
	if lim == limit:
		break
	
