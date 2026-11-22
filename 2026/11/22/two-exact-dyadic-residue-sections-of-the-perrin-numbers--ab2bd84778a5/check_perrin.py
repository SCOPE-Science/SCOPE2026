#!/usr/bin/env python3
"""Standalone finite verification of stated Perrin residue-section identities.
The infinite theorem follows from the separately written matrix proof.
"""
from collections import Counter

M=((0,1,0),(0,0,1),(1,1,0))
I=((1,0,0),(0,1,0),(0,0,1))

def prod(a,b):
    return tuple(tuple(sum(a[i][t]*b[t][j] for t in range(3)) for j in range(3)) for i in range(3))
def power(a,n):
    r=I
    while n:
        if n&1:r=prod(r,a)
        a=prod(a,a);n//=2
    return r
def trace(a): return sum(a[i][i] for i in range(3))
def scaled_diff(a,b,scale):
    assert all((a[i][j]-b[i][j])%scale==0 for i in range(3) for j in range(3))
    return tuple(tuple((a[i][j]-b[i][j])//scale for j in range(3)) for i in range(3))
def valuation2(x):
    return (abs(x)&-abs(x)).bit_length()-1 if x else 10**9

A=power(M,7);B=scaled_diff(A,I,2);C=scaled_diff(power(M,14),I,4)
assert A==((1,2,2),(2,3,2),(2,4,3))
assert B==((0,1,1),(1,1,1),(1,2,1))
assert C==((2,4,3),(3,5,4),(4,7,5))
assert [trace(prod(power(M,j),B)) for j in (1,3)]==[5,7]
assert [trace(prod(power(M,j),C)) for j in (1,3)]==[17,29]

P=[3,0,2]
for n in range(3,7*1024+4):P.append(P[n-2]+P[n-3])
assert [trace(power(M,j)) for j in range(20)]==P[:20]
assert P[:14]==[3,0,2,3,2,5,5,7,10,12,17,22,29,39]
checks=0
for j in (1,3):
    for a in range(100):
        for b in range(a):
            assert valuation2(P[7*a+j]-P[7*b+j])==1+valuation2(a-b)
            checks+=1
for k in range(1,11):
    modulus=1<<k
    length=7<<(k-1)
    p=[3%modulus,0,2%modulus]
    seq=[]
    for n in range(length):
        seq.append(p[0]);p=[p[1],p[2],(p[0]+p[1])%modulus]
    assert p==[3%modulus,0,2%modulus]
    assert len(set(seq))==modulus
    for j,parity in ((1,0),(3,1)):
        got=[seq[7*t+j] for t in range(1<<(k-1))]
        assert len(set(got))==1<<(k-1)
        assert set(got)==set(range(parity,modulus,2))
        checks+=len(got)
    if k>1:
        assert power(M,length//2)!=tuple(tuple(x%modulus for x in row) for row in I)
    checks+=1
print('PASS: exact matrix certificates, 2-adic pairwise distances, and complete residue sections; assertions groups=',checks)
