#!/usr/bin/env python3
"""Reproduce D5-orbit barycentric chains for the non-2-connected five-graph complex.
Standard Python 3 only. No external data files.
"""
from itertools import combinations
from collections import Counter

N = 5
EDGES = tuple(combinations(range(N), 2))
EIDX = {e: i for i, e in enumerate(EDGES)}

def is_connected(mask, removed):
    vertices = tuple(v for v in range(N) if v != removed)
    reached, pending = {vertices[0]}, [vertices[0]]
    while pending:
        v = pending.pop()
        for i, (a, b) in enumerate(EDGES):
            if not (mask >> i) & 1: continue
            u = b if a == v else a if b == v else -1
            if u >= 0 and u != removed and u not in reached:
                reached.add(u)
                pending.append(u)
    return len(reached) == len(vertices)

FACES = tuple(m for m in range(1, 1 << len(EDGES))
              if any(not is_connected(m, v) for v in range(-1, N)))
assert len(FACES) == 785
GROUP = tuple(tuple(EIDX[tuple(sorted(((a * sign + t) % N, (b * sign + t) % N)))]
                    for a,b in EDGES)
              for t in range(N) for sign in (1, -1))
assert len(set(GROUP)) == 10
ACTION = tuple(tuple(sum(1 << g[j] for j in range(10) if mask >> j & 1)
                      for mask in range(1 << 10)) for g in GROUP)

def canonical(flag):
    return min(tuple(a[mask] for mask in flag) for a in ACTION)

LEVELS = [sorted({canonical((mask,)) for mask in FACES})]
for d in range(1, 7):
    nextlevel = set()
    for flag in LEVELS[-1]:
        parent = flag[-1]
        sub = (parent - 1) & parent
        while sub:
            nextlevel.add(canonical(flag + (sub,)))
            sub = (sub - 1) & parent
    LEVELS.append(sorted(nextlevel))

COUNT = [len(x) for x in LEVELS]
assert COUNT == [97, 2286, 15678, 44928, 61680, 40320, 10080], COUNT
assert sum((-1)**d * count for d,count in enumerate(COUNT)) == 1
INDEX = [{flag: i for i, flag in enumerate(level)} for level in LEVELS]

# Differential is mod 2: order-complex vertices have distinct ranks,
# so the D5-action has no inversions after barycentric subdivision.
BOUNDARIES = [None]
RANKS = [0] * 7
for d in range(1, 7):
    columns = []
    pivots = {}
    for flag in LEVELS[d]:
        bitset = 0
        for i in range(len(flag)):
            subflag = flag[:i] + flag[i+1:]
            bitset ^= 1 << INDEX[d-1][canonical(subflag)]
        columns.append(bitset)
        reduced = bitset
        while reduced:
            leading = reduced.bit_length() - 1
            if leading not in pivots:
                pivots[leading] = reduced
                break
            reduced ^= pivots[leading]
    BOUNDARIES.append(columns)
    RANKS[d] = len(pivots)
assert RANKS == [0, 96, 2190, 13488, 31440, 30238, 10080], RANKS

# Independently enforce d^2 = 0 in every degree, including high dimensions.
for d in range(2, 7):
    for col in BOUNDARIES[d]:
        square = 0
        while col:
            lowest = col & -col
            row = lowest.bit_length() - 1
            square ^= BOUNDARIES[d-1][row]
            col ^= lowest
        assert square == 0, ('boundary-square', d)

BETTI_MOD_2 = [COUNT[d] - RANKS[d] - (RANKS[d+1] if d < 6 else 0)
               for d in range(7)]
assert BETTI_MOD_2 == [1, 0, 0, 0, 2, 2, 0], BETTI_MOD_2

# Independent signed simplicial Lefschetz traces on the original 785 faces.
def sign_of_edge_permutation(mask, perm):
    moved = [perm[i] for i in range(10) if (mask >> i) & 1]
    inversions = sum(a > b for j,a in enumerate(moved) for b in moved[j+1:])
    return -1 if inversions & 1 else 1

def signed_lefschetz(k):
    return sum((-1)**(mask.bit_count()-1) * sign_of_edge_permutation(mask, GROUP[k])
               for mask in FACES if ACTION[k][mask] == mask)

LEFSCHETZ = [signed_lefschetz(k) for k in range(10)]
assert LEFSCHETZ == [-5 if k==0 else (3 if k%2 else 0) for k in range(10)], LEFSCHETZ
# The labeled complex is a wedge of six 5-spheres, hence traces on H_5
# equal 1 - signed Lefschetz and the invariant multiplicity is zero.
TOP_TRACES = [1 - z for z in LEFSCHETZ]
assert sum(TOP_TRACES) == 0
print('nonempty original faces:', len(FACES))
print('D5 quotient barycentric cell numbers:', COUNT)
print('mod-2 boundary ranks:', RANKS)
print('mod-2 Betti numbers:', BETTI_MOD_2)
print('Euler characteristic:', sum((-1)**i*c for i,c in enumerate(COUNT)))
print('signed Lefschetz traces (identity/reflections/rotations):', LEFSCHETZ)
print('top rational trace average:', sum(TOP_TRACES), '/', len(TOP_TRACES))
print('all boundary squares zero; all assertions passed')
