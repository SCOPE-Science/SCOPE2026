#!/usr/bin/env python3
"""Standalone exact-integer checks for the double-deletion histogram identity."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import comb


def choose(n, k):
    return comb(n, k) if n >= 0 and 0 <= k <= n else 0


def outer_zero_arrangements(s, r, e):
    if s == 0 and r == 1 and e == 2:
        return 1
    if e == 0:
        return choose(s - 1, r)
    if e == 1:
        return 2 * choose(s - 1, r - 1)
    if e == 2:
        return choose(s - 1, r - 2)
    return 0


def exact_histogram(n, q):
    assert n >= 2 and q >= 2
    N = n - 1
    result = Counter({1: q})
    for m in range(1, N + 1):
        for r in range(1, m + 1):
            a = m - r
            s = N - m
            for e in range(3):
                scale = (q * choose(m - 1, r - 1)
                         * outer_zero_arrangements(s, r, e) * (q - 1) ** r)
                if not scale:
                    continue
                base = 1 + choose(m, 2) + 2 * r - e
                for k in range(a + 1):
                    result[base + k] += scale * choose(a, k) * (q - 2) ** k
    return +result


def direct_ball_size(w):
    n = len(w)
    return len({w[:i] + w[i + 1:j] + w[j + 1:]
                for i, j in combinations(range(n), 2)})


def structural_size(w):
    b = [int(w[i] != w[i + 1]) for i in range(len(w) - 1)]
    m = sum(b)
    a = sum(b[i] * b[i + 1] for i in range(len(b) - 1))
    t = sum(len({w[i], w[i + 1], w[i + 2]}) == 3
            for i in range(len(w) - 2))
    return 1 + choose(m, 2) + 2 * (m - a) - b[0] - b[-1] + t


def stated_moments(n, q):
    N = n - 1
    p, z = Fraction(q - 1, q), Fraction(1, q)
    mean = 1 + (N - 1) * p + choose(N, 2) * p * p
    variance = (N * (N - 1) ** 2 * p ** 3 * z
                + choose(N - 1, 2) * p ** 2 * z ** 2
                + (N - 1) * (z - 2 * z ** 2 + z ** 4))
    return mean, variance


def run():
    trials = 0
    for q, max_n in ((2, 10), (3, 8), (4, 7), (5, 6)):
        for n in range(2, max_n + 1):
            hist = Counter()
            for w in product(range(q), repeat=n):
                d = direct_ball_size(w)
                assert d == structural_size(w), (q, n, w, d)
                hist[d] += 1
            assert hist == exact_histogram(n, q), (q, n, hist, exact_histogram(n, q))
            assert sum(hist.values()) == q ** n
            mean = Fraction(sum(k * v for k, v in hist.items()), q ** n)
            second = Fraction(sum(k * k * v for k, v in hist.items()), q ** n)
            expected_mean, expected_var = stated_moments(n, q)
            assert mean == expected_mean, (q, n, mean, expected_mean)
            assert second - mean * mean == expected_var, (q, n)
            trials += 1
    assert stated_moments(7, 3) == (Fraction(11), Fraction(430, 27))
    assert stated_moments(7, 4) == (Fraction(211, 16), Fraction(4305, 256))
    print('VERIFY_OK', 'cases=', trials)


if __name__ == '__main__':
    run()
