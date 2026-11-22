#!/usr/bin/env python3
"""Independent exact checks of sparse fixed-window composition spectra.
Run: python3 verify_fixed_window.py
No third-party packages required.
"""
from collections import Counter
from math import comb


def direct_signature(n, h, i, j):
    # 0-based positions; literal overlapping window counting.
    counts = [0, 0, 0]
    for start in range(n-h+1):
        weight = int(start <= i < start+h) + int(start <= j < start+h)
        counts[weight] += 1
    return tuple(counts)


def interval_signature(n, h, i, j):
    # 1-based positions; independent overlap-of-intervals method.
    a = (max(1, i-h+1), min(i, n-h+1))
    b = (max(1, j-h+1), min(j, n-h+1))
    size = lambda x: max(0, x[1] - x[0] + 1)
    overlap = max(0, min(a[1], b[1]) - max(a[0], b[0]) + 1)
    total = size(a) + size(b)
    return (n-h+1-total+overlap, total-2*overlap, overlap)


def predicted(n,h,t,u):
    if t < 2 or t > 2*h or u<0 or u>min(h-1,(t-1)//2):
        return 0
    if t==2*h:
        if u==0:
            return comb(n-3*h+3, 2)
        return n-3*h+2+u
    if u>0:
        return 2
    if t <=h:
        return t-1
    return 2*n-3*t+3


def observed(n,h,method):
    out=Counter()
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            x=method(n,h,i,j)
            t=x[1]+2*x[2]
            out[(t,x[2])]+=1
    return out

assert direct_signature(5,3,0,4)==(1,2,0)
checks=0
literal_checks=0
for h in range(2,31):
    for n in range(3*h-1,3*h+22):
        obs=observed(n,h,interval_signature)
        exp=Counter({(t,u):predicted(n,h,t,u)
          for t in range(2,2*h+1) for u in range(0,h) if predicted(n,h,t,u)>0})
        assert obs==exp,(n,h,obs-exp,exp-obs)
        assert len(obs)==h*h+h-1,(n,h,len(obs))
        assert sum(obs.values())==comb(n,2),(n,h)
        checks+=1
    n=3*h-2
    if n>=h:
        obs=observed(n,h,interval_signature)
        full={(t,u) for t in range(2,2*h+1) for u in range(h) if predicted(3*h-1,h,t,u)>0}
        assert full-set(obs)=={(2*h,0)},(n,h,full-set(obs))
        assert len(obs)==h*h+h-2,(n,h)
        checks+=1
for h in range(2,11):
    for n in range(h,3*h+7):
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                assert direct_signature(n,h,i-1,j-1)==interval_signature(n,h,i,j),(n,h,i,j)
                literal_checks+=1
print('VERIFY_OK exact_fiber_formula_cases=',checks)
print('VERIFY_OK direct_read_comparisons=',literal_checks)
print('VERIFY_OK saturation= h*h+h-1 threshold=3*h-1')
