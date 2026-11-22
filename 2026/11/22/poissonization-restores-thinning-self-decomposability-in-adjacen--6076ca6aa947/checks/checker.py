"""Exact-rational corroboration of adjacent-gamma-mixed Poisson identities.

Run with: python checks/checker.py
Standard library only. Universal statements require the analytic proof.
"""
from fractions import Fraction as F
from math import factorial, comb


def parameters(r, s, theta):
    r, s, theta = F(r), F(s), F(theta)
    assert r > 0 and F(0) <= s <= 1 and theta > 0
    return r, s, theta


def qa(theta, s, u=F(1)):
    return u / (theta + u), s * u / (theta + s * u)


def canonical(r, s, theta, n, u=F(1)):
    q, a = qa(theta, s, u)
    return (r + 1) * q**n - a**n


def threshold_polynomial(r, s, theta):
    return (r + 1) * (theta + s)**2 - s * (theta + 1)**2


def mass_from_gamma_mix(r, s, theta, n):
    # These cases have integer r and use exact finite products.
    r = int(r)
    coeff_r = F(1)
    coeff_r1 = F(1)
    for k in range(n):
        coeff_r *= F(r + k, k + 1)
        coeff_r1 *= F(r + 1 + k, k + 1)
    q = 1 / (theta + 1)
    v = theta / (theta + 1)
    return s * coeff_r * v**r * q**n + (1-s) * coeff_r1 * v**(r+1) * q**n


def mass_from_rational_pgf(r, s, theta, n):
    # Coefficient of theta^r (theta+s-s*z)/(theta+1-z)^(r+1).
    r = int(r)
    q = 1 / (theta + 1)
    leading = (theta + s) * F(comb(r + n, n)) * q**n
    trailing = F(0) if n == 0 else s * F(comb(r + n - 1, n - 1)) * q**(n - 1)
    return theta**r / (theta + 1)**(r + 1) * (leading - trailing)


def pnxl_mass(theta, n):
    # Direct published formula, independent of the mixture calculation.
    return theta * (2 * theta + theta * n + 1) / (2 * (theta + 1)**(n + 2))


def coefficient_recurrence(r, s, theta, mass, n):
    # G'(z)/G(z)=sum_{k>=1} b_k z^(k-1): n*p_n=sum b_k*p_(n-k).
    return sum((canonical(r, s, theta, k) * mass[n-k] for k in range(1, n + 1)), F(0))


def normalized_palm_weight(m):
    # Ratio of derivatives of the two gamma-generated pgfs at z=1.
    low = F(factorial(m), 1)
    high = F(factorial(m + 1), 1)
    return low / (low + high)


def test():
    for r in (1, 2, 3):
        for s in (F(0), F(1, 6), F(1, 4), F(1, 2), F(1)):
            for theta in (F(1, 100), F(1, 10), F(1, 4), F(1), F(9)):
                r, s, theta = parameters(r, s, theta)
                q, a = qa(theta, s)
                assert 0 <= a <= q < 1
                masses = [mass_from_gamma_mix(r, s, theta, n) for n in range(20)]
                for n in range(20):
                    assert masses[n] == mass_from_rational_pgf(r, s, theta, n)
                    if n >= 1:
                        assert n * masses[n] == coefficient_recurrence(r, s, theta, masses, n)
                    if r == 1 and s == F(1, 2):
                        assert masses[n] == pnxl_mass(theta, n)
                for n in range(1, 18):
                    assert canonical(r, s, theta, n) > 0
                crit = threshold_polynomial(r, s, theta) >= 0
                for n in range(1, 18):
                    diff = canonical(r, s, theta, n) - canonical(r, s, theta, n + 1)
                    if crit:
                        assert diff >= 0
                    elif n == 1:
                        assert diff < 0
                for c in (F(1, 2), F(9, 10), F(99, 100)):
                    for n in range(1, 12):
                        nu = (canonical(r, s, theta, n) - canonical(r, s, theta, n, c)) / n
                        if crit:
                            assert nu >= 0
    r, s = F(1), F(1, 4)
    assert canonical(r, s, F(1, 10), 1) - canonical(r, s, F(1, 10), 2) == -F(230, 5929)
    assert canonical(r, s, F(1, 4), 1) - canonical(r, s, F(1, 4), 2) == F(7, 100)
    assert threshold_polynomial(r, s, F(1, 10)) < 0
    assert threshold_polynomial(r, s, F(1, 4)) > 0
    for m in range(15):
        s = normalized_palm_weight(m)
        assert s == F(1, m + 2)
        assert threshold_polynomial(F(m + 1), s, F(1, 17)) > 0
        assert threshold_polynomial(F(m + 1), s, F(51)) > 0
        for theta in (F(1, 17), F(2, 3), F(51)):
            expectation = F(factorial(m) * (m + 2), 2) / theta**m
            for n in range(8):
                palm = F(factorial(n + m), factorial(n)) * pnxl_mass(theta, n + m) / expectation
                mixture = mass_from_gamma_mix(F(m + 1), s, theta, n)
                assert palm == mixture
    print('PASS: rational mixture, coefficient, rate-frontier, thinning and Palm checks')


if __name__ == '__main__':
    test()
