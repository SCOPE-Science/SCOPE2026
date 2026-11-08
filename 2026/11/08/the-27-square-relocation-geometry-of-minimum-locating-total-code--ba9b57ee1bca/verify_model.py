#!/usr/bin/env python3
"""Standalone isomorphism certificate for two conventional Pappus models."""
STATIC_EDGES=[(0,1),(0,5),(0,17),(1,2),(1,8),(2,3),(2,13),(3,4),(3,10),
(4,5),(4,15),(5,6),(6,7),(6,11),(7,8),(7,14),(8,9),(9,10),
(9,16),(10,11),(11,12),(12,13),(12,17),(13,14),(14,15),
(15,16),(16,17)]
# Node labels 0,...,8 are points (x,y)=(floor(i/3), i modulo 3).
# Node labels 9,...,17 are lines x=c, y=c, y-x=c, in that order.
INCIDENCE=set()
for x in range(3):
    for y in range(3):
        p=3*x+y
        for ell in (9+x,12+y,15+(y-x)%3):
            INCIDENCE.add(tuple(sorted((p,ell))))
# An explicit bijection from a standard 18-cycle + nine chords realization.
PERM=(0,9,2,17,3,12,6,16,1,13,7,11,8,14,5,10,4,15)
assert len(set(PERM))==18
mapped={tuple(sorted((PERM[i],PERM[j]))) for i,j in STATIC_EDGES}
assert len(INCIDENCE)==len(mapped)==27 and mapped==INCIDENCE
print('MODELS: explicit Pappus graph bijection verified, 18 vertices and 27 edges')
print('MODELS: PASS')
