#!/usr/bin/env python3
"""Standalone finite arithmetic checks for simplex Dirichlet fourth-moment identities.

Run with: python3 simplex_fourier_checker.py
Uses only Python standard library. The finite tests supplement, not replace, the proof.
"""
from collections import Counter
from itertools import product
from math import comb, factorial, isclose
from fractions import Fraction


def simp(d, n):
    return [v for v in product(range(n+1), repeat=d) if sum(v)<=n]


def containment(d,t):
    if t<0:return 0
    return sum(factorial(d)//(factorial(p)*factorial(q)*factorial(d-p-q))
               *comb(t,p)*comb(t,q) for p in range(d+1) for q in range(d-p+1)
               if p<=t and q<=t)


def formula(d,n):
    return sum((containment(d,t)-containment(d,t-1))*comb(n-t+d,d)**2
               for t in range(n+1))


def brute(d,n):
    pts=simp(d,n)
    counts=Counter(tuple(a_i-b_i for a_i,b_i in zip(a,b)) for a in pts for b in pts)
    return sum(v*v for v in counts.values())


def triangle(n):
    return (n+1)*(n+2)*(n*n+2*n+2)*(n*n+4*n+5)//20


def leading(d):
    return Fraction(factorial(2*d)**2, factorial(d)**4*factorial(3*d))


def normalized(d):
    return Fraction(factorial(2*d)**2, factorial(d)*factorial(3*d))


def run():
    checks=0
    for d,maxn in [(1,18),(2,12),(3,6),(4,3)]:
        for n in range(maxn+1):
            actual=brute(d,n)
            predicted=formula(d,n)
            assert actual==predicted, (d,n,actual,predicted)
            checks+=1
            if d==2:
                assert predicted==triangle(n), (d,n,predicted,triangle(n))
                checks+=1
    for n in range(80):
        assert formula(2,n)==triangle(n)
        checks+=1
    for d in range(1,9):
        assert 0<normalized(d)<=1
        assert normalized(d)==leading(d)*factorial(d)**3
        checks+=2
    assert normalized(1)==Fraction(2,3)
    assert normalized(2)==Fraction(2,5)
    assert normalized(3)==Fraction(5,21)
    checks+=3
    for d in range(1,10):
        assert normalized(d+1)<normalized(d)
        checks+=1
    print('PASS',checks,'exact comparisons; triangle e.g. n=2 energy',triangle(2),
          'd=3 normalized limit',normalized(3))

if __name__=='__main__':run()
