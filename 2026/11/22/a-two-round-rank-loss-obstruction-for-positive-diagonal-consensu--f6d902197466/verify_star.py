#!/usr/bin/env python3
"""Exact rational, standalone witness and spot checks for the star rank-drop obstruction."""
from fractions import Fraction as F

def mul(A,B):
    return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in zip(*B)] for row in A]

def star(A):
    n=len(A)
    assert all(len(r)==n for r in A)
    assert all(sum(r,F(0))==1 for r in A)
    assert all(A[i][i]>0 for i in range(n))
    assert all(x>=0 for r in A for x in r)
    assert all(A[i][j]==0 for i in range(1,n) for j in range(1,n) if i!=j)

def singular_star(b,c):
    # b: positive hub-to-leaf probabilities. Choose alpha from Schur zero condition.
    m=len(b)
    assert m==len(c)
    a=[1-v for v in c]
    alpha=sum((b[i]*c[i]/a[i] for i in range(m)),F(0))
    assert sum(b,F(0))+alpha==1
    M=[[alpha]+list(b)]
    for i in range(m):
        row=[c[i]]+[F(0)]*m;row[i+1]=a[i];M.append(row)
    star(M)
    return M

def check_pair(A,B):
    # For a singular A and B the canonical vectors give nonzero pairing.
    m=len(A)-1
    w=[F(1)]+[-A[0][i]/A[i][i] for i in range(1,m+1)]
    k=[F(1)]+[-B[i][0]/B[i][i] for i in range(1,m+1)]
    assert all(sum((w[i]*A[i][j] for i in range(m+1)),F(0))==0 for j in range(m+1))
    assert all(sum((B[i][j]*k[j] for j in range(m+1)),F(0))==0 for i in range(m+1))
    assert sum((w[i]*k[i] for i in range(m+1)),F(0))>=1

A1=[[F(1,2),F(1,2),F(0)],[F(1,2),F(1,2),F(0)],[F(0),F(0),F(1)]]
A2=[[F(1,2),F(0),F(1,2)],[F(0),F(1),F(0)],[F(5,6),F(0),F(1,6)]]
A3=[[F(2,3),F(1,3),F(0)],[F(2,3),F(1,3),F(0)],[F(1,2),F(0),F(1,2)]]
for A in (A1,A2,A3):star(A)
assert mul(A3,mul(A2,A1))==[[F(1,3)]*3 for _ in range(3)]
# Rational singular test factors with isolated and nonisolated spokes.
examples=[A1,A3]
for c in ([F(1,2),F(0)],[F(1,3),F(1,4)],[F(2,3),F(0)]):
    # Positive b with sum b_i/(1-c_i)=1 (equivalent Schur singularity).
    # Choose b_i proportional to a_i and normalize so b_i/a_i sum 1.
    a=[1-z for z in c]
    b=[a[i]/len(c) for i in range(len(c))]
    examples.append(singular_star(b,c))
for A in examples:
    for B in examples:
        check_pair(A,B)
print('PASS: 3-round exact average consensus; 25 exact singular-pair nullspace tests')
