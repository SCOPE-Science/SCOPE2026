#!/usr/bin/env python3
"""Exact finite rational-phase audit of block Young-orbit frequencies."""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
from math import gcd

cases=0
for q in range(2,11):
    for p in range(1,q):
        if gcd(p,q)!=1:continue
        alpha=F(p,q)
        for rho in [F(0),F(1,2*q)]:
            for n in range(1,11):
                # Exhaustive compositions through n=10; bounded selected compositions higher.
                cutsets=[]
                for r in range(1,min(n,5)+1):
                    x=list(combinations(range(1,n),r-1))
                    cutsets+=x[:min(len(x),5)]
                for cuts in cutsets:
                    s=(0,)+cuts+(n,)
                    lengths=[s[i+1]-s[i] for i in range(len(s)-1)]
                    cuts2={F(0),F(1)}
                    for S in s[1:]:
                        f=(S*alpha)%1
                        if f:cuts2.add(1-f)
                    boundaries=sorted(cuts2)
                    expected=[int(q*(b-a)) for a,b in zip(boundaries,boundaries[1:])]
                    cells={}
                    for t in range(q):
                        x=(t*alpha+rho)%1
                        j=next(i for i in range(len(boundaries)-1) if boundaries[i]<=x<boundaries[i+1])
                        obs=[]
                        for L,R in zip(s,s[1:]):
                            f=F(t)*alpha+rho
                            obs.append(((f+R*alpha).numerator//(f+R*alpha).denominator)-((f+L*alpha).numerator//(f+L*alpha).denominator))
                        obs=tuple(obs)
                        if j in cells:assert cells[j]==obs,(p,q,rho,s,j)
                        else:cells[j]=obs
                    assert len(cells)==len(boundaries)-1,(p,q,rho,s,cells,boundaries)
                    assert len(set(cells.values()))==len(cells),(p,q,rho,s,cells)
                    observed=Counter(next(i for i in range(len(boundaries)-1) if boundaries[i]<=((t*alpha+rho)%1)<boundaries[i+1]) for t in range(q))
                    assert [observed[i] for i in range(len(expected))]==expected,(p,q,rho,s,expected,observed)
                    cases+=1
print('PASS exact rational profile/frequency cases:',cases)
