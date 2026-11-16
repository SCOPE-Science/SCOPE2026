#!/usr/bin/env python3
"""Exact self-ambiguity support census for all normalized sixth-phase 7-words."""
from itertools import product
from collections import Counter

# Coefficient pair in the integral basis (1, zeta), zeta^2 = zeta - 1.
PAIR = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))

def autocorrelation_mask(a):
    mask = 0
    for x in (1, 2, 3):
        exponents = ((a[t] - a[(t - x) % 7]) % 6 for t in range(7))
        vals = [PAIR[e] for e in exponents]
        if sum(v[0] for v in vals) == 0 and sum(v[1] for v in vals) == 0:
            mask |= 1 << (x - 1)
    return mask

def canonical(a):
    return tuple((e - a[0]) % 6 for e in a)

def affine_conjugate_orbit(a):
    return {canonical(tuple((s * a[(u * t + v) % 7]) % 6 for t in range(7)))
            for u in range(1, 7) for v in range(7) for s in (1, -1)}

mask_counts = Counter()
support_counts = Counter()
exceptional = set()
for tail in product(range(6), repeat=6):
    a = (0,) + tail
    mask = autocorrelation_mask(a)
    mask_counts[mask] += 1
    support = 7 if all(x == 0 for x in a) else 43 - 2 * mask.bit_count()
    support_counts[support] += 1
    if mask.bit_count() == 2:
        exceptional.add(a)

assert sum(mask_counts.values()) == 6 ** 6
assert mask_counts == {0: 41868, 1: 1512, 2: 1512, 4: 1512,
                       3: 84, 5: 84, 6: 84}
assert support_counts == {7: 1, 39: 252, 41: 4536, 43: 41867}

representatives = ((0, 0, 0, 0, 0, 2, 3),
                   (0, 0, 0, 0, 2, 5, 2),
                   (0, 0, 0, 2, 2, 5, 2),
                   (0, 0, 2, 4, 1, 4, 2))
orbits = [affine_conjugate_orbit(a) for a in representatives]
assert [len(s) for s in orbits] == [84, 42, 84, 42]
assert all(not (orbits[i] & orbits[j]) for i in range(4) for j in range(i+1,4))
assert set().union(*orbits) == exceptional
print('PASS: normalized=46656; support', dict(sorted(support_counts.items())))
print('PASS: masks', dict(sorted(mask_counts.items())))
print('PASS: exceptional orbit sizes', [len(s) for s in orbits])
