#!/usr/bin/env python3
"""Exact supplementary checks for sparse triangular Jacobi residual powers.

No external data or third-party Python packages are needed.
"""
from fractions import Fraction
from itertools import product
from math import ceil, floor


def budget(m, d, k):
    return sum((m + d**j - 1) // (d**j) for j in range(k + 1))


def predicted(n, d, k):
    return max(m for m in range(1, d**k + 1) if budget(m, d, k) <= n)


def kth_descendant_max(parents, k):
    counts = [0] * len(parents)
    for i in range(len(parents)):
        a = i
        for _ in range(k):
            a = parents[a]
            if a < 0:
                break
        else:
            counts[a] += 1
    return max(counts)


def all_parent_forests(n, d):
    children = [0] * n
    parents = [-1] * n

    def rec(i):
        if i == n:
            yield tuple(parents)
            return
        for p in range(-1, i):
            if p >= 0 and children[p] == d:
                continue
            parents[i] = p
            if p >= 0:
                children[p] += 1
            yield from rec(i + 1)
            if p >= 0:
                children[p] -= 1

    yield from rec(1)


def matrix_power_times_vector(G, b, k):
    n = len(b)
    out = list(b)
    for _ in range(k):
        out = [sum((G[i][j] * out[j] for j in range(i)), Fraction(0))
               for i in range(n)]
    return out


def check_all():
    checks = 0
    for n in range(2, 8):
        for d in (1, 2, 3):
            exact_max = [0] * n
            for parents in all_parent_forests(n, d):
                for k in range(1, n):
                    z = kth_descendant_max(parents, k)
                    assert z <= predicted(n, d, k), (n, d, k, parents, z)
                    exact_max[k] = max(z, exact_max[k])
                    checks += 1
            for k in range(1, n):
                assert exact_max[k] == predicted(n, d, k), (n, d, k, exact_max[k])
                checks += 1

    n = 7
    q = Fraction(3, 4)
    G = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for i, j in ((1, 0), (2, 0), (3, 1), (4, 1), (5, 2), (6, 2)):
        G[i][j] = q
    b = [Fraction(1)] + [Fraction(0)] * (n - 1)
    r1 = matrix_power_times_vector(G, b, 1)
    r2 = matrix_power_times_vector(G, b, 2)
    assert r1 == [Fraction(0), q, q] + [Fraction(0)] * 4
    assert r2 == [Fraction(0)] * 3 + [q*q] * 4
    assert sum(x*x for x in r2) == Fraction(81, 64)
    assert predicted(7, 2, 2) == 4
    checks += 4

    # Strict rational-boundary tests for the first amplified dimension.
    for (d, k, q) in ((2, 1, Fraction(3, 4)),
                      (2, 2, Fraction(3, 4)),
                      (3, 2, Fraction(2, 3)),
                      (4, 3, Fraction(3, 4))):
        m = 1
        while m <= d**k and (q**(2*k)) * m <= 1:
            m += 1
        if m <= d**k:
            nc = budget(m, d, k)
            assert nc >= k + 1
            assert (q**(2*k)) * predicted(nc, d, k) > 1
            assert (q**(2*k)) * predicted(nc - 1, d, k) <= 1
            checks += 3
    print(f"PASS: {checks} exact finite supplementary checks")


if __name__ == '__main__':
    check_all()
