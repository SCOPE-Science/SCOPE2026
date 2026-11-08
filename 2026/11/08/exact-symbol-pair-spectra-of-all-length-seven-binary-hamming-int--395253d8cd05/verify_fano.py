"""Independent Fano-incidence and cyclic-interleaver classification check."""
from collections import Counter, defaultdict
from itertools import combinations, permutations

points = tuple(range(1, 8))
lines = frozenset(frozenset((x, y, x ^ y)) for x, y in combinations(points, 2))
assert len(lines) == 7
assert all(len(x & y) == 1 for x, y in combinations(lines, 2))


def canonical(c):
    k = c.index(1)
    r = c[k:] + c[:k]
    return min(r, (1,) + tuple(reversed(r[1:])))


def consecutive_lines(c):
    return frozenset(frozenset(c[(i+j) % 7] for j in range(3)) for i in range(7)) & lines

cyclics = set()
for tail in permutations(range(2, 8)):
    cyclics.add(canonical((1,) + tail))
assert len(cyclics) == 360
count = Counter(len(consecutive_lines(c)) for c in cyclics)
assert dict(count) == {0: 24, 1: 168, 2: 168}
assert sum(len(consecutive_lines(c)) for c in cyclics) == 7 * 72
assert sum(len(consecutive_lines(c))*(len(consecutive_lines(c))-1)//2 for c in cyclics) == 21 * 8

# All 168 invertible 3-by-3 F_2 matrices, encoded by images of a basis.
G = []
for x, y, z in permutations(points, 3):
    image = {v: ((x if v & 1 else 0) ^ (y if v & 2 else 0) ^ (z if v & 4 else 0)) for v in points}
    if len(set(image.values())) == 7:
        G.append(image)
assert len(G) == 168
orbits = defaultdict(list)
for a in (0, 1, 2):
    remaining = {c for c in cyclics if len(consecutive_lines(c)) == a}
    while remaining:
        seed = next(iter(remaining))
        orbit = {canonical(tuple(g[v] for v in seed)) for g in G}
        assert orbit <= remaining
        orbits[a].append(len(orbit))
        remaining -= orbit
assert {k: v for k, v in orbits.items()} == {0: [24], 1: [168], 2: [168]}
print("FANO_VERIFY_OK 360 cycles; line moments 504/168; automorphism orbits 24/168/168")
