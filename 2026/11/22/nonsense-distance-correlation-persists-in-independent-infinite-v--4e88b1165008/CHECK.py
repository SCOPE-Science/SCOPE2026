"""Finite diagnostics for pathwise distance correlation; not an infinite-law proof."""
import itertools
import numpy as np
from scipy.stats import levy_stable

def metric(x,y):
    x=np.asarray(x,float);y=np.asarray(y,float)
    a=np.abs(x[:,None]-x[None,:]);b=np.abs(y[:,None]-y[None,:])
    def center(z):return z-z.mean(axis=0)[None,:]-z.mean(axis=1)[:,None]+z.mean()
    A=center(a);B=center(b);K=np.mean(A*B)
    v1=np.mean(A*A);v2=np.mean(B*B)
    return max(K,0), np.sqrt(max(K,0)/np.sqrt(v1*v2)) if v1*v2>0 else 0

count=0
x=np.array([0.,1.,3.,-2.,4.]);y=np.array([1.,-1.,2.,5.,0.])
k,r=metric(x,y)
assert 0<r<1;count+=1
assert abs(r-metric(8*x-3,2*y+5)[1])<1e-12;count+=1
a=np.abs(x[:,None]-x[None,:]);b=np.abs(y[:,None]-y[None,:])
ks=[]
for perm in itertools.permutations(range(len(x))):
    ks.append(metric(x,y[list(perm)])[0])
assert abs(np.mean(ks)-a.mean()*b.mean()/(len(x)-1))<1e-12;count+=1
rg=np.random.default_rng(20261120)
for alpha in (.7,1.3):
    for trial in range(8):
        sx=np.cumsum(levy_stable.rvs(alpha,0,size=120,random_state=rg))
        sy=np.cumsum(levy_stable.rvs(alpha,0,size=120,random_state=rg))
        _,v=metric(sx,sy)
        assert np.isfinite(v) and 0<v<1
        count+=1
print(f'{count} assertions passed (diagnostic, not a proof).')
