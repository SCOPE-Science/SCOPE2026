"""Finite independent checks for Eulerian translated-frustum formulas.

Only exact arithmetic and directly evaluated lattice inequalities are used where
possible. Numeric Gaussian-window checks are illustrative, never an infinite proof.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial, sqrt, exp, pi, erf
import random

def eulerian(n):
    row=[1]
    for size in range(2,n+1):
        row=[(j+1)*(row[j] if j<len(row) else 0)
             +(size-j)*(row[j-1] if j else 0) for j in range(size)]
    return row

def atoms(r,c):
    weights=Counter()
    for k in range(1,c+1):
        for j,a in enumerate(eulerian(r+1)):
            t=k-j
            weights[comb(t+r,r) if t>=0 else 0]+=a
    denom=c*factorial(r+1)
    return {v:Fraction(w,denom) for v,w in weights.items()}

def geometry_count(r,c,phase):
    height=1-phase[-1]
    result=0
    for xs in product(range(1,c+3),repeat=r):
        if all(xs[i]-phase[i]>=0 for i in range(r)) and \
              sum(xs[i]-phase[i] for i in range(r))<=1+c*height+1e-10:
            result+=1
    return result

def section_formula(r,c,phase):
    t=1+c*(1-phase[-1])-sum(1-a for a in phase[:-1])
    m=int(t//1)
    return comb(m+r,r) if m>=0 else 0

def main():
    rng=random.Random(20261117)
    count=0
    for r in range(2,5):
        for c in range(1,5):
            d=atoms(r,c)
            assert sum(d.values())==1
            assert set(d)=={0}|{comb(m+r,r) for m in range(c+1)}
            volume=Fraction((c+1)**(r+1)-1,c*factorial(r+1))
            assert sum(v*p for v,p in d.items())==volume
            for _ in range(25):
                phase=[rng.random() for _ in range(r+1)]
                assert geometry_count(r,c,phase)==section_formula(r,c,phase)
                count+=1
    for r,c in ((2,1),(3,4),(5,10),(10,2),(20,14)):
        d=atoms(r,c)
        assert sum(d.values())==1
        assert sum(v*p for v,p in d.items())==Fraction((c+1)**(r+1)-1,c*factorial(r+1))
    # Critical-window convergence is tested on a coarse, finite scale only.
    for r in (120,250,500):
        row=eulerian(r+1)
        c=r//2
        numerator=sum(a*min(c,max(0,c-j+1)) for j,a in enumerate(row))
        p=numerator/(c*factorial(r+1))
        limit=2/sqrt(12*2*pi)
        assert abs(sqrt(r)*p-limit)<0.13
    print('PASS: 300 direct translated-frustum counts; exact atom laws, supports, means; Gaussian finite checks')
if __name__=='__main__':
    main()
