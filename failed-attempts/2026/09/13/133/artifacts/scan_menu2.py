import numpy as np, sys, time
sys.path.insert(0,'output/artifacts')
from delta import Delta
def maxratio(x, menu, N=14):
    return max(abs(Delta(x,a,b,N=N))/abs(a*b) for (a,b) in menu)
t0=time.time()
menu12=[(s1*h,s2*h) for h in [0.03,0.015] for s1 in [1,-1] for s2 in [1,-1]]+[(s1*0.05,s2*0.05) for s1 in [1,-1] for s2 in [1,-1]]
n=150; xs=np.linspace(0,1,n,endpoint=False)
mn=1e9; arg=None
for i in range(n):
    for j in range(n):
        v=maxratio(np.array([xs[i],xs[j]]),menu12)
        if v<mn: mn=v; arg=(xs[i],xs[j])
print("menu12 gridmin",mn,"at",arg,"time",time.time()-t0)
