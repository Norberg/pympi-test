import random, hashlib
from boost import mpi
from glob import glob

def computePi(brute_hash):
	rank, size = mpi.rank, mpi.size
	oldpi, pi, mypi = 0.0,0.0,0.0
	done = False
#	print "rank", rank, "size", size
	files = glob("dicts/x*")
	for i in range(rank, len(files), size): 
		words = open(files[i])
		for word in words.readlines():
			new_hash = hashlib.sha256(word.strip()).hexdigest()
			#print "word:", word, "hash:", new_hash
			if new_hash == brute_hash:
				return word
	return None

if __name__=="__main__":
	passwd = computePi(hashlib.sha256("simon").hexdigest())
	print passwd
	if(mpi.rank==0):
		print "Computed passwd on",mpi.size,"processors is", passwd
	

