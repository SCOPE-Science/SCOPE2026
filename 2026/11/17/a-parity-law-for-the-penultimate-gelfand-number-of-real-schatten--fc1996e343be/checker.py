#!/usr/bin/env python3
"""Exact finite diagnostic of conformal real matrix pencils (not an infinite proof).
Only Python standard library. Run: python checker.py
"""
from fractions import Fraction

def transpose(A):
    return [list(row) for row in zip(*A)]

def multiply(A, B):
    return [[sum(x*y for x,y in zip(row,col)) for col in transpose(B)] for row in A]

def block_rotation(n):
    assert n % 2 == 0 and n >= 2
    J = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(0,n,2):
        J[i][i+1]=-1
        J[i+1][i]=1
    return J

def pencil(n,a,b):
    m=n if n%2==0 else n-1
    J=block_rotation(m)
    A=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        for j in range(m):
            A[i][j]=a*(i==j)+b*J[i][j]
    return A

count=0
for n in range(2,16):
    m=n-(n%2)
    for a in range(-4,5):
        for b in range(-4,5):
            A=pencil(n,a,b)
            ATA=multiply(transpose(A),A)
            expect=[[int(i==j and i<m)*(a*a+b*b) for j in range(n)] for i in range(n)]
            assert ATA==expect, (n,a,b)
            count+=1
    J=block_rotation(m)
    assert multiply(transpose(J),J)==[[int(i==j) for j in range(m)] for i in range(m)]
    assert all(J[i][j] == -J[j][i] for i in range(m) for j in range(m))
    count+=2
# Exact finite counterexample to a parity-blind formula:
# in odd size a nonzero pencil vector has exactly n-1 equal singular values.
for n in (3,5,7,9,11,13,15):
    A=pencil(n,3,4)
    AA=multiply(transpose(A),A)
    assert AA[n-1][n-1]==0 and all(AA[i][i]==25 for i in range(n-1))
    count+=1
print('PASS: %d exact integer assertions on conformal-pencil Gram identities.'%count)
print('Limits: these finite identities do not prove the universal Gelfand-number theorem.')
