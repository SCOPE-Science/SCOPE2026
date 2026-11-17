#!/usr/bin/env python3
"""Exact self-contained checker for a finite Paley-tournament block complex.

Requires Python 3.10 or later; no external modules. Integer masks label simplices.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations

P = 19
Q = frozenset((i * i) % P for i in range(1, P))
assert len(Q) == 9 and 0 not in Q and all(((-i) % P) not in Q for i in Q)
BLOCKS = tuple(sum(1 << ((a + q) % P) for q in Q) for a in range(P))
assert len(set(BLOCKS)) == 19
assert all(b.bit_count() == 9 for b in BLOCKS)
assert all((b & c).bit_count() == 4 for b, c in combinations(BLOCKS, 2))

# Enumerator A: descend all 19 blocks through their full subset lattices.
FACES = {0}
for block in BLOCKS:
    sub = block
    while sub:
        FACES.add(sub)
        sub = (sub - 1) & block
FACES.discard(0)
# Enumerator B: check every nonempty vertex subset by the defining quantifier.
DIRECT = {s for s in range(1, 1 << P)
          if any(s & ~block == 0 for block in BLOCKS)}
assert FACES == DIRECT
VECTOR = tuple(sum(1 for s in FACES if s.bit_count() == d + 1)
               for d in range(9))
assert VECTOR == (19, 171, 969, 2223, 2394, 1596, 684, 171, 19)
assert sum((-1)**d * n for d, n in enumerate(VECTOR)) == -76

def boundary(simplex):
    """Signed oriented boundary, vertices in ascending order."""
    pos, remain = 0, simplex
    while remain:
        bit = remain & -remain
        yield simplex ^ bit, (-1 if pos & 1 else 1)
        remain ^= bit
        pos += 1

# Standard sequential vertex matchings on the remaining face poset.
# Each stage pairs lower s with upper s union {v}, both still unmatched.
remaining = set(FACES)
matched = {}
for v in range(P):
    bit = 1 << v
    for s in sorted(remaining):
        t = s | bit
        if not (s & bit) and s in remaining and t in remaining:
            matched[s] = t
            remaining.remove(s)
            remaining.remove(t)
assert len(matched) == 4080
critical = {d: tuple(sorted(s for s in remaining if s.bit_count() == d+1))
            for d in range(9)}
assert {d: len(ss) for d, ss in critical.items() if ss} == {0: 1, 2: 4, 3: 81}

# Complete Hasse graph: point down from upper to lower except matched edges,
# which point upward. A topological sort is a finite acyclicity certificate.
adj = defaultdict(list)
indegree = Counter()
cover_count = 0
for upper in FACES:
    for lower, sign in boundary(upper):
        if not lower:
            continue
        cover_count += 1
        tail, head = ((lower, upper) if matched.get(lower) == upper
                      else (upper, lower))
        adj[tail].append(head)
        indegree[head] += 1
assert cover_count == 40014
queue = [s for s in FACES if indegree[s] == 0]
visited = 0
while queue:
    s = queue.pop()
    visited += 1
    for t in adj[s]:
        indegree[t] -= 1
        if indegree[t] == 0:
            queue.append(t)
assert visited == len(FACES)

# Integral reduction of dimension-two chains along gradient pairs. A face
# matched above is eliminated using the signed boundary of its matched coface;
# a face matched below contributes zero, and critical faces are retained.
reverse = {upper: lower for lower, upper in matched.items()}
c2 = critical[2]
c3 = critical[3]
@lru_cache(maxsize=None)
def project_two(face):
    if face in c2:
        return {face: 1}
    if face in reverse:
        return {}
    assert face in matched and face.bit_count() == 3
    upper = matched[face]
    co = dict(boundary(upper))
    pivot = co[face]
    accum = defaultdict(int)
    for other, sign in co.items():
        if other == face:
            continue
        for critical_face, coeff in project_two(other).items():
            accum[critical_face] -= pivot * sign * coeff
    return {k: v for k, v in accum.items() if v}

morse = [[0 for _ in c3] for _ in c2]
for j, upper in enumerate(c3):
    column = defaultdict(int)
    for face, sign in boundary(upper):
        for critical_face, coeff in project_two(face).items():
            column[critical_face] += sign * coeff
    for i, critface in enumerate(c2):
        morse[i][j] = column[critface]

# Entire 4 x 81 signed integer matrix has the primitive left null relation
# (1,-2,-1,1), and a 3 x 3 unimodular minor. These two elementary integer
# witnesses prove rank 3 and a torsion-free rank-one cokernel.
relation = (1, -2, -1, 1)
assert len(c2) == 4 and len(c3) == 81
assert all(sum(relation[i] * morse[i][j] for i in range(4)) == 0
           for j in range(81))
def det3(rows):
    a, b, c = rows
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))
unit_minor = det3([[morse[i][j] for j in (0, 1, 4)] for i in (0, 1, 2)])
assert unit_minor == -1

# Independent simplicial homology check over F_2: reduce full boundary matrices.
bydim = {d: sorted(s for s in FACES if s.bit_count() == d+1) for d in range(9)}
def gf2_rank(columns):
    pivots = {}
    for column in columns:
        while column:
            k = column.bit_length() - 1
            if k not in pivots:
                pivots[k] = column
                break
            column ^= pivots[k]
    return len(pivots)
ranks = {}
for d in range(1, 9):
    index = {s: i for i, s in enumerate(bydim[d-1])}
    columns = []
    for upper in bydim[d]:
        column = 0
        for face, sign in boundary(upper):
            column ^= 1 << index[face]
        columns.append(column)
    ranks[d] = gf2_rank(columns)
assert tuple(ranks[d] for d in range(1, 9)) == (18,153,815,1330,1064,532,152,19)
assert tuple(VECTOR[d] - ranks.get(d, 0) - ranks.get(d+1, 0) for d in range(9)) == (1,0,1,78,0,0,0,0,0)

print('quadratic_residues', sorted(Q))
print('block_design', '2-(19,9,4)', len(BLOCKS))
print('simplices', len(FACES), 'f_vector', VECTOR, 'euler', -76)
print('matching_pairs', len(matched), 'critical_cells',
      {d: len(v) for d, v in critical.items() if v})
print('Hasse_cover_relations', cover_count, 'acyclic_toposort', visited)
print('morse_boundary_size', (len(c2),len(c3)),
      'left_null',relation, 'unit_minor',unit_minor)
print('mod2_boundary_ranks', tuple(ranks[d] for d in range(1,9)))
print('reduced_integral_homotopy', 'S^2 wedge 78 copies of S^3')
print('ALL_CHECKS_PASS')
