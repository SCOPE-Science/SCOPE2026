#!/usr/bin/env python3
"""Exact finite checks for triangle/open-wedge covariance in random graphs.

Only Python's standard library is needed. Full finite graph enumeration is
independent of the overlap-counting expressions and is not an infinite proof.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def q(n, m, r):
    N = comb(n, 2)
    if not 0 <= m <= N:
        raise ValueError("invalid edge count")
    if r > m:
        return Fraction(0)
    return Fraction(comb(m, r), comb(N, r))


def covariance_fixed_by_overlaps(n, m):
    N = comb(n, 2)
    Q = comb(n, 3)
    edge_sharing = Q * 3 * (n - 3)
    edge_disjoint = Q * Q - Q - edge_sharing
    return (2 * edge_sharing * (q(n, m, 4) - q(n, m, 5))
            + 3 * edge_disjoint * (q(n, m, 5) - q(n, m, 6))
            - 3 * Q * Q * q(n, m, 3) *
            (q(n, m, 2) - q(n, m, 3)))


def covariance_fixed_factored(n, m):
    N = comb(n, 2)
    R = (n - 1) * (n * n - n - 4) + m * (n * n - 3 * n - 8)
    num = (-4 * m * (m - 1) * (m - 2) * (N - m) * (N - m - 1) * R)
    den = ((n + 1) ** 2 * (n + 2) * (N - 5) * (N - 4) *
           (N - 2) ** 2)
    return Fraction(num, den)


def covariance_independent(n, p):
    return 3 * comb(n, 3) * p**4 * (1-p) * (2*(n-3) - (3*n-8)*p)


def exhaustive(n):
    edges = list(combinations(range(n), 2))
    idx = {e: i for i, e in enumerate(edges)}
    triples = [tuple(1 << idx[e] for e in combinations(vs, 2))
               for vs in combinations(range(n), 3)]
    N = len(edges)
    entries = [[0, 0, 0, 0] for _ in range(N + 1)]
    for mask in range(1 << N):
        m = mask.bit_count()
        t, o = 0, 0
        for e1, e2, e3 in triples:
            c = bool(mask & e1) + bool(mask & e2) + bool(mask & e3)
            if c == 3:
                t += 1
            elif c == 2:
                o += 1
        a = entries[m]
        a[0] += 1
        a[1] += t
        a[2] += o
        a[3] += t * o
    return entries


def run():
    checks = 0
    for n in (4, 5, 6):
        N = comb(n, 2)
        rows = exhaustive(n)
        for m, (cnt, st, so, sto) in enumerate(rows):
            assert cnt == comb(N, m)
            direct = Fraction(sto, cnt) - Fraction(st * so, cnt * cnt)
            assert direct == covariance_fixed_by_overlaps(n, m)
            assert direct == covariance_fixed_factored(n, m)
            checks += 3
        for p in (Fraction(1, 8), Fraction(1, 4), Fraction(1, 2),
                  Fraction(2, 3), Fraction(3, 4), Fraction(7, 8)):
            ET = EO = ETO = Fraction(0)
            for m, (_, st, so, sto) in enumerate(rows):
                prob_each = p**m * (1-p)**(N-m)
                ET += prob_each * st
                EO += prob_each * so
                ETO += prob_each * sto
            assert ETO - ET*EO == covariance_independent(n, p)
            checks += 1
    for n in range(4, 36):
        N = comb(n, 2)
        for m in range(N + 1):
            assert covariance_fixed_by_overlaps(n, m) == covariance_fixed_factored(n, m)
            assert (covariance_fixed_factored(n, m) < 0) == (3 <= m <= N-2)
            checks += 2
    print(f"PASS: {checks:,} exact comparisons, complete G(n,m) enumerations for n=4,5,6")


if __name__ == '__main__':
    run()
