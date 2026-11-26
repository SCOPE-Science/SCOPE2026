"""Independent finite-section normalization checks for a differential Hilbert operator.

This script tests finite identities; it does not prove asymptotic limits.
Requires NumPy and SciPy.
"""
from math import isclose, gamma, log
import numpy as np
from scipy.special import gammaln


def log_weight(gamma_parameter, indices):
    return (gammaln(gamma_parameter + 2) + gammaln(indices + 1)
            - gammaln(indices + gamma_parameter + 2))


def finite_hs(alpha, delta, size):
    n = np.arange(size, dtype=float)
    source_norm = np.exp(log_weight(alpha, n))
    target_norm = np.exp(log_weight(alpha + 2 + delta, n))
    coefficient = (n[:, None] + 1) / (n[:, None] + n[None, :] + 1)
    matrix = coefficient * np.sqrt(target_norm[:, None] / source_norm[None, :])
    return float(np.sum(matrix * matrix)), matrix


def main():
    for alpha in (-0.75, -0.5, -0.2):
        c0 = gamma(alpha + 4) * gamma(-alpha)
        assert c0 > 0
        data = []
        for n in (64, 128, 256, 512):
            s, mat = finite_hs(alpha, 0, n)
            assert np.all(np.isfinite(mat))
            assert abs(s - float(np.linalg.norm(mat, 'fro')**2)) < 1e-8 * s
            assert all(mat[i, j] > 0 for i, j in ((0, 0), (1, 2), (n - 1, n - 1)))
            # Independently evaluate the first and second matrix entries by monomial norms.
            assert isclose(mat[0, 0], 1.0, rel_tol=2e-13)
            expected = (2 / 4) * np.sqrt(np.exp(log_weight(alpha + 2, np.array([1.0]))[0]
                                                  - log_weight(alpha, np.array([2.0]))[0]))
            assert isclose(mat[1, 2], expected, rel_tol=2e-13)
            data.append((n, s))
        assert all(data[i][1] < data[i + 1][1] for i in range(3))
        # A nontrivial finite-cutoff test: increments are approaching the predicted log slope.
        slope = (data[-1][1] - data[-2][1]) / log(2)
        assert 0 < slope < c0
        for delta in (0.01, 0.06):
            v, _ = finite_hs(alpha, delta, 256)
            w, _ = finite_hs(alpha, 0, 256)
            assert 0 < v < w
        print('alpha=', alpha, 'critical_coefficient=', round(c0, 10),
              'finite_log_slope=', round(slope, 10), 'PASS')
    print('Finite normalization checks passed; no claim of numerical proof of limits.')

if __name__ == '__main__':
    main()
