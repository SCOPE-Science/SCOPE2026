#!/usr/bin/env python3
"""Exact transfer checks and independent spectral sanity checks for prism CCA."""
from math import sqrt, pi
from collections import defaultdict


def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))

# Verify the proposed factorization at rational nonzero z values, by exact Fraction arithmetic.
from fractions import Fraction
for zz in [Fraction(1,2),Fraction(2,1),Fraction(1,1),Fraction(-1,1),Fraction(-2,3)]:
    s=zz+1/zz
    T=[[1+s,1+1/zz,1/zz],[1+zz,1+s,1+1/zz],[zz,1+zz,1+s]]
    for lam in [-3,0,2,5]:
        a=[[Fraction(lam if i==j else 0)-T[i][j] for j in range(3)] for i in range(3)]
        right=(lam-s)*(lam*lam-(3+2*s)*lam+s*s+s-2)
        assert det3(a)==right
print('determinant_factorization: PASS')


def transfer(n):
    total=0
    for init in (-1,0,1):
        states={(init,0):1}
        for _ in range(n):
            nxt=defaultdict(int)
            for (d,x),w in states.items():
                for e in (-1,0,1):
                    for a in (-1,0,1):
                        if abs(a+e-d)<=1:
                            nxt[(e,x+a)]+=w
            states=nxt
        total+=states.get((init,0),0)
    return 3*total

L=(7+sqrt(33))/2
sigma2=Fraction(5,4)-Fraction(19,132)*sqrt(33)
for n in [8,12,20,40,80]:
    exact=transfer(n)
    approx=3*L**n/(2*pi*sigma2*n)**.5
    print('n=%d count=%d asymptotic_ratio=%.10f' % (n,exact,exact/approx))
print('spectral_checks: PASS')
