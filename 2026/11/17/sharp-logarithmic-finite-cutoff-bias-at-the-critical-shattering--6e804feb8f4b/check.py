#!/usr/bin/env python3
"""Finite cross-checks for the critical complete-monomer-shattering recurrence.

This checker does not prove the infinite asymptotic in RESULT.md.
Only the Python standard library is needed.
"""
from math import log
from fractions import Fraction

# Exact low-order coefficient checks.
a=[Fraction(0), Fraction(4,5)]
for k in range(2,15):
    a.append(Fraction(k,2*(k+4))*sum(a[i]*a[k-i] for i in range(1,k)))
assert a[1]==Fraction(4,5)
assert a[2]==Fraction(8,75)
for k in range(2,15):
    assert 2*(k+4)*a[k]==k*sum(a[i]*a[k-i] for i in range(1,k))

# Independent floating-point recurrence for n_k, with a_k=k*n_k.
N=2500
b=[0.0]*(N+1)
b[1]=0.8
for k in range(2,N+1):
    b[k]=k/(2.0*(k+4))*sum(b[i]*b[k-i] for i in range(1,k))
    assert b[k]>0.0

for z in (0.3, 0.5, 0.7, 0.85):
    G=sum((b[k]/k)*z**k for k in range(1,N+1))
    A=sum(b[k]*z**k for k in range(1,N+1))
    Aprime=sum(k*b[k]*z**(k-1) for k in range(1,N+1))
    assert abs(0.5*A*A-A-4*G+4*z)<1e-11
    assert abs(z*(1-A)*Aprime-4*(z-A))<1e-10

m2partial=[0.0]*(N+1)
for k in range(1,N+1):
    m2partial[k]=m2partial[k-1]+k*b[k]
for k in (100, 500, 1000, 2000, 2500):
    deficit=2.0-m2partial[k]
    print('cutoff=%d, second-moment tail=%.12f, (log cutoff)*tail/2=%.7f' %
          (k,deficit,log(k)*deficit/2))
    assert 0 < m2partial[k] < 2
assert m2partial[100]<m2partial[500]<m2partial[1000]<m2partial[2500]
print('PASS: exact recurrence, interior generating identities and finite positive tails')
