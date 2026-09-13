import numpy as np, sys, time
sys.path.insert(0,'output/artifacts')
from fastdelta import Delta_grid
t0=time.time()
menu=[(s1*h,s2*h) for h in [0.05,0.03,0.015] for s1 in (1,-1) for s2 in (1,-1)]
n=400; xs=np.linspace(0,1,n,endpoint=False)
XX,YY=np.meshgrid(xs,xs); Xg=np.stack([XX.ravel(),YY.ravel()],axis=1)
best=np.full(len(Xg),1e9)
for (a,b) in menu:
    v=np.abs(Delta_grid(Xg,a,b,N=12))/abs(a*b)
    best=np.minimum(best,v)
print("menu12 grid400: min",best.min(),"p1",np.percentile(best,1),"p5",np.percentile(best,5),"median",np.median(best))
i=np.argmin(best); print("argmin",Xg[i],"val",best[i])
for (a,b) in menu:
    print((a,b), Delta_grid(Xg[i:i+1],a,b,N=14)[0]/(a*b))
print("time",time.time()-t0)
np.save('output/artifacts/best400.npy',best.reshape(n,n))
