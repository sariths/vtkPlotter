#  This example shows how to use a variant of a 1 dimensional 
# Moving Least Squares (MLS) algorithm to project a cloud 
# of unordered points to become a smooth line.
# The parameter f controls the size of the local regression.
# The input actor's polydata is modified by the method
# so more than one pass is possible.
# If showNLines>0 an actor is built demonstrating the 
# details of the regression for some random points
#
from __future__ import division, print_function
from plotter import vtkPlotter, arange, sin, cos
import numpy as np

N = 3  # nr. of iterations

# build some initial cloud of noisy points along a line
pts = [ (sin(6*x), sin(2*x)/(x+1), cos(9*x)) for x in arange(0,1, .001)]
#pts = [ (0, sin(x), cos(x)) for x in arange(0,6, .01) ]

pts += np.random.randn(len(pts), 3)/50 # add noise
np.random.shuffle(pts) # make sure points are not ordered

vp = vtkPlotter(N=N)
a = vp.points(pts)
vp.show(a, at=0, legend='cloud')
        
for i in range(1, N):
    a = a.clone().color(i)
    vp.smoothMLS1D(a, f=0.4)
    
    # at last iteration make sure points are separated by tol
    if i==N-1: vp.cleanPolydata(a, tol=.01)

    print('iteration',i,'#points:',len(a.coordinates()))
    vp.show(a, at=i, legend='iter #'+str(i))

vp.show(interactive=1)












































