import random, hashlib
from boost import mpi
from glob import glob

def computePi(brute_hash):
	rank, size = mpi.rank, mpi.size
	oldpi, pi, mypi = 0.0,0.0,0.0
	done = False
#	print "rank", rank, "size", size
	files = glob("pympi-test/dicts/x*")
	for i in range(rank, len(files), size): 
		words = open(files[i])
		for word in words.readlines():
			for i in range(-1,10):
				if i == -1:
					hash_word = word.strip()
				else:
					hash_word = word.strip() + str(i)
				new_hash = hashlib.sha256(hash_word).hexdigest()
				#print "word:", hash_word, "hash:", new_hash
				if new_hash == brute_hash:
					return hash_word
	return None

if __name__=="__main__":
	passwd = computePi(hashlib.sha256("simon22").hexdigest())
	print passwd
	if(mpi.rank==0):
		print "Computed passwd on",mpi.size,"processors is", passwd
	

