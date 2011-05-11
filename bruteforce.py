from find_password import find_password
import hashlib
from boost import mpi

if __name__=="__main__":
	rank, size = mpi.rank, mpi.size
	passwd = find_password(hashlib.sha256("simon22").hexdigest(), rank, size)
	print passwd
