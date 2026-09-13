import numpy as np
import sys
sys.path.insert(0, 'output/artifacts')
from delta import Delta, r, eu, es
# single pair min
pairs_single = [(0.04,0.04)]
n=200
xs = np.linspace(0,1,n,endpoint=False)
# vectorize Delta? loop but with N=10 for speed
import time
def max_ratio(x, pairs, N=12):
    best=0
    for (a,b) in pairs:
        best=max(best, abs(Delta(x,a,b,N=N))/abs(a*b))
    return best
# coarse single-pair scan
t0=time.time()
vals=np.zeros((n,n))
for i in range(n):
    for j in range(n):
        vals[i,j]=abs(Delta(np.array([xs[i],xs[j]]),0.04,0.04,N=10))/0.0016
print("single pair (0.04,0.04): min",vals.min(),"mean",vals.mean(),"pct",np.percentile(vals,[0,1,5,50]))
print("time",time.time()-t0)
# where is min?
idx=np.unravel_index(np.argmin(vals),(n,n))
print("argmin",xs[idx[0]],xs[idx[1]])
# check other sign combos at that xmin
x=np.array([xs[idx[0]],xs[idx[1]]])
for (a,b) in [(0.04,0.04),(0.04,-0.04),(-0.04,0.04),(0.03,0.03),(0.04,0.02),(0.02,0.04)]:
    print((a,b), Delta(x,a,b,N=14)/(a*b))
