#!/usr/bin/env python3
"""Exact small-size checks for source/sink/isolated counts in independent directed graphs.

Run with: python3 verify.py
The infinite-dimensional and conditional-limit arguments are proved in RESULT.md,
not inferred from finite computation.
"""
from fractions import Fraction
from itertools import product
from math import exp, sqrt


def formulas(n, p):
    q = 1 - p
    a = q ** (n-1)
    b = a*a
    var_s = n*a*(1-a)
    cov_sk = n*(n-1)*p*q**(2*n-3)
    var_i = n*b*(1-b) + n*(n-1)*q**(4*n-6)*(1-q*q)
    cov_si = n*b*(1-a) + n*(n-1)*p*q**(3*n-4)
    return [n*a,n*a,n*b,var_s,var_s,var_i,cov_sk,cov_si,cov_si]


def exhaustive(n,p):
    arcs = [(u,v) for u in range(n) for v in range(n) if u != v]
    q = 1-p
    N = len(arcs)
    accum=[Fraction(0)]*9
    for mask in range(1 << N):
        incoming=[0]*n; outgoing=[0]*n; k=0
        for j,(u,v) in enumerate(arcs):
            if (mask >> j)&1:
                incoming[v] += 1
                outgoing[u] += 1
                k += 1
        s=sum(x==0 for x in incoming)
        t=sum(x==0 for x in outgoing)
        i=sum(incoming[v]==0 and outgoing[v]==0 for v in range(n))
        w=p**k*q**(N-k)
        for j,x in enumerate([s,t,i,s*s,t*t,i*i,s*t,s*i,t*i]):
            accum[j] += w*x
    means=accum[:3]
    return means+[accum[j]-means[a]*means[b] for j,a,b in
                  [(3,0,0),(4,1,1),(5,2,2),(6,0,1),(7,0,2),(8,1,2)]]


def limiting(lam):
    s = exp(-lam); t = s*s
    v = s*(1-s)
    c = lam*t
    d = t*(1-s) + lam*s*t
    w = t*(1-t) + 2*lam*t*t
    return ((v,c,d),(c,v,d),(d,d,w))


def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
           -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
           +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def main():
    checks=0
    for n in range(2,5):
        for p in [Fraction(1,5),Fraction(1,2),Fraction(3,4)]:
            x=exhaustive(n,p)
            y=formulas(n,p)
            for a,b in zip(x,y):
                assert a==b, (n,p,a,b)
                checks+=1
    for lam in [0.05,0.2,0.5,0.8,0.99]:
        a=limiting(lam)
        assert a[0][0]>0 and a[0][0]**2>a[0][1]**2 and det3(a)>0
        checks+=3
        n=100000
        exact=formulas(n,lam/n)
        candidates=(exact[3]/n,exact[5]/n,exact[6]/n,exact[7]/n)
        targets=(a[0][0],a[2][2],a[0][1],a[0][2])
        for x,y in zip(candidates,targets):
            assert abs(x-y)<0.00002,(lam,x,y)
            checks+=1
    print(f'VERIFY_OK {checks} exact/algebraic and limit checks')

if __name__=='__main__': main()
