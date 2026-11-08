"""Reproducible algebra and finite spectral checks for symmetric sunlet chains.

Run: python verify.py
Requires: numpy and sympy. Finite tests supplement the written proof.
"""
import math
import random

import numpy as np
import sympy as sp


def formulas(m):
    z = math.sqrt(2) * math.sin(math.pi / m)
    d = z * z + 2 * z + 2
    return z, (z + 2) / (2 * d), z * (z + 1) / d, 2 * (z + 1) / d


def matrix(m, a, b):
    p = np.zeros((2*m, 2*m))
    for i in range(m):
        j = (i + 1) % m
        p[i, j] = p[j, i] = a
        p[i, m+i] = p[m+i, i] = b
        p[i, i] = 1 - 2*a - b
        p[m+i, m+i] = 1 - b
    return p


def mode_eigenvalues(m, a, b):
    eig = []
    for k in range(m):
        ell = 2 * (1 - math.cos(2 * math.pi * k / m))
        rad = math.sqrt(b*b + a*a*ell*ell/4)
        eig.extend([1-b-a*ell/2-rad, 1-b-a*ell/2+rad])
    return sorted(eig)


def audit():
    z = sp.symbols('z', positive=True)
    d = z*z + 2*z + 2
    a = (z + 2) / (2*d)
    b = z * (z + 1) / d
    rho = 2 * (z + 1) / d
    identities = [
        1-2*a-b,
        b*b + a*a*z**4 - z*z/4,
        rho - (1-b-a*z*z+z/2),
        (2-z*z) + (-2*(1-2*a)+a*z**4)/(z/2),
        rho**2 - (b*b+4*a*a) - z*(z+2)*(2-z*z)/d**2,
        rho - (1-2*b) - z*(z+2)/d,
        1-rho - z*z/d,
    ]
    for expression in identities:
        assert sp.factor(expression) == 0, str(expression)

    rng = random.Random(260711)
    checked = 0
    perturbations = 0
    for m in list(range(3, 41)) + [48, 64, 100]:
        zv, av, bv, optimum = formulas(m)
        assert 2*av + bv <= 1 + 2e-14
        p = matrix(m, av, bv)
        assert np.min(p) >= -2e-14
        assert np.max(abs(p.sum(axis=1)-1)) < 3e-14
        actual = sorted(float(e) for e in np.linalg.eigvalsh(p))
        expected = mode_eigenvalues(m, av, bv)
        assert max(abs(u-v) for u, v in zip(actual, expected)) < 3e-12
        assert abs(max(abs(e) for e in actual[:-1])-optimum) < 2e-12
        checked += 1
        for _ in range(80):
            a0 = rng.random() / 2
            b0 = rng.random() * (1 - 2*a0)
            e = mode_eigenvalues(m, a0, b0)
            mu = max(abs(v) for v in e[:-1])
            assert mu >= optimum - 1e-11
            perturbations += 1
    unrestricted_samples = 0
    for m in range(3, 17):
        _, optimal_a, optimal_b, optimum = formulas(m)
        for _ in range(55):
            a_edges = [optimal_a * (0.64 + 0.36*rng.random()) for _ in range(m)]
            b_edges = [optimal_b * (0.64 + 0.36*rng.random()) for _ in range(m)]
            p = np.zeros((2*m, 2*m))
            for i in range(m):
                j = (i + 1) % m
                p[i, j] = p[j, i] = a_edges[i]
                p[i, m+i] = p[m+i, i] = b_edges[i]
            for i in range(m):
                p[i, i] = 1 - a_edges[i] - a_edges[(i-1)%m] - b_edges[i]
                p[m+i, m+i] = 1 - b_edges[i]
            assert np.min(p) >= -1e-13
            assert np.max(abs(p.sum(axis=1)-1)) < 3e-14
            eigs = np.linalg.eigvalsh(p - np.ones_like(p)/(2*m))
            mu = max(abs(e) for e in eigs)
            assert mu >= optimum - 1e-11
            unrestricted_samples += 1
    assert checked == 41
    assert perturbations == 3280
    assert unrestricted_samples == 770
    assert abs(formulas(4)[1]-0.3) < 1e-15
    assert abs(formulas(4)[2]-0.4) < 1e-15
    assert abs(formulas(4)[3]-0.8) < 1e-15
    print(f'PASS: 7 exact symbolic identities, {checked} actual matrix spectra, '
          f'{perturbations} feasible invariant perturbations, '
          f'{unrestricted_samples} feasible noninvariant matrices.')


if __name__ == '__main__':
    audit()
