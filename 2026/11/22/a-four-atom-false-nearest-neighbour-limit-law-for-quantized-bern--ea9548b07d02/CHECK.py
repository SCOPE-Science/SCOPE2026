#!/usr/bin/env python3
"""Self-contained exact first-hit certificate and finite-sample reproducibility checks."""
from fractions import Fraction
from itertools import product
import random

def exact_joint(p):
    p=Fraction(p); q=1-p
    # Four disjoint first two symbol branches: 00,01,10,11.
    # In 00 or 11 the next symbol following the as-yet-unseen other
    # symbol is a fresh Bernoulli(p), by independence after first hit.
    d={(a,b):Fraction(0) for a,b in product(range(2), repeat=2)}
    for x0,x1 in product(range(2), repeat=2):
        w=(p if x0 else q)*(p if x1 else q)
        if x0==x1:
            for fresh in (0,1):
                d[(x1,fresh) if x0==0 else (fresh,x1)]+=w*(p if fresh else q)
        else:
            for fresh in (0,1):
                d[(x1,fresh) if x0==0 else (fresh,x1)]+=w*(p if fresh else q)
    return d

def observed(bits):
    n=len(bits)-1
    appearances={b:[i for i,x in enumerate(bits[:n]) if x==b] for b in (0,1)}
    if min(map(len,appearances.values()))<2:
        return None
    bad=0
    for i in range(n):
        indices=appearances[bits[i]]
        j=indices[0] if indices[0]!=i else indices[1]
        bad+=bits[i+1]!=bits[j+1]
    return Fraction(bad,n)

def predicted(bits,p):
    a=[]
    for b in (0,1):
        t=bits.index(b)
        a.append(bits[t+1])
    q=1-p
    return q*(q if a[0] else p)+p*(q if a[1] else p)

def verify():
    for num in range(1,20):
        p=Fraction(num,20);q=1-p
        d=exact_joint(p)
        for (a,b),mass in d.items():
            assert mass==(p if a else q)*(p if b else q), (p,a,b,mass)
        values={a: (p if a==0 else q) for a in (0,1)}
        m=sum(d[a,b]*(q*values[a]+p*values[b]) for a,b in d)
        v=sum(d[a,b]*(q*values[a]+p*values[b]-m)**2 for a,b in d)
        assert m==2*p*q
        assert v==p*q*(p-q)**2*(p*p+q*q)
    for p in (Fraction(1,4),Fraction(1,2),Fraction(3,4)):
        rng=random.Random(int(1000*p))
        bits=[int(rng.random()<float(p)) for _ in range(300001)]
        f=observed(bits)
        assert f is not None
        L=predicted(bits,p)
        assert abs(float(f-L))<0.015,(p,f,L)
        print('p=',p,'n=300000','empirical=',float(f),'predicted=',float(L))
    print('PASS: 19 exact rational joint laws and moments; 3 sample comparisons')
if __name__=='__main__':verify()
