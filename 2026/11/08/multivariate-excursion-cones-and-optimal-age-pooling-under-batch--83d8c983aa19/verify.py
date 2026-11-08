#!/usr/bin/env python3
"""Finite diagnostics for the multivariate batch-reset excursion theorem.

Run: python3 verify.py
Only the accompanying analytical argument proves the all-parameter statement.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import math
import random


def increments(n: int, m: int, k: int) -> list[Fraction]:
    if not (n >= 4 and 2 <= m <= n - 2 and 3 <= k <= n - m + 1):
        raise ValueError('Invalid theorem parameters')
    return [Fraction(math.comb(n - j, m - 1), math.comb(n, m))
            for j in range(1, k + 1)]


def pooled_rate(n: int, m: int, a: tuple[float, ...], r=1.0, D=1.0):
    k = len(a)
    d = list(map(float, increments(n, m, k)))
    aa = sorted(a, reverse=True)
    blocks = [([j], d[j], aa[j]**2) for j in range(k)]
    j = 0
    while j < len(blocks) - 1:
        # The fitted squared ages must be nonincreasing.
        if blocks[j][2]/blocks[j][1] < blocks[j+1][2]/blocks[j+1][1]:
            b1, b2 = blocks[j], blocks[j+1]
            blocks[j:j+2] = [
                (b1[0]+b2[0], b1[1]+b2[1], b1[2]+b2[2])]
            j = max(0, j-1)
        else:
            j += 1
    t = [0.0]*k
    for labels, p, s in blocks:
        for idx in labels:
            t[idx] = math.sqrt(s / (4*D*r*p))
    rate = math.sqrt(r/D)*sum(math.sqrt(p*s) for _,p,s in blocks)
    return rate, tuple(tuple(group) for group,_,_ in blocks), t


def age_action(n, m, a, t, r=1.0, D=1.0):
    aa = sorted(a, reverse=True)
    d = list(map(float, increments(n,m,len(aa))))
    assert all(t[j] >= t[j+1] - 1e-10 for j in range(len(t)-1))
    assert all(v>0 for v in t)
    return r*sum(x*y for x,y in zip(d,t)) + sum(
        x*x/(4*D*y) for x,y in zip(aa,t))


def run():
    checks = 0
    # Direct combinatorial enumeration of the exact no-hit hazard.
    for n in range(4, 13):
        for m in range(2, n-1):
            for k in range(3,n-m+2):
                dd=increments(n,m,k)
                batches=list(combinations(range(n),m))
                for j in range(1,k+1):
                    p=Fraction(sum(any(x<j for x in s) for s in batches),len(batches))
                    assert p==sum(dd[:j])
                    checks+=1
    # Four distinct optimal age-clustering arrangements.
    samples=[((3.,2.,1.),((0,),(1,),(2,))),
             ((1.6,1.4,1.),((0,1),(2,))),
             ((2.,1.2,1.),((0,),(1,2))),
             ((1.,1.,1.),((0,1,2),))]
    for a,expected in samples:
        rate,blocks,ages=pooled_rate(5,2,a)
        assert blocks==expected,(a,blocks)
        assert abs(rate-age_action(5,2,a,ages))<2e-12
        checks+=1
    rng=random.Random(20261101)
    for _ in range(2000):
        n=rng.randint(4,13)
        m=rng.randint(2,n-2)
        k=rng.randint(3,n-m+1)
        a=tuple(math.exp(rng.uniform(-2.,2.)) for _ in range(k))
        r=math.exp(rng.uniform(-1.,1.))
        D=math.exp(rng.uniform(-1.,1.))
        rate,blocks,t=pooled_rate(n,m,a,r,D)
        d=list(map(float,increments(n,m,k)))
        s=sorted(a,reverse=True)
        assert abs(age_action(n,m,s,t,r,D)-rate)<1e-9*(1+rate)
        checks+=1
        # Check stationarity and nonnegative KKT multipliers for every pool.
        for group in blocks:
            q=sum(d[j] for j in group)
            z=sum(s[j]**2 for j in group)
            t0=math.sqrt(z/(4*D*r*q))
            for j in group:
                assert abs(t[j]/t0-1)<1e-12
            v=0.
            for j in group[:-1]:
                v+=r*d[j]-s[j]**2/(4*D*t0*t0)
                assert v>=-1e-9*(1+r)
            checks+=1
        for __ in range(10):
            perturbed=sorted((t[j]*math.exp(rng.uniform(-.8,.8)) for j in range(k)),reverse=True)
            assert age_action(n,m,s,perturbed,r,D) >= rate-1e-9*(1+rate)
            checks+=1
    # Exact equal-threshold formula and k=3 age-pooling transition.
    for n in range(4,16):
        for m in range(2,n-1):
            for k in range(3,n-m+2):
                rr=pooled_rate(n,m,(1.,)*k)[0]
                p=1-Fraction(math.comb(n-k,m),math.comb(n,m))
                assert abs(rr-math.sqrt(k*float(p)))<2e-12
                checks+=1
    # A regular C^1 but not C^2 boundary with two distinct limiting curvatures.
    a1=4/math.sqrt(3)
    d2=math.sqrt(0.7)*4/(a1*a1+4)**1.5
    assert d2>0.1
    checks+=1
    print(f'PASS {checks} deterministic tests (combinatorial hazards, four regimes, KKT, convex samples, equal-level law)')
    print('The logarithmic LDP and non-C2 claims require the written proof.')


if __name__=='__main__':
    run()
