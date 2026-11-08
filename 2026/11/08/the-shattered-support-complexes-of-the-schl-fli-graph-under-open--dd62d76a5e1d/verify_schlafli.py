#!/usr/bin/env python3
"""Independent exact verification of Schlaefli graph neighborhood shattering.
Standard-library Python 3; run: python3 verify_schlafli.py
"""
from collections import Counter
from itertools import combinations, permutations

I = range(6)
V = ([('a', i) for i in I] +
     [('c', i, j) for i, j in combinations(I, 2)] +
     [('b', i) for i in I])
assert len(V) == 27

def picard_vector(v):
    typ = v[0]
    if typ == 'a':
        return (0, *(-int(k == v[1]) for k in I))
    if typ == 'b':
        return (2, *(int(k != v[1]) for k in I))
    return (1, *(int(k in v[1:]) for k in I))

def skew_from_intersection(x, y):
    if x == y:
        return False
    p, q = picard_vector(x), picard_vector(y)
    intersection = p[0] * q[0] - sum(p[k] * q[k] for k in range(1, 7))
    assert intersection in (0, 1)
    return intersection == 0

def skew_from_labels(x, y):
    if x == y:
        return False
    tx, ty = x[0], y[0]
    if tx == ty == 'c':
        return bool(set(x[1:]) & set(y[1:]))
    if tx == ty:
        return True  # distinct a's, or distinct b's
    if tx == 'c' or ty == 'c':
        c = x if tx == 'c' else y
        u = y if tx == 'c' else x
        return u[1] not in c[1:]
    return x[1] == y[1]  # a_i -- b_i

A = [[skew_from_intersection(x, y) for y in V] for x in V]
B = [[skew_from_labels(x, y) for y in V] for x in V]
assert A == B
assert all(not A[i][i] for i in range(27))
assert all(A[i][j] == A[j][i] for i in range(27) for j in range(27))
assert {sum(row) for row in A} == {16}
assert {sum(A[i][k] and A[j][k] for k in range(27))
        for i, j in combinations(range(27), 2) if A[i][j]} == {10}
assert {sum(A[i][k] and A[j][k] for k in range(27))
        for i, j in combinations(range(27), 2) if not A[i][j]} == {8}

rows = {}
for mode in ('open', 'closed'):
    rows[mode] = [sum((1 << j) for j in range(27)
                      if A[i][j] or (mode == 'closed' and i == j))
                  for i in range(27)]


def trace_set_direct(S, mode):
    return {tuple(int(B[i][j] or (mode == 'closed' and i == j)) for j in S)
            for i in range(27)}


def trace_set_masks(S, mode):
    answer = set()
    for row in rows[mode]:
        answer.add(sum(((row >> j) & 1) << k for k, j in enumerate(S)))
    return answer

counts = {'open': Counter(), 'closed': Counter()}
induced = Counter()
for k in range(5):
    for S in combinations(range(27), k):
        clique = all(A[u][v] for u, v in combinations(S, 2))
        e = sum(A[u][v] for u, v in combinations(S, 2))
        induced[(k, e)] += 1
        for mode in ('open', 'closed'):
            tm = trace_set_masks(S, mode)
            td = trace_set_direct(S, mode)
            assert tm == {sum(bit << i for i, bit in enumerate(t)) for t in td}
            shattered = len(tm) == (1 << k)
            if k <= 2:
                expected = True
            elif k == 3:
                expected = (e >= 1) if mode == 'open' else clique
            else:
                expected = clique
            assert shattered == expected, (mode, S, e, tm, expected)
            counts[mode][k] += shattered

assert [counts['open'][i] for i in range(5)] == [1, 27, 351, 2880, 1080]
assert [counts['closed'][i] for i in range(5)] == [1, 27, 351, 720, 1080]
assert [induced[(3, e)] for e in range(4)] == [45, 1080, 1080, 720]
assert [induced[(4, e)] for e in range(7)] == [0, 0, 2160, 6480, 4590, 3240, 1080]
# Independent orbit count for the top-dimensional faces under the natural S_6.
vid = {v: i for i, v in enumerate(V)}
group = []
for p in permutations(I):
    mapping = []
    for x in V:
        if x[0] == 'c':
            i, j = sorted((p[x[1]], p[x[2]]))
            target = ('c', i, j)
        else:
            target = (x[0], p[x[1]])
        mapping.append(vid[target])
    assert all(A[i][j] == A[mapping[i]][mapping[j]]
               for i, j in combinations(range(27), 2))
    group.append(mapping)

four_cliques = {S for S in combinations(range(27), 4)
                if all(A[u][v] for u, v in combinations(S, 2))}
orbit_sizes = []
while four_cliques:
    S = min(four_cliques)
    orbit = {tuple(sorted(p[i] for i in S)) for p in group}
    assert orbit <= four_cliques
    orbit_sizes.append(len(orbit))
    four_cliques -= orbit
assert sorted(orbit_sizes) == sorted([15, 60, 180, 120, 60, 180,
                                     30, 120, 60, 180, 60, 15])

# One explicit shattered support, with witness for each of its 16 traces.
S = (0, 1, 2, 3)
for mode in ('open', 'closed'):
    witnesses = {}
    for center in range(27):
        sig = tuple(int(B[center][j] or (mode == 'closed' and center == j))
                    for j in S)
        witnesses.setdefault(sig, center)
    assert len(witnesses) == 16

# No size >= 5 support may be shattered: 27 concepts < 2**5.
assert len(V) < 2**5
print('SCHLAEFLI_SHATTER_PASS 27 vertices 351 pairs 2925 triples 17550 quadruples 12 S6 top orbits')
print('open 1+27z+351z^2+2880z^3+1080z^4')
print('closed 1+27z+351z^2+720z^3+1080z^4')
