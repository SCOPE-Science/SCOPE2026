import numpy as np, sys, time
sys.path.insert(0,'output/artifacts')
from fastdelta import Delta_grid
t0=time.time()
def maxratio_cont(x, N=16, nh=25):
    hs = np.concatenate([np.linspace(0.005,0.05,nh), -np.linspace(0.005,0.05,nh)])
    best=0; arg=None
    for a in hs:
        v = np.abs(Delta_grid(np.tile(x,(len(hs),1)), a, hs, N=N))/np.abs(a*hs)
        # Delta_grid broadcasts? no, takes scalar a,b. loop b
        for j,b in enumerate(hs):
            q = abs(float(Delta_grid(x[None,:],a,b,N=N)[0])/abs(a*b))
            if q>best: best=q; arg=(a,b)
    return best,arg
for pt in [np.array([0.6325,0.115]), np.array([0.8225,0.6125]), np.array([0.13,0.71])]:
    b,a = maxratio_cont(pt)
    print("pt",pt,"contmax",b,"at",a,"time",round(time.time()-t0,1))
