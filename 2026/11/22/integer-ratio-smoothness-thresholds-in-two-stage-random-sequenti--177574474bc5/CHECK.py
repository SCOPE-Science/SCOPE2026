"""Numerical checks for a two-stage, long-first random sequential adsorption law.

Dependencies: Python 3, numpy, scipy. All calculations are finite or quadrature
checks and do not substitute for the analytic limit and jump proofs.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import exp1
from numpy.polynomial.legendre import leggauss

EULER = 0.5772156649015328606065120900824024


def envelope(z):
    if z == 0:
        return 1.0
    return math.exp(-2 * (EULER + math.log(z) + float(exp1(z))))


def count(y):
    if y < 1:
        return 0.0
    if y <= 2:
        return 1.0
    if y <= 3:
        return 1 + 2 * (y - 2) / (y - 1)
    if y <= 4:
        return 1 + (6 * y - 16 - 4 * math.log(y - 2)) / (y - 1)
    raise ValueError('For this diagnostic, use ratios at most four.')


def spectral(a):
    return quad(lambda z: z * math.exp(-a * z) * envelope(z),
                0, 130, epsabs=2e-11, epsrel=2e-11)[0]


renyi = quad(envelope, 0, math.inf, epsabs=2e-11, epsrel=2e-11)[0]
I = spectral(1)


def continuum(L):
    breaks = [1] + [i for i in (2, 3) if i < L] + [L]
    return renyi + sum(
        quad(lambda y: 2 * count(y) * spectral(y / L) / L ** 2,
             a, b, epsabs=1e-10)[0]
        for a, b in zip(breaks[:-1], breaks[1:])
    )


def old_formula(L):
    return renyi + 2 / L * quad(
        lambda z: (math.exp(-z / L) - math.exp(-z)) * envelope(z),
        0, 130, epsabs=2e-11)[0]


def discrete(k, L):
    K = math.floor(k * L)
    means = [0.0] * K
    partial = [0.0] * (K + 1)
    for length in range(k, K):
        means[length] = k + 2 * partial[length - k + 1] / (length - k + 1)
        partial[length + 1] = partial[length] + means[length]
    x, wt = leggauss(450)
    z = (x + 1) * K / 2
    dz = wt * K / 2
    s = 1 - z / K
    H = np.exp(-2 * sum((1 - s ** j) / j for j in range(1, K)))
    first = np.dot(dz, H)
    common = 2 / K ** 2 * dz * z * H
    gaps = [np.dot(common, s ** ell) for ell in range(k, K)]
    return first + np.dot(gaps, means[k:K])


def main():
    print('Renyi constant', renyi)
    print('Universal jump integral I', I)
    assert abs(renyi - 0.7475979202533) < 5e-10
    for L in (1.2, 1.5, 2):
        actual = continuum(L)
        assert abs(actual - old_formula(L)) < 1e-9, (L, actual)
    expected = {2: 0.852335031343, 2.5: 0.866054359924,
                3: 0.877826189789, 4: 0.891477464702}
    for L, value in expected.items():
        result = continuum(L)
        print('ratio', L, 'coverage', result)
        assert abs(result - value) < 2e-8
    for L in (2.5, 3):
        errors = [abs(discrete(k, L) - continuum(L)) for k in (8, 16, 32, 64)]
        print('finite-rod convergence at', L, 'errors', errors)
        assert all(errors[i + 1] < errors[i] for i in range(3))
    for m in (2, 3, 4):
        print('predicted order', m, 'derivative jump',
              2 ** m * I / (m * m * math.factorial(m - 1)))
    for delta in (0.03, 0.01, 0.003):
        ratio = (continuum(2 + delta) - old_formula(2 + delta)) / delta ** 2
        print('first threshold ratio', delta, ratio)
        assert abs(ratio - I / 2) < 0.006
    print('ALL FINITE DIAGNOSTIC CHECKS PASSED')


if __name__ == '__main__':
    main()
