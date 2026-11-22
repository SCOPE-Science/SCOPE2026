"""Reproduce exact cosine-profile coefficients and independent Galerkin evidence.

Run: python check.py
Requires numpy and scipy. Numerical eigenvalue checks are supplementary;
the infinite-dimensional assertion follows from the proof in RESULT.md.
"""
from fractions import Fraction as F
from math import pi
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.linalg import eigh


def exact_coefficients(b, c):
    """For beta=1+eps*b*cos(x)-c*eps**2, gamma=1+eps*cos(x)."""
    f = (b - 1)**2 - c
    p = f + (b - 1) / F(4)
    return f, p


def spectral_reproduction_numbers(eps, b, c, degree=14, quadrature=96):
    """Independent Neumann cosine-Galerkin variational eigensolvers.

    Fick: A=integral(g grad(v)grad(w)+gamma vw), B=integral(beta vw)
    Fokker-Planck after Psi=g I:
       A=integral(grad(v)grad(w)+(gamma/g)vw),
       B=integral((beta/g)vw).
    """
    abscissae, weights = leggauss(quadrature)
    x = (abscissae + 1) * (pi / 2)
    weights = weights * (pi / 2)
    n = np.arange(degree + 1)[:, None]
    V = np.cos(n * x)
    D = -n * np.sin(n * x)
    gamma = 1 + eps * np.cos(x)
    beta = 1 - float(c) * eps**2 + float(b) * eps * np.cos(x)
    g = 1 / (1 + gamma)
    A_f = (D * (weights * g)) @ D.T + (V * (weights * gamma)) @ V.T
    B_f = (V * (weights * beta)) @ V.T
    A_p = (D * weights) @ D.T + (V * (weights * gamma / g)) @ V.T
    B_p = (V * (weights * beta / g)) @ V.T
    eig_f = eigh(A_f, B_f, eigvals_only=True, subset_by_index=(0, 0))[0]
    eig_p = eigh(A_p, B_p, eigvals_only=True, subset_by_index=(0, 0))[0]
    return 1 / eig_f, 1 / eig_p


def main():
    pairs = [
        (F(2), F(9, 8), F(-1, 8), F(1, 8)),
        (F(0), F(7, 8), F(1, 8), F(-1, 8)),
    ]
    print('Exact rational order-two coefficients:')
    for b, c, expected_f, expected_p in pairs:
        cf, cp = exact_coefficients(b, c)
        assert (cf, cp) == (expected_f, expected_p)
        print(f'  b={b}, c={c}: Fick={cf}, Fokker-Planck={cp}')
        for eps in [0.05, 0.02, 0.01]:
            rf, rp = spectral_reproduction_numbers(eps, b, c)
            assert (rf - 1) * float(cf) > 0
            assert (rp - 1) * float(cp) > 0
            assert abs((rf - 1) / eps**2 - float(cf)) < 3 * eps
            assert abs((rp - 1) / eps**2 - float(cp)) < 3 * eps
            print(f'    eps={eps:.3g}: RF={rf:.12f}, RP={rp:.12f}')
    print('PASS: exact coefficients, both sign-reversing threshold families, and spectral convergence checks')


if __name__ == '__main__':
    main()
