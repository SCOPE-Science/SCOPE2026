#!/usr/bin/env python3
"""Exact finite checks for the three-descent Eulerian residue theorem."""
from collections import Counter
from math import comb

def v2(x):
    assert x != 0
    return (abs(x) & -abs(x)).bit_length() - 1

def F(n):
    return -(n+1)*3**n - comb(n+1, 3)

checks = 0
for k in range(4, 11):
    m=1 << k
    T=2*m
    vals=[F(n) % m for n in range(3*T+k+1)]
    c=Counter(vals[:T])
    for y in range(m):
        assert c[y] == (9 if y % 16 in (0,10) else 1)
        checks+=1
    for a in (0, k, k+5, T+3):
        cc=Counter(vals[a:a+T])
        assert cc == c
        checks+=1
    for n in range(2*T+k):
        assert vals[n+T] == vals[n]
        checks+=1
    assert vals[k] != vals[k+T//2] if k % 2 == 0 else any(vals[n] != vals[n+T//2] for n in range(k, k+T))
    checks+=1
    # Independent Eulerian recurrence, rather than inclusion-exclusion.
    old=[1,0,0,0]
    for n in range(1,2*T+k+1):
        nxt=[0]*4
        for d in range(4):
            nxt[d]=((d+1)*old[d]+(n-d)*old[d-1] if d else old[0]) % m
        if n>=k:
            assert nxt[3] == vals[n]
            checks+=1
        old=nxt
# Exact distance laws, samples of even shifts and odd eight-divisible shifts.
for x in range(1,90):
    for h in range(2,66,2):
        if x%2 == 0 or h%8 == 0:
            got=v2(F(x+h)-F(x))
            want=v2(h)+(-1 if x%2==0 else 1)
            assert got == want, (x,h,got,want)
            checks+=1
print('PASS', checks, 'assertions')
