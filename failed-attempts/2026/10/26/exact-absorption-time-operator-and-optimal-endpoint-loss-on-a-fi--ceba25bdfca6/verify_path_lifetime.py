"""Standalone finite-size checks for the exact absorbing-time operator of a lossy path.
Run: python verify_path_lifetime.py
Dependencies: numpy, scipy, sympy.
Finite tests complement, but do not replace, the dimension-free Lyapunov proof.
"""
from fractions import Fraction
import json
import math
import numpy as np
import sympy as sp
from scipy.linalg import solve_continuous_lyapunov


def proposed(n, gamma, imaginary=1j):
    """Exact formula for Q = integral exp(A^*t)exp(At)dt (1-based indices)."""
    q = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            a, b = i + 1, j + 1
            z = sp.Rational(n-b+1, 2) * (
                (a-1)*gamma + a/gamma if (b-a)%2 == 0 else imaginary
            )
            q[i][j] = z
            q[j][i] = z if i == j else sp.conjugate(z)
    return sp.Matrix(q)


def exact_checks():
    count = 0
    # Explicit rational identities in the non-Hermitian Lyapunov equation.
    for n in range(2, 17):
        H = sp.zeros(n)
        for k in range(n - 1):
            H[k, k + 1] = H[k + 1, k] = 1
        P = sp.zeros(n)
        P[0, 0] = 1
        for numerator, denominator in [(1,3), (2,5), (1,1), (3,2), (7,3)]:
            g = sp.Rational(numerator, denominator)
            Q = proposed(n, g, sp.I)
            residue = g*(P*Q+Q*P)-sp.I*(H*Q-Q*H)-sp.eye(n)
            assert not any(v != 0 for v in residue), (n, g)
            count += n*n
    return count


def independent_checks():
    count = 0
    max_error = 0.0
    for n in range(2, 24):
        H = np.diag(np.ones(n-1), 1) + np.diag(np.ones(n-1), -1)
        for gamma in (0.25, 0.5, 1., 1.4, 3.):
            A = -1j*H
            A = A.copy()
            A[0,0] -= gamma
            target = solve_continuous_lyapunov(A.conj().T, -np.eye(n))
            calculated = np.asarray(proposed(n, sp.Rational(str(gamma))), dtype=np.complex128)
            error = float(np.max(np.abs(target-calculated)))
            max_error = max(max_error, error)
            assert np.allclose(target, calculated, rtol=2e-9, atol=2e-9), (n, gamma, error)
            assert np.max(np.real(np.linalg.eigvals(A))) < -1e-13
            for a in range(1, n+1):
                expected = (n-a+1)/2 * ((a-1)*gamma + a/gamma)
                assert abs(target[a-1, a-1].real-expected) < 2e-9 * max(1., abs(expected))
                count += 1
    return count, max_error

if __name__ == '__main__':
    exact = exact_checks()
    independent, maximum = independent_checks()
    report = {'exact_matrix_entry_checks': exact,
              'independent_diagonal_checks': independent,
              'independent_matrix_cases': 22*5,
              'largest_absolute_matrix_difference': maximum,
              'status': 'passed',
              'scope': 'finite numerical comparisons and exact rational Lyapunov residuals, not a substitute for the analytical all-length proof'}
    with open('verification_report.json', 'w', encoding='utf-8') as fp:
        json.dump(report, fp, ensure_ascii=False, indent=2)
        fp.write('\n')
    print(json.dumps(report, indent=2))
