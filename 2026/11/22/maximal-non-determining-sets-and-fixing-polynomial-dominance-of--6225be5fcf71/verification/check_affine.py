#!/usr/bin/env python3
"""Algebraic exhaustive certificate for pointwise determining sets on two 16-vertex graphs."""
from itertools import product, permutations
from collections import Counter
from math import comb

P = list(product(range(4), repeat=2))
ix = {u: i for i,u in enumerate(P)}
steps = {(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
L = []
for a,b,c,d in product(range(4), repeat=4):
    if {((a*x+b*y)%4,(c*x+d*y)%4) for x,y in steps} == steps:
        L.append((a,b,c,d))
assert len(L) == 12
shri = set()
for a,b,c,d in L:
    for s,t in P:
        shri.add(tuple(ix[((a*x+b*y+s)%4,(c*x+d*y+t)%4)] for x,y in P))
assert len(shri)==192
rook = set()
for pa in permutations(range(4)):
    for pb in permutations(range(4)):
        for swap in (0,1):
            rook.add(tuple(ix[(pa[y] if swap else pa[x], pb[x] if swap else pb[y])] for x,y in P))
assert len(rook)==1152

def by_automorphisms(group):
    ident = tuple(range(16))
    fixes = [sum(1<<i for i,j in enumerate(g) if i==j) for g in group if g!=ident]
    masks=set(fixes)
    maximal={f for f in masks if not any(f != h and f&h==f for h in masks)}
    coefficients=[0]*17
    good=[0]*65536
    for x in range(65536):
        ok=not any(x&f==x for f in maximal)
        good[x]=int(ok)
        coefficients[x.bit_count()]+=ok
    return coefficients,maximal,good

S, FS, gs=by_automorphisms(shri)
R, FR, gr=by_automorphisms(rook)
bs=[comb(16,k)-S[k] for k in range(17)]
br=[comb(16,k)-R[k] for k in range(17)]
assert bs == [1,16,120,112,28]+[0]*12,bs
assert br == [1,16,120,560,812,672,336,96,12]+[0]*8,br
assert Counter(f.bit_count() for f in FS)=={4:28}
assert Counter(f.bit_count() for f in FR)=={8:12,4:24}
# Enumerate the order-four cosets independently.
subgroups=set()
for p in P:
    for q in P:
        if p==(0,0) or q==(0,0):continue
        H=frozenset(((i*p[0]+j*q[0])%4,(i*p[1]+j*q[1])%4) for i in range(4) for j in range(4))
        if len(H)==4: subgroups.add(H)
assert len(subgroups)==7
cosets={sum(1<<ix[((x+a)%4,(y+b)%4)] for x,y in H) for H in subgroups for a,b in P}
assert cosets==FS
slabs={sum(1<<ix[(i,j)] for i,j in P if i in rows) for rows in __import__('itertools').combinations(range(4),2)} | {sum(1<<ix[(i,j)] for i,j in P if j in cols) for cols in __import__('itertools').combinations(range(4),2)}
trans={sum(1<<ix[(i,pa[i])] for i in range(4)) for pa in permutations(range(4))}
assert len(slabs)==12 and len(trans)==24 and slabs|trans==FR
assert [S[k]-R[k] for k in range(3,9)]==[448,784,672,336,96,12]
print('PASS: affine group=192, rook group=1152')
print('PASS: maximal fixed sets: Shrikhande=28 subgroup cosets; rook=12 slabs plus 24 transversals')
print('PASS: failure-coefficients Shrikhande', bs)
print('PASS: failure-coefficients rook', br)
print('PASS: successful coefficients Shrikhande',S)
print('PASS: successful coefficients rook',R)
