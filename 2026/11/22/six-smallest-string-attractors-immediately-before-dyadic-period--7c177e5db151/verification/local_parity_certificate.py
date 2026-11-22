#!/usr/bin/env python3
"""Finite factor-window certificate for period-doubling attractor parity.

This checker enumerates every possible centered length-nine factor in the
infinite substitution fixed point using fourth-order two-block images.
It does not extrapolate from a finite prefix: the exhaustive reduction to
these blocks is proved in the accompanying document.
"""
from itertools import product

def phi(w):
    return ''.join('01' if a == '0' else '00' for a in w)

def iterate(w, n):
    for _ in range(n):
        w = phi(w)
    return w

M = 5
T5 = iterate('0', 5)[:-1]
assert len(T5) == 31
U = sorted({T5[i:j] for i in range(31) for j in range(i+1, min(i+M,31)+1)})
assert len(U)==24
I={u:i for i,u in enumerate(U)}

def cover(x, pos):
    z=0
    for a in range(max(0,pos-M+1),pos+1):
        for b in range(pos+1,min(len(x),a+M)+1):
            u=x[a:b]
            if u in I:
                z |= 1 << I[u]
    return z

A=set(); B=set()
for xy in ('00','01','10'):
    w=iterate(xy,4)
    assert len(w)==32
    for i in range(len(w)-9+1):
        x=w[i:i+9]
        center=i+4
        if center%2==0 and x[4]=='0':
            A.add(cover(x,4))
        if center%2==1 and x[4]=='1':
            B.add(cover(x,4))

# Beginning-of-word windows that do not have four preceding symbols.
inf=iterate('0',9)
for p in range(4):
    if p%2==0 and inf[p]=='0':
        A.add(cover(inf[:p+5],p))
    if p%2==1 and inf[p]=='1':
        B.add(cover(inf[:p+5],p))

full=(1<<len(U))-1
bad=[(a,b) for a,b in product(A,B) if (a|b)==full]
assert not bad, bad
print('T5 factor set lengths 1..5:',len(U))
print('Possible coverage masks for 0 at zero-based even position:',len(A))
print('Possible coverage masks for 1 at zero-based odd position:',len(B))
print('Full-coverage pairs of these masks:',len(bad))
print('FINITE PARITY CERTIFICATE PASS')
