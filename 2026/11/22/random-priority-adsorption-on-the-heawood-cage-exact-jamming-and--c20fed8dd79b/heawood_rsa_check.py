#!/usr/bin/env python3
"""Exact independent checks of the Heawood hard-core random-priority adsorption law.

Only Python standard-library modules are needed.  Every arithmetic operation
used for the claimed probabilities is rational (no simulations).
"""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations, permutations
from math import comb
from collections import Counter, defaultdict

N = 14
P = tuple(range(7))
L = tuple(range(7, 14))
# Difference set of the projective plane over seven points.
LINES = [frozenset((j, (j + 1) % 7, (j + 3) % 7)) for j in range(7)]
assert len(set(LINES)) == 7
assert all(sum(int({a,b} <= s) for s in LINES)==1 for a,b in combinations(P,2))
NEIGHBORS = [set() for _ in range(N)]
for j, line in enumerate(LINES):
    for p in line:
        NEIGHBORS[p].add(j + 7)
        NEIGHBORS[j + 7].add(p)
assert all(len(x) == 3 for x in NEIGHBORS)

CLOSED = [1 << u | sum(1 << v for v in NEIGHBORS[u]) for u in range(N)]
ALL = (1 << N) - 1

# Independent check 1: first-eligible-vertex backward recursion on residual masks.
@lru_cache(None)
def backwards(mask):
    if not mask:
        return {0: Q(1)}
    possible = [v for v in range(N) if mask & (1 << v)]
    law = defaultdict(Q)
    for v in possible:
        for r, prob in backwards(mask & ~CLOSED[v]).items():
            law[r + 1] += prob / len(possible)
    return dict(law)

# Enumerate the complete finite set system, not a sampled family.
independent = []
maximal = []
for mask in range(1 << N):
    good = all(not(mask & (1 << u) and mask & (1 << v))
               for u in P for v in NEIGHBORS[u])
    if good:
        independent.append(mask)
        if all(mask & CLOSED[v] for v in range(N)):
            maximal.append(mask)
assert Counter(mask.bit_count() for mask in independent) == {
    0: 1, 1: 14, 2: 70, 3: 154, 4: 147, 5: 56, 6: 14, 7: 2
}

# Geometric classification: type (points chosen, lines chosen).
types = Counter((sum(bool(mask & (1 << v)) for v in P),
                 sum(bool(mask & (1 << v)) for v in L))
                for mask in maximal)
assert types == {(7, 0): 1, (0, 7): 1,
                 (4, 1): 7, (1, 4): 7, (2, 2): 21}, types

# Independent check 2: integrate the exact output-set event over independent
# uniform arrival times.  For each outside vertex u, some selected neighbour
# must arrive before u, i.e. U_u > min_{v in I intersect N(u)} U_v.
# The simplex integral for a fixed ordering of chosen sites is computed by
# repeated polynomial antiderivatives, using rational arithmetic.
def simplex_probability(freq):
    polynomial = [Q(1)]
    for f in freq:
        new = [Q(0)] * (len(polynomial) + f)
        for d, coeff in enumerate(polynomial):
            for r in range(f + 1):
                new[d + r] += coeff * (-1 if r % 2 else 1) * comb(f, r)
        polynomial = [Q(0)] + [a / (d + 1) for d, a in enumerate(new)]
    return sum(polynomial)

def output_probability(selected):
    remaining = [u for u in range(N) if u not in selected]
    total = Q(0)
    for order in permutations(selected):
        rank = {v: i for i, v in enumerate(order)}
        freq = [0] * len(selected)
        for u in remaining:
            earliest = min(rank[v] for v in NEIGHBORS[u] if v in rank)
            freq[earliest] += 1
        total += simplex_probability(freq)
    return total

per_type = defaultdict(set)
by_size = defaultdict(Q)
for mask in maximal:
    selected = tuple(v for v in range(N) if mask & (1 << v))
    prob = output_probability(selected)
    typ = (sum(v in P for v in selected), sum(v in L for v in selected))
    per_type[typ].add(prob)
    by_size[len(selected)] += prob
assert dict(by_size) == {4: Q(4, 21), 5: Q(7, 15), 7: Q(12, 35)}
assert per_type == {
    (7, 0): {Q(6, 35)}, (0, 7): {Q(6, 35)},
    (4, 1): {Q(1, 30)}, (1, 4): {Q(1, 30)},
    (2, 2): {Q(4, 441)}
}
assert backwards(ALL) == dict(by_size)
assert sum(by_size.values()) == 1
mean = sum(k * p for k, p in by_size.items())
assert mean == Q(577, 105)
assert mean / 14 == Q(577, 1470)
assert mean / 14 - Q(3, 8) == Q(103, 5880)
assert by_size[7] / Q(2, len(maximal)) == Q(222, 35)
assert Q(1, 2) * sum(abs(per_type[typ].copy().pop() - Q(1, 37)) * count
                         for typ, count in types.items()) == Q(293, 777)
print('PASS: 2^14-set exhaustive census, rational residual-process DP,')
print('      and independent event-integral calculation for all 37 outputs.')
print('Independent set coefficient sequence:', Counter(mask.bit_count() for mask in independent))
print('Maximal-set geometric types:', sorted(types.items()))
print('Each output probability:', sorted((k, sorted(v)) for k,v in per_type.items()))
print('Size distribution:', sorted(by_size.items()))
print('Mean and mean occupancy:', mean, mean/14)
print('Full-side selection amplification:', Q(222,35))
print('TV versus uniform maximal-set distribution:', Q(293,777))
# Finite-time rate-one kinetics: each site has one independent Exp(1) arrival.
# Conditional on k arrivals by t, the arrived set is a uniform k-subset
# and its arrival order is uniform, so its expected accepted count is mu[k].
mean_by_k = defaultdict(Q)
for mask in range(1 << N):
    mean_by_k[mask.bit_count()] += sum(r * p for r, p in backwards(mask).items())
mu = tuple(mean_by_k[k] / comb(N, k) for k in range(N + 1))
assert mu == (
 Q(0), Q(1), Q(23,13), Q(31,13), Q(413,143), Q(43,13),
 Q(2143,585), Q(131,33), Q(381863,90090), Q(67261,15015),
 Q(70573,15015), Q(6698,1365), Q(2323,455), Q(1447,273), Q(577,105)
)
assert all(mu[k+1] >= mu[k] for k in range(N))
print('Time-dependent occupancy Bernstein means mu[k]:')
print(' '.join(f'{k}:{x}' for k,x in enumerate(mu)))
print('States in independent residual-process DP:', backwards.cache_info().currsize)
