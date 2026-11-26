#!/usr/bin/env python3
"""Reproduce exact product-rank counts for commuting idempotent maps.

Only standard-library integer arithmetic; independent direct enumeration to size 6.
"""
from itertools import product
from math import comb, factorial


def component_counts(n):
    h = [0] * (n + 1)
    for m in range(1, n + 1):
        for a in range(m):
            for b in range(m - a):
                c = m - 1 - a - b
                ways = factorial(m) // (factorial(a) * factorial(b) * factorial(c))
                h[m] += ways * ((a + 1) * (b + 1)) ** c
    return h


def rank_distribution(n, h):
    # Choose one distinguished component in an unordered component partition.
    tab = [[0] * (n + 1) for _ in range(n + 1)]
    tab[0][0] = 1
    for size in range(1, n + 1):
        for k in range(1, size + 1):
            numerator = sum(comb(size, m) * h[m] * tab[size - m][k - 1]
                            for m in range(1, size + 1))
            assert numerator % k == 0
            tab[size][k] = numerator // k
    return tab


def brute_force(n):
    all_maps = product(range(n), repeat=n)
    idem = [f for f in all_maps if all(f[f[x]] == f[x] for x in range(n))]
    answer = [0] * (n + 1)
    for e in idem:
        for f in idem:
            if all(e[f[x]] == f[e[x]] for x in range(n)):
                answer[len({e[f[x]] for x in range(n)})] += 1
    return answer, len(idem)


def main():
    nmax = 10
    h = component_counts(nmax)
    tab = rank_distribution(nmax, h)
    exact = {
        1: [1],
        2: [6, 1],
        3: [39, 18, 1],
        4: [300, 264, 36, 1],
        5: [2785, 3840, 930, 60, 1],
        6: [30798, 58920, 21780, 2400, 90, 1],
    }
    edge_counts = {2: 0, 3: 15, 4: 240, 5: 3515, 6: 55410}
    totals = [1, 7, 58, 601, 7616, 113989, 1963060, 38178193]
    assert [sum(tab[n]) for n in range(1, 9)] == totals
    for n in range(1, 7):
        direct, e_num = brute_force(n)
        assert direct == tab[n][:n + 1]
        assert direct[1:] == exact[n]
        formula_e = sum(comb(n, j) * j ** (n - j) for j in range(1, n + 1))
        assert e_num == formula_e
        if n >= 2:
            c = sum(direct)
            assert (c - 3 * formula_e + 2) % 2 == 0
            assert (c - 3 * formula_e + 2) // 2 == edge_counts[n]
    # Full-rank pair must consist of two identities.
    assert all(tab[n][n] == 1 for n in range(1, nmax + 1))
    # One-product-image count equals rooted single component number.
    assert all(tab[n][1] == h[n] for n in range(1, nmax + 1))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
