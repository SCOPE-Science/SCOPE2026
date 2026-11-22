#!/usr/bin/env python3
"""Standalone exact checker for rank >=3 relative to triangle-free finite graphs.
Only Python standard library is required. The direct recurrence is independent of
six-point witness generation; the exhaustive finite census is not the proof of
its all-order characterization.
"""
from itertools import combinations, permutations, product
from collections import Counter
from math import factorial

N = 6
PAIRS = tuple(combinations(range(N), 2))
IDX = {e: i for i, e in enumerate(PAIRS)}
PERMS = tuple(permutations(range(N)))
TRANSPORT = tuple(tuple(1 << IDX[tuple(sorted((p[a], p[b])))] for a,b in PAIRS)
                  for p in PERMS)

def relabel(mask, transport):
    out = 0
    for i, flag in enumerate(transport):
        if mask & (1 << i):
            out |= flag
    return out

def adj(mask, v, w):
    if v == w:
        return False
    return bool(mask & (1 << IDX[tuple(sorted((v, w)))]))

def triangle_free(mask):
    for a,b,c in combinations(range(N), 3):
        if adj(mask,a,b) and adj(mask,a,c) and adj(mask,b,c):
            return False
    return True

def pair_rank_one(mask, u, v):
    # All admissible one-point extensions of the induced pair must be realized.
    # The double-adjacency type is admissible precisely for a nonedge pair.
    required = (0, 1, 2) if adj(mask,u,v) else (0, 1, 2, 3)
    seen = set()
    for w in range(N):
        if w != u and w != v:
            seen.add((1 if adj(mask,w,u) else 0) | (2 if adj(mask,w,v) else 0))
    return all(k in seen for k in required)

def directly_rank_three(mask):
    # Literal two successor steps from the empty marking, no structural criterion used.
    for u in range(N):
        if all(any((adj(mask,u,v) == edge_type) and pair_rank_one(mask,u,v)
                   for v in range(N) if v != u) for edge_type in (False, True)):
            return True
    return False

def shattered_nonedge(mask):
    # Entirely separate test: one nonedge pair has all four possible traces.
    return any(not adj(mask,u,v) and pair_rank_one(mask,u,v)
               for u,v in combinations(range(N),2))

# Use canonical vertices 0=u, 1=v, 2=a (u only), 3=b (v only),
# 4=c (both), 5=d (neither). The four forced edges are
# (0,2),(0,4),(1,3),(1,4). Other possible edges are
# (2,3),(2,5),(3,5),(4,5). Only the triangle (2,3,5) is forbidden.
MANDATORY = ((0,2),(0,4),(1,3),(1,4))
OPTIONAL = ((2,3),(2,5),(3,5),(4,5))

def encoding(edges):
    return sum(1 << IDX[tuple(sorted(e))] for e in edges)

shapes=[]
for flags in product((0,1), repeat=4):
    if flags[:3] == (1,1,1):
        continue
    edges = list(MANDATORY) + [OPTIONAL[i] for i,b in enumerate(flags) if b]
    m = encoding(edges)
    assert triangle_free(m)
    shapes.append(m)
assert len(shapes) == 14

# Independent template orbit expansion.
from_templates = {relabel(m, tr) for m in shapes for tr in TRANSPORT}
# Direct exhaustive enumeration of all labeled simple 6-vertex graphs.
from_recurrence = set()
all_triangle_free = 0
for m in range(1 << len(PAIRS)):
    if not triangle_free(m):
        continue
    all_triangle_free += 1
    literal = directly_rank_three(m)
    structural = shattered_nonedge(m)
    assert literal == structural, f'defining rank recurrence mismatch at {m}'
    if literal:
        from_recurrence.add(m)

assert from_recurrence == from_templates, 'template generation mismatch'
assert len(from_recurrence) == 2292
assert all_triangle_free == 5789, all_triangle_free
assert Counter(m.bit_count() for m in from_recurrence) == {4:360, 5:792, 6:780, 7:360}

remaining = set(from_recurrence)
orbits=[]
while remaining:
    representative = min(remaining)
    orbit = {relabel(representative, tr) for tr in TRANSPORT}
    assert orbit <= from_recurrence
    remaining -= orbit
    aut = factorial(N)//len(orbit)
    orbits.append((representative.bit_count(), representative, len(orbit), aut))
orbits.sort()
assert len(orbits)==9
assert Counter(e for e,_,_,_ in orbits)=={4:1,5:3,6:3,7:2}
assert sum(s for _,_,s,_ in orbits) == len(from_recurrence)
print('CHECK_OK triangle_free_total', all_triangle_free)
print('CHECK_OK six_vertex_labeled',len(from_recurrence),'isomorphism_classes',len(orbits))
print('CHECK_OK edge_distribution_labeled',sorted(Counter(m.bit_count() for m in from_recurrence).items()))
print('CHECK_OK edge_distribution_isoclasses',sorted(Counter(e for e,_,_,_ in orbits).items()))
print('CHECK_OK distinct_templates',len(shapes))
print('ORBIT_TABLE columns=edges,canonical_mask,labeled_orbit,automorphisms')
for rec in orbits:
    print(*rec)
print('ALL_CHECKS_OK')
