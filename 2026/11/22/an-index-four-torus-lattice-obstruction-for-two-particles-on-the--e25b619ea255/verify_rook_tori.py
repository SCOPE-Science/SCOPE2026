#!/usr/bin/env python3
"""Exact integer chain verifier for two points on the 3-by-3 rook graph.

Requires Python 3 and SymPy. The only inputs are the graph definition below.
All matrices, cycle pairs, and minors are regenerated deterministically.
"""
from itertools import combinations
from collections import Counter
from sympy import zeros, Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

V = tuple(range(9))
E = tuple((u, v) for u in V for v in V if u < v
          and (u // 3 == v // 3 or u % 3 == v % 3))
C0 = tuple(combinations(V, 2))
C1 = tuple((e, v) for e in E for v in V if v not in e)
C2 = tuple((e, f) for e, f in combinations(E, 2) if set(e).isdisjoint(f))
assert (len(E), len(C0), len(C1), len(C2)) == (18, 36, 126, 99)
idx1 = {cell: k for k, cell in enumerate(C1)}
idx2 = {cell: k for k, cell in enumerate(C2)}

# The product orientation of (e,f) uses the lexically ordered oriented edges.
B2 = zeros(len(C1), len(C2))
for j, (e, f) in enumerate(C2):
    B2[idx1[(f, e[1])], j] += 1
    B2[idx1[(f, e[0])], j] -= 1
    B2[idx1[(e, f[1])], j] -= 1
    B2[idx1[(e, f[0])], j] += 1
B1 = zeros(len(C0), len(C1))
idx0 = {cell: k for k, cell in enumerate(C0)}
for j, ((u, v), w) in enumerate(C1):
    B1[idx0[tuple(sorted((v, w)))], j] += 1
    B1[idx0[tuple(sorted((u, w)))], j] -= 1
assert B1 * B2 == zeros(len(C0), len(C2))
B2smith = smith_normal_form(B2, domain=ZZ)
invB2 = [abs(int(B2smith[k,k])) for k in range(min(B2smith.shape)) if B2smith[k,k] != 0]
assert len(invB2) == 81 and Counter(invB2) == Counter({1:80, 2:1})

adj = {v: [] for v in V}
for u, v in E:
    adj[u].append(v)
    adj[v].append(u)
cycles = set()
def walk(path):
    start = path[0]
    for nxt in adj[path[-1]]:
        if nxt == start and len(path) >= 3:
            seq = tuple(path)
            if start == min(seq):
                rev = (seq[0],) + tuple(reversed(seq[1:]))
                cycles.add(min(seq, rev))
        elif nxt > start and nxt not in path:
            walk(path + [nxt])
for start in V:
    walk([start])
cycles = sorted(cycles, key=lambda c: (len(c), c))
assert Counter(map(len, cycles)) == {3:6,4:9,5:36,6:60,7:72,8:81,9:48}

pairs = []
vectors = []
for a, b in combinations(cycles, 2):
    if not set(a).isdisjoint(b):
        continue
    chain = zeros(len(C2), 1)
    for i in range(len(a)):
        x, y = a[i], a[(i+1) % len(a)]
        e = tuple(sorted((x, y)))
        sign_e = 1 if x < y else -1
        for j in range(len(b)):
            s, t = b[j], b[(j+1) % len(b)]
            f = tuple(sorted((s, t)))
            sign_f = 1 if s < t else -1
            cell = (e, f) if e < f else (f, e)
            chain[idx2[cell]] += sign_e * sign_f * (1 if e < f else -1)
    assert B2 * chain == zeros(len(C1), 1)
    pairs.append((a,b))
    vectors.append(chain)
assert len(pairs) == 78

def type_indices(a, b):
    return [i for i, pair in enumerate(pairs)
            if sorted((len(pair[0]), len(pair[1]))) == [a,b]]
ids33 = type_indices(3,3)
ids34 = type_indices(3,4)
assert (len(ids33), len(ids34)) == (6,18)
T34 = Matrix.hstack(*(vectors[i] for i in ids34))
T24 = Matrix.hstack(*(vectors[i] for i in ids34 + ids33))

# An integral maximal minor of the 18 triangle-square torus columns.
rows34 = (0, 2, 3, 5, 8, 11, 13, 19, 22, 23, 25, 27, 44, 50, 53, 55, 69, 82)
assert T34[list(rows34),:].det() == -4
D34 = smith_normal_form(T34,domain=ZZ)
diag34 = [abs(int(D34[i,i])) for i in range(18)]
assert Counter(diag34) == Counter({1:16, 2:2})

# A primitive 18-torus subfamily selected from 18 square-plus-triangle
# and 6 triangle-plus-triangle classes. The indices refer to T24 columns.
columns24 = (15, 5, 18, 23, 13, 10, 17, 11, 14, 16, 1, 21, 6, 9, 2, 4, 7, 8)
rows24 = (21, 28, 96, 49, 90, 25, 1, 81, 39, 9, 16, 78, 86, 26, 52, 6, 32, 62)
assert T24[list(rows24), list(columns24)].det() == 1
D24 = smith_normal_form(T24,domain=ZZ)
assert [abs(int(D24[i,i])) for i in range(18)] == [1]*18

# Since ker(B2) is a primitive rank-18 sublattice of Z^99,
# the 24 tori generate it integrally. The 18 mixed-length tori
# generate a subgroup of quotient (Z/2)^2, with no free quotient.
print('ROOK_P9_TWO_PARTICLE_INTEGRAL_TORUS_LATTICE_OK')
print('graph vertices=9 edges=18, cells=(36,126,99), rank(B2)=81')
print('H2 rank=18, triangle-square torus quotient=(Z/2)^2')
print('triangle-triangle plus triangle-square tori span H2 integrally')

# The two independent obstructions are removed by one disjoint-row-triangle
# pair and one disjoint-column-triangle pair.
row_pair = next(i for i in ids33 if all(v // 3 == pairs[i][0][0] // 3 for v in pairs[i][0]))
col_pair = next(i for i in ids33 if all(v % 3 == pairs[i][0][0] % 3 for v in pairs[i][0]))
T20 = Matrix.hstack(T34, vectors[row_pair], vectors[col_pair])
D20 = smith_normal_form(T20, domain=ZZ)
assert [abs(int(D20[k,k])) for k in range(18)] == [1]*18
print('two extra triangle-triangle tori (row-row and column-column) suffice')
