import random, hashlib
from boost import mpi
from glob import glob

def find_password(brute_hash, start_chunk, nr_of_instances):
	files = glob("pympi-test/dicts/x*")
	for i in range(start_chunk, len(files), nr_of_instances): 
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
	rank, size = mpi.rank, mpi.size
	passwd = find_password(hashlib.sha256("simon22").hexdigest(), rank, size)
	print passwd
