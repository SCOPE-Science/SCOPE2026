#!/usr/bin/env python3
"""Reproducibility checks for a two-route ecological colonization example.

Uses exact rational arithmetic. This finite audit supplements, but cannot
replace, the symbolic proof for arbitrary nonnegative investments.
"""
from fractions import Fraction as F
from math import comb


def p(x):
    return x / (1 + x)


def R(a,b,c,d):
    return 1 - (1 - p(a)*p(b))*(1 - p(c)*p(d))


def h(t):
    return (1+2*t)/(1+t)**2


def P(s):
    return 2*s**3+s*s-8*s-8


def reliability_benchmarks(B):
    concentrate = p(B/2)**2
    balance = 1-(1-p(B/4)**2)**2
    return concentrate, balance


def verify():
    checks = 0
    # Within-branch equal allocation and full four-edge allocation.
    for n in range(1,29):
        B = F(n,4)
        c, b = reliability_benchmarks(B)
        best = max(c,b)
        for i in range(n+1):
            a = F(i,4)
            for j in range(n-i+1):
                x = F(j,4)
                for k in range(n-i-j+1):
                    y = F(k,4)
                    z = B-a-x-y
                    assert R(a,x,y,z) <= best
                    checks += 1
    # Exact identities used to compare the two candidate extrema.
    for j in range(1,81):
        s = F(j,20)
        lhs = h(s)-h(s/2)**2
        rhs = s*s*P(s)/(16*(1+s)**2*(1+s/2)**4)
        assert lhs == rhs
        checks += 1
    # Rational separated examples around the unique positive cubic root.
    assert P(F(2)) < 0 < P(F(5,2))
    for B, sign in [(F(4),-1),(F(17,4),-1),(F(9,2),1),(F(5),1)]:
        c,b = reliability_benchmarks(B)
        assert (b>c)-(b<c) == sign
        checks += 1
    # Numerical threshold bracketing is NOT used as a theorem proof.
    lo, hi = F(2178677,1000000), F(2178679,1000000)
    assert P(lo) < 0 < P(hi)
    checks += 1
    print('PASS',checks,'exact-rational assertions; unique positive root bracket',lo,hi)

if __name__=='__main__':
    verify()
