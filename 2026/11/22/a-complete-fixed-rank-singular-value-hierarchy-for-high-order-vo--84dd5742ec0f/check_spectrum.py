"""Finite exact and numerical diagnostics for high-order Volterra singular spectra.

Requires Python 3, SymPy, NumPy, and SciPy. The analytical proof is in RESULT.md.
"""
import math
import numpy as np
import sympy as sp
from scipy.special import roots_laguerre


def exact_laguerre_determinant_checks():
    for rank in range(1, 9):
        gram = sp.Matrix([
            [sp.Rational(math.factorial(a+b), 2**(a+b+1))
             for b in range(rank)] for a in range(rank)
        ])
        expected = sp.Rational(
            math.prod(math.factorial(k)**2 for k in range(rank)),
            2**(rank*rank),
        )
        assert gram.det() == expected, (rank, gram.det(), expected)
    print("EXACT_GRAM_DETERMINANTS_OK")


def finite_singular_spectra():
    x, w = roots_laguerre(80)
    s = x[:, None] + x[None, :]
    for alpha in (80.0, 160.0, 320.0):
        h = np.maximum(1 - s / alpha, 0)**(alpha-1)
        matrix = np.sqrt(w[:, None] * w[None, :]) * np.exp(s/2) * h
        eigenvalues = np.linalg.eigvalsh(matrix)
        singular = np.sort(np.abs(eigenvalues))[::-1]
        for rank in range(1, 5):
            target = math.factorial(rank-1) / 2**(2*rank-1)
            scaled = singular[rank-1] * alpha**(rank-1)
            assert abs(scaled/target - 1) < 0.10, (alpha, rank, scaled, target)
        exact_mass = 1 / (4 - 2/alpha)
        numerical_mass = float(np.dot(singular, singular))
        assert abs(numerical_mass - exact_mass) < 2e-7, (alpha, numerical_mass, exact_mass)
    print("FINITE_NYSTROM_DIAGNOSTICS_OK")


if __name__ == "__main__":
    exact_laguerre_determinant_checks()
    finite_singular_spectra()
