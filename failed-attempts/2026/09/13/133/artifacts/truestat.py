import numpy as np, sys, time
sys.path.insert(0,'output/artifacts')
from fastdelta import Delta_grid
t0=time.time()
scales=[0.05,0.04,0.03,0.02,0.015,0.01]
menu=[(s1*h1,s2*h2) for h1 in scales for h2 in scales for s1 in (1,-1) for s2 in (1,-1)]
print("menu size",len(menu))
n=200; xs=np.linspace(0,1,n,endpoint=False)
XX,YY=np.meshgrid(xs,xs); Xg=np.stack([XX.ravel(),YY.ravel()],axis=1)
M=np.zeros(len(Xg))
for (a,b) in menu:
    v=np.abs(Delta_grid(Xg,a,b,N=14))/abs(a*b)
    M=np.maximum(M,v)
print("M(x)=max_pairs: inf",M.min(),"p1%",np.percentile(M,1),"median",np.median(M))
i=np.argmin(M); print("argmin",Xg[i])
print("time",round(time.time()-t0,1))
np.save('output/artifacts/M200.npy',M.reshape(n,n))
