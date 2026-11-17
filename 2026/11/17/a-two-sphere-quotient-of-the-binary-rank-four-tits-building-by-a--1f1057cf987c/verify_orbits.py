#!/usr/bin/env python3
"""Exact face-orbit enumeration for the type-A3 building over F2."""
from itertools import combinations

MODULUS=0b10011

def multiply(x,y):
    z=0
    while y:
        if y & 1:z ^= x
        y >>= 1
        x <<= 1
        if x & 16:x ^= MODULUS
    return z

def span(basis):
    values={0}
    for b in basis:values |= {x^b for x in tuple(values)}
    return frozenset(values)

subspaces=[]
for rank in (1,2,3):
    subspaces += [(rank,S) for S in sorted({span(A) for A in combinations(range(1,16),rank) if len(span(A))==(1<<rank)},key=lambda x:tuple(sorted(x)))]
I={v:i for i,v in enumerate(subspaces)}
assert len(subspaces)==65

def permutation(func):
    return tuple(I[(rank,frozenset(func(x) for x in S))] for rank,S in subspaces)

shift=permutation(lambda x:multiply(2,x))
frob=permutation(lambda x:multiply(x,x))
id_perm=tuple(range(65))
perms={id_perm}
frontier=[id_perm]
while frontier:
    g=frontier.pop()
    for h in (shift,frob):
        gh=tuple(h[g[i]] for i in range(65))
        if gh not in perms:
            perms.add(gh)
            frontier.append(gh)
assert len(perms)==60

faces=[[(i,) for i in range(65)]]
for dim in (2,3):
    faces.append([f for f in combinations(range(65),dim) if all(subspaces[f[j]][0]<subspaces[f[j+1]][0] and subspaces[f[j]][1]<subspaces[f[j+1]][1] for j in range(dim-1))])
assert [len(F) for F in faces]==[65,315,315]
def representative(face):
    return min(tuple(g[i] for i in face) for g in perms)
orbits=[{representative(f) for f in F} for F in faces]
assert [len(S) for S in orbits]==[4,9,7]
assert sum((-1)**i*len(S) for i,S in enumerate(orbits))==2
print('group_order=60')
print('face_counts=(65,315,315)')
print('orbit_cell_counts=(4,9,7)')
print('euler_characteristic=2')
print('PASS')
