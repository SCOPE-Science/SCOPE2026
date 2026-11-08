#!/usr/bin/env python3
"""Exact rational checks for the stated two-map covering profiles.
These checks corroborate scalar consequences, not the topological lemma.
"""
from fractions import Fraction as F
from itertools import product

def profile(blocks):
    """blocks: list of (degree, nonnegative rational mass), total mass 1."""
    assert blocks and sum((w for d, w in blocks), F(0)) == 1
    assert all(isinstance(d, int) and d >= 1 and w >= 0 for d, w in blocks)
    trivial = sorted((w for d, w in blocks if d == 1), reverse=True)
    t1, t2 = (trivial + [F(0), F(0)])[:2]
    u = max((w / d for d, w in blocks if d > 1), default=F(0))
    H = max(t1 + t2, u)
    Heq = max(t1, min(t1, F(1, 2)) + min(t2, F(1, 2)), u)
    return 2*(1-H), 2*(1-Heq)

count = 0
for degrees in product((1, 2, 3, 5), repeat=3):
    for a in range(11):
        for b in range(11-a):
            weights = (F(a, 10), F(b, 10), F(10-a-b, 10))
            d, e = profile(list(zip(degrees, weights)))
            assert F(0) <= d <= e <= F(2)
            count += 1

for degree in range(2, 14):
    assert profile([(degree, F(1))]) == (F(2)*(1-F(1, degree)),)*2
    count += 1

for k in range(1, 30):
    eps = F(1, 1000*k)
    blocks = [(1, F(3, 4)), (1, F(1,4)-eps), (2, eps)]
    assert profile(blocks) == (2*eps, F(1,2))
    count += 1

assert profile([(1,F(3,5)),(1,F(3,10)),(2,F(1,10))]) == (F(1,5),F(2,5))
print('COMPONENTWISE_MARKOV_RATIONAL_CHECK_OK', count)
