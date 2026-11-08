#!/usr/bin/env python3
"""Exact integer characteristic-polynomial certificate for the square-flat transfer."""
from fractions import Fraction

def step(a,b):return ((b-a+1)%3)-1
states=[(a,b) for a in range(3) for b in range(3)]
A=[[int(step(a,c)+step(c,d)-step(b,d)-step(a,b)==0) for c,d in states] for a,b in states]
n=len(A)
identity=[[Fraction(i==j) for j in range(n)] for i in range(n)]
B=identity
coef=[1]
for k in range(1,n+1):
    C=[[sum(A[i][l]*B[l][j] for l in range(n)) for j in range(n)] for i in range(n)]
    c=-sum(C[i][i] for i in range(n))/k
    assert c.denominator==1
    coef.append(int(c))
    B=[[C[i][j]+c*(i==j) for j in range(n)] for i in range(n)]
assert coef==[1,-9,12,42,-63,-93,90,108,-24,-32],coef
# Hand-expansion target: (x-2)^3 (x+1)^4 (x^2-7x+4).
from math import sqrt
r=sqrt(33)
lam=(7+r)/2
variance=(2+4/r)/lam
closed=1.25-19*r/132
assert abs(variance-closed)<1e-14
assert variance>0
print('characteristic_polynomial',coef)
print('principal_eigenvalue',f'{lam:.12f}')
print('winding_variance',f'{variance:.12f}')
print('ALGEBRA_OK')
