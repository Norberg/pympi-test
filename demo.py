import boost.mpi as mpi

print "I am aprocess %d of %d" % (mpi.rank, mpi.size)
