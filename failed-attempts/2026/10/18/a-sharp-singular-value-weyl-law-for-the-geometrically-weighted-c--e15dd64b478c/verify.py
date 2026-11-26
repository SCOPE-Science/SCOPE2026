"""Numerical checks for the singular-value law of geometric Cesaro matrices.

Requirements: Python 3 and NumPy. The theorem's proof is analytic; these
finite-dimensional checks are independent diagnostics, not an infinite proof.
"""

import math
import numpy as np


def predicted_coefficient(t, grid_size=32768):
    angles = (2.0 * math.pi / grid_size) * np.arange(grid_size)
    return float(np.mean(1.0 / np.abs(1.0 - t * np.exp(1.0j * angles))))


def finite_section(t, dimension):
    index = np.arange(dimension)
    diff = index[:, None] - index[None, :]
    # Negative differences are masked before raising powers.
    return np.where(diff >= 0, t ** np.maximum(diff, 0) / (index[:, None] + 1), 0.0)


def run():
    count = 0
    for t in (0.4, 0.7):
        coef = predicted_coefficient(t)
        assert coef > 1.0
        count += 1
        a = finite_section(t, 320)
        assert np.all(np.diag(a) == 1.0 / np.arange(1, 321))
        count += 1
        singular = np.linalg.svd(a, compute_uv=False)
        assert np.all(np.diff(singular) <= 1.0e-12)
        count += 1
        for n in (40, 60, 80, 100):
            ratio = n * singular[n - 1] / coef
            assert abs(ratio - 1.0) < 0.001, (t, n, ratio, coef)
            count += 1
        print(f"t={t:.1f}, coefficient={coef:.12f}, 100*s_100={100*singular[99]:.12f}")
    assert abs(predicted_coefficient(0.0) - 1.0) < 1.0e-14
    count += 1
    print(f"PASS: {count} deterministic checks. Finite tests do not prove the infinite limit.")


if __name__ == "__main__":
    run()
