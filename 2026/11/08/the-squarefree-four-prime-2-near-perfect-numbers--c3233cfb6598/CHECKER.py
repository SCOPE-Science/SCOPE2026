#!/usr/bin/env python3
"""Exact finite certificate for the four-distinct-prime squarefree 2-near-perfect classification.

The accompanying proof reduces every possible prime triple to p in {3,5,7},
q in {5,7,11,13,17,19,23} if p=3, q in {7,11,13,17} if p=5,
and q=11 if p=7, with r at most 167. This code exhausts the reduced range.
"""
from math import isqrt, prod

def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))

def reduced_triples():
    P = list(filter(is_prime, range(3, 168)))
    Q = {3: (5, 7, 11, 13, 17, 19, 23), 5: (7, 11, 13, 17), 7: (11,)}
    for p, qs in Q.items():
        for q in qs:
            for r in P:
                if r > q:
                    yield p, q, r

def proper_divisors(p, q, r):
    return sorted(prod(s) for s in ((1,), (2,), (p,), (q,), (r,), (2, p),
       (2, q), (2, r), (p, q), (p, r), (q, r), (2, p, q),
       (2, p, r), (2, q, r), (p, q, r)))

def exact_solutions():
    ans=[]
    for p, q, r in reduced_triples():
        n=2*p*q*r
        ds=proper_divisors(p, q, r)
        assert len(ds)==15 and len(set(ds))==15 and all(n%d==0 and d<n for d in ds)
        sigma=prod(x+1 for x in (2,p,q,r))
        assert sigma==n+sum(ds)
        residual=sigma-2*n
        if residual<=0:continue
        matches=[(d,e) for i,d in enumerate(ds) for e in ds[i+1:] if d+e==residual]
        if matches:ans.append((n,p,q,r,residual,matches))
    return sorted(ans)

if __name__=='__main__':
    arr=exact_solutions()
    assert len(arr)==15, arr
    for n,p,q,r,D,matches in arr:
        print(f'{n:6} = 2*{p}*{q}*{r}: sigma(n)-2n={D}; pairs={matches}')
    print(f'EXACT_CERTIFICATE_OK count={len(arr)} largest={arr[-1][0]} tested_prime_triples={sum(1 for _ in reduced_triples())}')
