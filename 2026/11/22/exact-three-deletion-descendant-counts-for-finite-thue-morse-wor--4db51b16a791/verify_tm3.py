#!/usr/bin/env python3
"""Exact rational certificate and independent small-case verification for a deletion spectrum."""
import json
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path

HERE=Path(__file__).resolve().parent
D=json.loads((HERE/'tm3_coefficients.json').read_text(encoding='utf-8'))
DEG=6
Z=(F(0),)*(DEG+1)

def pad(a):
    a=tuple(a);return a+(F(0),)*(DEG+1-len(a))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def multiply(a,b):
    return tuple(sum(a[i]*b[j-i] for i in range(j+1)) for j in range(DEG+1))
def scale_x(a,factor): return tuple(v*(factor**i) for i,v in enumerate(a))
def eval_x(a,n): return sum(v*n**i for i,v in enumerate(a))
def load(parity):
    return [[[pad(F(a,b) for a,b in D[str(parity)][z][i][j]) for j in range(4)] for i in range(4)] for z in range(4)]
def mm(A,B):
    return [[[sum_polys([multiply(A[i][u][v],B[k-i][v][j]) for i in range(k+1) for v in range(4)]) for j in range(4)] for u in range(4)] for k in range(4)]
def sum_polys(parts):
    r=Z
    for p in parts:r=add(r,p)
    return r

def complement(A):
    p=(0,2,1,3)
    return [[[A[k][p[i]][p[j]] for j in range(4)] for i in range(4)] for k in range(4)]
def symbol(a):
    Q=[[[Z for j in range(4)] for i in range(4)] for k in range(4)]
    for p in range(4):
        mask=1 if a==0 else 2
        Q[1][p][p|mask]=pad((F(1),))
        if not(p&mask): Q[0][p][0]=pad((F(1),))
    return Q

def direct(word):
    A=[[[pad((F(i==j),)) for j in range(4)] for i in range(4)]]+[[[Z for j in range(4)] for i in range(4)] for k in range(3)]
    for a in word:A=mm(A,symbol(int(a)))
    return A

def thue(m):
    s='0'
    for _ in range(m):s=''.join('01' if c=='0' else '10' for c in s)
    return s

def count_dp(s,d=3):
    # Independent last-appearance subsequence count, indexed by deletions.
    v=[1]+[0]*d
    prev={}
    hist=[v[:]]
    for i,c in enumerate(s,1):
        z=[0]*(d+1)
        for t in range(d+1):
            z[t]=v[t]+(v[t-1] if t else 0)
            if c in prev:
                span=i-prev[c]
                if t>=span:z[t]-=hist[prev[c]-1][t-span]
        prev[c]=i;v=z;hist.append(z[:])
    return v[d]

def expected(m):
    n=2**m
    return ((2*n-5)*(2*n*n-n+26)//81 if m%2==0 else 2*(n-2)*(n+1)*(2*n-1)//81)

A=[load(0),load(1)]
for parity in range(2):
    for k in range(4):
        for i in range(4):
            for j in range(4):
                assert len(A[parity][k][i][j])==DEG+1
    n=4 if parity==0 else 8
    literal=direct(thue(2 if parity==0 else 3))
    for k in range(4):
        for i in range(4):
            for j in range(4):
                assert eval_x(A[parity][k][i][j],n)==literal[k][i][j][0],(parity,k,i,j)
    # Check one explicit polynomial identity at every coefficient and row/column.
    other=A[1-parity]
    twice=mm(A[parity],complement(A[parity]))
    for k in range(4):
        for i in range(4):
            for j in range(4):
                assert all(v==0 for v in add(scale_x(other[k][i][j],2),tuple(-x for x in twice[k][i][j]))),(parity,k,i,j)

for parity in range(2):
    poly=sum_polys([A[parity][3][0][j] for j in range(4)])
    nvars=(1,2,3,4,5,6,7)
    if parity==0: target=pad(tuple(map(F,(-130,57,-12,4))))
    else: target=pad(tuple(map(F,(4,-6,-6,4))))
    assert poly==tuple(x/81 for x in target)

for n in range(3,9):
    for bits in product('01',repeat=n):
        s=''.join(bits)
        lit=len({''.join(s[i] for i in range(n) if i not in pos) for pos in combinations(range(n),3)})
        assert count_dp(s)==lit,(s,lit,count_dp(s))
for m in range(2,6):
    s=thue(m);n=len(s)
    brute=len({''.join(s[i] for i in range(n) if i not in pos) for pos in combinations(range(n),3)})
    assert brute==expected(m)==count_dp(s)
for m in range(2,15):
    assert count_dp(thue(m))==expected(m),(m,count_dp(thue(m)),expected(m))
print('VERIFY_OK: 128 cubic-matrix polynomial identities, direct bases, all binary words length 3-8, literal Thue-Morse deletion checks m=2..5, independent recurrence m=2..14')
