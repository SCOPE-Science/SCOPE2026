#!/usr/bin/env python3
"""Exact-rational and independent convex-hull checks for ratio-bounded simplex polars.

Requires Python 3.10+. The independent geometric volume tests use NumPy and SciPy.
The exact rational tests use only the Python standard library.
"""
from fractions import Fraction as F
from math import comb, factorial, sqrt
from itertools import combinations


def polar_volume_over_sqrt_m(m, c):
    """Exact rational value of intrinsic polar volume divided by sqrt(m)."""
    assert m >= 2 and c > 1
    answer = F(0)
    for k in range(1, m):
        ell = m - k
        answer += (F(comb(m, k)) * (m + (c - 1) * k)
                   * c ** (ell - 1) / (factorial(k - 1) * factorial(ell - 1)))
    return F(m ** (m - 2), m - 1) * answer / (c - 1) ** (m - 1)


def primal_fraction(m, c):
    """Volume fraction of the simplex, via the independently integrated beta product."""
    v = F(m, 1) / (c - 1)
    # (m/(c-1)) B(m/(c-1),m) = product(j/(v+j)), j=1,...,m-1
    out = F(1)
    for j in range(1, m):
        out *= F(j) / (v + j)
    return out


def test_exact():
    count = 0
    expected = [F(6), F(117, 2), F(672), F(66875, 8), F(545292, 5), F(1057546861, 720)]
    for m, e in enumerate(expected, 2):
        assert polar_volume_over_sqrt_m(m, F(2)) == e
        count += 1
    for m in range(2, 16):
        assert primal_fraction(m, F(2)) == F(1, comb(2*m-1, m-1))
        count += 1
    # Check every predicted vertex against all polar support inequalities.
    for m in range(2, 9):
        for c in (F(3, 2), F(2), F(5, 2), F(3)):
            for k in range(1, m):
                for highs in combinations(range(m), k):
                    high = set(highs)
                    D = m + (c - 1) * k
                    x = [c/D if a in high else 1/D for a in range(m)]
                    z = [t - F(1, m) for t in x]
                    for i in range(m):
                        for j in range(m):
                            if i == j:
                                continue
                            a = [(F(m, 1)/(c-1))
                                 * ((int(h==i)-c*int(h==j))+(c-1)/m)
                                 for h in range(m)]
                            dot = sum((a[t]*z[t] for t in range(m)), F(0))
                            assert dot <= 1
                            assert (dot == 1) == (i in high and j not in high)
                            count += 2
    return count


def test_independent_hulls():
    import numpy as np
    from scipy.spatial import ConvexHull
    count = 0
    for m in range(2, 8):
        for c in (1.5, 2.0, 3.0):
            # Generate the entire polar vertex set directly from inequalities.
            projector = np.eye(m) - np.ones((m, m))/m
            U, _, _ = np.linalg.svd(projector)
            B = U[:, :m-1]
            points = []
            for i in range(m):
                for j in range(m):
                    if i != j:
                        a = np.zeros(m)
                        a[i] += 1
                        a[j] -= c
                        a += (c-1)/m
                        points.append((m/(c-1))*a@B)
            vol = ((max(p[0] for p in points)-min(p[0] for p in points))
                   if m == 2 else ConvexHull(np.asarray(points)).volume)
            formula = sqrt(m)*float(polar_volume_over_sqrt_m(m, F(str(c))))
            assert abs(vol-formula) < 1e-8*max(vol, formula)
            count += 1
    return count


if __name__ == '__main__':
    a = test_exact()
    b = test_independent_hulls()
    print(f'PASS: {a} exact rational inequality/identity assertions; '
          f'{b} independent geometric convex-hull volumes.')
