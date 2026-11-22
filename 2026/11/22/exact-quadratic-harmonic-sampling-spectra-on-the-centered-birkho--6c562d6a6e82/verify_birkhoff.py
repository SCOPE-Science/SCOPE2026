#!/usr/bin/env python3
"""Standalone finite tests for the normalized Birkhoff-vertex harmonic kernel.
Analytic all-n conclusions are proved separately; numerical tests are diagnostic.
"""
from itertools import permutations
from math import factorial
import numpy as np

def check(n):
    ps=list(permutations(range(n)))
    N=len(ps)
    P=np.array(ps,dtype=np.int16)
    F=(P[:,None,:] == P[None,:,:]).sum(axis=2).astype(np.int64)
    G=(F*(F-2)).astype(float)/(n*(n-2))
    assert np.allclose(np.diag(G),1.)
    assert np.max(abs(G.sum(axis=1))) < 1e-10
    d1=n-1
    d2=n*(n-3)//2
    d3=(n-1)*(n-2)//2
    pos=[]
    for d in (d1,d2,d3): pos.extend([factorial(n)/(n*(n-2)*d)]*(d*d))
    predicted=np.sort(np.array(pos + [0.]*(N-len(pos)),dtype=float))
    actual=np.linalg.eigvalsh(G)
    err=np.max(abs(actual-predicted))
    assert err<2e-10,(n,err)
    print('n',n,'samples',N,'rank',len(pos),'positive eig range',min(pos),max(pos),'max_abs_error',err)
    return err

if __name__=='__main__':
    for n in [4,5,6]: check(n)
    print('PASS')
