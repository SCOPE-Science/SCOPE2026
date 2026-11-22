#!/usr/bin/env python3
"""Reproducibility checks for a reservoir-coupled invasion threshold.
Uses only the Python standard library; the general proof is in RESULT.md.
"""
from fractions import Fraction as F
from itertools import permutations
from random import Random
from math import isclose


def loop_root(a, u, v):
    n = len(u)
    U, V = sum(u), sum(v)
    Q = sum(x*y for x, y in zip(u,v))
    lo = max(a, Q**0.5)
    hi = max(2.0, 2*lo)
    while (hi-a)*(hi*hi-Q) < a*U*V/n:
        hi *= 2
    for _ in range(90):
        mid = (lo+hi)/2
        if (mid-a)*(mid*mid-Q) >= a*U*V/n:
            hi=mid
        else:
            lo=mid
    return (lo+hi)/2


def direct_perron(a,u,v):
    n=len(u)
    x=[1.0]*(n+1)
    last=0.0
    for k in range(20000):
        s=sum(x[:n])
        z=[a*s/n+u[i]*x[n] for i in range(n)]
        z.append(sum(v[i]*x[i] for i in range(n)))
        norm=max(z)
        x=[t/norm for t in z]
        if k>20 and abs(norm-last)<2e-13:
            return norm
        last=norm
    raise AssertionError('direct power iteration did not settle')


def checks():
    cases=0
    a=F(1,2)
    u=(F(9,10),F(1,10))
    vs=((F(9,10),F(1,10)),(F(1,10),F(9,10)))
    U=sum(u)
    for v,expected in zip(vs,(F(33,25),F(17,25))):
        Q=sum(x*y for x,y in zip(u,v))
        loop=Q+a*U*sum(v)/(2*(1-a))
        assert loop==expected
        row_sums=[a+u[0],a+u[1],sum(v)]
        assert row_sums==[F(7,5),F(3,5),F(1)]
        rr=loop_root(float(a),list(map(float,u)),list(map(float,v)))
        pd=direct_perron(float(a),list(map(float,u)),list(map(float,v)))
        assert abs(rr-pd)<1e-10
        assert (rr>1)==(expected>1)
        cases+=1
    rng=Random(4371)
    for n in range(2,9):
        for j in range(32):
            aa=rng.uniform(0.15,1.1)
            uu=[rng.uniform(0.1,1.3) for _ in range(n)]
            vv=[rng.uniform(0.1,1.3) for _ in range(n)]
            rv=loop_root(aa,uu,vv)
            rp=direct_perron(aa,uu,vv)
            assert abs(rv-rp)<2e-9,(n,j,rv,rp)
            if aa<1 and abs(rv-1)>1e-7:
                gain=sum(x*y for x,y in zip(uu,vv)) + aa*sum(uu)*sum(vv)/(n*(1-aa))
                assert (rv>1)==(gain>1)
            cases+=1
    for n in range(2,6):
        for j in range(32):
            aa=rng.uniform(.15,.95)
            uu=sorted(rng.uniform(.1,1.2) for _ in range(n))
            vv=sorted(rng.uniform(.1,1.2) for _ in range(n))
            vals=[loop_root(aa,uu,p) for p in permutations(vv)]
            assert isclose(max(vals),loop_root(aa,uu,vv),abs_tol=2e-12)
            assert isclose(min(vals),loop_root(aa,uu,vv[::-1]),abs_tol=2e-12)
            cases+=len(vals)
    print(f'PASSED: {cases} independent exact, eigen-iteration, and permutation checks')

if __name__=='__main__':
    checks()
