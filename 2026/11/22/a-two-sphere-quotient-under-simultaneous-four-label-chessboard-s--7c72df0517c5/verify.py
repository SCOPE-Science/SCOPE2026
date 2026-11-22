#!/usr/bin/env python3
"""Exact cellular chain computation of a diagonal S4 chessboard quotient.

Uses only the Python standard library; no floating point or external data.
Barycentric chains ensure the simplicial action has no inversions.
"""
from itertools import combinations, permutations

N = 4
FACES = []
for k in range(1, N + 1):
    for rows in combinations(range(N), k):
        for cols in permutations(range(N), k):
            FACES.append(frozenset(N * i + j for i, j in zip(rows, cols)))
face_id = {f: i for i, f in enumerate(FACES)}
assert len(FACES) == len(face_id) == 208

def ordered_partitions(items):
    def rec(i, blocks):
        if i == len(items):
            yield [tuple(block) for block in blocks]
            return
        v = items[i]
        for j in range(len(blocks)):
            nxt = [list(b) for b in blocks]
            nxt[j].append(v)
            yield from rec(i + 1, nxt)
        for j in range(len(blocks) + 1):
            nxt = [list(b) for b in blocks]
            nxt.insert(j, [v])
            yield from rec(i + 1, nxt)
    yield from rec(0, [])

chains = [[] for _ in range(N)]
seen = set()
for f in FACES:
    for partition in ordered_partitions(sorted(f)):
        acc = set()
        chain = []
        for block in partition:
            acc.update(block)
            chain.append(face_id[frozenset(acc)])
        chain = tuple(chain)
        assert chain not in seen
        seen.add(chain)
        chains[len(chain) - 1].append(chain)
assert [len(x) for x in chains] == [208, 1056, 1440, 576]

PERMS = list(permutations(range(N)))
def action(chain, perm):
    return tuple(face_id[frozenset(N * perm[v // N] + perm[v % N]
                                       for v in FACES[index])] for index in chain)

representatives = []
index_maps = []
for basis in chains:
    seen_orbits = {}
    reps = []
    for chain in basis:
        if chain in seen_orbits:
            continue
        orbit = {action(chain, perm) for perm in PERMS}
        label = len(reps)
        assert all(c not in seen_orbits for c in orbit)
        for c in orbit:
            seen_orbits[c] = label
        reps.append(chain)
    assert len(seen_orbits) == len(basis)
    representatives.append(reps)
    index_maps.append(seen_orbits)
assert [len(x) for x in representatives] == [19, 59, 66, 24]

B = [None]
for k in range(1, N):
    a = [[0] * len(representatives[k]) for _ in representatives[k - 1]]
    for j, chain in enumerate(representatives[k]):
        for t in range(k + 1):
            face_chain = chain[:t] + chain[t + 1:]
            a[index_maps[k - 1][face_chain]][j] += -1 if t & 1 else 1
    B.append(a)

def compose_zero(low, high):
    # low: m x n, high: n x p
    if not low or not high:
        return True
    assert len(low[0]) == len(high)
    for i, row in enumerate(low):
        for j in range(len(high[0])):
            if sum(v * high[k][j] for k, v in enumerate(row)):
                return False
    return True

assert all(compose_zero(B[k - 1], B[k]) for k in range(2, N))
assert [len(FACES[0])] and [sum(len(f) == k for f in FACES) for k in range(1, 5)] == [16, 72, 96, 24]
assert sum((-1) ** i * len(representatives[i]) for i in range(N)) == 2
ranks = [len(x) for x in representatives]
cancels = [0] * N
for degree in range(N - 1, 0, -1):
    while True:
        matrix = B[degree]
        pivot = next(((i, j, value) for i, row in enumerate(matrix)
                      for j, value in enumerate(row) if abs(value) == 1), None)
        if pivot is None:
            break
        i, j, unit = pivot
        cols = len(matrix[0])
        B[degree] = [[matrix[r][c] - matrix[r][j] * matrix[i][c] * unit
                      for c in range(cols) if c != j]
                     for r in range(len(matrix)) if r != i]
        if degree + 1 < N:
            B[degree + 1] = [row for r, row in enumerate(B[degree + 1]) if r != j]
        if degree - 1 >= 1:
            B[degree - 1] = [[v for c, v in enumerate(row) if c != i]
                             for row in B[degree - 1]]
        ranks[degree] -= 1
        ranks[degree - 1] -= 1
        cancels[degree] += 1
        assert all(compose_zero(B[k - 1], B[k]) for k in range(2, N))

assert cancels == [0, 18, 41, 24], cancels
assert ranks == [1, 0, 1, 0], ranks
assert all(not any(any(x != 0 for x in row) for row in B[k]) for k in range(1, N))
print('FACE_COUNTS=16,72,96,24')
print('BARYCENTRIC_COUNTS=208,1056,1440,576')
print('QUOTIENT_COUNTS=19,59,66,24')
print('UNIT_CANCELLATIONS=18,41,24')
print('REMAINING_CHAIN_RANKS=1,0,1,0')
print('VERIFY_OK')
