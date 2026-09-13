import numpy as np, sys, time
sys.path.insert(0,'output/artifacts')
from fastdelta import Delta_grid
# Fine menu: scales x signs, plus asymmetric pairs
scales=[0.05,0.04,0.03,0.02,0.015,0.01]
menu=[(s1,s2) for s1 in scales for s2 in scales]+[(-s1,s2) for s1 in scales for s2 in scales]+[(s1,-s2) for s1 in scales for s2 in scales]+[(-s1,-s2) for s1 in scales for s2 in scales]
menu=list(dict.fromkeys(menu))
print("menu size",len(menu))
n=400; xs=np.linspace(0,1,n,endpoint=False)
XX,YY=np.meshgrid(xs,xs); Xg=np.stack([XX.ravel(),YY.ravel()],axis=1)
best=np.full(len(Xg),1e9)
t0=time.time()
for k,(a,b) in enumerate(menu):
    v=np.abs(Delta_grid(Xg,a,b,N=12))/abs(a*b)
    best=np.minimum(best,v)
    if k%24==0: print(k,"time",round(time.time()-t0,1),"curmin",best.min())
print("FINAL min",best.min(),"p0.1%",np.percentile(best,0.1),"p1%",np.percentile(best,1))
i=np.argmin(best); print("argmin",Xg[i])
np.save('output/artifacts/best_big.npy',best.reshape(n,n))
