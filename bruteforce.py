import random, hashlib
from boost import mpi
from glob import glob

def computePi(brute_hash):
	rank, size = mpi.rank, mpi.size
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
				if new_hash == brute_hash:
					return hash_word
	return None

if __name__=="__main__":
	passwd = computePi(hashlib.sha256("simon22").hexdigest())
	print passwd
