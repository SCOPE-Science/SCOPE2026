#!/usr/bin/env python3
"""Complete independent set-based verification of 3-neighbour percolation on Q4.
Python 3.9+. No nonstandard dependencies."""
from itertools import permutations
from collections import Counter

N = {v: frozenset(v ^ (1 << i) for i in range(4)) for v in range(16)}
V = frozenset(range(16))


def infected_after(mask):
    active = frozenset(v for v in V if mask & (1 << v))
    rounds = 0
    while True:
        additions = frozenset(v for v in V.difference(active)
                             if len(N[v].intersection(active)) >= 3)
        if not additions:
            return active == V, rounds
        active = active.union(additions)
        rounds += 1


# Exhaust all initial configurations independently of inclusion-minimality.
results = [infected_after(m) for m in range(1 << 16)]
minimal = {}
for m in range(1 << 16):
    successful, rounds = results[m]
    if successful and all(not results[m & ~(1 << v)][0]
                          for v in V if m & (1 << v)):
        minimal[m] = rounds

h = Counter((m.bit_count(), t) for m, t in minimal.items())
assert h == {(6, 2): 8, (7, 3): 160, (7, 4): 768}, h
assert len(minimal) == 936
# Check all 65,536 cases against their independently reconstructed orbits.
EXPECTED = [
    (5736, 6, 2, 8),
    (5782, 7, 3, 64),
    (5801, 7, 3, 96),
    (5785, 7, 4, 192),
    (5804, 7, 4, 192),
    (5786, 7, 4, 384),
]

def transform(m, perm, shift):
    result = 0
    for x in V:
        if m & (1 << x):
            y = 0
            for coordinate in range(4):
                if (x >> coordinate) & 1:
                    y |= 1 << perm[coordinate]
            result |= 1 << (y ^ shift)
    return result

orbits = []
for rep, weight, delay, expected_size in EXPECTED:
    orbit = {transform(rep, perm, shift)
             for perm in permutations(range(4)) for shift in range(16)}
    assert len(orbit) == expected_size
    assert all(x in minimal and x.bit_count() == weight
               and minimal[x] == delay for x in orbit)
    orbits.append(orbit)
assert all(orbits[i].isdisjoint(orbits[j])
           for i in range(6) for j in range(i+1, 6))
assert set.union(*orbits) == set(minimal)

parity_complements = set()
for p in (0, 1):
    side = {v for v in V if v.bit_count() % 2 == p}
    for v in side:
        pair = {v, v ^ 15}
        parity_complements.add(sum(1 << x for x in side.difference(pair)))
assert len(parity_complements) == 8
assert parity_complements == {m for m in minimal if m.bit_count() == 6}

# Exhaustive records also certify that no inclusion-minimal set has >7 vertices.
print('PASS: all 65,536 subsets; 936 inclusion-minimal sets; six affine orbits')
print('orbit table:', EXPECTED)
print('minimal delayed histogram:', sorted(h.items()))

