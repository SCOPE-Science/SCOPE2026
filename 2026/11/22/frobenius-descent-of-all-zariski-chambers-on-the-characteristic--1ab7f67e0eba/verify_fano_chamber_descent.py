#!/usr/bin/env python3
"""Exact, dependency-free incidence and finite-field chamber-descent checks."""
from collections import Counter, defaultdict
from itertools import product
from fractions import Fraction

V = tuple(range(1, 8))
def dot(a, b):
    return (a & b).bit_count() & 1

def move(rows, v):
    return sum(dot(rows[i], v) << i for i in range(3))

G = [rows for rows in product(V, repeat=3)
     if len({move(rows, v) for v in V}) == 7]
assert len(G) == 168

# Component labels: 0..6 are exceptional divisors E_v,
# and 7..13 are proper transforms L_a of the Fano lines a.v=0.
A = [[0] * 14 for _ in range(14)]
for i in range(7):
    A[i][i] = -1
    A[i+7][i+7] = -2
    for j in range(7):
        if dot(V[i], V[j]) == 0:
            A[j][7+i] = A[7+i][j] = 1
assert all(sum(A[i][j] == 1 for j in range(14)) == 3 for i in range(14))

perms = []
for rows in G:
    p = [V.index(move(rows, v)) for v in V]
    for a in V:
        # The line a.v=0 maps to the unique line annihilating
        # all transformed points of that original line.
        moved = [move(rows,v) for v in V if dot(a,v)==0]
        possible = [b for b in V if all(dot(b,w)==0 for w in moved)]
        assert len(possible) == 1
        p.append(7+V.index(possible[0]))
    assert len(set(p)) == 14
    assert all(A[i][j] == A[p[i]][p[j]]
               for i in range(14) for j in range(14))
    perms.append(tuple(p))
assert len(set(perms)) == 168

def perm_order(p):
    image = list(range(14))
    for k in range(1,169):
        image = [p[x] for x in image]
        if image == list(range(14)):
            return k
    raise AssertionError('not a group permutation')

def is_chamber(s):
    # This is the exact induced-matching/negative-definite criterion.
    for i in range(14):
        if (s >> i)&1:
            if sum(((s>>j)&1) and A[i][j]==1 for j in range(14))>1:
                return False
    return True

def is_negative_definite(s):
    # Independent exact rational LDL^t test of the actual curve intersection matrix.
    idx = [i for i in range(14) if (s>>i)&1]
    B = [[Fraction(-A[i][j]) for j in idx] for i in idx]
    for k in range(len(idx)):
        d = B[k][k]
        if d <= 0:
            return False
        for i in range(k+1, len(idx)):
            for j in range(i, len(idx)):
                B[j][i] = B[i][j] = B[i][j]-B[i][k]*B[j][k]/d
    return True

# Check all 16384 subsets against actual negative definiteness.
chambers = []
for s in range(1<<14):
    criterion = is_chamber(s)
    assert criterion == is_negative_definite(s), ('bad geometry',s)
    if criterion: chambers.append(s)
assert len(chambers) == 2257
geometric = tuple(Counter(s.bit_count() for s in chambers)[i] for i in range(8))
assert geometric == (1,14,91,322,651,728,392,58)

def push(p, s):
    return sum(1<<p[i] for i in range(14) if (s>>i)&1)

# Two independent enumerations of fixed chambers:
# (a) all 2257 supports tested directly, (b) vertex-orbit unions.
fixed = defaultdict(set)
orders = Counter()
representatives = {}
for p in perms:
    o = perm_order(p)
    orders[o] += 1
    representatives.setdefault(o,p)
    hist = tuple(Counter(s.bit_count() for s in chambers if push(p,s)==s)[i]
                 for i in range(8))
    seen = set()
    vertex_orbits = []
    for v in range(14):
        if v in seen: continue
        orb = []
        w = v
        while w not in seen:
            seen.add(w); orb.append(w); w=p[w]
        vertex_orbits.append(sum(1<<i for i in orb))
    hist2 = [0] * 8
    for choice in range(1<<len(vertex_orbits)):
        s = 0
        for i, mask in enumerate(vertex_orbits):
            if (choice>>i)&1: s |= mask
        if is_chamber(s):hist2[s.bit_count()]+=1
    assert hist == tuple(hist2)
    fixed[o].add(hist)
assert orders == Counter({1:1,2:21,3:56,4:42,7:48}), orders
assert all(len(v)==1 for v in fixed.values())
expected = {
    1:(1,14,91,322,651,728,392,58),
    2:(1,6,19,34,51,48,40,10),
    3:(1,2,1,4,6,2,5,4),
    4:(1,2,3,2,3,4,4,2),
    7:(1,0,0,0,0,0,0,2),
}
assert {o: next(iter(v)) for o,v in fixed.items()} == expected

# Independently reconstruct every full collineation orbit and prove the
# support-size and orbit-size distribution by a disjoint partition.
remaining = set(chambers)
orbit_details = Counter()
orbit_size_dist = Counter()
while remaining:
    seed = min(remaining)
    orbit = {push(p,seed) for p in perms}
    assert orbit <= remaining
    remaining.difference_update(orbit)
    orbit_details[(seed.bit_count(),len(orbit))] += 1
    orbit_size_dist[len(orbit)] += 1
assert sum(k * v for k,v in orbit_size_dist.items()) == 2257
assert sum(orbit_size_dist.values()) == 54
assert orbit_size_dist == Counter({1:3,7:10,21:8,28:12,42:4,84:16,168:1})
assert sum(orders[o] * sum(expected[o]) for o in orders)//168 == 54
assert sum(orders[o] * sum(expected[o]) for o in orders)%168 == 0

# The all-group invariant supports are just empty, all seven point curves,
# and all seven line curves, all with orbit size one.
assert orbit_details[(0,1)]==1 and orbit_details[(7,1)]==2
print('BINARY_COLLINEATIONS=168',sorted(orders.items()))
print('GEOMETRIC_CHAMBERS=2257',geometric)
for o in sorted(expected):
    p=expected[o]
    print('FROBENIUS_ORDER=%d CLASS_COUNT=%d FIXED=%d POLY=%s' %
          (o, orders[o], sum(p),','.join(map(str,p))))
print('CHAMBER_G_ORBITS=54')
print('ORBIT_SIZE_DISTRIBUTION='+','.join('%d:%d'%item for item in sorted(orbit_size_dist.items())))
print('ORBIT_SUPPORT_SIZE_TABLE='+','.join('%d/%d:%d'%(a,b,n) for (a,b),n in sorted(orbit_details.items())))
print('SEVEN_CYCLE_FIXED=EMPTY+ALL_SEVEN_EXCEPTIONALS+ALL_SEVEN_FANO_LINES')
print('FANO_FROBENIUS_ZARISKI_CHAMBER_DESCENT_OK')
