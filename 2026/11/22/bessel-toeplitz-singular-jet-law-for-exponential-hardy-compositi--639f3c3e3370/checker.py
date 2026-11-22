"""Numerical corroboration of the singular-jet theorem; requires numpy and scipy."""
from math import factorial
import numpy as np
from scipy.special import iv


def truncated_iterate(A, q, size):
    """Compression of exp(A*(1-q)*z) f(q*z) in the Hardy monomial basis."""
    coefficients = np.array([float((A*(1-q))**k/factorial(k)) for k in range(size)])
    matrix = np.zeros((size, size))
    for k in range(size):
        matrix[k:, k] = (q**k) * coefficients[:size-k]
    return matrix


def determinants(A, max_rank):
    ds = [1.0]
    for j in range(1, max_rank+1):
        gram = np.array([[iv(i-k, 2*A) for k in range(j)] for i in range(j)])
        ds.append(float(np.linalg.det(gram)))
    return np.array(ds)


def run():
    assertions = 0
    for A in (0.35, 1.0, 1.6):
        ds = determinants(A, 6)
        assert np.all(ds > 0)
        constants = np.sqrt(ds[1:]/ds[:-1])
        assert np.all(constants > 1-1e-10)
        assert np.all(np.diff(constants) <= 1e-9)
        assertions += 3
        for q in (0.03, 0.015, 0.0075):
            n = 50
            matrix = truncated_iterate(A, q, n)
            singular = np.linalg.svd(matrix, compute_uv=False)
            for j in range(1, 5):
                ratio = singular[j-1]/q**(j-1)
                assert np.isclose(ratio, constants[j-1], rtol=0.05, atol=1e-6), (A, q, j, ratio, constants[j-1])
                assertions += 1
            # Compare the monomial matrix entries with a direct Hardy Taylor coefficient.
            for i, k in ((0, 0), (2, 0), (6, 2)):
                expected = (q**k)*(A*(1-q))**(i-k)/factorial(i-k)
                assert np.isclose(matrix[i, k], expected, atol=1e-14)
                assertions += 1
    print(f"PASS: {assertions} finite checks; these are not infinite-dimensional proofs")


if __name__ == '__main__':
    run()
