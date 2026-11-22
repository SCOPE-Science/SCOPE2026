#!/usr/bin/env python3
"""Exact subset recurrence and 5-point-symmetry check for dominated partitions."""
from functools import lru_cache
from itertools import combinations, permutations
from collections import Counter

V = list(combinations(range(5), 2))
idx = {a:i for i,a in enumerate(V)}
ALL = (1 << 10) - 1
# Petersen vertices are edges of K5, with adjacency iff disjoint.
Pnb = [sum(1 << j for j,b in enumerate(V) if a != b and not (set(a) & set(b))) for a in V]
# H is the complement of the Petersen graph, the triangular graph T5.
Hnb = [((ALL ^ (1 << i)) & ~Pnb[i]) for i in range(10)]

@lru_cache(None)
def matchings(mask):
    if mask == 0:
        return (1,)
    i = (mask & -mask).bit_length()-1
    a = list(matchings(mask ^ (1 << i)))
    nbr = Hnb[i] & mask
    while nbr:
        j = (nbr & -nbr).bit_length()-1
        nbr &= nbr-1
        b = matchings(mask ^ (1 << i) ^ (1 << j))
        while len(a) <= len(b):
            a.append(0)
        for k,c in enumerate(b):
            a[k+1] += c
    return tuple(a)

m0 = matchings(ALL)
m1 = matchings(ALL ^ Pnb[0])
assert m0 == (1,30,285,980,1020,144), m0
assert m1 == (1,15,54,40), m1
# Exactly 15 ways to choose two disjoint complete 3-vertex classes.
disjoint_centers = [(a,b) for a in range(10) for b in range(a+1,10) if not(Pnb[a] & Pnb[b])]
assert len(disjoint_centers) == 15
for a,b in disjoint_centers:
    rem = ALL ^ (Pnb[a] | Pnb[b])
    assert rem.bit_count() == 4
    assert matchings(rem) == (1,4,2)

coeff = Counter()
for t, poly, choices in [(0,m0,1),(1,m1,10),(2,(1,4,2),15)]:
    for p,count in enumerate(poly):
        coeff[10-2*t-p] += choices*count
assert dict(coeff) == {10:1,9:30,8:295,7:1130,6:1575,5:604,4:30}

# Construct every optimum from two disjoint size-three classes and one of
# the two perfect matchings of the remaining induced four-cycle.
optimal = set()
for a,b in disjoint_centers:
    rem=ALL ^ (Pnb[a] | Pnb[b]); U=[i for i in range(10) if rem>>i&1]
    for j in U[1:]:
        if Hnb[U[0]] >> j & 1:
            unused=rem ^ (1<<U[0]) ^ (1<<j)
            ss=[i for i in U if unused>>i&1]
            if Hnb[ss[0]] >> ss[1]&1:
                optimal.add(tuple(sorted([Pnb[a],Pnb[b],(1<<U[0])|(1<<j),unused])))
assert len(optimal) == 30

# All optima are in one orbit under permutation of the five underlying points.
seed = next(iter(optimal))
images = set()
for perm in permutations(range(5)):
    mp = [idx[tuple(sorted((perm[a],perm[b])))] for a,b in V]
    images.add(tuple(sorted(sum(1<<mp[i] for i in range(10) if block>>i&1) for block in seed)))
assert images == optimal, (len(images), len(optimal))

# Exact root certificate: six disjoint negative intervals have sign changes.
from fractions import Fraction as Q
q = [30,604,1575,1130,295,30,1]
def evaluate(x):
    out=Q(0)
    for c in q[::-1]:out = out*x+c
    return out
intervals=[(-15,-14),(-9,-8),(-5,-4),(-2,Q(-3,2)),(-1,Q(-1,2)),(Q(-1,10),0)]
root_signs=[]
for l,r in intervals:
    a,b=evaluate(Q(l)),evaluate(Q(r))
    assert a*b < 0
    root_signs.append((str(l),str(r),str(a),str(b)))
print('MATCHING_CERTIFICATE_OK')
print('m(T5)=' + str(m0))
print('m(T5-minus-open-neighborhood)=' + str(m1))
print('optimal-colorings=' + str(len(optimal)) + '; automorphism-orbit=' + str(len(images)))
print('partition-counts=' + repr(sorted(coeff.items())))
print('root-sign-intervals=' + repr(root_signs))
