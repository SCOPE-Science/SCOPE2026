#!/usr/bin/env python3
"""Exact finite-field and coefficient tests for prime-power osculating scrolls."""
from math import comb
from itertools import product


def coordinates(p, m, d, t, lambdas):
    return [sum(lambdas[j] * comb(i,j) * t**(i-j) for j in range(min(i,m-1)+1))%p for i in range(d+1)]


def verify_binomial_factorization(p, m, d):
    assert m>=3
    n=m
    while n>1:
        assert n%p==0
        n//=p
    degrees=[(d-r)//m for r in range(m)]
    assert min(degrees)>=1
    assert sum(a+1 for a in degrees)==d+1
    assert sum(degrees)==d-m+1
    for i in range(d+1):
        q,r=divmod(i,m)
        lhs={(i-j,j):comb(i,j)%p for j in range(min(i,m-1)+1) if comb(i,j)%p}
        rhs={(m*q+r-j,j):comb(r,j)%p for j in range(r+1) if comb(r,j)%p}
        assert lhs==rhs,(p,m,d,i,lhs,rhs)
    return degrees


def verify_scroll_equations(p,m,d,coordinates):
    pairs=[]
    for r in range(m):
        for q in range((d-r)//m):
            pairs.append((coordinates[m*q+r],coordinates[m*(q+1)+r]))
    for i in range(len(pairs)):
        for j in range(i+1,len(pairs)):
            a,b=pairs[i]; c,e=pairs[j]
            assert (a*e-b*c)%p==0,(p,m,d,i,j)


for p,m in ((3,3),(2,4),(5,5),(2,8),(3,9)):
    for d in range(2*m-1,3*m+2):
        degs=verify_binomial_factorization(p,m,d)
        print('SYMBOLIC_OK',p,m,d,'directrices',degs,'degree',d-m+1)

for p,m,d in ((3,3,5),(3,3,8),(2,4,7),(2,4,10),(5,5,9),(2,8,15)):
    image=set()
    for t in range(p):
        for rest in product(range(p),repeat=m-1):
            cs=coordinates(p,m,d,t,(1,)+rest)
            verify_scroll_equations(p,m,d,cs)
            image.add(tuple(cs))
    assert len(image)==p**m,(p,m,d,len(image))
    print('FINITE_AFFINE_OK',p,m,d,'incidences',p**m,'distinct_image_points',len(image))

print('ALL_CHECKS_PASSED')
