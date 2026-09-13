import numpy as np, sys
sys.path.insert(0,'output/artifacts')
from delta import Delta
# Max-ratio over refined menu at suspected-worst points; find global min of max-ratio
def maxratio(x, menu, N=12):
    return max(abs(Delta(x,a,b,N=N))/abs(a*b) for (a,b) in menu)
menu=[(s1*h,s2*h) for h in [0.05,0.03,0.015] for s1 in (1,-1) for s2 in (1,-1)]
# coarse + refine
n=60; xs=np.linspace(0,1,n,endpoint=False)
vals=np.zeros((n,n))
for i in range(n):
    for j in range(n):
        vals[i,j]=maxratio(np.array([xs[i],xs[j]]),menu)
print("min",vals.min(),"mean",vals.mean(),"pct",np.percentile(vals,[0,1,5,50]))
idx=np.unravel_index(np.argmin(vals),(n,n)); print("argmin",(xs[idx[0]],xs[idx[1]]))
# local refine: random starts
rng=np.random.default_rng(0)
best=(1e9,None)
for t in range(300):
    x=rng.random(2)
    # coordinate descent
    step=0.02
    for it in range(80):
        cur=maxratio(x,menu)
        moved=False
        for d in [np.array([1.,0.]),np.array([0.,1.])]:
            for s in (step,-step):
                v=maxratio((x+s*d)%1.0,menu,N=12)
                if v<cur: x=(x+s*d)%1.0; cur=v; moved=True
        if not moved: step*=0.5
        if step<1e-6: break
    if cur<best[0]: best=(cur,x.copy())
print("random-search min",best)
