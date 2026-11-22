#!/usr/bin/env python3
"""Exact certificate for centered graph-ball maximal averaging on cycles C3-C6.
Python standard library only. Reconstructs every ball, every branch and every cut.
"""
from fractions import Fraction as F
from itertools import product
from math import lcm

def tv(v):
    return sum(abs(v[(i+1) % len(v)] - v[i]) for i in range(len(v)))

def data(n):
    balls = []
    for i in range(n):
        rr=[]
        for r in range(n//2 + 1):
            rr.append(tuple(j for j in range(n) if min((i-j)%n,(j-i)%n) <= r))
        balls.append(rr)
    S = lcm(*(len(b) for rr in balls for b in rr))
    rows = [[tuple(S//len(b) if j in b else 0 for j in range(n)) for b in rr] for rr in balls]
    return balls, S, rows

def branch_envelope(n):
    balls, scale, rows = data(n)
    cut_data = []
    for mask in range(1,(1<<n)-1):
        vec = tuple((mask >> j)&1 for j in range(n))
        cut_data.append((vec, tv(vec)))
    rmax=n//2+1
    maxratio=F(0)
    exceptional=[]
    high=[]
    for choice in product(range(rmax), repeat=n):
        chosen = [rows[i][choice[i]] for i in range(n)]
        best=F(0)
        for vec, denom in cut_data:
            out=tuple(sum(row[j] for j in range(n) if vec[j]) for row in chosen)
            ratio=F(tv(out), scale*denom)
            if ratio>best: best=ratio
        if best>maxratio:
            maxratio=best
        if n==6 and best>F(19,10): high.append((choice,best))
    if n==6:
        assert len(high)==3, high
        assert set(m for m,g in high) == {
            (3,0,0,3,0,0), (0,3,0,0,3,0), (0,0,3,0,0,3)
        }, high
        assert all(g==2 for m,g in high)
    assert maxratio=={3:F(1),4:F(5,4),5:F(7,5),6:F(2)}[n],(n,maxratio)
    print('COMPLETE_BRANCH_CUT_PASS',n,'branches',rmax**n,'cuts',len(cut_data), 'unconstrained',maxratio, 'excluded',len(high))

def mean(x,ball):
    return sum(F(x[j],len(ball)) for j in ball)

def apply(x,balls):
    return tuple(max(mean(x,b) for b in rr) for rr in balls)

def witnesses():
    records = [
      (3,(0,3,3),(1,0,0),(1,1,0),F(1)),
      (4,(0,10,13,13),(2,0,0,0),(0,0,1,0),F(5,4)),
      (5,(11,11,0,14,14),(1,0,2,0,0),(0,1,1,1,0),F(7,5)),
      (6,(0,9,9,8,9,9),(3,0,0,2,0,0),(0,0,1,1,1,0),F(19,10)),
    ]
    for n,x,choice,h,sharp in records:
        balls, scale, rows=data(n)
        assert all(v>=0 for v in x)
        for i in range(n):
            chosen=mean(x,balls[i][choice[i]])
            assert all(chosen>mean(x,balls[i][r]) for r in range(n//2+1) if r!=choice[i]),(n,i)
        epsilon=F(1,100)
        y=tuple(F(x[i])+epsilon*h[i] for i in range(n))
        for i in range(n):
            chosen=mean(y,balls[i][choice[i]])
            assert all(chosen>mean(y,balls[i][r]) for r in range(n//2+1) if r!=choice[i]),(n,i)
        diff=tuple(apply(y,balls)[i]-apply(x,balls)[i] for i in range(n))
        ratio=tv(diff)/tv(tuple(epsilon*hi for hi in h))
        assert ratio==sharp,(n,ratio)
        print('STRICT_NONNEGATIVE_PAIR_PASS',n,'gain',ratio,'diff',diff)

if __name__=='__main__':
    for n in range(3,7): branch_envelope(n)
    witnesses()
    print('ALL_CENTERED_CYCLE_LIPSCHITZ_CHECKS_PASSED')
