"""Finite reproducibility checks for radial Bergman kernel root-staircase formulas.

The universal root count is proved analytically in the accompanying result;
these finite tests are not an exhaustive or independent proof.
"""
import cmath
import math
from fractions import Fraction


def kernel_closed(beta, s):
    N = beta + 2.0
    if abs(s) < 1e-15:
        return (beta + 1.0) * (beta + 2.0)
    return (beta + 1.0) * ((1.0 - s)**(-N) - 1.0) / s


def kernel_series(beta, s, terms=450):
    coeff = (beta + 1.0) * (beta + 2.0)
    power = 1.0 + 0j
    out = 0j
    for n in range(terms):
        out += coeff * power
        coeff *= (n + beta + 3.0) / (n + 2.0)
        power *= s
    return out


def thresholds(beta, r):
    if r <= 0.0:
        return []
    N = beta + 2.0
    return [k for k in range(1, int(math.ceil(N / 4.0)) + 1)
            if 2.0 * math.sin(math.pi * k / N) < r - 1e-12
            and k * 2.0 * math.pi / N < math.pi / 2.0]


def count_formula(beta, r):
    if r <= 0:
        return 0
    x = (beta + 2.0) * math.asin(r / 2.0) / math.pi
    return 2 * max(0, math.ceil(x - 1e-12) - 1)


def test():
    check_count = 0
    for beta in (-.8, -.25, 0, .2, 1.25, 3, 4, 4.1, 5, 7.1, 10, 10.1, 11, 16, 18.3, 22, 47.1):
        for s in (.13 + .18j, -.24 + .16j, .0 + 0j):
            a = kernel_closed(beta, s)
            b = kernel_series(beta, s)
            assert abs(a-b) < 1e-9 * max(1.0, abs(a)), (beta, s, a, b)
            check_count += 1
        N = beta + 2.0
        for r in (0, .2, .35, .55, .8, .99, 1.0):
            ks = thresholds(beta, r)
            assert count_formula(beta, r) == 2 * len(ks), (beta, r, ks)
            check_count += 1
            for k in ks:
                for sign in (-1, 1):
                    s = 1.0 - cmath.exp(sign * 2j * math.pi * k / N)
                    assert abs(s) < r + 1e-11
                    assert abs(kernel_closed(beta, s)) < 2e-7 * max(1.0, N), (beta, r, k, s)
                    w = r * cmath.exp(.27j)
                    z = s / w.conjugate()
                    assert abs(z) < 1 + 1e-10
                    check_count += 1
    # Prove symbolic polynomial agreement for the integer slice by coefficient sums.
    # The exact coefficient of s^n in the numerator of (1-s)^(-N)/s-1/s
    # must be the coefficient in the standard beta-moment kernel.
    for m in range(0, 20):
        N = m + 2
        for n in range(0, 16):
            c_from_moments = Fraction(math.factorial(n+m+2), math.factorial(n+1)*math.factorial(m))
            c_from_binomial = Fraction((m+1)*math.comb(n+N, N-1))
            assert c_from_moments == c_from_binomial
            check_count += 1
    # Boundary roots at the six-step transition are excluded from the open disk.
    for k in range(1, 8):
        N = 6*k
        s = 1.0 - cmath.exp(2j*math.pi*k/N)
        assert abs(abs(s)-1.0) < 1e-13
        assert count_formula(N-2, 1.0) == 2*(k-1)
        check_count += 1
    print('RADIAL_BERGMAN_STAIRCASE_PASS checks=' + str(check_count))


if __name__ == '__main__':
    test()
