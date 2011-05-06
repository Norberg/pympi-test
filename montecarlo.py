"""
This example computes PI to certain precision using 
4 processors and a monte carlo simulation.
"""

import random
import boost.mpi as mpi

def computePi(nsamples):
	rank, size = mpi.rank, mpi.size
	oldpi, pi, mypi = 0.0,0.0,0.0
	
	done = False
	while(not done):
		inside = 0
		for i in xrange(nsamples):
			x = random.random()
			y = random.random()
			if ((x*x)+(y*y)<1):
				inside+=1
		
		oldpi = pi
		mypi = (inside * 1.0)/nsamples
		pi =  (4.0 / mpi.size) +mypi#* mpi.reduce(mypi, lambda x,y: x+y) 
		
		delta = abs(pi - oldpi)
		if(mpi.rank==0):
			print "pi:",pi," - delta:",delta
		if(delta < 0.00001):
			done = True
	return pi

if __name__=="__main__":
	pi = computePi(10000)
	if(mpi.rank==0):
		print "Computed value of pi on",mpi.size,"processors is",pi
	

