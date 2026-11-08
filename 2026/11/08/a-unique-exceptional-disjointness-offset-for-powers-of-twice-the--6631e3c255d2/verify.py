#!/usr/bin/env python3
"""Exact finite checks for the disjointness classification of powers of 2 phi."""
from math import gcd, isqrt

def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a

def algebraic_criterion(i,j):
    d=j-i
    if d%2==0:return False
    den=fib(d)
    return (1<<i)*fib(j)%den==0 and (1<<(d+i))*fib(i)%den==0

def theorem(i,j):
    d=j-i
    return d%2==1 and (d==3 or i%d==0)

cases=0
for i in range(1,161):
    for d in range(1,161):
        j=i+d
        assert algebraic_criterion(i,j)==theorem(i,j), (i,j)
        cases+=1
print('LUCAS_DIVISIBILITY_EQUIVALENCE_OK',cases)

def powers(m):
    a,b=1,1
    for _ in range(1,m):a,b=a+5*b,a+b
    return a,b

def beatty(m,nmax):
    a,b=powers(m)
    return {k*a+isqrt(5*(k*b)**2) for k in range(1,nmax//a+2) if k*a+isqrt(5*(k*b)**2)<=nmax}

nmax=500000
B={i:beatty(i,nmax) for i in range(1,8)}
for i in range(1,8):
    for j in range(i+1,8):
        # Avoid false empty if the first term of R_j is beyond nmax.
        if min(B[j],default=nmax+1)>nmax:continue
        if theorem(i,j):assert not (B[i]&B[j]), (i,j)
        elif B[i]&B[j]:pass
        else:print('NO_FINITE_WITNESS_NOT_AN_IMPOSSIBILITY',i,j)
print('FINITE_BEATTY_DISJOINTNESS_OK', nmax)
assert theorem(1,4) and not theorem(1,6)
assert powers(4)==(56,24)
print('SPECIAL_OFFSET3_OK', 'alpha^4=3*alpha^3+8')
print('VERIFY_OK')
