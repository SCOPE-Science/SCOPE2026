#!/usr/bin/env python3
"""Independent brute-force check of the stated finite permutation groups.

Run with python3 verify.py; uses only Python standard library.
"""
from itertools import permutations
from math import factorial


def compositions(total, parts):
    if parts == 1:
        yield (total,)
    else:
        for first in range(1, total - parts + 2):
            for rest in compositions(total - first, parts - 1):
                yield (first,) + rest


def factor_orbit(period, n):
    p = len(period)
    return {''.join(period[(start + i) % p] for i in range(n))
            for start in range(p)}


def symmetry_group_size(period, n):
    factors = factor_orbit(period, n)
    count = 0
    for pi in permutations(range(n)):
        if all(''.join(f[j] for j in pi) in factors for f in factors):
            count += 1
    return count


def formula(p, n):
    m, r = divmod(n, p)
    assert m >= 1
    return (p if r == 0 else 1) * factorial(m + 1) ** r * factorial(m) ** (p - r)


def test_all():
    tests = 0
    for p in range(3, 9):
        for q in range(3, p + 1):
            for runs in compositions(p, q):
                period = ''.join(str(i) * run for i, run in enumerate(runs))
                for n in range(p, 9):
                    exact = symmetry_group_size(period, n)
                    expected = formula(p, n)
                    assert exact == expected, (period, n, exact, expected)
                    tests += 1
    assert tests == 382, tests

    # A sharp three-colour versus two-colour boundary.
    assert symmetry_group_size('0012', 4) == 4
    assert symmetry_group_size('0011', 4) == 8
    print('VERIFY_OK configurations=382; two-colour boundary=8 versus 4')


if __name__ == '__main__':
    test_all()
