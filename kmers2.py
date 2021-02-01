import seqlib
import sys
import itertools

for k in range(5,15):
	print(k)
	# count kmers that actually exist
	counts = {}
	for name, seq in seqlib.read_fasta(sys.argv[1]):
		seq = seq.upper()
		for i in range(len(seq) - k + 1):
			kmer = seq[i:i+k]
			if 'N' in kmer: continue
			if kmer in counts: counts[kmer] += 1
			else: counts[kmer] = 1
	kcounts = sorted(counts.items(), key = lambda item: item[1], reverse =  True)
	print(kcounts[0:5])
	print(kcounts[-5:])
	best = kcounts[0][1]
	worst = kcounts[-1][1]
	print(best/worst)
	
	if len(counts.keys()) != 4 ** k:
		for tup in itertools.product('ACTG', repeat=k):
			kmer = ''.join(tup)
			#if kmer not in counts: print(''.join(kmer))
		sys.exit()		
		
			
			
			

		




		

