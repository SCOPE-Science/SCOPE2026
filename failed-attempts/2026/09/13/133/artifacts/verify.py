import numpy as np, sys, time
sys.path.insert(0,'output/artifacts')
from fastdelta import Delta_grid
from delta import Delta
rng = np.random.default_rng(1)
X = rng.random((5,2))
t0=time.time()
for (a,b) in [(0.03,0.03),(0.03,-0.03),(0.05,0.02)]:
    fast = Delta_grid(X,a,b,N=14)
    slow = np.array([Delta(x,a,b,N=14) for x in X])
    print((a,b),"maxdiff",np.abs(fast-slow).max())
print("time",time.time()-t0)
# speed: big grid
n=200; xs=np.linspace(0,1,n,endpoint=False)
XX,YY=np.meshgrid(xs,xs); Xg=np.stack([XX.ravel(),YY.ravel()],axis=1)
t0=time.time()
v=Delta_grid(Xg,0.03,0.03,N=12)
print("grid200 time",time.time()-t0,"meanabs",np.abs(v).mean(),"minabs",np.abs(v).min())
