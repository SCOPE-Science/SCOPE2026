#!/usr/bin/env python3
"""Exact checks for a fourth-autocorrelation Fourier-support theorem.

Requires only Python's standard library. The general proof is in RESULT.md;
this script tests its finite combinatorial mechanism and boundary example.
"""
from itertools import combinations, product

count = 0
nonfull = 0
for m in range(1, 19):
    h = set(range(m))
    # Strictly fewer than one-third of all coset frequencies may be zero.
    for d in range((m - 1) // 3 + 1):
        for holes in combinations(range(m), d):
            a = h - set(holes)
            for t in h:
                assert any(x in a and (x + t) % m in a for x in h)
                for u in h:
                    assert any(
                        x in a and (x + t) % m in a
                        and (x + t + u) % m in a for x in h
                    )
                    count += 1
            if d:
                nonfull += 1

# The exact Fourier products at the sharp density boundary on Z/6Z.
support = (1, 5)
f = {1: 1, 5: 1}
g = {1: 1j, 5: -1j}
zero_sum = [q for q in product(support, repeat=4) if sum(q) % 6 == 0]
assert len(zero_sum) == 6
assert all(
    f[q[0]] * f[q[1]] * f[q[2]] * f[q[3]]
    == g[q[0]] * g[q[1]] * g[q[2]] * g[q[3]]
    for q in zero_sum
)
# The phase ratio i has order four, not an order dividing six.
assert 1j ** 4 == 1 and 1j ** 6 != 1
print('THREE_TRANSLATE_CHECKS', count)
print('NONFULL_SUPPORT_CASES', nonfull)
print('ZERO_SUM_SHARPNESS_PRODUCTS', len(zero_sum))
print('CHECKS_PASSED')
