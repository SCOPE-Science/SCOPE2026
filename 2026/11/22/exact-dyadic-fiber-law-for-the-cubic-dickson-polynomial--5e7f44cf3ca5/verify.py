#!/usr/bin/env python3
"""Reproduce finite checks for a cubic Dickson polynomial modulo 2^k.

The proof establishes all exponents. These finite checks independently count
polynomial fibers, compare the proposed formula, and test the 2-adic square
root multiplicity formula at the tested levels. Python 3, standard library only.
"""
from collections import Counter


def square_roots_formula(m, a):
    """Number of roots of t*t == a (mod 2**m), m >= 1."""
    assert m >= 1
    mod = 1 << m
    a %= mod
    if a == 0:
        return 1 << (m // 2)
    v = (a & -a).bit_length() - 1
    if v & 1:
        return 0
    s = v // 2
    d = m - 2 * s
    u = a >> (2 * s)
    if d == 1:
        rho = 1
    elif d == 2:
        rho = 2 if u % 4 == 1 else 0
    else:
        rho = 4 if u % 8 == 1 else 0
    return (1 << s) * rho


SMALL = {
    1: ({0}, 2),
    2: ({2}, 3),
    3: ({2, 6}, 3),
    4: ({2, 14}, 5),
    5: ({2, 14, 18, 30}, 5),
    6: ({2, 18, 46, 62}, 9),
}


def expected_fiber(k, y):
    assert 1 <= k and 0 <= y < 2**k
    if y & 1:
        return 0
    if k <= 6:
        special, count = SMALL[k]
        return count if y in special else 1
    if y % 128 in (18, 110):
        return 17
    if y % 64 == 62:
        m = 1 << (k - 6)
        a = ((y + 2) // 64 * pow(3, -1, m)) % m
        return 1 + 8 * square_roots_formula(k - 6, a)
    if y % 64 == 2:
        m = 1 << (k - 6)
        a = ((y - 2) // 64 * pow(5, -1, m)) % m
        return 1 + 8 * square_roots_formula(k - 6, a)
    return 1


def predicted_max(k):
    if k <= 5:
        return [0, 2, 3, 3, 5, 5][k]
    return 1 + (1 << ((k + 1) // 2))


def predicted_max_targets(k):
    if k == 1 or k == 2:
        return 1
    if k == 3 or k == 4:
        return 2
    if k == 5 or k == 6:
        return 4
    return 2 if k % 2 else 8


def check():
    for m in range(1, 13):
        mod = 1 << m
        counts = Counter((t * t) % mod for t in range(mod))
        for a in range(mod):
            actual = counts.get(a, 0)
            assert actual == square_roots_formula(m, a), (m, a, actual)
    print('Square-root count checked for every target at moduli 2^m, 1 <= m <= 12.')

    total_inputs = 0
    total_targets = 0
    for k in range(1, 17):
        mod = 1 << k
        fibers = Counter((x**3 - 3*x) % mod for x in range(mod))
        assert len(fibers) == mod // 2
        assert all(y % 2 == 0 for y in fibers)
        actual_max = max(fibers.values())
        actual_max_targets = sum(n == actual_max for n in fibers.values())
        assert actual_max == predicted_max(k), (k, 'max', actual_max)
        assert actual_max_targets == predicted_max_targets(k), (k, 'max target count', actual_max_targets)
        for y in range(mod):
            assert fibers.get(y, 0) == expected_fiber(k, y), (k, y, fibers.get(y, 0), expected_fiber(k, y))
        total_inputs += mod
        total_targets += mod
        print('k=%2d: targets=%5d, image=%5d, maximum=%3d, maximizing targets=%d' %
              (k, mod, len(fibers), actual_max, actual_max_targets))
    print('SUCCESS: %d polynomial evaluations and %d exact fiber comparisons.' %
          (total_inputs, total_targets))


if __name__ == '__main__':
    check()
