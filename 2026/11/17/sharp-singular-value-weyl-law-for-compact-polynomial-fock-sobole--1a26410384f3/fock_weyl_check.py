"""Finite-section diagnostics for a Fock-space polynomial integral-sum example.
These tests are supplementary: the infinite-dimensional law is proved analytically.
"""
from math import sqrt, pi, factorial, isclose
import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigh_tridiagonal


def weights(k):
    """Column coefficients for I^3(z f+f') on the normalized monomial basis."""
    a = sqrt((k + 1) / ((k + 2) * (k + 3) * (k + 4)))
    b = 0.0 if k == 0 else 1.0 / sqrt((k + 1) * (k + 2))
    return a, b


def finite_section_singular_values(M):
    """Diagonalize T_M^* T_M, where T_M is the first M input columns."""
    k = np.arange(M, dtype=float)
    a = np.sqrt((k+1) / ((k+2)*(k+3)*(k+4)))
    b = 1 / np.sqrt((k+1)*(k+2))
    b[0] = 0.0
    eigenvalues = []
    for parity in (0, 1):
        idx = np.arange(parity, M, 2)
        diagonal = a[idx] ** 2 + b[idx] ** 2
        off_diagonal = a[idx[:-1]] * b[idx[1:]]
        eigenvalues.extend(eigh_tridiagonal(diagonal, off_diagonal,
                                           eigvals_only=True, check_finite=False))
    return np.sqrt(np.maximum(np.sort(eigenvalues)[::-1], 0.0))


def verify():
    checks = 0
    for k in range(1, 81):
        a, b = weights(k)
        # I^3 (z * z^k) and I^3 D(z^k), including monomial Hilbert norms.
        direct_a = sqrt(factorial(k + 4) / factorial(k)) / ((k+2)*(k+3)*(k+4))
        direct_b = k * sqrt(factorial(k+2) / factorial(k)) / (k*(k+1)*(k+2))
        assert isclose(a, direct_a, rel_tol=2e-13)
        assert isclose(b, direct_b, rel_tol=2e-13)
        checks += 2
    for M in (128, 256, 512, 1024):
        s = finite_section_singular_values(M)
        assert np.all(np.diff(s) <= 2e-13)
        checks += 1
        for j in (10, 30, 60, 100):
            assert 1.0 < j * s[j-1] < 4/pi
            checks += 1
    mean_abs = quad(lambda t: abs(1+np.exp(1j*t)), 0, 2*pi,
                    epsabs=1e-12)[0]/(2*pi)
    mean_abs_sq = quad(lambda t: abs(1+np.exp(1j*t))**2, 0, 2*pi,
                       epsabs=1e-12)[0]/(2*pi)
    assert isclose(mean_abs, 4/pi, rel_tol=3e-13)
    assert isclose(mean_abs_sq, 2, rel_tol=3e-13)
    checks += 2
    print('FOCK_POLYNOMIAL_SUM_DIAGNOSTICS_OK', checks)
    print('critical angular coefficient:', repr(mean_abs))
    print('finite sections: rank-100 scaled singular value:',
          [(M, float(100*finite_section_singular_values(M)[99]))
           for M in (128, 256, 512, 1024)])


if __name__ == '__main__':
    verify()
