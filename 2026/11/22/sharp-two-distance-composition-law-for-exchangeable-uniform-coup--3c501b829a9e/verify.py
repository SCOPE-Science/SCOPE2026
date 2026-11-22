"""Exact-rational witnesses for sharp two-distance symmetric copula bounds.

Run with Python 3.9 or later; no third-party packages are required.
The finite assertions check the displayed constructions and formulas;
analytical bounds for arbitrary orders are proved separately.
"""
from fractions import Fraction
from math import gcd

H = Fraction(1, 2)


def weights(n, endpoint):
    """Return a fractional perfect matching of step-1/step-2 path square."""
    assert n >= 2 and endpoint in ('low', 'high')
    w = {}

    def edge(i, j, a):
        assert 0 <= i < j < n and 1 <= j - i <= 2
        key = (i, j)
        w[key] = w.get(key, Fraction(0)) + a

    def triangle(i):
        edge(i, i + 1, H)
        edge(i + 1, i + 2, H)
        edge(i, i + 2, H)

    def pentagon(i):
        for u, v in [(0, 1), (1, 3), (3, 4), (2, 4), (0, 2)]:
            edge(i + u, i + v, H)

    def blocks4(start):
        for i in range(start, n, 4):
            edge(i, i + 2, Fraction(1))
            edge(i + 1, i + 3, Fraction(1))

    if endpoint == 'low':
        start = 0
        if n % 2:
            triangle(0)
            start = 3
        for i in range(start, n, 2):
            edge(i, i + 1, Fraction(1))
    else:
        r = n % 4
        if r == 0:
            blocks4(0)
        elif r == 1:
            assert n >= 5
            pentagon(0)
            blocks4(5)
        elif r == 2:
            edge(0, 1, Fraction(1))
            blocks4(2)
        else:
            triangle(0)
            blocks4(3)

    degrees = [Fraction(0) for _ in range(n)]
    long_mass = Fraction(0)
    for (i, j), a in w.items():
        assert a > 0
        degrees[i] += a
        degrees[j] += a
        if j - i == 2:
            long_mass += 2 * a
    assert all(x == 1 for x in degrees)
    expected = (n % 2) if endpoint == 'low' else (n if n % 4 == 0 else n - 2)
    assert long_mass == expected
    return w, long_mass


def bounds(d):
    assert Fraction(0) < d <= H
    q = d.denominator // d.numerator
    r = 1 - q * d
    assert q >= 2 and 0 <= r < d
    assert q * (d - r) + (q + 1) * r == 1
    l = r if q % 2 == 0 else d - r
    h = (1 - 2 * r if q % 4 == 0 else
         1 - 2 * (d - r) if q % 4 == 3 else 1 - 2 * d)
    wm, lm = weights(q, 'low')
    wM, hm = weights(q, 'high')
    xn, zn = weights(q + 1, 'low')
    xM, zM = weights(q + 1, 'high')
    assert l == (d - r) * lm + r * zn
    assert h == (d - r) * hm + r * zM
    assert 0 <= l <= h <= 1
    return q, r, l, h


def run():
    count = 0
    for n in range(2, 161):
        for kind in ('low', 'high'):
            weights(n, kind)
            count += 1
    for denominator in range(2, 121):
        for numerator in range(1, denominator // 2 + 1):
            if gcd(numerator, denominator) > 1:
                continue
            bounds(Fraction(numerator, denominator))
            count += 1
    assert bounds(Fraction(1, 2))[2:] == (0, 0)
    assert bounds(Fraction(1, 3))[2:] == (Fraction(1, 3), Fraction(1, 3))
    assert bounds(Fraction(1, 4))[2:] == (0, 1)
    assert bounds(Fraction(3, 10))[2:] == (Fraction(1, 5), Fraction(3, 5))
    assert bounds(Fraction(1, 5))[2:] == (Fraction(1, 5), Fraction(3, 5))
    count += 5
    print(f'PASS: {count} exact rational witness/range tests')


if __name__ == '__main__':
    run()
