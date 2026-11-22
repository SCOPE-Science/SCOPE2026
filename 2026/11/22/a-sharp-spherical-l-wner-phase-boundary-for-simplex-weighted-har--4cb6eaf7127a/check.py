#!/usr/bin/env python3
"""Exact finite checks for the harmonic-polytope spherical-ellipsoid threshold.

This program checks the finite vertex geometry and the rearrangement
extrema independently of the symbolic all-n argument in RESULT.md.
"""
from itertools import permutations
from fractions import Fraction as F
from math import factorial

def centered(p):
    n = len(p)
    return tuple(F(2*a-n-1,2) for a in p)

def shell_and_contacts(n, lam):
    perms = list(permutations(range(1,n+1)))
    mid = F(n+1,2) + lam/F(n)
    radius_sq = F(n*(n*n-1),6) + 2*lam*(n-1) + 2*lam*lam*F(n-1,n)
    num_contact = 0
    top = F(-1)
    for p in perms:
        for q in perms:
            for k in range(n):
                v = tuple(F(x) + (lam if j==k else 0) - mid for j,x in enumerate(p))
                w = tuple(F(x) + (lam if j==k else 0) - mid for j,x in enumerate(q))
                norm2 = sum(x*x for x in v+w)
                if norm2>top: top=norm2
                if norm2 == radius_sq:
                    assert p[k]==n and q[k]==n
                    num_contact += 1
    assert top==radius_sq
    assert num_contact==n*factorial(n-1)**2
    return num_contact

def cross_extrema(n, lam):
    h = F(n-1,2)
    ranks = [F(2*i-n-1,2) for i in range(1,n)]
    mn=None;mx=None
    for q in permutations(ranks):
        dot = h*h + sum(a*b for a,b in zip(ranks,q))
        cross = dot + 2*lam*h + lam*lam*F(n-1,n)
        if mn is None or cross<mn: mn=cross
        if mx is None or cross>mx: mx=cross
    formula_min = F(n-1)*( -F(n*(n-5),12)+lam+lam*lam/F(n))
    formula_max = F(n*(n*n-1),12)+lam*(n-1)+lam*lam*F(n-1,n)
    assert mn==formula_min,(n,mn,formula_min)
    assert mx==formula_max,(n,mx,formula_max)
    return mn,mx

def threshold_predicate(n, lam):
    return n>=6 and 12*(lam*lam+n*lam)<=n*n*(n-5)

if __name__=='__main__':
    checked=0
    for n in range(2,6):
        for lam in (F(1,3),F(1),F(5,2)):
            assert shell_and_contacts(n,lam)==n*factorial(n-1)**2
            checked+=1
    cross_checks=0
    for n in range(2,9):
        for lam in (F(1,3),F(1),F(5,2)):
            lo,hi=cross_extrema(n,lam)
            assert (lo<=0)==threshold_predicate(n,lam)
            assert hi>0
            cross_checks+=1
    assert threshold_predicate(6,F(1)) is False
    assert threshold_predicate(7,F(1)) is True
    assert threshold_predicate(6,F(1,3)) is True
    assert threshold_predicate(7,F(3,2)) is False
    print('HARMONIC_LOEWNER_THRESHOLD_PASS',
          'formal_vertex_cases=',checked,
          'rearrangement_cases=',cross_checks)
