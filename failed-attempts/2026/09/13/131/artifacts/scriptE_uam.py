"""Script E: Ulam matrix of P on box partition (INDICATIVE). Box map by vertex tracking
is unreliable for sheared+linear image; instead estimate each column by sampling:
column j = distribution of f(X), X uniform in box j, over Nsub subsamples."""
import numpy as np, math
Amat=np.array([[2.,1.,0.],[1.,2.,1.],[0.,1.,1.]])
a,b=0.03,0.02
def f(x):
    z=np.stack([x[...,0]+a*np.sin(2*np.pi*x[...,1]),x[...,1]+b*np.sin(2*np.pi*x[...,2]),x[...,2]],axis=-1)%1
    return (z@Amat.T)%1
for m in [4,6]:
    d=m**3
    def box_id(y): return (np.floor(y[...,0]*m).astype(int)*m+np.floor(y[...,1]*m).astype(int))*m+np.floor(y[...,2]*m).astype(int)
    rng=np.random.default_rng(7); Nsub=400
    M=np.zeros((d,d))
    for j in range(d):
        base=np.array([(j//m**2)%m,(j//m)%m,j%m])/m
        X=base+rng.random((Nsub,3))/m
        M[box_id(f(X)),j]+=1/Nsub
    ev=np.linalg.eigvals(M); o=np.argsort(-np.abs(ev))
    print(f"m={m} d={d} top10 |eig|:",np.abs(ev[o[:10]]).round(4))
