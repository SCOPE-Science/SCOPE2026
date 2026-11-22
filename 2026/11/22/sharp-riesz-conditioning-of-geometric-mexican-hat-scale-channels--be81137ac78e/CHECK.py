"""Reproducible supplementary checks of the all-dimensional Gaussian-scale Gram theorem.

Requirements: Python 3, NumPy and SciPy. Finite checks are not infinite proofs.
"""
import math
import numpy as np
from scipy.special import loggamma, gamma


def symbol_direct(nu, h, theta, count=240):
    k = np.arange(1, count + 1, dtype=float)
    coeff = np.cosh(np.minimum(k * h / 2, 700)) ** (-nu)
    return float(1 + 2 * np.dot(coeff, np.cos(k * theta)))


def symbol_gamma(nu, h, theta, count=25):
    a = nu / 2
    m = np.arange(-count, count + 1, dtype=float)
    z = a + 1j * (theta + 2 * np.pi * m) / h
    terms = np.exp(2 * np.real(loggamma(z)))
    return float((2 ** nu / (h * gamma(nu))) * terms.sum())


def asymptotic(nu, h):
    ga = gamma(nu / 2)
    gn = gamma(nu)
    B = 2 ** nu * ga ** 2 / (h * gn)
    A = 2 ** (nu + 2) * np.pi ** nu / gn * h ** (-nu) * np.exp(-np.pi ** 2 / h)
    return A, B


def run():
    tests = 0
    for d in (1, 2, 3, 4, 6):
        nu = (d + 4) / 2
        for h in (0.6, 1.0, 2.0):
            angles = np.linspace(0, np.pi, 21)
            seq = [symbol_gamma(nu, h, angle) for angle in angles]
            assert all(seq[i] > seq[i + 1] for i in range(len(seq) - 1))
            tests += 20
            for angle in (0.0, np.pi / 7, np.pi / 2, 5 * np.pi / 6, np.pi):
                direct = symbol_direct(nu, h, angle)
                period = symbol_gamma(nu, h, angle)
                assert abs(direct - period) <= 1e-8 * max(1.0, period), (d, h, angle, direct, period)
                tests += 1
            assert 0 < seq[-1] < seq[0]
            tests += 1
    for h in (0.6, 1.0, 2.0):
        bs = [symbol_gamma((d + 4) / 2, h, 0) for d in (1, 2, 3, 4, 6)]
        aa = [symbol_gamma((d + 4) / 2, h, np.pi) for d in (1, 2, 3, 4, 6)]
        assert all(bs[i] > bs[i+1] for i in range(4))
        assert all(aa[i] < aa[i+1] for i in range(4))
        tests += 8
    for d in (1, 2, 4):
        nu = (d + 4) / 2
        for h in (0.5, 0.35, 0.25):
            A, B = asymptotic(nu, h)
            a = symbol_gamma(nu, h, np.pi)
            b = symbol_gamma(nu, h, 0)
            assert abs(a / A - 1) < 0.08, (d, h, 'A', a, A)
            assert abs(b / B - 1) < 0.025, (d, h, 'B', b, B)
            tests += 2
    # Five principal-minor Gram eigenvalue sanity checks. No finite test replaces the proof.
    for d, h in ((1, 1.3), (2, 0.7), (2, 1.5), (4, 0.85), (6, 1.2)):
        nu = (d+4)/2
        idx = np.arange(21)
        dif = np.abs(idx[:, None] - idx[None, :]) * h/2
        gram = np.cosh(dif)**(-nu)
        eigen = np.linalg.eigvalsh(gram)
        assert eigen.min() > symbol_gamma(nu, h, np.pi) - 1e-10
        assert eigen.max() < symbol_gamma(nu, h, 0) + 1e-10
        tests += 2
    print('PASS:', tests, 'supplementary numerical assertions')


if __name__ == '__main__':
    run()
