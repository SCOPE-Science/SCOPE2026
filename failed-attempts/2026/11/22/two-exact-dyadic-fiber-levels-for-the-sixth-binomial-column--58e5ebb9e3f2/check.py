"""Exact finite checks of the sixth Pascal column residue-fiber theorem.

Run with Python 3: python check.py
Only integer arithmetic and the standard library are used.
"""
from collections import Counter
from math import comb


def f(n):
    return comb(n, 6) if n >= 6 else 0


def w(n):
    return (n - 2) * (n - 3) // 2


def a(u, modulus):
    return u * (2 * u - 1) * (2 * u - 3) * pow(45, -1, modulus) % modulus


def c0(v, modulus):
    return v * (4 * v + 1) * (2 * v - 1) * pow(45, -1, modulus) % modulus


def c1(v, modulus):
    return v * (4 * v + 3) * (2 * v + 1) * pow(45, -1, modulus) % modulus


for n in range(6, 500):
    t = w(n)
    assert t * (t - 1) * (t - 3) == 90 * f(n)

for j in range(1, 10):
    modulus = 1 << j
    for fn in (a, c0, c1):
        assert len({fn(v, modulus) for v in range(modulus)}) == modulus

for k in range(1, 12):
    modulus = 1 << k
    period = 1 << (k + 2)
    frequencies = Counter(f(n) % modulus for n in range(period))
    assert sum(frequencies.values()) == period
    for y in range(modulus):
        expected = (6 if y % 2 == 0 else 2) if k == 1 else (10 if y % 4 == 0 else 2)
        assert frequencies[y] == expected, (k, y, frequencies[y], expected)
    for n in range(2 * period):
        assert f(n + period) % modulus == f(n) % modulus
    assert f(2 + (period // 2)) % modulus != f(2) % modulus
    print(f'k={k:2d} period={period:5d} targets={modulus:4d} total={period:5d}: PASS')
print('Branch permutations, polynomial identity, least periods, and target fibers: PASS')
