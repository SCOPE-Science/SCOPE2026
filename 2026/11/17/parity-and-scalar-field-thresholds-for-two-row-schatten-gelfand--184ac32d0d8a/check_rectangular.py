#!/usr/bin/env python3
"""Supplementary finite checks for two-row Schatten threshold witnesses."""
import numpy as np

def ratio(A,p,q):
    s=np.linalg.svd(A,compute_uv=False)
    def vecnorm(r):
        return max(s) if r==float('inf') else np.sum(s**r)**(1/r)
    return vecnorm(q)/vecnorm(p)

total=0
for n in range(3,18):
    d=n//2
    J=np.zeros((2*d,2*d))
    for j in range(d):
        J[2*j,2*j+1]=-1.;J[2*j+1,2*j]=1.
    rng=np.random.default_rng(410+n)
    for p,q in [(0.4,1.),(0.4,2.),(1.,2.),(1.,float('inf')),(2.,float('inf'))]:
        beta=2**((0 if q==float('inf') else 1/q)-1/p)
        for _ in range(20):
            u=rng.standard_normal(2*d)
            A=np.vstack([np.pad(u,(0,n-2*d)),np.pad(J@u,(0,n-2*d))])
            assert abs(ratio(A,p,q)-beta)<2e-9
            total+=1
            v=rng.standard_normal(d)+1j*rng.standard_normal(d)
            B=np.vstack([np.pad(v,(0,n-d)),np.pad(v,(d,n-2*d))])
            assert abs(ratio(B,p,q)-beta)<2e-9
            total+=1
        # Pure rank-one extremes, either field
        A=np.zeros((2,n));A[0,0]=1
        assert abs(ratio(A,p,q)-1)<1e-12; total+=1
print('TWO_ROW_RECTANGULAR_WITNESSES_OK',total)
