# a multi-threaded code which postprocesses the *.dat files for visualization
# run as :
# python3 postp.py 

from igakit.io import PetIGA,VTK
from numpy import linspace, zeros
import glob
from multiprocessing import Pool
import time

# read in discretization info and potentially geometry
nrb = PetIGA().read("iga.dat")

# enter the refinement factor
refinement = 2

# write a function to sample the nrbs object (100 points from beginning to end)
uniform = lambda U: linspace(U[0], U[-1], int(len(U)*refinement))

# function to print the fields into VTK files
def print_file(infile):
	sol = PetIGA().read_vec(infile,nrb)
	outfile_petiga = infile.split(".")[0] + ".vtk"	
	VTK().write(outfile_petiga,# output filename
        nrb,                   # igakit NURBS object
        fields=sol,            # sol is the numpy array to plot 
        sampler=uniform,
        scalars={'pressure':3},
	    vectors={'velocity':[0,1,2]})							

if __name__ == '__main__':
	list_of_files = glob.glob("nsvms*.dat")
	t0 = time.time()
	p = Pool(24)
	p.map(print_file, list_of_files)
	t1 = time.time()
	print('Total post-processing time = %f secs'%(t1 - t0))






