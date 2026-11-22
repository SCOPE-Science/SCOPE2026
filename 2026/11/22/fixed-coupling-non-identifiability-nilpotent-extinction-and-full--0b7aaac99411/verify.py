#!/usr/bin/env python3
"""Exact rational checks for a rank-one matrix quadratic map.
This is a finite diagnostic; the analytical proof covers all dimensions/states.
"""
from fractions import Fraction as Q
from itertools import product

def multiply(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))

def transpose(A):return tuple(zip(*A))
def quadratic(B,H):
    IminusH=tuple(tuple(Q(i==j)-H[i][j] for j in range(2)) for i in range(2))
    return multiply(multiply(multiply(B,H),IminusH),transpose(B))

I=((Q(1),Q(0)),(Q(0),Q(1)))
P=((Q(1),Q(0)),(Q(0),Q(0)))
ZERO=((Q(0),Q(0)),(Q(0),Q(0)))

def check(v0,v1):
    B=((2*v0,2*v1),(Q(0),Q(0)))
    BB=multiply(B,transpose(B))
    assert BB==((Q(4),Q(0)),(Q(0),Q(0)))
    lam=4*v0*v0
    for h in [Q(0),Q(1,8),Q(1,4),Q(1,3),Q(1,2),Q(3,4),Q(1)]:
        H=((h,Q(0)),(Q(0),h))
        X=quadratic(B,H)
        s=4*h*(1-h)
        assert X==((s,Q(0)),(Q(0),Q(0)))
        for _ in range(12):
            nextX=quadratic(B,X)
            s=lam*s*(1-s)
            assert nextX==((s,Q(0)),(Q(0),Q(0)))
            X=nextX
    return lam

for v0,v1 in [(Q(1),Q(0)),(Q(0),Q(1)),(Q(3,5),Q(4,5)),(Q(5,13),Q(12,13))]:
    lam=check(v0,v1)
    print('PASS rational nonnormal orientation; scalar gain =',lam)
Bzero=((Q(0),Q(2)),(Q(0),Q(0)))
for a,b,c in [(Q(1,4),Q(1,3),Q(2,5)),(Q(1),Q(0),Q(1)),(Q(1,2),Q(0),Q(1,2))]:
    H=((a,b),(b,c))
    if a < 0 or c < 0 or a > 1 or c > 1 or b*b>min(a*c,(1-a)*(1-c)):continue
    assert quadratic(Bzero,quadratic(Bzero,H))==ZERO
print('PASS: second iterate identically zero in nilpotent endpoint diagnostics')
print('ALL_CHECKS_PASS')
