#!/usr/bin/env python3
"""Exact certificate for face-trimer adsorption on the regular icosahedron.
No external packages, floating-point calculations, or external inputs required.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from itertools import permutations, combinations

N = 12
ALL = (1 << N) - 1
U = lambda j: 1 + j % 5
L = lambda j: 6 + j % 5
FACES = sorted({tuple(sorted(tri)) for i in range(5) for tri in [
    (0, U(i), U(i + 1)),
    (11, L(i), L(i + 1)),
    (U(i), U(i + 1), L(i)),
    (U(i), L(i - 1), L(i)),
]})
TRI = tuple(sum(1 << x for x in f) for f in FACES)
assert len(FACES) == 20 and len(set(TRI)) == 20

# A direct finite combinatorial description of the surface, independent of a graph package.
EDGES = sorted(set(tuple(sorted(pair)) for f in FACES for pair in combinations(f, 2)))
assert len(EDGES) == 30
assert all(sum(v in f for f in FACES) == 5 for v in range(N))
assert all(sum(set(e) <= set(f) for f in FACES) == 2 for e in EDGES)
EDGE_THIRDS = {e: tuple(next(v for v in f if v not in e)
                         for f in FACES if set(e) <= set(f)) for e in EDGES}

def available(occupied):
    return tuple(t for t in TRI if not (occupied & t))

# First method: rational, memoized backward Markov recurrence on occupied vertex masks.
@lru_cache(None)
def backward(occupied):
    options = available(occupied)
    if not options:
        return {occupied: Q(1)}
    accum = defaultdict(Q)
    for t in options:
        for final, prob in backward(occupied | t).items():
            accum[final] += prob / len(options)
    return dict(accum)

BACK = backward(0)
assert sum(BACK.values(), Q()) == 1
assert backward.cache_info().currsize == 202

# Independent method: enumerate ordered accepted face sequences rather than state recursion.
# Each path carries exact probability and its exact waiting-time rate sequence.
DIRECT = defaultdict(Q)
PATHS = []
def walk(occupied, probability, rates, sequence):
    candidates = available(occupied)
    if not candidates:
        DIRECT[occupied] += probability
        PATHS.append((sequence, probability, rates, occupied))
        return
    inv = Q(1, len(candidates))
    for face in candidates:
        walk(occupied | face, probability * inv, rates + (len(candidates),), sequence + (face,))
walk(0, Q(1), (), ())
assert dict(DIRECT) == BACK
assert sum(p for _, p, _, _ in PATHS) == 1

# A local transition table valid after ANY of the twenty initial faces.
for first in TRI:
    assert len(available(first)) == 10
    distribution = Counter(len(available(first | second)) for second in available(first))
    assert distribution == {0: 1, 2: 3, 4: 6}, distribution
    for second in available(first):
        third_candidates = available(first | second)
        if len(third_candidates) == 4:
            assert Counter(len(available(first | second | third)) for third in third_candidates) == {0: 2, 1: 2}
        elif len(third_candidates) == 2:
            assert all(len(available(first | second | third)) == 0 for third in third_candidates)
        else:
            assert not third_candidates

# Three terminal strata. The per-labelled-pattern equalities are stronger than a size census.
COUNT = Counter(m.bit_count() for m in BACK)
assert COUNT == {6: 10, 9: 60, 12: 1}, COUNT
for occ, prob in BACK.items():
    assert prob == (Q(3, 10) if occ == ALL else Q(1, 100)), (occ, prob)
SIZE_PROB = {n: sum((prob for occ, prob in BACK.items() if occ.bit_count() == n), Q())
             for n in [6, 9, 12]}
assert SIZE_PROB == {6: Q(1, 10), 9: Q(3, 5), 12: Q(3, 10)}
assert sum(Q(occ.bit_count(), 12) * prob for occ, prob in BACK.items()) == Q(4, 5)

# Independently derive the 120 icosahedral automorphisms by propagating images of a face.
# A vertex map is fixed by an oriented face; two faces incident to each edge force the rest.
AUTOMORPHISMS = set()
for target in FACES:
    for oriented in permutations(target):
        mapping = {0: oriented[0], 1: oriented[1], 2: oriented[2]}
        while True:
            changed = False
            for (u, v), (w, z) in EDGE_THIRDS.items():
                if u not in mapping or v not in mapping:
                    continue
                image_edge = tuple(sorted((mapping[u], mapping[v])))
                a, b = EDGE_THIRDS[image_edge]
                if w in mapping and z not in mapping:
                    assert mapping[w] in (a, b)
                    mapping[z] = b if mapping[w] == a else a
                    changed = True
                if z in mapping and w not in mapping:
                    assert mapping[z] in (a, b)
                    mapping[w] = b if mapping[z] == a else a
                    changed = True
            if not changed:
                break
        assert len(mapping) == 12 and len(set(mapping.values())) == 12
        autom = tuple(mapping[i] for i in range(N))
        assert {tuple(sorted(autom[x] for x in face)) for face in FACES} == set(FACES)
        AUTOMORPHISMS.add(autom)
assert len(AUTOMORPHISMS) == 120

def move_mask(mask, perm):
    return sum((1 << perm[i]) for i in range(N) if (mask >> i) & 1)
remaining = set(BACK)
orbits = []
while remaining:
    seed = min(remaining)
    orbit = {move_mask(seed, perm) for perm in AUTOMORPHISMS}
    assert orbit <= remaining
    assert len({BACK[x] for x in orbit}) == 1
    orbits.append((seed.bit_count(), len(orbit)))
    remaining -= orbit
assert sorted(orbits) == [(6, 10), (9, 60), (12, 1)]

# Waiting times are independent exponentials, with rates given by the number of
# still-available face placements at each successful step.
def exp_laplace(rates, s):
    ans = Q(1)
    for rate in rates:
        ans *= Q(rate) / (Q(rate) + s)
    return ans

def target_laplace(s):
    prefix = Q(20) / (20 + s) * Q(10) / (10 + s)
    return prefix * (Q(1, 10) + Q(3, 10) * Q(4) / (4 + s)
                     + Q(3, 10) * Q(2) / (2 + s)
                     + Q(3, 10) * Q(4) / (4 + s) * Q(1) / (1 + s))

for s in [Q(0), Q(1, 2), Q(1), Q(2), Q(3), Q(7)]:
    direct_laplace = sum((prob * exp_laplace(rates, s) for _, prob, rates, _ in PATHS), Q())
    assert direct_laplace == target_laplace(s)

# Check the first two exact moments from directly enumerated pathwise rates.
def mean_var_for_rates(rates):
    m = sum((Q(1, r) for r in rates), Q())
    v = sum((Q(1, r * r) for r in rates), Q())
    return m, v
M1 = sum((prob * mean_var_for_rates(rates)[0] for _, prob, rates, _ in PATHS), Q())
M2 = sum((prob * (mean_var_for_rates(rates)[0] ** 2 + mean_var_for_rates(rates)[1])
          for _, prob, rates, _ in PATHS), Q())
assert M1 == Q(3, 4)
assert M2 - M1 * M1 == Q(251, 400)

print('PASS: surface has 12 vertices, 30 edges, 20 triangular faces')
print('PASS: 202 reachable occupied masks; 120 graph automorphisms')
print('PASS: forward sequence and backward DP agree on all 71 terminal masks')
print('PASS: 3 automorphism orbits, terminal counts 10/60/1 and probabilities 1/100, 1/100, 3/10')
print('PASS: full 20-by-10 branch table, exact terminal coverage distribution and mean 4/5')
print('PASS: independent Laplace transform checks at 6 exact rational arguments')
print('PASS: adsorption jamming time mean 3/4, variance 251/400')
