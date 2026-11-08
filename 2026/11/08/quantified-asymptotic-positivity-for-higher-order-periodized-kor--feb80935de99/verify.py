"""Distinct implementations of Fourier-alias and Gram-solve formulas for a periodic weighted quadrature rule.

Requires only Python 3 and numpy. These finite diagnostics check formulas and
scales; they are not a substitute for the all-N proof.
"""
import math
import numpy as np


def density(y):
    return np.pi / 2 * np.abs(np.sin(2 * np.pi * y))


def fourier_density(h):
    h = np.asarray(h, dtype=np.int64)
    z = np.zeros(h.shape, dtype=np.float64)
    z[h == 0] = 1.0
    e = (h != 0) & (h % 2 == 0)
    z[e] = -1.0 / (h[e].astype(np.float64) ** 2 - 1.0)
    return z


def fourier_kernel(h, alpha, gamma):
    h = np.asarray(h, dtype=np.int64)
    z = np.ones(h.shape, dtype=np.float64)
    e = h != 0
    z[e] = gamma * np.abs(h[e].astype(np.float64)) ** (-2.0 * alpha)
    return z


def alias_weights(n, alpha, gamma, periods=400):
    h = np.arange(-periods * n, periods * n + 1, dtype=np.int64)
    a = fourier_kernel(h, alpha, gamma)
    b = a * fourier_density(h)
    aa = np.bincount(h % n, weights=a, minlength=n)
    bb = np.bincount(h % n, weights=b, minlength=n)
    weights = np.fft.ifft(bb / aa).real
    return weights, aa, bb


def direct_weights(n, alpha, gamma, periods=400):
    h = np.arange(-periods * n, periods * n + 1, dtype=np.int64)
    a = fourier_kernel(h, alpha, gamma)
    m = fourier_density(h)
    # For integer alpha, the two Fourier sums converge absolutely.
    j = np.arange(n)
    phases = np.exp(2j * np.pi * np.outer(j, h) / n)
    kernel = (phases * a).dot(phases.conj().T).real
    rhs = (phases * (a * m)).sum(axis=1).real
    return np.linalg.solve(kernel, rhs)


def main():
    comparisons = 0
    for alpha in [2, 3, 4]:
        for gamma in [0.05, 1.0, 30.0, 1000.0]:
            for n in [5, 7, 12, 19]:
                w, a, b = alias_weights(n, alpha, gamma)
                v = direct_weights(n, alpha, gamma)
                assert np.max(np.abs(w - v)) < 2e-7, (n, alpha, gamma)
                assert abs(np.sum(w) - b[0] / a[0]) < 2e-10
                comparisons += 2
    for alpha in [2, 3, 4]:
        for gamma in [0.1, 1.0, 100.0]:
            scaled_errors = []
            negative_masses = []
            mass_errors = []
            for n in [32, 64, 128, 256]:
                w, _, _ = alias_weights(n, alpha, gamma)
                y = np.arange(n) / n
                scaled_errors.append(n * n * np.max(np.abs(w - density(y) / n)))
                negative_masses.append(n * n * (-np.sum(w[w < 0])))
                mass_errors.append(n ** (2 * alpha) * (1.0 - np.sum(w)))
                assert scaled_errors[-1] < 50000
                assert negative_masses[-1] < 50000
                comparisons += 2
            assert max(scaled_errors) < 10 * max(1, min(scaled_errors))
            if alpha == 2 and gamma < 2.0:
                target = 2 * gamma * sum(1.0 / k ** (2 * alpha) for k in range(1, 10000))
                assert abs(mass_errors[-1] / target - 1) < 0.02, (mass_errors, target)
                comparisons += 1
    # The limiting-kernel obstruction: fixed even grids, large gamma.
    for alpha in [2, 3, 4]:
        for n in [2, 4, 6, 8]:
            w, _, _ = alias_weights(n, alpha, 1e9)
            assert w[0] < -1e-5, (n, alpha, w[0])
            comparisons += 1
    # Test exact Fourier formula directly via high-resolution quadrature.
    x = np.arange(32768) / 32768
    fx = density(x)
    for h in range(-50, 51):
        value = np.mean(fx * np.exp(-2j * np.pi * h * x))
        expected = fourier_density(np.array([h]))[0]
        assert abs(value - expected) < 3e-8, (h, value, expected)
        comparisons += 1
    print('PASS:', comparisons, 'finite diagnostics')


if __name__ == '__main__':
    main()
