#!/usr/bin/env python3
"""Independent exact-arithmetic checks for weighted triangular-book cut games.

Run with Python 3.9+ and no third-party packages: python3 verify.py
This is a finite consistency checker, not a substitute for the theorem's proof.
"""
from fractions import Fraction as F
from itertools import product
from math import comb
import random


def prediction(a,b,t):
    k=len(a)
    A=sum(a,F(0)); B=sum(b,F(0))
    strict=[i for i in range(k) if a[i]>b[i]]
    free=[i for i in range(k) if a[i]==b[i]]
    A0=sum((a[i] for i in strict),F(0))
    B0=sum((b[i] for i in strict),F(0))
    low=(A-t)/2-A0; high=(B+t)/2-B0
    split=0
    for bits in product((0,1),repeat=len(free)):
        s=sum((a[i] for i,e in zip(free,bits) if e),F(0))
        if low <= s <= high: split+=1
    same=(t<=min(A,B))
    values=[]
    if same: values.extend([A+B]*2)
    if split: values.extend([t+sum(map(max,a,b))]*(2*split))
    opt=max(A+B,t+sum(map(max,a,b)))
    return len(values),opt,min(values),same,split


def direct(a,b,t):
    k=len(a)
    edges=[(0,1,t)] + [(0,i+2,a[i]) for i in range(k)] + [(1,i+2,b[i]) for i in range(k)]
    best=F(0); eq=[]
    for p in product((0,1),repeat=k+2):
        payoff=[F(0)]*(k+2)
        cut=F(0)
        for u,v,w in edges:
            if p[u]!=p[v]:
                payoff[u]+=w; payoff[v]+=w; cut+=w
        if cut>best: best=cut
        stable=True
        for i in range(k+2):
            # Flip i, the only deviator: compare current vs new incident sum.
            changed=sum((w if p[i]==p[v if u==i else u] else -w
                         for u,v,w in edges if u==i or v==i),F(0))
            if changed>0:
                stable=False;break
        if stable: eq.append((p,cut))
    return len(eq),best,min(w for p,w in eq),eq


def test(a,b,t):
    got=direct(a,b,t)
    exp=prediction(a,b,t)
    assert got[:3]==exp[:3],(a,b,t,got[:3],exp[:3])
    same=sum(p[0]==p[1] for p,w in got[3])
    assert same==2*int(exp[3]),(a,b,t,same,exp)
    assert len(got[3])-same==2*exp[4]
    return 2**(len(a)+2)


def run():
    settings=0; profiles=0
    for k in range(1,5):
        for coordinates in product((F(1),F(2)),repeat=2*k):
            a=coordinates[:k]; b=coordinates[k:]
            for t in (F(1,2),F(1),F(3,2),F(2),F(3),F(5)):
                profiles+=test(a,b,t); settings+=1
    rng=random.Random(20261102)
    for k, trials in ((5,250),(6,160),(7,100)):
        for _ in range(trials):
            a=tuple(F(rng.randint(1,7),rng.choice((1,2,3))) for i in range(k))
            b=tuple(F(rng.randint(1,7),rng.choice((1,2,3))) for i in range(k))
            t=F(rng.randint(1,10),rng.choice((1,2,3)))
            profiles+=test(a,b,t); settings+=1
    for k in range(1,12):
        a=b=tuple(F(1) for _ in range(k))
        for t in (F(1,2),F(1),F(2),F(k),F(k+1)):
            profiles+=test(a,b,t); settings+=1
            # Confirm binomial count for all-unit spoke weights.
            expected=2*(t<=k)+2*sum(comb(k,j) for j in range(k+1) if abs(2*j-k)<=t)
            assert prediction(a,b,t)[0]==expected
    for k in (2,4,6,8,10):
        t=F(1,2); e=F(1,100)
        unpert=prediction((F(1),)*k,(F(1),)*k,t)[0]
        pert=prediction((F(1)+e,)*k,(F(1)-e,)*k,t)[0]
        assert unpert==2+2*comb(k,k//2)
        assert pert==2
    print(f'PASS: {settings} independent parameter settings, {profiles} directly enumerated labeled profiles; exact equilibria, welfare, counts, and perturbation cases')

if __name__=='__main__':
    run()
