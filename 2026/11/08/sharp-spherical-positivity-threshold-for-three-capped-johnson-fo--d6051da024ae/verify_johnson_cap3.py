#!/usr/bin/env python3
"""Independent small-dimension checks of a capped Johnson-distance spectrum.

Usage: python3 check_johnson_cap3.py
Dependencies: Python 3 and NumPy. The integer adjacency relations and powers
are assembled from four-subsets, independently of the formula under test.
"""
from itertools import combinations
from math import comb, log
import numpy as np


def predicted(n, j, t):
    theta = (4-j)*(n-4-j)-j
    p2 = (theta*theta-(n-2)*theta-4*(n-4))/4
    return -3**t+(1-3**t)*theta+(2**t-3**t)*p2


def root(n):
    def l3(x):
        return (n-10)-3*(n-8)*2**x+(2*n-15)*3**x
    lo, hi=0.0, 1.0
    assert l3(lo)<0<l3(hi)
    for _ in range(70):
        mid=(lo+hi)/2
        if l3(mid)>0: hi=mid
        else: lo=mid
    return (lo+hi)/2


for n in (8,9,10):
    X = list(combinations(range(n),4))
    N=len(X)
    raw=np.fromiter((min(4-len(set(a)&set(b)),3) for a in X for b in X),dtype=np.float64,count=N*N).reshape(N,N)
    a1=(raw==1).astype(np.int64)
    a2=(raw==2).astype(np.int64)
    assert np.array_equal(a1 @ a1, 4*(n-4)*np.eye(N,dtype=np.int64)+(n-2)*a1+4*a2)
    for p in (0.2, root(n), 1.0):
        distances = np.where(raw>0,raw**p,0)
        # Full eigenspectrum computed from explicit matrix, without scheme formulas.
        got=np.linalg.eigvalsh(distances)
        target=[sum(comb(4,i)*comb(n-4,i)*min(i,3)**p for i in range(1,5))]
        for j in range(1,5):
            target += [predicted(n,j,p)]*(comb(n,j)-comb(n,j-1))
        want=np.array(sorted(target))
        assert len(want)==N
        assert np.max(np.abs(got-want))<1e-7,(n,p,np.max(np.abs(got-want)))
        j3=predicted(n,3,p)
        for j in (1,2,4):
            assert predicted(n,j,p)<j3+1e-9
        if abs(p-root(n))<1e-9:
            assert abs(j3)<1e-9
            assert all(predicted(n,j,p)<-1e-5 for j in (1,2,4))
    print('n=%d vertices=%d beta=%.12f endpoint_nullity=%d'%(n,N,root(n),comb(n,3)-comb(n,2)))
for n in (100,1000,10000):
    value=n*root(n)
    assert abs(value-1/log(9/8))<350.0/n
    print('n=%d n*beta=%.9f'%(n,value))
print('JOHNSON_CAP3_DISTANCE_CHECKS_PASS')
