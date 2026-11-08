#!/usr/bin/env python3
"""Independent finite-matrix checks of the stated finite-chain renewal formulas.

Requires numpy and scipy. This checks finite examples, not asymptotic or
all-parameter theorem statements.
"""
import math
import numpy as np
from scipy.linalg import eigh
from scipy.special import roots_legendre, zeta

# Integrate a bounded (possibly weakly endpoint-nonsmooth) physical-time correction.
N_QUAD = 360
nodes, weights = roots_legendre(N_QUAD)
nodes = (nodes + 1.0) / 2.0
weights = weights / 2.0


def spectral_function(alpha, tau, s):
    s = np.asarray(s, dtype=float)
    a = (tau * s) ** alpha
    correction = ((1 - nodes[None, :] ** alpha) /
                  (1 + a[:, None] * nodes[None, :] ** alpha)) @ weights
    return tau / a + tau * correction


def exact_from_explicit_modes(length, start, alpha, tau):
    theta = (2 * np.arange(length) + 1) * np.pi / (2 * length + 1)
    eig = 1 - np.cos(theta)
    coeff = 2.0 / (2 * length + 1) * np.sin(start * theta) / np.tan(theta / 2)
    return float(coeff @ spectral_function(alpha, tau, eig))


def exact_from_matrix(length, alpha, tau):
    A = np.diag(np.ones(length))
    A[-1, -1] = 0.5
    for i in range(length - 1):
        A[i, i + 1] = A[i + 1, i] = -0.5
    eig, modes = eigh(A)
    return modes @ (spectral_function(alpha, tau, eig) * (modes.T @ np.ones(length)))


def leading_constant(alpha):
    return (2 ** (3 * alpha + 1) / np.pi ** (2 * alpha)
            * (1 - 2 ** (-2 * alpha)) * zeta(2 * alpha, 1))


def close(a, b, atol=4e-9):
    if not math.isclose(float(a), float(b), rel_tol=4e-10, abs_tol=atol):
        raise AssertionError((a, b))


def run():
    comparisons = 0
    # Direct diagonalization of the finite absorbing/reflecting generator
    # versus the analytic sine/cotangent eigenexpansion, for every site.
    for length in range(1, 12):
        for alpha in (0.2, 0.5, 0.8, 1.0):
            for tau in (0.3, 1.0, 2.1):
                direct = exact_from_matrix(length, alpha, tau)
                for start in range(1, length + 1):
                    close(direct[start - 1], exact_from_explicit_modes(length, start, alpha, tau))
                    comparisons += 1
    # Nonnegative, uniformly bounded exact correction for the finite generator.
    for length in (1, 3, 9, 25):
        for alpha in (0.15, 0.55, 0.95, 1.0):
            tau = 1.3
            A = np.diag(np.ones(length))
            A[-1, -1] = 0.5
            for i in range(length - 1):
                A[i, i + 1] = A[i + 1, i] = -0.5
            eig, vec = eigh(A)
            f = spectral_function(alpha, tau, eig)
            corr_s = f - tau ** (1 - alpha) * eig ** (-alpha)
            corr = vec @ (corr_s * (vec.T @ np.ones(length)))
            assert np.min(corr) > -1e-8
            assert np.max(corr) <= tau * alpha / (1 + alpha) + 1e-8
            comparisons += length
    # Large-volume predictions, a convergence test, NOT a proof.
    for alpha in (0.65, 0.8, 1.0):
        N = 12000
        val = exact_from_explicit_modes(N, 2, alpha, 1.0)
        ratio = val / (2 * leading_constant(alpha) * N ** (2 * alpha - 1))
        assert abs(ratio - 1) < (0.14 if alpha == 0.65 else 0.04), (alpha, ratio)
        comparisons += 1
    N = 12000
    val = exact_from_explicit_modes(N, 2, 0.5, 1.0)
    ratio = val / ((4 * np.sqrt(2) / np.pi) * np.log(N))
    assert 1.0 < ratio < 1.11, ratio
    comparisons += 1
    # Critical-window comparison: its finite-size error is O(1/log N).
    N = 30000
    for u in (-0.7, 0.0, 0.7):
        alpha = 0.5 + u / np.log(N)
        val = exact_from_explicit_modes(N, 1, alpha, 1.0)
        scaled = val / ((2 * np.sqrt(2) / np.pi) * np.log(N))
        target = np.expm1(2 * u) / (2 * u) if u else 1.0
        assert abs(scaled - target) < 0.55, (u, scaled, target)
        comparisons += 1
    print('PASS: {} finite-matrix, correction and asymptotic numerical checks'.format(comparisons))

if __name__ == '__main__':
    run()
