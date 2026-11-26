"""Exact finite checks for occupancy and branching comparisons.

The assertions test finite examples. Universal conclusions require the proof.
This file uses only the Python standard library.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial


def stirling2(n, k):
    if n == k == 0:
        return 1
    if n == 0 or k == 0:
        return 0
    return k * stirling2(n - 1, k) + stirling2(n - 1, k - 1)


def iid_occupancy(n, d):
    if n == 0:
        return {0: F(1)}
    return {k: F(factorial(d) // factorial(d - k) * stirling2(n, k), d ** n)
            for k in range(1, min(n, d) + 1)}


def stars_bars_occupancy(n, d):
    if n == 0:
        return {0: F(1)}
    return {k: F(comb(d, k) * comb(n - 1, k - 1), comb(n + d - 1, d - 1))
            for k in range(1, min(n, d) + 1)}


def tail(p, k):
    return sum((v for j, v in p.items() if j >= k), F(0))


def general_iid(n, weights):
    d = len(weights)
    weights = tuple(F(w, sum(weights)) for w in weights)
    dp = {0: F(1)}
    for _ in range(n):
        ndp = {}
        for mask, prob in dp.items():
            for j in range(d):
                m = mask | (1 << j)
                ndp[m] = ndp.get(m, F(0)) + prob * weights[j]
        dp = ndp
    output = {}
    for mask, p in dp.items():
        k = mask.bit_count()
        output[k] = output.get(k, F(0)) + p
    return output


def f_pg(s, law):
    return sum((v * s ** k for k, v in law.items()), F(0))


def main():
    checks = 0
    # Exact stochastic comparisons and the sharp k=2 deficit.
    for d in range(1, 9):
        for n in range(0, 17):
            a, b = iid_occupancy(n, d), stars_bars_occupancy(n, d)
            assert sum(a.values()) == sum(b.values()) == 1
            checks += 1
            for k in range(1, min(n, d) + 2):
                diff = tail(a, k) - tail(b, k)
                assert diff >= 0
                if d >= 2 and n >= 2 and 2 <= k <= min(n, d):
                    assert diff > 0
                if k == 2 and d >= 2 and n >= 1:
                    expected = F(d, comb(n + d - 1, d - 1)) - F(d, d ** n)
                    assert diff == expected
                checks += 1
    # Exact Schur-maximality for nonuniform iid allocations; positive and boundary vectors.
    for d, hi, nmax in [(2, 6, 9), (3, 4, 7), (4, 3, 6)]:
        for w in product(range(hi + 1), repeat=d):
            if sum(w) == 0:
                continue
            for n in range(0, nmax + 1):
                a = iid_occupancy(n, d)
                b = general_iid(n, w)
                for k in range(1, min(n, d) + 2):
                    assert tail(a, k) >= tail(b, k), (d, n, w, k)
                    checks += 1
                if n >= 2 and len(set(w)) > 1:
                    assert tail(a, 2) > tail(b, 2)
                    checks += 1
    # Smallest supercritical nontrivial exact survival comparison.
    t = F(4, 5)
    # Y=0 with probability 1-t, and Y=2 with probability t; d=2.
    independent = {0: 1 - t, 1: t / 2, 2: t / 2}
    composition = {0: 1 - t, 1: 2 * t / 3, 2: t / 3}
    qi, qc = F(1, 2), F(3, 4)
    assert f_pg(qi, independent) == qi
    assert f_pg(qc, composition) == qc
    assert qi < qc
    checks += 3
    for horizon in range(1, 12):
        pi = pc = F(0)
        for _ in range(horizon):
            pi = f_pg(pi, independent)
            pc = f_pg(pc, composition)
        assert pi <= pc, (horizon, pi, pc)
        checks += 1
    print(f'PASS {checks} exact rational assertions')


if __name__ == '__main__':
    main()
