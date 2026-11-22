#!/usr/bin/env python3
"""Exact finite verification of the third-cumulant identity for degree statistics."""
from fractions import Fraction as F
from math import comb
from itertools import combinations


def bin_mean(n, p, func):
    return sum((F(comb(n,k))*p**k*(1-p)**(n-k)*func(k) for k in range(n+1)), F(0))


def formula(n,p,h):
    mu=bin_mean(n-1,p,h)
    m2=bin_mean(n-1,p,lambda k:h(k)**2)
    m3=bin_mean(n-1,p,lambda k:h(k)**3)
    a=bin_mean(n-2,p,lambda k:h(k+1)-h(k))
    b=bin_mean(n-2,p,lambda k:h(k+1)**2-h(k)**2)
    beta=bin_mean(n-3,p,lambda k:h(k+1)-h(k))
    gamma=bin_mean(n-3,p,lambda k:h(k+2)-2*h(k+1)+h(k))
    return (n*(m3-3*mu*m2+2*mu**3)
        +3*n*(n-1)*p*(1-p)*a*(b-2*mu*a)
        +n*(n-1)*(n-2)*p**2*(1-p)**2*gamma*(3*beta**2+6*p*beta*gamma+p*(2*p+1)*gamma**2))


def enumerate_graphs(n,p,h):
    edges=list(combinations(range(n),2))
    M=len(edges)
    raw=[F(0)]*4
    for mask in range(1<<M):
        degrees=[0]*n
        for j,(u,v) in enumerate(edges):
            if mask & (1<<j):
                degrees[u]+=1; degrees[v]+=1
        t=sum(h(x) for x in degrees)
        ones=mask.bit_count()
        weight=p**ones*(1-p)**(M-ones)
        for r in range(4):raw[r]+=weight*t**r
    assert raw[0]==1
    return raw[3]-3*raw[2]*raw[1]+2*raw[1]**3


def main():
    checks=0
    for n in range(3,7):
        for p in [F(1,3),F(2,5),F(3,4)]:
            h_cases=[lambda k: F(k), lambda k:F(k*k), lambda k:F(k%2),
                     lambda k:F(k==0), lambda k:F(k==1),
                     lambda k:F(k>=2),lambda k:F((-1)**k)]
            for h in h_cases:
                target=formula(n,p,h)
                brute=enumerate_graphs(n,p,h)
                assert target==brute,(n,p,target,brute)
                checks+=1
    for n in range(3,40):
        for p in [F(1,7),F(1,2),F(5,6)]:
            h=lambda k:F(k)
            assert formula(n,p,h)==4*n*(n-1)*p*(1-p)*(1-2*p)
            checks+=1
    print(f'PASS: {checks} exact rational third-cumulant assertions')

if __name__=='__main__': main()
