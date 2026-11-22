"""Reproducible numerical and rational checks for the bipartite adoption theorem.

These tests corroborate identities and examples; the all-size theorem is proved
analytically in RESULT.md and is not inferred from finite samples.
"""
from fractions import Fraction
from math import isclose


def F(z, d):
    return z ** (d + 1) / (1 - z)


def inverse_F(v, d):
    lo, hi = 0.0, 1.0
    for _ in range(140):
        mid = (lo + hi) / 2
        if F(mid, d) < v:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def state_at_x(x, m, n, d):
    y = inverse_F((m / n) * F(x, d), d)
    lam = y / (m * x ** d * (1 - y))
    return x, y, lam


def fold(m, n, d):
    lo, hi = 0.0, 1.0
    for _ in range(140):
        x = (lo + hi) / 2
        y = inverse_F((m / n) * F(x, d), d)
        if (1 - x) * (1 - y) > 1 / (d * d):
            lo = x
        else:
            hi = x
    return state_at_x((lo + hi) / 2, m, n, d)


def branches(m, n, d, lam):
    xc = fold(m, n, d)[0]
    assert lam > fold(m, n, d)[2]
    roots = []
    for lo, hi, decreasing in ((1e-14, xc, True), (xc, 1 - 1e-14, False)):
        for _ in range(140):
            x = (lo + hi) / 2
            value = state_at_x(x, m, n, d)[2]
            if (value > lam) == decreasing:
                lo = x
            else:
                hi = x
        roots.append(state_at_x((lo + hi) / 2, m, n, d))
    return roots


def assert_rel(a, b, tol=1e-8):
    assert isclose(a, b, rel_tol=tol, abs_tol=tol), (a, b)


def run():
    tests = 0
    # Rational exact fold witnesses for equal bipartite sides.
    z = Fraction(1, 2)
    assert z ** 2 * (1 - z) == Fraction(1, 8)
    assert Fraction(1, 1) / (z * (1 - z)) == 4
    assert Fraction(1, 1) / (z ** 2 * (1 - z)) == 8
    z = Fraction(2, 3)
    assert (1 - z) ** 2 == Fraction(1, 9)
    assert Fraction(1, 2) / (z ** 2 * (1 - z)) == Fraction(27, 8)
    tests += 5

    for m, n in ((1, 1), (1, 2), (1, 10), (2, 3), (3, 8), (4, 4)):
        for d in (1.25, 1.5, 2.0, 3.0, 4.0):
            xc, yc, lc = fold(m, n, d)
            assert_rel((1 - xc) * (1 - yc), 1 / d ** 2)
            assert_rel(F(xc, d) / F(yc, d), n / m)
            assert_rel(xc / (1 - xc), lc * n * yc ** d)
            assert_rel(yc / (1 - yc), lc * m * xc ** d)
            low, high = branches(m, n, d, 1.25 * lc)
            for j, (x, y, lam) in enumerate((low, high)):
                assert_rel(x / (1 - x), lam * n * y ** d)
                assert_rel(y / (1 - y), lam * m * x ** d)
                determinant = 1 / ((1 - x) * (1 - y)) - d ** 2
                assert (determinant < 0) if j == 0 else (determinant > 0)
                tests += 3
            tests += 4

    # The exact limiting prefactor is approached from above on large stars.
    for d, size in ((1.5, 10 ** 10), (2., 10 ** 10), (3., 10 ** 10), (4., 10 ** 10)):
        x, y, lc = fold(1, size, d)
        asymptotic = d ** (2 / (d + 1)) * (1 - d ** -2) ** (1 - d)
        ratio = lc * size ** (1 / (d + 1)) / asymptotic
        assert 1 < ratio < 1.1, (d, ratio)
        assert abs(x - (1 - d ** -2)) < 0.03, (d, x)
        tests += 2
    print('PASS: %s exact-rational / numerical identity and sign checks' % tests)
    print('Interpretation: finite checks only; the proof uses monotonicity and full Jacobian factorization.')


if __name__ == '__main__':
    run()
