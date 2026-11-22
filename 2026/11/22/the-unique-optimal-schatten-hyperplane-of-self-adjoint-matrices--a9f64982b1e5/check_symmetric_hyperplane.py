#!/usr/bin/env python3
"""Independent finite-dimensional numerical consistency checks for a sharp hyperplane width.
These checks are illustrative, not substitutes for the all-dimensional proof.
"""
import math
import random


def target(n,p):
    return (2.0**(-1.0/p) if p<=1 else (1.0+(n-1)**(1.0-p))**(-1.0/p))


def ratio(vals,p):
    return max(map(abs, vals))/(sum(abs(v)**p for v in vals)**(1.0/p))

checks=0
rng=random.Random(20261105)
for n in range(2,12):
    for p in (0.4,0.7,1.0,1.25,1.8,2.0,3.0,6.0):
        k=target(n,p)
        x=([1.0,-1.0]+[0.0]*(n-2) if p<=1 else [n-1.0]+[-1.0]*(n-1))
        assert abs(ratio(x,p)-k)<1e-12
        checks+=1
        for _ in range(100):
            vals=[rng.uniform(-2,2) for j in range(n-1)]
            vals.append(-sum(vals))
            if max(abs(v) for v in vals)>1e-12:
                assert ratio(vals,p)<=k*(1+1e-10)
            checks+=1
        for _ in range(20):
            a=[math.exp(rng.uniform(-2,2)) for j in range(n)]
            amin=min(a);amax=max(a)
            if p>=1:
                t=amin/sum(a)
                vals=[1.0-t]+[-t]*(n-1)
            else:
                vals=[amax,-amin]+[0.0]*(n-2)
            assert ratio(vals,p)>=k*(1-1e-12)
            checks+=1

print('SYMMETRIC_HYPERPLANE_DIAGNOSTIC_OK', checks)
