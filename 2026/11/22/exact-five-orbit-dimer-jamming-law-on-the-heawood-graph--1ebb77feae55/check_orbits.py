#!/usr/bin/env python3
"""Standalone five-orbit census and exact terminal-microstate probabilities."""
from itertools import permutations
from collections import Counter
from functools import lru_cache
from fractions import Fraction

L = [frozenset((j + d) % 7 for d in (0, 1, 3)) for j in range(7)]
E = sorted((i, j + 7) for j, line in enumerate(L) for i in line)
edge_index = {e: k for k, e in enumerate(E)}
line_index = {line: j for j, line in enumerate(L)}

# Enumerate every vertex-collineation by all 7! point permutations.
automorphisms = []
for p in permutations(range(7)):
    mapped = [line_index.get(frozenset(p[i] for i in line)) for line in L]
    if any(j is None for j in mapped):
        continue
    automorphisms.append(tuple(p) + tuple(7 + j for j in mapped))
assert len(automorphisms) == 168

# An incidence-preserving duality doubles the collineations to 336.
duality = tuple(7 + (-i) % 7 for i in range(7)) + tuple((-j) % 7 for j in range(7))
automorphisms += [tuple(duality[p[i]] for i in range(14)) for p in automorphisms]
assert len(set(automorphisms)) == 336
edge_actions = []
for a in automorphisms:
    image = tuple(edge_index[tuple(sorted((a[u], a[v])))] for u, v in E)
    assert len(set(image)) == 21
    edge_actions.append(image)

# Enumerate every matching by independent include/exclude decisions, keeping
# only inclusion-maximal matchings (no disjoint edge can be added).
terminal = set()
def visit(i, used, M):
    if i == 21:
        if all((used >> u & 1) or (used >> v & 1) for u, v in E):
            terminal.add(M)
        return
    u, v = E[i]
    visit(i + 1, used, M)
    if not (used >> u & 1 or used >> v & 1):
        visit(i + 1, used | (1 << u) | (1 << v), M | (1 << i))
visit(0, 0, 0)
assert Counter(M.bit_count() for M in terminal) == {5: 42, 6: 168, 7: 24}

@lru_cache(None)
def arrival_count(used):
    return sum(1 for u, v in E if not (used >> u & 1 or used >> v & 1))

def probability_of(M):
    bits = [i for i in range(21) if M >> i & 1]
    k = len(bits)
    @lru_cache(None)
    def probability(subset):
        if subset == (1 << k) - 1:
            return Fraction(1)
        used = 0
        for t, edge_id in enumerate(bits):
            if subset >> t & 1:
                u, v = E[edge_id]
                used |= (1 << u) | (1 << v)
        d = arrival_count(used)
        return sum((probability(subset | (1 << t)) / d
                    for t in range(k) if not subset >> t & 1), Fraction(0))
    return probability(0)

orbits = []
seen = set()
for M in terminal:
    if M in seen: continue
    orbit = set()
    for action in edge_actions:
        image = 0
        for i in range(21):
            if M >> i & 1: image |= 1 << action[i]
        orbit.add(image)
    assert orbit <= terminal
    assert orbit.isdisjoint(seen)
    seen.update(orbit)
    reps = min(orbit)
    p = probability_of(reps)
    assert all(probability_of(N) == p for N in orbit)
    orbits.append((reps.bit_count(), len(orbit), p, p * len(orbit)))
assert seen == terminal and len(orbits) == 5
assert sorted((k, count) for k, count, p, mass in orbits) == [(5, 42), (6, 28), (6, 56), (6, 84), (7, 24)]
expected = {(5, 42): Fraction(19, 13860),
            (6, 28): Fraction(261, 98560),
            (6, 56): Fraction(8257, 1995840),
            (6, 84): Fraction(91723, 23950080),
            (7, 24): Fraction(1247, 95040)}
assert {(k, count): p for k, count, p, mass in orbits} == expected
assert sum(mass for _, _, _, mass in orbits) == 1
print('PASS symmetry group of order 336 and exact five terminal orbits:')
for size, count, p, mass in sorted(orbits):
    print('dimers',size,'orbit',count,'each probability',p,'orbit mass',mass)
