"""Reproducible checks for a scalar noisy Anderson projection benchmark.

This script verifies algebraic identities and numerical consequences; it is not
an external proof or an independent scientific audit.
"""
from fractions import Fraction as F
import math


def q(lam, v, d):
    return (lam * lam + 2 * v * d * d) / (d * d + lam)**2


def qprime(lam, v, d):
    return 2 * d * d * (lam - 2 * v) / (d * d + lam)**3


def qprime_direct(lam, v, d):
    D = d * d + lam
    return 2 * lam / (D * D) - 2 * (lam * lam + 2 * v * d * d) / D**3


def project_error(a, lam, D, M):
    Rplus = M + D / 2
    return a - 2 * a * D * Rplus / (D * D + lam)


def normal_expectation(func, mean, variance):
    # Deterministic trapezoidal quadrature on a symmetric, 13-SD normal grid.
    sd = math.sqrt(variance)
    N = 20000
    low, high = -13., 13.
    h = (high - low) / N
    total = 0.0
    for j in range(N + 1):
        z = low + h * j
        weight = 0.5 if j in (0, N) else 1.0
        total += weight * math.exp(-z*z/2) / math.sqrt(2*math.pi) * func(mean + sd*z)
    return total*h


def main():
    checks = 0
    for a_n in (1, 2, 5):
        for v_n in (1, 2, 7):
            for lam_n in (1, 3, 5):
                for d_n in (-4, -1, 0, 2, 7):
                    a, v, lam, d = map(F, (a_n, v_n, lam_n, d_n))
                    for M_n in (-3, 0, 2):
                        M = F(M_n)
                        left = project_error(a, lam, d, M)
                        right = a*lam/(d*d+lam)-2*a*M*d/(d*d+lam)
                        assert left == right
                        checks += 1
                    assert qprime(lam, v, d) == qprime_direct(lam, v, d)
                    assert q(2*v, v, d) == 2*v/(d*d+2*v)
                    checks += 2
    for a, c, sig in ((1.0, 0.5, 0.5), (2.0, -1.2, 0.7), (0.8, 2.0, 1.0)):
        mu, v = 2*c*a, sig**2
        def risk(lam):
            return a*a * normal_expectation(lambda D: q(lam, v, D),mu,2*v)
        rm = risk(2*v)
        assert risk(v) > rm and risk(3*v) > rm
        assert abs(rm-2*a*a*v*normal_expectation(lambda D: 1/(D*D+2*v),mu,2*v)) < 1e-10
        checks += 3
    print('VERIFY_OK', checks, 'exact identities and 3 quadrature cases')


if __name__ == '__main__':
    main()
