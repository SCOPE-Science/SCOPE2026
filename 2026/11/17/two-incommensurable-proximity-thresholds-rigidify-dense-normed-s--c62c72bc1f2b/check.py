"""Supplementary exact-arithmetic checks of the rational-ratio witness.

The infinite-dimensional and dense-set theorem is established analytically;
these finite calculations check only the explicit one-dimensional example.
"""
from fractions import Fraction


def periodic_nonlinear(x, delta):
    k = x // delta
    u = x - k * delta
    return k * delta + u * u / delta


def check():
    delta = Fraction(3, 5)
    a = 2 * delta
    b = 3 * delta
    assert periodic_nonlinear(delta / 2, delta) == delta / 4
    points = [Fraction(j, 28) for j in range(-150, 151)]
    checked = 0
    for x in points:
        for y in points:
            before = abs(x - y)
            after = abs(periodic_nonlinear(x, delta) - periodic_nonlinear(y, delta))
            for radius in (a, b, 5 * delta, 8 * delta):
                assert (before < radius) == (after < radius)
                checked += 1
    for k in range(-10, 11):
        for x in points:
            assert periodic_nonlinear(x + k * delta, delta) == periodic_nonlinear(x, delta) + k * delta
    print(f"PASS: {checked} exact threshold comparisons and 6321 translations")


if __name__ == '__main__':
    check()
