#!/usr/bin/env python3
"""Exact integer verification of the cyclic quotient of the NC(6) order complex.

Uses Python's standard library only. All chain matrices and reductions are rebuilt
from the definition of noncrossing partitions; no precomputed matrices are needed.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import gcd

N = 6


def all_partitions(n):
    blocks = []
    def go(i):
        if i == n:
            yield tuple(tuple(b) for b in blocks)
            return
        for j in range(len(blocks)):
            blocks[j].append(i)
            yield from go(i + 1)
            blocks[j].pop()
        blocks.append([i])
        yield from go(i + 1)
        blocks.pop()
    yield from go(0)


def canonical(blocks):
    return tuple(sorted(tuple(sorted(block)) for block in blocks))


def noncrossing(partition):
    block_of = {x: j for j, block in enumerate(partition) for x in block}
    for a, b, c, d in combinations(range(N), 4):
        if block_of[a] == block_of[c] and block_of[b] == block_of[d] and block_of[a] != block_of[b]:
            return False
    return True


def finer(p, q):
    block_of = {x: j for j, block in enumerate(q) for x in block}
    return all(len({block_of[x] for x in block}) == 1 for block in p)


poset = sorted({canonical(p) for p in all_partitions(N)
                if 1 < len(p) < N and noncrossing(p)})
assert len(poset) == 130
lookup = {p: j for j, p in enumerate(poset)}
rank = [N - len(p) for p in poset]
assert Counter(rank) == {1: 15, 2: 50, 3: 50, 4: 15}
up = [[j for j, q in enumerate(poset) if rank[j] > rank[i] and finer(p, q)]
      for i, p in enumerate(poset)]
faces = [[(i,) for i in range(len(poset))]]
for dimension in range(1, 4):
    faces.append([f + (j,) for f in faces[-1] for j in up[f[-1]]])
assert list(map(len, faces)) == [130, 1035, 2160, 1296]
rotation = [lookup[canonical([[(x + 1) % N for x in block] for block in p])]
            for p in poset]
assert all(rotation[rotation[rotation[rotation[rotation[rotation[i]]]]]] == i
           for i in range(len(poset)))

# An order-preserving rank-preserving action fixes every vertex of any stabilized
# simplex, so orbit faces form a cellular quotient without orientation inversions.
orbit_reps, orbit_index = [], []
for dimension_faces in faces:
    representatives, index = [], {}
    for face in dimension_faces:
        if face in index:
            continue
        j = len(representatives)
        representatives.append(face)
        t = face
        while t not in index:
            index[t] = j
            t = tuple(rotation[v] for v in t)
    assert len(index) == len(dimension_faces)
    orbit_reps.append(representatives)
    orbit_index.append(index)
assert list(map(len, orbit_reps)) == [26, 177, 360, 216]

# Exact signed cellular differentials. The chain orientation is rank order.
differentials = []
for d in range(1, 4):
    entries = {}
    for j, face in enumerate(orbit_reps[d]):
        for k in range(len(face)):
            i = orbit_index[d - 1][face[:k] + face[k + 1:]]
            entries[i, j] = entries.get((i, j), 0) + (-1) ** k
    differentials.append({key: value for key, value in entries.items() if value})
assert [len(matrix) for matrix in differentials] == [354, 1080, 864]


def composition_zero(lower, upper):
    by_middle = defaultdict(list)
    for (i, j), v in lower.items():
        by_middle[j].append((i, v))
    composite = Counter()
    for (j, k), v in upper.items():
        for i, w in by_middle[j]:
            composite[i, k] += w * v
    return not any(composite.values())

assert composition_zero(differentials[0], differentials[1])
assert composition_zero(differentials[1], differentials[2])
active = [set(range(len(x))) for x in orbit_reps]
counts = []
for d in (1, 2, 3):
    cancellations = 0
    while True:
        matrix = differentials[d - 1]
        row_degree = Counter(i for i, _ in matrix)
        col_degree = Counter(j for _, j in matrix)
        units = [((row_degree[i] - 1) * (col_degree[j] - 1), i, j, v)
                 for (i, j), v in matrix.items() if abs(v) == 1]
        if not units:
            break
        _, r, c, v = min(units)
        row = {j: x for (i, j), x in matrix.items() if i == r and j != c}
        col = {i: x for (i, j), x in matrix.items() if j == c and i != r}
        for i, x in col.items():
            for j, y in row.items():
                new_value = matrix.get((i, j), 0) - x * y * v
                if new_value:
                    matrix[i, j] = new_value
                else:
                    matrix.pop((i, j), None)
        for key in list(matrix):
            if key[0] == r or key[1] == c:
                del matrix[key]
        active[d - 1].remove(r)
        active[d].remove(c)
        if d >= 2:
            for key in list(differentials[d - 2]):
                if key[1] == r:
                    del differentials[d - 2][key]
        if d <= 2:
            for key in list(differentials[d]):
                if key[0] == c:
                    del differentials[d][key]
        cancellations += 1
    counts.append(cancellations)
    if d >= 2:
        assert composition_zero(differentials[d - 2], differentials[d - 1])
    if d <= 2:
        assert composition_zero(differentials[d - 1], differentials[d])

assert counts == [25, 152, 207]
assert list(map(len, active)) == [1, 0, 1, 9]
assert [len(matrix) for matrix in differentials] == [0, 0, 1]
assert sorted(differentials[2].values()) == [3]
assert sum((-1) ** i * len(x) for i, x in enumerate(orbit_reps)) == -7

# For Armstrong's theorem: two point-stabilizer elements generate the rotation group.
def rotate_vertex(i, k):
    for _ in range(k):
        i = rotation[i]
    return i

fixed2 = [i for i in range(len(poset)) if rotate_vertex(i, 2) == i]
fixed3 = [i for i in range(len(poset)) if rotate_vertex(i, 3) == i]
assert len(fixed2) == 4 and len(fixed3) == 18
assert gcd(2, 3) == 1
print('NC6_CYCLIC_QUOTIENT_EXACT_PASS')
print('poset=130 original_faces=130,1035,2160,1296 orbit_cells=26,177,360,216')
print('boundary_compositions=zero unit_pivot_cancellations=25,152,207')
print('residual_chain_dims=1,0,1,9 residual_boundary=3')
print('rotation_squared_fixed_vertices=4 rotation_cubed_fixed_vertices=18')
print('homology_H2=Z/3 homology_H3=Z^8 pi1=trivial')
