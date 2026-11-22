#!/usr/bin/env python3
"""Exact-rational checks for quadratic finite-population temporary-group epidemics.

Run: python check.py
The analytic rank theorem is proved in RESULT.md; finite tests support it.
"""
from fractions import Fraction as F
from math import comb


def falling(x, k):
    out = 1
    for j in range(k): out *= x-j
    return out


def hazard_direct(n_population, infected, qdist, eta):
    """Exact expectation of (infected sampled partners)^2 / partners^eta."""
    ans = F(0)
    for t, p in qdist.items():
        for ell in range(max(0, t-(n_population-1-infected)), min(t,infected)+1):
            probability = F(comb(infected,ell)*comb(n_population-1-infected,t-ell),comb(n_population-1,t))
            ans += p * probability * F(ell*ell,t**eta)
    return ans


def hazard_moments(n_population, infected, qdist, eta):
    m1 = sum((p*F(t,t**eta) for t,p in qdist.items()),F(0))
    m2 = sum((p*F(t*(t-1),t**eta) for t,p in qdist.items()),F(0))
    return m1*F(infected,n_population-1)+m2*F(falling(infected,2),falling(n_population-1,2))


def determinant(mat):
    a,b,c=mat[0]; d,e,f=mat[1]; g,h,i=mat[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)


checks=0
for eta in range(5):
    for n in range(4,11):
        for t in range(1,n):
            for I in range(n):
                qdist={t:F(1)}
                assert hazard_direct(n,I,qdist,eta)==hazard_moments(n,I,qdist,eta)
                checks+=1
    for n in range(4,11):
        for I in range(n):
            qdist={1:F(1,4),2:F(1,4),3:F(1,2)}
            assert hazard_direct(n,I,qdist,eta)==hazard_moments(n,I,qdist,eta)
            checks+=1

A={2:F(1)}
B_harm={1:F(1,4),3:F(3,4)}
B_arith={1:F(1,2),3:F(1,2)}
for n in range(4,15):
    for I in range(n):
        assert hazard_direct(n,I,A,2)==hazard_direct(n,I,B_harm,2)
        assert hazard_direct(n,I,A,1)==hazard_direct(n,I,B_arith,1)
        checks+=2

for t1 in range(1,7):
    for t2 in range(t1+1,8):
        for t3 in range(t2+1,9):
            for eta in range(0,7):
                mat=[[F(1) for t in (t1,t2,t3)],
                     [F(t,t**eta) for t in (t1,t2,t3)],
                     [F(t*(t-1),t**eta) for t in (t1,t2,t3)]]
                d=determinant(mat)
                assert (d==0)==(eta in (1,2)),(t1,t2,t3,eta,d)
                checks+=1
            mat=[[F(1) for t in (t1,t2,t3)],
                 [F(t) for t in (t1,t2,t3)],
                 [F(1,t) for t in (t1,t2,t3)]]
            assert determinant(mat)!=0
            checks+=1

print('PASS:',checks,'exact rational checks; direct hypergeometric vs moments, both exceptional equivalences, rank transitions, combined protocol')
