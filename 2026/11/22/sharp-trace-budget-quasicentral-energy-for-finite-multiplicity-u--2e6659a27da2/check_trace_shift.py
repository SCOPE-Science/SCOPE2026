"""Exact-rational supplemental checks for the finite-trace shift commutator law.

This checks sample active sets and first-order optimality identities; the
infinite-dimensional theorem requires the mathematical proof in RESULT.md.
"""
from fractions import Fraction


def profile(m: int, b: Fraction):
    q = Fraction(3) * (m + 1 - 2 * b) / (m * (m * m - 1))
    p = Fraction(1, m) - q * m
    x = [(m - n) * (p + q * (m - n)) for n in range(m)] + [Fraction(0)]
    return x, p, q


def run():
    tests = 0
    for m in range(2, 151):
        lo, hi = Fraction(m + 1, 3), Fraction(m + 2, 3)
        for k in range(0, 21):
            b = lo + (hi - lo) * Fraction(k, 20)
            x, p, q = profile(m, b)
            assert x[0] == 1; tests += 1
            assert sum(x) == b; tests += 1
            assert all(Fraction(0) <= y <= 1 for y in x); tests += 1
            assert all(x[i] >= x[i + 1] for i in range(m)); tests += 1
            assert all(x[i] > 0 for i in range(m - 1)); tests += 1
            assert 0 <= q; tests += 1
            assert q >= p; tests += 1
            energy = sum((x[i] - x[i + 1]) ** 2 for i in range(m))
            predicted = Fraction(1, m) + 3 * (m + 1 - 2 * b) ** 2 / (m * (m * m - 1))
            assert energy == predicted; tests += 1
            if m >= 3 and k == 0:
                xp, _, _ = profile(m - 1, b)
                assert xp == x[0:m]; tests += 1
            for j in range(1, m):
                # Stationarity: 2(2x_j-x_(j-1)-x_(j+1))+4q = 0.
                assert 2 * (2 * x[j] - x[j - 1] - x[j + 1]) + 4 * q == 0; tests += 1
            # Boundary zero-cell reduced gradient: -2*x_(m-1)+4q>=0.
            assert -2 * x[m-1] + 4 * q >= 0; tests += 1
        # At the right boundary, adjoining one more active cell changes nothing.
        xb, _, _ = profile(m, hi)
        xn, _, _ = profile(m + 1, hi)
        assert xn == xb + [0]; tests += 1
    # independent check of the B=3/2 sample.
    x, _, _ = profile(3, Fraction(3, 2))
    assert x == [1, Fraction(5, 12), Fraction(1, 12), 0]; tests += 1
    assert sum((x[j] - x[j+1])**2 for j in range(3)) == Fraction(11,24); tests += 1
    # Multiplicities: trace and energy scale by r; sharp asymptotic value per r.
    for r in range(1, 11):
        for m in (3, 6, 20, 50):
            b = Fraction(2 * m + 3, 6)
            # Clamp into this m's interval by taking midpoint instead.
            b = (Fraction(m+1,3) + Fraction(m+2,3)) / 2
            x, _, _ = profile(m, b)
            B = r*b
            assert r*sum(x) == B; tests += 1
            assert r*sum((x[j]-x[j+1])**2 for j in range(m)) == r*(Fraction(1,m)+3*(m+1-2*B/r)**2/(m*(m*m-1))); tests += 1
    print('TRACE_SHIFT_EXACT_RATIONAL_OK', tests)


if __name__ == '__main__':
    run()
