#!/usr/bin/env python3
"""Exact rational supporting checks for farthest-vertex cross-polytope contraction."""
from fractions import Fraction as Q
from itertools import product

def F(x,lam):
    d=len(x)
    j=max(range(d), key=lambda i:abs(x[i]))
    s=1 if x[j]>0 else -1
    if x[j]==0: s=1
    c=1-lam
    y=[lam*z for z in x]
    y[j]-=c*s
    return tuple(y), j

def argmax(x): return max(range(len(x)),key=lambda i:abs(x[i]))

count=0
for d in range(3,8):
    for lam in [Q(1,8),Q(1,3),Q(1,2)]:
        c=1-lam; u=c/(1+lam)
        for j in range(d):
            for s in [-1,1]:
                v=tuple(s*u if i==j else Q(0) for i in range(d))
                w,j0=F(v,lam)
                assert j0==j and w==tuple(-z for z in v)
                count+=1
        for z in product(range(-2,3),repeat=min(d,4)):
            x=tuple(Q(t,2*d+5) for t in z)+(Q(0),)*(d-min(d,4))
            assert sum(map(abs,x))<1
            if not any(x): continue
            y,j=F(x,lam)
            assert argmax(y)==j and abs(y[j])>max((abs(y[i]) for i in range(d) if i!=j),default=Q(0))
            for k in range(5):
                yy,jj=F(y,lam)
                assert jj==j and abs(yy[j])>max((abs(yy[i]) for i in range(d) if i!=j),default=Q(0))
                y=yy;count+=1
for lam in [Q(3,5),Q(2,3),Q(3,4),Q(9,10),Q(99,100)]:
    # perturb the boundary center inward and toward the first coordinate
    eps=Q(1,100000)
    x=(Q(1,2)-eps,Q(1,2)-2*eps,Q(0))
    y,j=F(x,lam)
    assert j==0 and argmax(y)==1
    count+=1
print('PASS: '+str(count)+' exact-rational supporting assertions')
