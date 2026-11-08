"""Reproducible numerical and exact-arithmetic checks for a Gaussian rowwise diagonal estimator.

The mathematical proof uses spherical symmetry, inverse-chi-square moments,
and a multivariate central limit theorem. Numerical checks are supplementary.
"""
import math
from fractions import Fraction
import numpy as np


def exact_variance(A, q):
    A = np.asarray(A, dtype=float)
    n = A.shape[0]
    off = A - np.diag(np.diag(A))
    return float(np.sum(off * off) / (q - 2) +
                 2 * sum(A[i, j] * A[j, i]
                         for i in range(n) for j in range(i + 1, n)) / q)


def symmetry_variance(A, q):
    A = np.asarray(A, dtype=float)
    off = A - np.diag(np.diag(A))
    symmetric = (off + off.T) / 2
    skew = (off - off.T) / 2
    return float(2 * (q - 1) / (q * (q - 2)) * np.sum(symmetric**2)
                 + 2 / (q * (q - 2)) * np.sum(skew**2))


def main():
    rng = np.random.default_rng(20261005)
    checks = 0
    for n in (2, 3, 5, 7):
        for q in (3, 4, 8, 15, 36):
            for _ in range(50):
                A = rng.normal(size=(n, n))
                G = rng.normal(size=(n, q))
                Z = A @ G
                coefficients = np.sum(Z * G, axis=1) / np.sum(G * G, axis=1)
                independent_formula = np.diag(A).copy()
                for i in range(n):
                    for j in range(n):
                        if j != i:
                            independent_formula[i] += A[i, j] * np.dot(G[i], G[j]) / np.dot(G[i], G[i])
                assert np.allclose(coefficients, independent_formula, rtol=1e-11, atol=1e-11)
                assert math.isclose(exact_variance(A, q), symmetry_variance(A, q), rel_tol=1e-11, abs_tol=1e-11)
                checks += 2
    for q in (3, 4, 7, 23, 51):
        for a, b in ((Fraction(1, 3), Fraction(2, 7)),
                     (Fraction(-2, 5), Fraction(4, 9)),
                     (Fraction(3, 2), Fraction(-3, 2))):
            # In dimension two the expected trace error is zero and its
            # exact variance is (a^2+b^2)/(q-2)+2ab/q.
            lhs = (a * a + b * b) / (q - 2) + 2 * a * b / q
            symmetric = (a + b) / 2
            skew = (a - b) / 2
            rhs = Fraction(4 * (q - 1), q * (q - 2)) * symmetric**2 + Fraction(4, q * (q - 2)) * skew**2
            assert lhs == rhs
            checks += 1
    for q in (30, 100):
        samples = 120000
        g = rng.normal(size=(samples, 2, q))
        X = np.sum(g[:, 0] * g[:, 1], axis=1)
        U = np.sum(g[:, 0]**2, axis=1)
        V = np.sum(g[:, 1]**2, axis=1)
        for a, b in ((1., 1.), (1., -1.), (1., -1. + 0.5 / math.sqrt(q))):
            values = X * (a / U + b / V)
            theory = (a*a + b*b) / (q - 2) + 2*a*b / q
            empirical = np.mean(values**2)
            assert abs(empirical/theory - 1) < 0.075, (q, a, b, empirical, theory)
            checks += 1
        del g, X, U, V
    print(f'PASS: {checks} reproducible supplementary identities / sample-moment checks')


if __name__ == '__main__':
    main()
