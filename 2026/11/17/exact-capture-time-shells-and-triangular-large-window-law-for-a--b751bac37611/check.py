"""Exact finite algebra checks for a two-half-plane quarter-turn isometry.

The infinite assertions in the accompanying proof use the explicit rank
formula and its case-wise recurrence, not this finite sanity check.
"""
from fractions import Fraction


def square_step(m, n):
    return (-n - 1, m) if n < 0 else (-n, m - 1)


def rank(m, n):
    if n >= 1:
        return 2 * (n - m) + 1 if m <= -1 else 2 * (n + m)
    if n == 0:
        return -2 * m + 1 if m <= -1 else (0 if m == 0 else 2 * m - 1)
    if n == -1:
        return -2 * m - 1 if m <= -1 else (0 if m == 0 else 2 * m + 1)
    return 2 * (-m - n) - 2 if m <= 0 else 2 * (m - n) - 1


def point_step(x, y):
    if y < 0:
        return -y, x
    return 1 - y, x - 1


def square_of(x, y):
    return (x.numerator // x.denominator, y.numerator // y.denominator)


assert square_step(0, 0) == (0, -1)
assert square_step(0, -1) == (0, 0)
for m in range(-250, 251):
    for n in range(-250, 251):
        h = rank(m, n)
        assert h >= 0
        p = square_step(m, n)
        if (m, n) not in {(0, 0), (0, -1)}:
            assert rank(*p) == h - 1, (m, n, p, h)
        assert abs(h - 2 * (abs(m) + abs(n))) <= 3
        if abs(m) <= 14 and abs(n) <= 14:
            x = Fraction(m * 13 + 5, 13)
            y = Fraction(n * 17 + 7, 17)
            X, Y = point_step(x, y)
            assert square_of(X, Y) == p
            q = (x, y)
            for k in range(h):
                q = point_step(*q)
            assert square_of(*q) in {(0, 0), (0, -1)}
            if h:
                last = (x, y)
                for k in range(h - 1):
                    last = point_step(*last)
                assert square_of(*last) not in {(0, 0), (0, -1)}
            assert (lambda pp: point_step(*point_step(*point_step(*point_step(*pp)))))(q) == q
for K in range(1, 81):
    count_even = sum(rank(m, n) == 2 * K for m in range(-K - 4, K + 5) for n in range(-K - 4, K + 5))
    count_odd = sum(rank(m, n) == 2 * K - 1 for m in range(-K - 4, K + 5) for n in range(-K - 4, K + 5))
    assert count_even == count_odd == 2 * K, (K, count_odd, count_even)
print('QUARTER_TURN_EXACT_LATTICE_AND_SHELL_CHECK_OK')
