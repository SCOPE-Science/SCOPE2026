#!/usr/bin/env python3
"""Reproducible finite checks for normal-cone exposure in weighted staircase simplices.

Run: python3 verify_exposure.py
Requires Python 3, numpy, scipy.
These checks supplement (and do not replace) the all-dimensional proof.
"""
import math
import numpy as np
from scipy.special import gammaln


def index_from_increments(increments):
    return int(np.argmin(np.concatenate(([0.0], np.cumsum(increments)))))


def index_from_vertices(increments):
    n = len(increments)
    weights = np.arange(1, n + 1, dtype=float)  # these are only labels
    # Each vertex objective is suffix sum of increments; final zero is included.
    suffix = np.cumsum(increments[::-1])[::-1]
    return int(np.argmax(np.r_[suffix, 0.0]))


def empirical_exposure(n, alpha, reps, seed):
    rng = np.random.default_rng(seed)
    counts = np.zeros(n + 1, dtype=np.int64)
    weights = np.arange(1, n + 1, dtype=float) ** alpha
    batch = 250
    for i in range(0, reps, batch):
        m = min(batch, reps - i)
        increments = rng.standard_normal((m, n)) * weights
        cs = np.column_stack((np.zeros(m), np.cumsum(increments, axis=1)))
        idx = np.argmin(cs, axis=1)
        counts += np.bincount(idx, minlength=n + 1)
    return counts / reps


def arcsine_cdf(t):
    return 2 * np.arcsin(np.sqrt(t)) / np.pi


def analytic_n2(alpha):
    a, b = 1.0, 2.0 ** alpha
    den = math.hypot(a, b)
    p0 = 0.25 + math.asin(a / den) / (2 * math.pi)
    p1 = 0.25
    p2 = 0.25 + math.asin(b / den) / (2 * math.pi)
    assert abs(p0 + p1 + p2 - 1) < 1e-13
    return np.array((p0, p1, p2))


def main():
    rng = np.random.default_rng(15973)
    for n in range(2, 15):
        for _ in range(400):
            x = rng.standard_normal(n) * (np.arange(1, n + 1) ** rng.uniform(-1.8, 2.2))
            assert index_from_increments(x) == index_from_vertices(x)
    print('GEOMETRIC_SUFFIX_IDENTITY_PASS samples=5200')

    for alpha in (-1.1, -0.5, 0., 1., 2.):
        predicted = analytic_n2(alpha)
        empirical = empirical_exposure(2, alpha, 150000, seed=100)
        error = float(np.max(np.abs(predicted - empirical)))
        assert error < 0.006, (alpha, error)
        print(f'EXACT_N2_GAUSSIAN_PASS alpha={alpha} maxerr={error:.5f}')

    # Finite-dimensional Sparre Andersen (all i.i.d. continuous symmetric increments).
    n = 9
    u = np.array([math.comb(2 * k, k) / 4**k for k in range(n + 1)])
    probabilities = np.array([u[k] * u[n - k] for k in range(n + 1)])
    assert abs(sum(probabilities) - 1) < 1e-13
    observed = empirical_exposure(n, 0, 150000, seed=2026)
    assert np.max(np.abs(observed - probabilities)) < 0.008
    print('DISCRETE_ARCSINE_PASS n=9')

    # Macroscopic / logarithmic angular laws. No finite n check certifies a limit.
    n = 7000
    reps = 7000
    for alpha in (0., 1., -.5):
        masses = empirical_exposure(n, alpha, reps, seed=200 + int(100 * alpha))
        indices = np.arange(n + 1)
        if alpha == -.5:
            locations = np.log(indices + 1) / np.log(n)
            theoretical = arcsine_cdf
        else:
            locations = indices / n
            theoretical = lambda t, alpha=alpha: arcsine_cdf(t ** (2 * alpha + 1))
        errors = [abs(float(sum(masses[locations <= t])) - theoretical(t)) for t in (0.2, 0.5, 0.8)]
        print(f'ASYMPTOTIC_DIAGNOSTIC alpha={alpha} n={n} reps={reps} maxcdferr={max(errors):.5f}')
        assert max(errors) < (0.13 if alpha == -.5 else 0.045)

    # Subcritical finite index is a.s. eventually stable under the same infinite sequence.
    # This is a diagnostic, not a proof of almost-sure stabilization.
    n = 30000
    weights = np.arange(1, n + 1) ** (-1.4)
    r = np.random.default_rng(4410)
    pairs = []
    for _ in range(2000):
        x = weights * r.standard_normal(n)
        cs = np.r_[0., np.cumsum(x)]
        pairs.append((int(np.argmin(cs[:5001])), int(np.argmin(cs))))
    fraction = sum(a == b for a, b in pairs) / len(pairs)
    print(f'SUBCRITICAL_STABILITY_DIAGNOSTIC alpha=-1.4 n=5000,30000 agreement={fraction:.4f}')
    assert fraction > .98
    print('POWER_STAIRCASE_EXPOSURE_PASS')

if __name__ == '__main__':
    main()
