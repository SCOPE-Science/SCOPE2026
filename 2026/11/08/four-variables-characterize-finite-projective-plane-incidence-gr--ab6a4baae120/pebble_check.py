#!/usr/bin/env python3
"""Exhaustively test a permanent three-pebble response invariant."""
from collections import defaultdict
from itertools import product

def levi(blocks,n):
    E=[[False]*(n+len(blocks)) for _ in range(n+len(blocks))]
    for j,b in enumerate(blocks):
        for p in b:
            E[p][n+j]=E[n+j][p]=True
    return E

def cyclic_fano(complement=False):
    b=[{(t+d)%7 for d in (0,1,3)} for t in range(7)]
    if complement:b=[set(range(7))-s for s in b]
    return levi(b,7),7

def plane3():
    def norm(v):
        k=next(q for q in v if q)
        return tuple((q*(1 if k==1 else 2))%3 for q in v)
    v=sorted({norm(a) for a in product(range(3),repeat=3) if any(a)})
    blocks=[{j for j,p in enumerate(v) if sum(a*b for a,b in zip(p,l))%3==0} for l in v]
    return levi(blocks,len(v)),len(v)

def profiles(E,boundary):
    n=len(E)
    signatures=defaultdict(set)
    for x in range(n):
        for y in range(n):
            pair=(x<boundary,y<boundary,x==y,E[x][y])
            possible=frozenset((z<boundary,z==x,z==y,E[z][x],E[z][y]) for z in range(n))
            signatures[pair].add(possible)
    assert all(len(s)==1 for s in signatures.values())
    return {t:next(iter(s)) for t,s in signatures.items()}

A=profiles(*cyclic_fano(False))
B=profiles(*cyclic_fano(True))
C=profiles(*plane3())
assert len(A)==len(B)==len(C)==8
assert A==B==C
# An existing pebble may be moved after forgetting it; two surviving pebbles
# determine one of these eight types. All possible third-pebble atomic
# extension profiles are present on either structure, indefinitely.
print('ORDERED_REFINED_TWO_PEBBLE_TYPES=8')
print('EXACT_EXTENSION_SUPPORT_FANO_COMPLEMENT_FANO_PG(2,3)=IDENTICAL')
print('UNLIMITED_THREE_PEBBLE_RESPONSE_INVARIANT=PASS')
