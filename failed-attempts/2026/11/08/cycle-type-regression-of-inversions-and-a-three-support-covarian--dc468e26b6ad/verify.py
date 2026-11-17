#!/usr/bin/env python3
"""Exact finite verification of cycle-type inversion regression and covariances."""
from itertools import permutations
from collections import defaultdict
from fractions import Fraction
from math import factorial

checks=0

def test(ok, desc):
    global checks
    assert ok, desc
    checks+=1

for n in range(3,9):
    grouped=defaultdict(lambda:[0,0])
    sums=[0]*(n+1)
    cross=[0]*(n+1)
    invsum=0
    for pi in permutations(range(n)):
        seen=set(); c=[0]*(n+1)
        for a in range(n):
            if a not in seen:
                b=a; m=0
                while b not in seen:
                    seen.add(b);m+=1;b=pi[b]
                c[m]+=1
        inversions=sum(pi[i]>pi[j] for i in range(n) for j in range(i+1,n))
        key=tuple(c)
        grouped[key][0]+=inversions
        grouped[key][1]+=1
        invsum+=inversions
        for k in range(1,n+1):
            sums[k]+=c[k];cross[k]+=c[k]*inversions
    nf=factorial(n)
    test(Fraction(invsum,nf)==Fraction(n*(n-1),4),f'mean n={n}')
    for key,(s,count) in grouped.items():
        f,t=key[1],key[2]
        prediction=Fraction(n*(n-1),4)+Fraction(n*(1-f),6)-Fraction(f*(f-1),12)+Fraction(t,6)
        test(Fraction(s,count)==prediction,f'conditional n={n}, type={key}')
    for k in range(1,n+1):
        test(Fraction(sums[k],nf)==Fraction(1,k),f'cycle mean {n},{k}')
        cov=Fraction(cross[k],nf)-Fraction(sums[k]*invsum,nf*nf)
        if k==1:
            expected=Fraction(-(n+1),6)
        elif k==2:
            expected=Fraction(1,12)
        elif k==n:
            expected=Fraction(1,6)
        else:
            expected=Fraction(0)
        test(cov==expected,f'cycle covariance {n},{k}: got {cov}, expected {expected}')
print(f'{checks} exact assertions passed for all permutations of 3 through 8 elements')
