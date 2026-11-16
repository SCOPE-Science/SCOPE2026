#!/usr/bin/env python3
"""Independent exact small-group checks for a class-constrained mixing theorem.
No external dependencies. Standard Python 3.10+.
"""
from itertools import permutations
from fractions import Fraction
from math import isclose

def compose(a,b):return tuple(a[b[i]] for i in range(5))
def inverse(a):return tuple(a.index(i) for i in range(5))
def parity(a):return sum(a[i]>a[j] for i in range(5) for j in range(i+1,5))%2
def order(a):
    e=tuple(range(5));x=e
    for n in range(1,61):
        x=compose(a,x)
        if x==e:return n
    raise AssertionError
G=[p for p in permutations(range(5)) if parity(p)==0]
assert len(G)==60
S=[p for p in G if order(p) in (3,5)]
assert len(S)==44
assert sum(order(g)==2 for g in G)==15
assert sum(order(g)==3 for g in G)==20
assert sum(order(g)==5 for g in G)==24
idx={g:i for i,g in enumerate(G)}
n=60
A=[[0]*n for _ in range(n)]
for i,g in enumerate(G):
    for s in S:
        j=idx[compose(g,s)]
        A[i][j]=1
assert all(sum(row)==44 for row in A)
assert all(A[i][j]==A[j][i] for i in range(n) for j in range(n))
def mul(B,C):
    out=[[0]*n for _ in range(n)]
    for i in range(n):
        ri=out[i]
        for k,x in enumerate(B[i]):
            if x:
                for j,y in enumerate(C[k]):
                    ri[j]+=x*y
    return out
I=[[int(i==j) for j in range(n)] for i in range(n)]
A2=mul(A,A)
A3=mul(A2,A)
A4=mul(A3,A)
# (x-44)(x-4)(x+1)(x+4) = x^4 -43x^3-60x^2+688x+704.
for i in range(n):
 for j in range(n):
  assert A4[i][j]-43*A3[i][j]-60*A2[i][j]+688*A[i][j]+704*I[i][j] == 0, ('polynomial',i,j)
tr=[60, sum(A[i][i] for i in range(n)), sum(A2[i][i] for i in range(n)),sum(A3[i][i] for i in range(n))]
for k in range(4):
    assert tr[k] == (44**k + 18*4**k + 16*(-1)**k + 25*(-4)**k),(k,tr[k])
# Check expected eigenvalue sum and class support and exact Markov stationarity.
for i in range(n):
    assert A[i][i]==0
    assert sum(A[i])==44
    assert sum(A[j][i] for j in range(n))==44
# At the candidate equal-weight walk A/44, smallest nonconstant contraction is max(4,1,4)/44=1/11.
# Verify a primal/dual rational LP certificate on 1001 convex class-mass points.
for k in range(1001):
    x=Fraction(k,1000)
    dual=max((1-x)/6,x/5)
    assert dual>=Fraction(1,11)
x=Fraction(5,11)
assert max((1-x)/6,x/5,abs(2*x-1)/4)==Fraction(1,11)
print('PASS: exactly 60 rotations, 44 admissible moves, 15 excluded involutions')
print('PASS: exact 60x60 adjacency annihilating polynomial and traces',tr)
print('PASS: adjacency spectrum 44 (1), 4 (18), -1 (16), -4 (25)')
print('PASS: uniform allowed transition has sharp mean-zero operator norm 1/11')
print('PASS: exact rational mass balance and convex dual lower bound')
