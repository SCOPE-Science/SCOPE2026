#!/usr/bin/env python3
from fractions import Fraction
from math import factorial, isqrt


def degree(n, r):
    """Degree of projective n x n matrices of rank <= r."""
    if not (1 <= r <= n):
        raise ValueError((n, r))
    if r == n:
        return 1
    z = Fraction(1, 1)
    for j in range(n-r):
        z *= Fraction(factorial(n+j) * factorial(j),
                      factorial(r+j) * factorial(n-r+j))
    assert z.denominator == 1
    return z.numerator


def rank_ratio_closed(n, r):
    """D[n,r+1]/D[n,r], 1 <= r < n."""
    s = n-r
    return Fraction(
        factorial(r) * factorial(2*s-2) * factorial(2*s-1),
        factorial(s-1)**2 * factorial(r+2*s-1),
    )


def curvature_closed(n, r):
    """D[n,r-1] D[n,r+1] / D[n,r]^2, 2 <= r < n."""
    s = n-r
    return Fraction(r*(r+2*s), 4*(2*s-1)*(2*s+1))


# Replay the degree formula against the closed adjacent-rank ratio and curvature.
checks = 0
for n in range(2, 41):
    ds = [None] + [degree(n, r) for r in range(1, n+1)]
    for r in range(1, n):
        assert Fraction(ds[r+1], ds[r]) == rank_ratio_closed(n, r)
        checks += 1
    for r in range(2, n):
        q = Fraction(ds[r-1]*ds[r+1], ds[r]*ds[r])
        assert q == curvature_closed(n, r)
        # q <= 1 iff 17(n-r)^2 >= n^2+4.
        lhs = 17*(n-r)*(n-r)
        rhs = n*n + 4
        assert (q < 1) == (lhs > rhs)
        assert (q == 1) == (lhs == rhs)
        assert (q > 1) == (lhs < rhs)
        checks += 1

# Stress-test the sign transition without computing giant degrees.
for n in range(2, 1001):
    signs = []
    for r in range(2, n):
        q = curvature_closed(n, r)
        signs.append((q > 1) - (q < 1))
        lhs = 17*(n-r)*(n-r)
        rhs = n*n + 4
        assert (q <= 1) == (lhs >= rhs)
    # Once log-convexity begins, it cannot revert to log-concavity.
    seen_positive = False
    for sig in signs:
        if sig > 0:
            seen_positive = True
        if seen_positive:
            assert sig >= 0

# Exact neutral-curvature Pell points in a broad finite window.
pell = []
for s in range(1, 10000):
    v = 17*s*s - 4
    n = isqrt(v)
    if n*n == v:
        pell.append((n, s, n-s))
assert pell == [(8, 2, 6), (536, 130, 406), (35368, 8578, 26790)]

# The first equality example is visible directly in the degree sequence.
d8 = [degree(8, r) for r in range(1, 9)]
assert d8[5]**2 == d8[4]*d8[6]  # r=6 in 1-based rank indexing

print("VERIFY_OK")
print("degree_and_ratio_checks", checks)
print("sign_transition_checked_through_n", 1000)
print("pell_equalities_s_lt_10000", pell)
print("n8_degrees", d8)
