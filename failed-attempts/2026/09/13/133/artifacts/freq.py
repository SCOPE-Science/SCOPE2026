import numpy as np, sys
sys.path.insert(0,'output/artifacts')
from fastdelta import Delta_grid
# Measure actual oscillation frequency content: central differences along eu/es at fine scale
rng=np.random.default_rng(0)
X=rng.random((4000,2))
from delta import eu, es
for h in [0.05,0.03]:
    for direc,name in [(eu,'u'),(es,'s')]:
        D1=Delta_grid((X+1e-3*direc)%1.0,h,h,N=14); D0=Delta_grid(X,h,h,N=14)
        g=np.abs(D1-D0)/1e-3
        print("h",h,"dir",name,"max",g.max().round(4),"p99",np.percentile(g,99).round(4),"mean",g.mean().round(4))
