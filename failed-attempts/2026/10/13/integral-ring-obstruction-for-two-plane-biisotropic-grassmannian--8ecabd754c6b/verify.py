#!/usr/bin/env python3
"""Integer-only checks for two-plane biisotropic Grassmannian degree comparison.

Not an independent proof of the universal assertions. Requires Python >=3.8.
"""
from math import factorial
from itertools import combinations


def degree_by_ballot_dp(N):
    """Count paths to the 2 x (N-2) Young rectangle by Pieri additions."""
    m = N - 2
    if m < 0:
        raise ValueError(N)
    steps = {(0, 0): 1}
    for a in range(m + 1):
        for b in range(a + 1):
            if (a, b) == (0, 0):
                continue
            steps[(a, b)] = steps.get((a - 1, b), 0) + steps.get((a, b - 1), 0)
    return steps[(m, m)]


def catalan(m):
    return factorial(2 * m) // (factorial(m) * factorial(m + 1))


def source_cell_ranks(n):
    """Fonarev--Kuznetsov k=2 unit-free fixed-point dimension formula."""
    counts = {}
    for a, b in combinations(range(-n, n + 1), 2):
        if a + b in (-1, 1):
            continue
        d = a + b + (2*n - 1) - (a + b > 1) - (a + b > -1)
        assert 0 <= d <= 4*n-4
        counts[d] = counts.get(d, 0) + 1
    return counts


def ordinary_grassmannian_ranks(n):
    counts = {}
    for i, j in combinations(range(1, 2*n + 1), 2):
        d = i + j - 3
        counts[d] = counts.get(d, 0) + 1
    return counts


def main():
    assert degree_by_ballot_dp(3) == degree_by_ballot_dp(2) == 1
    for n in range(2, 21):
        bx = degree_by_ballot_dp(2*n+1)
        by = degree_by_ballot_dp(2*n)
        assert bx == catalan(2*n-1), (n, bx)
        assert by == catalan(2*n-2), (n, by)
        assert n * bx == (4*n-3) * by
        assert bx > by
        if n <= 10:
            a = source_cell_ranks(n)
            b = ordinary_grassmannian_ranks(n)
            assert a == b, (n, a, b)
            assert a[1] == 1
    assert (degree_by_ballot_dp(5), degree_by_ballot_dp(4)) == (5, 2)
    assert (degree_by_ballot_dp(7), degree_by_ballot_dp(6)) == (42, 14)
    print('VERIFY_OK: degree DP, Catalan identities, cell ranks, boundary n=1')


if __name__ == '__main__':
    main()
