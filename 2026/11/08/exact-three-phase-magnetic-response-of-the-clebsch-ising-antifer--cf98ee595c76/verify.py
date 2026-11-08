#!/usr/bin/env python3
"""Standalone exhaustive finite verification of a magnetic phase diagram on a 16-vertex folded cube.

Uses exact integer arithmetic for all 2**16 labelled configurations, then checks
all phase minima by rational fields without relying on floating-point comparisons.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations

N = 16
A = [(i, i ^ (1 << j)) for i in range(N) for j in range(4) if i < (i ^ (1 << j))]
A += [(i, i ^ 15) for i in range(N) if i < (i ^ 15)]
assert len(A) == 40 and len(set(A)) == 40
nbr = [0] * N
for u,v in A:
    nbr[u] |= 1 << v
    nbr[v] |= 1 << u
assert all(x.bit_count() == 5 for x in nbr)
assert all(((nbr[i] & nbr[j]).bit_count() == (0 if (nbr[i] >> j) & 1 else 2))
           for i in range(N) for j in range(i + 1, N))

sector = defaultdict(Counter)
independence = Counter()
for s in range(1 << N):
    k = s.bit_count()
    e = sum(((s >> u) & 1) & ((s >> v) & 1) for u,v in A)
    energy = 40 - 10 * k + 4 * e
    sector[k][energy] += 1
    if e == 0:
        independence[k] += 1
assert [independence[k] for k in range(7)] == [1,16,80,160,120,16,0]
assert sum(independence.values()) == 393
assert [min(sector[k]) for k in range(9)] == [40,30,20,10,0,-10,-12,-18,-24]
assert [sector[8][-24], sector[5][-10]] == [10,16]

expected = {
    Fraction(0): (Fraction(-24), {(8, -24): 10}),
    Fraction(2): (Fraction(-24), {(8, -24): 10}),
    Fraction(7,3): (Fraction(-24), {(8, -24): 10, (5, -10): 16}),
    Fraction(3): (Fraction(-28), {(5, -10): 16}),
    Fraction(5): (Fraction(-40), {(k, 40 - 10*k): independence[k] for k in range(6)}),
    Fraction(6): (Fraction(-56), {(0, 40): 1}),
}
for h, (minimum, expected_sectors) in expected.items():
    minval = min(Fraction(en) - h * (16 - 2*k) for k, energies in sector.items() for en in energies)
    assert minval == minimum, (h, minval, minimum)
    winners = {(k,en):count for k, energies in sector.items() for en,count in energies.items()
               if Fraction(en) - h * (16 - 2*k) == minval}
    assert winners == expected_sectors, (h, winners)

# Independent structural cross-check: 5-independent-sets are precisely neighborhoods.
max_inds = {s for s in range(1 << N) if s.bit_count() == 5 and all(not ((s >> u)&1 and (s >> v)&1) for u,v in A)}
assert max_inds == set(nbr)
assert all((a & b).bit_count() <= 2 for a,b in combinations(max_inds,2))

# Supporting sharp induced-edge lower bounds underlying the hand proof.
for k,minimum in [(6,2),(7,3),(8,4)]:
    assert min((e + 10*k - 40)//4 for e in sector[k]) == minimum
print('PASS: 65,536 states; independence polynomial 1+16z+80z^2+160z^3+120z^4+16z^5; phase degeneracies 10/26/16/393/1')
