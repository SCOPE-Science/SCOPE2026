#!/usr/bin/env python3
"""Exact integral certificate for the Desargues-configuration basis Walsh spectrum.
No third-party dependencies; Python 3.9+.
"""
from itertools import combinations, permutations
from collections import Counter
from math import comb

V = range(5)
E = list(combinations(V, 2))
INDEX = {edge: i for i, edge in enumerate(E)}

def mask_for(edges):
    return sum(1 << INDEX[tuple(sorted(e))] for e in edges)

TRI = [mask_for(combinations(t, 2)) for t in combinations(V, 3)]
BASES = [sum(1 << i for i in inds) for inds in combinations(range(10), 3) if sum(1 << i for i in inds) not in TRI]
assert len(TRI) == 10 and len(set(TRI)) == 10 and len(BASES) == 110
assert len(set(BASES)) == 110

# Direct character counting, without a transform or a Krawtchouk formula.
W_direct = [sum(1 if ((f & b).bit_count() % 2 == 0) else -1 for b in BASES) for f in range(1024)]

# Independent Möbius/Walsh-Hadamard transform of the full sparse kernel.
W_fwht = [int(t in BASES) for t in range(1024)]
for bit in range(10):
    jump = 1 << bit
    for block in range(0, 1024, 2 * jump):
        for j in range(jump):
            a, b = W_fwht[block+j], W_fwht[block+j+jump]
            W_fwht[block+j], W_fwht[block+j+jump] = a+b, a-b
assert W_direct == W_fwht

def kraw3(k):
    return sum((-1)**j * comb(k, j) * comb(10-k, 3-j) for j in range(4) if j<=k and 3-j<=10-k)

def signed_line(f):
    return sum(-1 if (f & t).bit_count()%2 else 1 for t in TRI)

W_formula = [kraw3(f.bit_count())-signed_line(f) for f in range(1024)]
assert W_direct == W_formula

# Enumerate exact S5 orbits without graph isomorphism software.
perms = list(permutations(V))
index_maps = [[INDEX[tuple(sorted((p[u], p[v])))] for u, v in E] for p in perms]
def apply_perm(mask, m):
    return sum(1 << m[i] for i in range(10) if mask >> i & 1)
def degree_sequence(f):
    d = [0]*5
    for i,(u,v) in enumerate(E):
        if f >> i & 1:
            d[u] += 1
            d[v] += 1
    return tuple(sorted(d,reverse=True))
def triangles_in_graph(f):
    return sum((t & f) == t for t in TRI)

unseen=set(range(1024)); orbit_records=[]
while unseen:
    s=min(unseen)
    orb={apply_perm(s,p) for p in index_maps}
    assert orb <= unseen
    assert len(orb)*120//len(orb) == 120
    unseen.difference_update(orb)
    vals={W_formula[x] for x in orb}
    assert len(vals)==1
    rec=(s.bit_count(),len(orb),W_formula[s],degree_sequence(s),triangles_in_graph(s),s)
    orbit_records.append(rec)
assert sum(a[1] for a in orbit_records)==1024
assert len(orbit_records)==34, len(orbit_records)

by_weight=Counter()
for f,w in enumerate(W_direct):
    by_weight[(f.bit_count(),w)] += 1
EXPECTED_BY_WEIGHT={
 0:{110:1},1:{44:10},2:{6:30,10:15},
 3:{-8:60,-4:40,-12:20},
 4:{-6:120,-10:75,2:10,-18:5},
 5:{-4:90,4:90,0:72},
 6:{6:120,10:75,-2:10,18:5},
 7:{8:60,4:40,12:20},
 8:{-6:30,-10:15},9:{-44:10},10:{-110:1}
}
for k in range(11):
    assert {w:count for (l,w),count in by_weight.items() if l==k}==EXPECTED_BY_WEIGHT[k]

EXACT={-110:1,-44:10,-18:5,-12:20,-10:90,-8:60,-6:150,-4:130,-2:10,0:72,
       2:10,4:130,6:150,8:60,10:90,12:20,18:5,44:10,110:1}
assert Counter(W_direct)==EXACT
zeros = [f for f,w in enumerate(W_direct) if w == 0]
assert len(zeros)==72
assert {f.bit_count() for f in zeros} == {5}
zero_orbits=[r for r in orbit_records if r[2]==0]
assert len(zero_orbits)==2
assert sorted((r[1],r[3],r[4]) for r in zero_orbits)==[
    (12,(2,2,2,2,2),0),
    (60,(3,3,2,1,1),1)]
assert len([r for r in orbit_records if r[0]==5])==6
assert min(abs(w) for w in W_direct if w) == 2
assert max(map(abs,W_direct)) == 110
assert sum(w>0 for w in W_direct)==476
assert sum(w<0 for w in W_direct)==476
assert all(W_direct[f ^ 1023] == -W_direct[f] for f in range(1024))
assert all(w%2==0 for w in W_direct)

if __name__=='__main__':
    print('Complete 1024-character check PASS: direct sums = FWHT = Krawtchouk-minus-lines')
    print('S5 orbit classification PASS: {} orbits'.format(len(orbit_records)))
    print('Signed spectral histogram:', sorted(EXACT.items()))
    print('Nullity=72, rank=952, inertia=(476,476,72), sharp nonzero gap=2, condition=55')
    print('Zero frequency S5 orbits (size, degree sequence, K5 triangle count, representative mask):')
    for k,o,w,d,t,s in zero_orbits:
        print((o,d,t,s))
    print('Orbit certificate for character weights 0 through 5:')
    for k,o,w,d,t,s in sorted((r for r in orbit_records if r[0]<=5),key=lambda z:(z[0],z[2],z[3])):
        print(f'weight={k} orbit={o} multiplier={w} degree={d} triangles={t} mask={s}')
