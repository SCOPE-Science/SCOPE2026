#!/usr/bin/env python3
"""Exhaustive finite proof for reconfiguring geodesic transversals of the 4-cube."""
from collections import Counter, deque
from itertools import permutations

N = 16
U = (1 << N) - 1
# Each maximal geodesic flips all four coordinates, once each.
paths = set()
for start in range(N):
    for order in permutations(range(4)):
        vertices = [start]
        x = start
        for bit in order:
            x ^= 1 << bit
            vertices.append(x)
        assert x == start ^ 15
        paths.add(sum(1 << v for v in vertices))
assert len(paths) == 192

ok = bytearray(1 << N)
by_size = Counter()
for mask in range(1 << N):
    good = all(mask & p for p in paths)
    if good:
        ok[mask] = 1
        by_size[mask.bit_count()] += 1
assert dict(sorted(by_size.items())) == {
    6: 40, 7: 560, 8: 2910, 9: 5920, 10: 6376,
    11: 4176, 12: 1820, 13: 560, 14: 120, 15: 16, 16: 1,
}
minimal = Counter()
mins = []
for s in range(1 << N):
    if not ok[s]:
        continue
    if s.bit_count() == 6:
        mins.append(s)
    if not any(ok[s ^ (1 << b)] for b in range(N) if s >> b & 1):
        minimal[s.bit_count()] += 1
assert minimal == Counter({6: 40, 7: 160, 8: 260})

# Compare the known two structural families of minimizers.
A = set()
for a in range(N):
    A.add(sum(1 << x for x in range(N) if (x ^ a).bit_count() == 2))
B = set()
for free in range(4):
    coords = [j for j in range(4) if j != free]
    for b in range(8):
        B.add(sum(1 << x for x in range(N) if
                  sum(((x >> j) & 1) != ((b >> i) & 1)
                      for i, j in enumerate(coords)) == 1))
assert len(A) == 8 and len(B) == 32 and A.isdisjoint(B)
assert set(mins) == A | B

# The addition/removal graph on the set of feasible masks of size at most budget.
def components(budget):
    members = {s for s in range(1 << N) if ok[s] and s.bit_count() <= budget}
    unseen = members.copy()
    sizes = []
    component_of = {}
    while unseen:
        root = min(unseen)
        unseen.remove(root)
        q = deque([root])
        size = 0
        idx = len(sizes)
        while q:
            s = q.popleft()
            component_of[s] = idx
            size += 1
            for v in range(N):
                t = s ^ (1 << v)
                if t in unseen:
                    unseen.remove(t)
                    q.append(t)
        sizes.append(size)
    return members, Counter(sizes), component_of

expected = {
    6: {1: 40},
    7: {1: 160, 11: 40},
    8: {1: 260, 3250: 1},
    9: {9430: 1},
}
for b, want in expected.items():
    members, sizes, assignment = components(b)
    assert dict(sizes) == want, (b, sizes)
    assert len(members) == sum(k * n for k, n in want.items())
    if b == 7:
        assert len({assignment[x] for x in mins}) == 40
    if b in (8, 9):
        assert len({assignment[x] for x in mins}) == 1

# Intrinsic shortest TAR paths between minima, at budget eight.
members, _, _ = components(8)
pairs = Counter()
type_pairs = Counter()
for i, s in enumerate(mins):
    distances = {s: 0}
    q = deque([s])
    while q:
        x = q.popleft()
        for bit in range(N):
            y = x ^ (1 << bit)
            if y in members and y not in distances:
                distances[y] = distances[x] + 1
                q.append(y)
    assert len(distances) == 3250
    for t in mins[i+1:]:
        dist = distances[t]
        pairs[dist] += 1
        typ = ('A' if s in A else 'B') + ('A' if t in A else 'B')
        type_pairs[(''.join(sorted(typ)), dist)] += 1
assert pairs == Counter({4: 60, 6: 160, 8: 480, 12: 80}), pairs
assert type_pairs == Counter({
    ('AA',4):12, ('AA',12):16,
    ('AB',6):64, ('AB',8):192,
    ('BB',4):48, ('BB',6):96, ('BB',8):288, ('BB',12):64,
}), type_pairs

print('PATHS_OK 192')
print('TRANSVERSAL_SPECTRUM_OK total=22499 minimum=40')
print('MINIMAL_SPECTRUM_OK 40z6+160z7+260z8')
print('COMPONENTS_OK budgets=6,7,8,9')
print('OPTIMAL_DISTANCE_PROFILE_OK 4:60 6:160 8:480 12:80')
print('VERIFY_PRIMARY_OK')
