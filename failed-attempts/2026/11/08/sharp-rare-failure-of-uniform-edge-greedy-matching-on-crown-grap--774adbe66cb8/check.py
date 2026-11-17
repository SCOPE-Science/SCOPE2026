"""Exact checks for the edge-uniform greedy matching process on crown graphs.

Run: python3 check.py
All checks use rational arithmetic except the displayed asymptotic diagnostics.
"""
from fractions import Fraction
from functools import lru_cache
from math import log

@lru_cache(None)
def state_failure(m, r):
    assert 0 <= r <= m and m >= 1
    if m == 1:
        return Fraction(r)
    denominator = m * m - r
    terms = [(r * (r - 1), r - 2),
             (2 * r * (m - r), r - 1),
             ((m - r)**2, r)]
    return sum((Fraction(weight, denominator) * state_failure(m - 1, rr)
                for weight, rr in terms if weight), Fraction(0))

@lru_cache(None)
def explicit_failure(left, right):
    m = left.bit_count()
    assert m == right.bit_count()
    if m == 1:
        return Fraction(int(left == right))
    edges = [(i, j) for i in range(left.bit_length()) if left >> i & 1
             for j in range(right.bit_length()) if right >> j & 1 and i != j]
    assert len(edges) == m * m - (left & right).bit_count()
    return sum((explicit_failure(left ^ (1 << i), right ^ (1 << j))
                for i, j in edges), Fraction(0)) / len(edges)

def forward_law(n):
    dist = {n: Fraction(1)}
    result = {n: dist}
    for m in range(n, 1, -1):
        next_dist = {}
        for r, p in dist.items():
            denominator = m * m - r
            for count, rr in ((r * (r - 1), r - 2),
                              (2 * r * (m - r), r - 1),
                              ((m - r)**2, r)):
                if count:
                    next_dist[rr] = next_dist.get(rr, Fraction(0)) + p * Fraction(count, denominator)
        assert sum(next_dist.values()) == 1
        dist = next_dist
        result[m - 1] = dist
    return result

def moments(dist):
    return (sum(Fraction(r) * p for r,p in dist.items()),
            sum(Fraction(r * (r - 1)) * p for r,p in dist.items()))

assertions = 0
for n in range(2, 7):
    expected = state_failure(n, n)
    assert expected == explicit_failure((1 << n) - 1, (1 << n) - 1)
    assertions += 1
    distribution = forward_law(n)
    assert distribution[1].get(1, Fraction(0)) == expected
    assertions += 1
    left = Fraction(1, n + 1) - expected / 2
    right = Fraction(0)
    for m in range(2, n + 1):
        dist = distribution[m]
        right += Fraction(2, m * (m-1)*(m+1)) * sum(
            (p * Fraction(r * (r-1), m*m-r) for r, p in dist.items()), Fraction(0))
    assert left == right
    assertions += 1

assert state_failure(2,2) == 0
assert state_failure(3,3) == Fraction(1,3)
assert state_failure(4,4) == Fraction(4,21)
assert state_failure(5,5) == Fraction(4,21)
assertions += 4

for n in (10, 20, 40, 80, 160):
    p = state_failure(n,n)
    assert 0 < p < Fraction(2,n+1)
    assertions += 1
    # The asymptotic statement follows from the proof, not from these finite examples.
    scaled = float((Fraction(2,n+1)-p) * n*n)/log(n)
    print(f"n={n:3d}; failure_probability={float(p):.12f}; "
          f"n*probability={float(p)*n:.8f}; logarithmic_ratio={scaled:.7f}")
print(f"{assertions} exact independent comparisons passed")
