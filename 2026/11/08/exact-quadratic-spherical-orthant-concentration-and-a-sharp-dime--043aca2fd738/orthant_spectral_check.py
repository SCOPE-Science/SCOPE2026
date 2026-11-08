#!/usr/bin/env python3
"""Independent moment-matrix verification for quadratic harmonics on a spherical orthant.

Requires Python 3 and NumPy. No remote data or unpublished resources are needed.
"""
import math
import itertools
import numpy as np


def monomial_moment_scaled(exponents):
    """Return d(d+2) E[prod X_j**a_j | X_j >= 0], total degree four."""
    assert sum(exponents) == 4
    return 4.0 * math.prod(math.gamma((a + 1) / 2) / math.sqrt(math.pi) for a in exponents)


def quadratic_basis(d):
    out = []
    for k in range(1, d):
        u = np.zeros(d)
        u[:k] = 1 / math.sqrt(k * (k + 1))
        u[k] = -k / math.sqrt(k * (k + 1))
        poly = []
        for i in range(d):
            a = [0] * d
            a[i] = 2
            if u[i]:
                poly.append((tuple(a), float(u[i] / math.sqrt(2))))
        out.append(poly)
    for i, j in itertools.combinations(range(d), 2):
        a = [0] * d
        a[i] = a[j] = 1
        out.append([(tuple(a), 1.0)])
    return out


def spectrum_from_direct_moments(d):
    bas = quadratic_basis(d)
    C = np.empty((len(bas), len(bas)))
    for i, pi in enumerate(bas):
        for j, pj in enumerate(bas[: i + 1]):
            value = 0.0
            for ei, ci in pi:
                for ej, cj in pj:
                    value += ci * cj * monomial_moment_scaled([a + b for a, b in zip(ei, ej)])
            C[i, j] = C[j, i] = value
    return np.linalg.eigvalsh(C), C


def stated_spectrum(d, expand=True):
    a = 2 / math.pi
    alpha = (1 - a) ** 2
    beta = a * (1 - a)
    gamma = a * a
    s = math.sqrt((a * a / 2) * (d - 2))
    M = np.array([[1.0, s], [s, alpha + beta * (d - 2)]])
    lo, hi = np.linalg.eigvalsh(M)
    simple = alpha + 2 * beta * (d - 1) + gamma * d * (d - 1) / 2
    if not expand:
        return None, (simple, hi, lo, alpha)
    return np.sort([simple] + [hi] * (d - 1) + [lo] * (d - 1) + [alpha] * (d * (d - 3) // 2)), (simple, hi, lo, alpha)


def main():
    checks = 0
    for d in range(3, 13):
        eigen, matrix = spectrum_from_direct_moments(d)
        expected, (simple, hi, lo, alpha) = stated_spectrum(d)
        assert eigen.shape == expected.shape
        checks += 1
        for observed, predicted in zip(eigen, expected):
            assert abs(observed - predicted) < 1e-11, (d, observed, predicted)
            checks += 1
        assert abs(np.trace(matrix) - len(eigen)) < 1e-11
        checks += 1
        assert 0 < lo < hi < simple
        checks += 1
        if d >= 4:
            assert lo < alpha < hi
            checks += 1
    for d in [20, 30, 100, 1000, 10000, 100000]:
        _, (simple, hi, lo, alpha) = stated_spectrum(d, expand=False)
        assert 0 < lo < alpha < hi < simple
        checks += 1
    target = 2 * (math.pi - 2) / (math.pi ** 2 * (math.pi - 3))
    for d in [100, 1000, 10000, 100000]:
        _, (simple, _, lo, _) = stated_spectrum(d, expand=False)
        ratio = (simple / lo) / d ** 2
        assert abs(ratio / target - 1) < 6 / d
        checks += 1
    print('ORTHANT_HARMONIC_SPECTRUM_CHECKS_PASS', checks)


if __name__ == '__main__':
    main()
