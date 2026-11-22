#!/usr/bin/env python3
"""Exact finite checks for the sixth Stirling column's ternary fibers."""
from collections import Counter
from math import comb


def log3(unit, precision):
    modulus = 3 ** precision
    z = unit - 1
    total = 0
    for j in range(1, precision + 12):
        d, e = j, 0
        while d % 3 == 0:
            d //= 3
            e += 1
        term = ((z ** j // (3 ** e)) * pow(d, -1, modulus)) % modulus
        total = (total + (term if j % 2 else -term)) % modulus
    return total


def f(parity, t, k):
    q = 3 ** (k + 2)
    n = 2 * t + parity
    numerator = (-6 * pow(5, n, q) + 15 * pow(4, n, q)
                 + 15 * pow(2, n, q) - 6) % q
    assert numerator % 9 == 0
    return (numerator // 9 * pow(80, -1, 3 ** k)) % (3 ** k)


def gprime(t, k):
    q = 3 ** (k + 3)
    a, b, c = [log3(v, k + 3) for v in (25, 16, 4)]
    n = (-30 * pow(25, t, q) * a + 60 * pow(16, t, q) * b
         + 30 * pow(4, t, q) * c) % q
    assert n % 27 == 0
    return (n // 27 * pow(80, -1, 3 ** k)) % 3 ** k


def critical(k):
    alpha = 0
    assert gprime(alpha, 1) == 0
    for j in range(1, k):
        alpha = next(alpha + d * (3 ** j) for d in range(3)
                     if gprime(alpha + d * (3 ** j), j + 1) == 0)
    return alpha


def local_quadratic_unit(alpha, k):
    # u = f_1''(alpha)/6 = g''(alpha)/2, evaluated 3-adically.
    q = 3 ** (k + 3)
    a, b, c = [log3(v, k + 3) for v in (25, 16, 4)]
    num = (-30 * pow(25, alpha, q) * a * a
           + 60 * pow(16, alpha, q) * b * b
           + 30 * pow(4, alpha, q) * c * c) % q
    assert num % 27 == 0
    return (num // 27 * pow(160, -1, 3 ** k)) % 3 ** k


def stirling_column6(n):
    col = [0] * 7
    col[0] = 1
    for row in range(1, n + 1):
        new = [0] * 7
        for j in range(1, min(row, 6) + 1):
            new[j] = col[j - 1] + j * col[j]
        col = new
    return col[6]


def verify():
    for n in range(6, 48):
        numerator = (6 ** n - 6 * 5 ** n + 15 * 4 ** n
                     - 20 * 3 ** n + 15 * 2 ** n - 6)
        assert numerator % 720 == 0
        assert stirling_column6(n) == numerator // 720
    checks = 0
    for k in range(1, 8):
        q = 3 ** k
        alpha = critical(k + 1)
        delta = f(1, alpha, k)
        u = local_quadratic_unit(alpha, k)
        assert u % 3 == 2
        assert alpha % 3 == 0
        if k >= 3:
            assert delta % 27 == 21
        evens = Counter(f(0, t, k) for t in range(q))
        odds = Counter(f(1, t, k) for t in range(q))
        assert len(evens) == q and all(v == 1 for v in evens.values())
        predicted = Counter()
        m = 3 ** (k - 1)
        for z in range(m):
            y = (delta + 3 * u * z * z) % q
            predicted[y] += 3
        assert odds == predicted, (k, odds, predicted)
        if k <= 5:
            start = max(k + 2, 6)
            for n in range(start, start + 2 * q):
                assert stirling_mod(n, k) == f(n % 2, n // 2, k)
                checks += 1
        squares = len({z * z % m for z in range(m)})
        expected_squares = 1 + sum(3 ** (k - 2 - 2 * j)
                         for j in range((k - 2) // 2 + 1)) if k > 1 else 1
        assert squares == expected_squares == len(odds)
        assert sum(odds.values()) == q
        print(f'k={k} branch_period={q} special_residues={len(odds)} '
              f'delta_mod={delta} u_mod3={u % 3} passed')
    print(f'VERIFY_OK levels=1..7 direct_stirling_checks={checks} '
          f'critical_lifts=PASS square_fiber_histograms=PASS')


def stirling_mod(n, k):
    q = 3 ** (k + 2)
    numerator = (pow(6, n, q) - 6 * pow(5, n, q)
                 + 15 * pow(4, n, q) - 20 * pow(3, n, q)
                 + 15 * pow(2, n, q) - 6) % q
    assert numerator % 9 == 0
    return numerator // 9 * pow(80, -1, 3 ** k) % (3 ** k)


if __name__ == '__main__':
    verify()
