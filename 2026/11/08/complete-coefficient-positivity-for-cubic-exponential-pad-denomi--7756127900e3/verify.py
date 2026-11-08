#!/usr/bin/env python3
"""Finite exact checks supporting a symbolic cubic Padé positivity proof."""
from fractions import Fraction
from math import sqrt, hypot


def normalized(k):
    t = k + 1
    return (Fraction(1), -Fraction(3, t + 2),
            Fraction(3, (t + 1) * (t + 2)),
            -Fraction(1, t * (t + 1) * (t + 2)))


def coefficients(k, maximum):
    q = normalized(k)
    a = [Fraction(1)]
    for n in range(1, maximum + 1):
        a.append(-sum(q[j] * a[n - j]
                      for j in range(1, min(n, 3) + 1)))
    return a


def exact_cubic_translation(k, x):
    t = k + 1
    q = normalized(k)
    z = Fraction(t) + x
    lhs = t * (t + 1) * (t + 2) * sum(q[j] * z**j for j in range(4))
    rhs = 2 * t - 3 * t * x - x**3
    assert lhs == rhs


def pole_geometry(k):
    t = k + 1
    lo, hi = .5, 2 / 3
    for _ in range(65):
        u = (lo + hi) / 2
        if u**3 + 3 * t * u < 2 * t:
            lo = u
        else:
            hi = u
    u = (lo + hi) / 2
    R = t + u
    v = sqrt(3 * t + 3 * u * u / 4)
    s = hypot(t - u / 2, v)
    d = hypot(3 * u / 2, v)
    A = s * s / (d * d)
    twice_B = R * s / (v * d)
    assert s > R and A > twice_B
    return A - twice_B


def main():
    count = 0
    for k in range(81):
        a = coefficients(k, 150)
        assert all(value > 0 for value in a)
        assert a[0] == 1
        assert a[1] == Fraction(3, k + 3)
        for i in range(len(a)):
            assert sum(normalized(k)[j] * a[i-j]
                       for j in range(0, min(3, i) + 1)) == (1 if i == 0 else 0)
            count += 1
    for k in range(200):
        for x in (Fraction(0), Fraction(1, 4), Fraction(-3, 5), Fraction(7, 2)):
            exact_cubic_translation(k, x)
            count += 1
    for k in list(range(201)) + [500, 1000, 10000]:
        assert pole_geometry(k) > 0
        count += 1
    print('VERIFY_OK', count)


if __name__ == '__main__':
    main()
