#!/usr/bin/env python3
"""Exact integral orbit-cell and fundamental-group check for a Heawood complex.

Requires Python 3.10+ and SymPy for integer Smith normal forms.
All cells, maps and relators are reconstructed, not read from a saved table.
"""
from collections import Counter
from itertools import permutations
from sympy import zeros
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

POINTS = tuple(range(1, 8))
LINES = tuple(sorted({tuple(sorted((a, b, a ^ b)))
                      for a in POINTS for b in POINTS if a != b}))
assert len(LINES) == 7
point_id = {p: i for i, p in enumerate(POINTS)}
line_id = {frozenset(line): i for i, line in enumerate(LINES)}

# Vertex labels 0..6 are points and 7..13 are lines.
adjacency = [0] * 14
edges = set()
for i, p in enumerate(POINTS):
    for j, line in enumerate(LINES):
        if p in line:
            a, b = i, 7 + j
            adjacency[a] |= 1 << b
            adjacency[b] |= 1 << a
            edges.add((a, b))
assert len(edges) == 21

independent = []
for mask in range(1, 1 << 14):
    if all(not ((mask >> v & 1) and (mask & adjacency[v]))
           for v in range(14)):
        independent.append(mask)
assert Counter(m.bit_count() for m in independent) == {
    1: 14, 2: 70, 3: 154, 4: 147, 5: 56, 6: 14, 7: 2
}

# All invertible F_2-linear maps, specified by images of (1,2,4).
collineations = []
for u, v, w in permutations(POINTS, 3):
    if (u ^ v ^ w) == 0:
        continue
    def linear(x):
        return (u if x & 1 else 0) ^ (v if x & 2 else 0) ^ (w if x & 4 else 0)
    collineations.append(tuple(
        [point_id[linear(p)] for p in POINTS] +
        [7 + line_id[frozenset(linear(p) for p in line)] for line in LINES]
    ))
assert len(set(collineations)) == 168

# Point-line polarity for the symmetric dot product on F_2^3.
polarity = []
for p in POINTS:
    polar_line = frozenset(q for q in POINTS if (p & q).bit_count() % 2 == 0)
    assert len(polar_line) == 3
    polarity.append(7 + line_id[polar_line])
for line in LINES:
    normal = next(p for p in POINTS if all(
        (p & q).bit_count() % 2 == 0 for q in line))
    polarity.append(point_id[normal])
assert all(polarity[polarity[i]] == i for i in range(14))

automorphisms = collineations + [
    tuple(polarity[g[i]] for i in range(14)) for g in collineations
]
assert len(set(automorphisms)) == 336
for g in automorphisms:
    image_edges = {tuple(sorted((g[a], g[b]))) for a, b in edges}
    assert image_edges == {tuple(sorted(e)) for e in edges}

# Each simplex of the barycentric subdivision is a strictly increasing chain
# of nonempty independent subsets. Sizes strictly increase, hence the action
# on each simplex has no vertex permutations and no orientation reversals.
subsets = {mask: [sub for sub in independent if sub != mask and (sub & mask) == sub]
           for mask in independent}
chain_levels = []
level = [(mask,) for mask in independent]
while level:
    chain_levels.append(level)
    level = [(sub,) + chain for chain in level for sub in subsets[chain[0]]]
assert [len(x) for x in chain_levels] == [457, 5922, 25788, 55608, 65520, 40320, 10080]

mask_maps = [
    {mask: sum(1 << g[i] for i in range(14) if mask >> i & 1)
     for mask in independent}
    for g in automorphisms
]
orbit_index, representatives = [], []
for level in chain_levels:
    index, reps = {}, []
    for chain in level:
        if chain in index:
            continue
        orbit = {tuple(g[m] for m in chain) for g in mask_maps}
        j = len(reps)
        reps.append(min(orbit))
        for c in orbit:
            assert c not in index
            index[c] = j
    assert len(index) == len(level)
    orbit_index.append(index)
    representatives.append(reps)
cell_counts = [len(reps) for reps in representatives]
assert cell_counts == [14, 64, 149, 218, 210, 120, 30]

# Boundary matrices for ordinary geometric quotient, with characteristic-zero
# cellular coefficients. All orientations are inherited from increasing ranks.
boundaries = []
for k in range(1, len(representatives)):
    B = zeros(cell_counts[k-1], cell_counts[k])
    for j, chain in enumerate(representatives[k]):
        for i in range(k + 1):
            face = chain[:i] + chain[i+1:]
            B[orbit_index[k-1][face], j] += (-1)**i
    boundaries.append(B)
for lower, upper in zip(boundaries, boundaries[1:]):
    assert lower * upper == zeros(lower.rows, upper.cols)

ranks = []
for B in boundaries:
    smith = smith_normal_form(B, domain=ZZ)
    diag = [abs(int(smith[i,i])) for i in range(min(smith.rows, smith.cols))
            if smith[i,i] != 0]
    assert all(x == 1 for x in diag), 'nonunit integral Smith invariant'
    ranks.append(len(diag))
assert ranks == [13, 51, 98, 120, 90, 30]
assert [cell_counts[0]-ranks[0]] + [
    cell_counts[k] - ranks[k-1] - (ranks[k] if k < 6 else 0)
    for k in range(1, 7)
] == [1, 0, 0, 0, 0, 0, 0]

# Fundamental group via a spanning tree and triangular attaching words.
# A triangular orbit cell (a<b<c) contributes e(a,b)e(b,c)e(a,c)^(-1).
parents = list(range(cell_counts[0]))
def root(i):
    while parents[i] != i:
        i = parents[i]
    return i

generator = {}
for j, (a,b) in enumerate(representatives[1]):
    u, v = orbit_index[0][(a,)], orbit_index[0][(b,)]
    ru, rv = root(u), root(v)
    if ru != rv:
        parents[ru] = rv
    else:
        generator[j] = len(generator)+1
assert len({root(i) for i in range(cell_counts[0])}) == 1
assert len(generator) == 51
relators = []
for a,b,c in representatives[2]:
    word = []
    for face, sign in [((a,b),1), ((b,c),1), ((a,c),-1)]:
        e = orbit_index[1][face]
        if e in generator:
            word.append(sign * generator[e])
    relators.append(word)
assert len(relators) == 149

def freely_reduce(w):
    stack=[]
    for x in w:
        if stack and stack[-1] == -x:
            stack.pop()
        else:
            stack.append(x)
    return stack

# Length-one relators kill generators by genuine Tietze elimination, with
# substitution by the identity. This is enough: no stronger group solver.
removed = set()
while True:
    one = None
    for word in relators:
        reduced = freely_reduce(word)
        if len(reduced) == 1 and abs(reduced[0]) not in removed:
            one = abs(reduced[0])
            break
    if one is None:
        break
    removed.add(one)
    relators = [freely_reduce([x for x in word if abs(x) != one])
                for word in relators]
assert len(removed) == 51
assert all(not w for w in relators)
print('HEAWOOD_FULL_AUTOMORPHISM_ORBIT_CONTRACTIBLE_OK')
print('independent_sets=457 automorphisms=336 quotient_cells=',cell_counts)
print('integral_boundary_ranks=',ranks,'all_nonzero_Smith_entries=1')
print('pi1_spanning_tree=13  generators_killed=51  triangular_relators=149')
