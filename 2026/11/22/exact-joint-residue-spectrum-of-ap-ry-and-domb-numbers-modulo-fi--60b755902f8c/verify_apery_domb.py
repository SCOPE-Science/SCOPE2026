#!/usr/bin/env python3
"""Exact arithmetic verifier for a prime-five joint Apéry–Domb residue law."""
from math import comb
from collections import Counter

def apery(n):
    return sum(comb(n,k)**2 * comb(n+k,k)**2 for k in range(n+1))

def domb(n):
    return sum(comb(n,k)**2 * comb(2*k,k)*comb(2*n-2*k,n-k) for k in range(n+1))

def digit_pair(n):
    aa=[1,0,3,0,1]
    dd=[1,4,3,1,1]
    a=d=1
    while n:
        n,r=divmod(n,5)
        a=a*aa[r]%5
        d=d*dd[r]%5
    return a,d

def formula(L):
    # Group exponents r use 3**r modulo 5.
    diag=[0]*4
    for r in range(4):
        # convolution ring Z[g]/(g^4-1): (2+g)^L
        for j in range(r,L+1,4):
            diag[r]+=comb(L,j)*2**(L-j)
    out=Counter()
    for r in range(4):
        d=pow(3,r,5)
        out[(d,d)]=diag[r]
        out[(0,d)]=((5**L-1)//4 if r%2==0 else (5**L-2*3**L+1)//4)
    return out

assert [(apery(i)%5,domb(i)%5) for i in range(5)]==[(1,1),(0,4),(3,3),(0,1),(1,1)]
for L in range(5):
    counts=Counter(digit_pair(n) for n in range(5**L))
    assert counts==formula(L), (L,counts,formula(L))
    if L<=3:
        exact=Counter((apery(n)%5,domb(n)%5) for n in range(5**L))
        assert exact==counts,(L,exact,counts)
for n in range(300):
    assert (apery(n)%5,domb(n)%5)==digit_pair(n),n
for L in range(1,12):
    counts=formula(L)
    assert sum(counts.values())==5**L
    assert sum(v for (a,d),v in counts.items() if a!=0)==3**L
    assert all((a==0 or a==d) and d!=0 for a,d in counts if counts[a,d])
print('PASS: 300 independent direct pair evaluations; levels 0..4 complete; exact formulas levels 1..11.')
for L in (1,2,3):
    print('L',L,dict(sorted(formula(L).items())))
