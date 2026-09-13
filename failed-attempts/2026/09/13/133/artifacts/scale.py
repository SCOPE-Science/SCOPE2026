import numpy as np, sys
sys.path.insert(0,'output/artifacts')
from fastdelta import Delta_grid
# How does Delta scale with (a,b)? Fix x, vary scale h along fixed signs.
from delta import Delta
for x in [np.array([0.13,0.71]), np.array([0.8225,0.6125]), np.array([0.35,0.825])]:
    print("x",x)
    for h in [0.05,0.03,0.015,0.008,0.004]:
        print("  h",h,"D(h,h)/h^2",Delta(x,h,h,N=16)/h**2,"D(h,-h)/h^2",Delta(x,h,-h,N=16)/h**2)
