#!/usr/bin/env python3
"""Standalone row-state check, cut-polynomial factorization and even-subgraph order.
Run: python3 verify_rowstates.py. Uses only the Python standard library.
"""
from collections import Counter
from itertools import product
from math import comb

def bit(m, j):
    return (m >> j) & 1

def hcycle(a):
    return sum(bit(a, j) != bit(a, (j + 1) % 4) for j in range(4))

def hclique(a):
    return sum(bit(a, j) != bit(a, k) for j in range(4) for k in range(j+1, 4))

def cross_s(a,b):
    # Each row-to-next-row pair has four vertical and four diagonal links.
    return sum(bit(a,j) != bit(b,j) for j in range(4)) + sum(
        bit(a,j) != bit(b,(j+1)%4) for j in range(4))

def cross_r(a,b):
    return sum(bit(a,j) != bit(b,j) for j in range(4))

def histogram(s):
    h = Counter()
    for rows in product(range(16),repeat=4):
        if s:
            c = sum(hcycle(a) for a in rows) + sum(
                cross_s(rows[i], rows[(i+1)%4]) for i in range(4))
        else:
            c = sum(hclique(a) for a in rows) + sum(
                cross_r(rows[i], rows[j]) for i in range(4) for j in range(i+1,4))
        h[c]+=1
    assert sum(h.values())==65536
    return [h[k] for k in range(49)]

def multiply(p,q):
    v = [0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):
            v[i+j] += a*b
    return v

def power(p,n):
    v=[1]
    for _ in range(n):
        v=multiply(v,p)
    return v

r,s=histogram(False),histogram(True)
assert r[32]==90 and s[32]==42 and sum(r)==sum(s)==65536
# P_R(u)-P_S(u)=16*u^12*(u^2-1)^8*(3*u^4+2*u^2+1)
q=multiply([0]*12+[16],multiply(power([-1,0,1],8),[1,0,2,0,3]))
assert all(r[k]-s[k]==(q[k] if k<len(q) else 0) for k in range(49))
# From 2^-16 sum_{sigma}(1+t)^(48-c)(1-t)^c,
# coefficients are even-subgraph counts for the zero-field Ising model.
coeff=[]
for h in (r,s):
    a=[]
    for k in range(9):
        total=sum(h[c]*sum((-1)**j*comb(c,j)*comb(48-c,k-j)
          for j in range(max(0,k-48+c),min(k,c)+1)) for c in range(49))
        assert total%65536==0
        a.append(total//65536)
    coeff.append(a)
assert coeff[0][:8]==coeff[1][:8]==[1,0,0,32,60,288,1696,5568]
assert coeff[0][8]==19602 and coeff[1][8]==19506
print('VERIFY_ROWS_OK row_patterns=65536 each factorization_exact=1 first_difference_order=8 coefficient=96')
