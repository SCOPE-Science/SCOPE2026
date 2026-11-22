"""Independent exact 1024-state majority-flip absorption calculation.

Standard Petersen drawing: outer 5-cycle (0,...,4), inner step-two
5-cycle (5,...,9), and spokes i--(i+5). Python 3 standard library.
"""
from fractions import Fraction
from functools import lru_cache
from math import comb

N = 10
adj = [0] * N
edges = set()
for i in range(5):
    for a, b in ((i, (i + 1) % 5),
                 (5 + i, 5 + (i + 2) % 5),
                 (i, i + 5)):
        a, b = sorted((a, b))
        edges.add((a, b))
for u, v in edges:
    adj[u] |= 1 << v
    adj[v] |= 1 << u
assert len(edges) == 15 and all(x.bit_count() == 3 for x in adj)

FULL = (1 << N) - 1

def eligible(mask):
    for site in range(N):
        plus = (adj[site] & mask).bit_count()
        is_plus = (mask >> site) & 1
        if (is_plus and plus <= 1) or (not is_plus and plus >= 2):
            yield mask ^ (1 << site)

@lru_cache(maxsize=None)
def frozen_probability(mask):
    targets = list(eligible(mask))
    if not targets:
        return Fraction(mask not in (0, FULL))
    return sum((frozen_probability(m) for m in targets), Fraction(0)) / len(targets)

stable = [m for m in range(1 << N) if not list(eligible(m))]
assert len(stable) == 14
assert sum(m.bit_count() == 5 for m in stable) == 12
def is_induced_five_cycle(mask):
    return (mask.bit_count() == 5 and
            all((adj[i] & mask).bit_count() == 2
                for i in range(N) if (mask >> i) & 1))

cycles = {m for m in range(1 << N) if is_induced_five_cycle(m)}
assert len(cycles) == 12
assert {FULL ^ m for m in cycles} == cycles
assert set(stable) == {0, FULL} | cycles
assert {sum(((m >> u) & 1) != ((m >> v) & 1) for u, v in edges)
        for m in stable} == {0, 5}

# Unnormalized exact Bernoulli coefficients in the Bernstein basis.
weight = [sum((frozen_probability(m) for m in range(1 << N)
               if m.bit_count() == k), Fraction(0)) for k in range(N + 1)]
expected = [Fraction(0), Fraction(0), Fraction(0), Fraction(88, 9),
            Fraction(8242, 189), Fraction(12788, 189),
            Fraction(8242, 189), Fraction(88, 9),
            Fraction(0), Fraction(0), Fraction(0)]
assert weight == expected
assert sum(weight, Fraction(0)) / (1 << N) == Fraction(4121, 24192)
for i in range(11):
    p = Fraction(i, 10)
    x = p * (1 - p)
    lhs = sum((weight[k] * p**k * (1-p)**(10-k) for k in range(11)), Fraction(0))
    assert lhs == Fraction(2, 189) * x**3 * (924 + 425*x)
for m in range(1 << N):
    for next_mask in eligible(m):
        old_cut = sum(((m >> u) & 1) != ((m >> v) & 1) for u, v in edges)
        new_cut = sum(((next_mask >> u) & 1) != ((next_mask >> v) & 1)
                      for u, v in edges)
        assert new_cut in (old_cut - 1, old_cut - 3)

# Conditional probability for each fixed initial number of plus spins.
print('full-state dynamic programming: PASS')
print('terminal states:', len(stable))
print('unnormalized Bernstein coefficients:', *(str(x) for x in weight))
print('unbiased frozen probability:', str(sum(weight) / (1 << N)))
