#!/usr/bin/env python3
"""Finite arithmetic tests for the translated-simplex packing-minimum formula.
This tests finite direction ranges only; the complete theorem has an analytic proof.
"""
from itertools import product
from fractions import Fraction
from math import gcd
from functools import reduce
import random

def formula(a,b):
    n=len(a); vals=[]
    for mask in range(1,1<<n):
        s=sum(a[i] for i in range(n) if mask>>i&1)
        D=max(s,b-s)
        vals.append((D,mask))
    D=min(v[0] for v in vals)
    return Fraction(1,1)/D,{mask for val,mask in vals if val==D}

def brute(a,b,B):
    n=len(a); best=None; dirs=set()
    for z in product(range(-B,B+1),repeat=n):
        if not any(z) or reduce(gcd,z,0)!=1: continue
        m=min((0,*z)); M=max((0,*z)); t=sum(x*y for x,y in zip(a,z))
        D=max(b*M-t,t-b*m)
        if best is None or D<best:
            best=D; dirs={z}
        elif D==best: dirs.add(z)
    return Fraction(1,1)/best,dirs

rng=random.Random(20261113)
ct=0
for n in range(2,6):
 for j in range(75):
    a=[rng.randint(1,9) for _ in range(n)]
    b=sum(a)+rng.randint(1,10)
    theory, masks=formula(a,b)
    obs, dirs=brute(a,b,2)
    assert obs==theory,(n,a,b,obs,theory)
    pred=set()
    for mask in masks:
        z=tuple((mask>>i)&1 for i in range(n))
        pred|={z,tuple(-v for v in z)}
    assert dirs==pred,(n,a,b,dirs,pred)
    ct+=1
# Named reductions (positive and negative PARTITION instances) confirm the encoding.
for w in [[1,2,3],[3,5,7],[2,2,2,2],[1,1,1,1,2,2],[3,3,3]]:
    W=sum(w); q=2*W+1; a=[2*x for x in w]+[q]; b=2*(W+q)
    rho,_=formula(a,b)
    partition=any(sum(w[i] for i in range(len(w)) if mask>>i&1)*2==W for mask in range(1<<len(w)))
    assert (rho==Fraction(2,b))==partition
    ct+=1
print('PASS',ct,'exact rational tests (including complete primitive directions up to bound 2)')
