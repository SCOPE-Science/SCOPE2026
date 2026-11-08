"""Independent numerical checks of the magnetic-cycle local-absorption theorem.

Requires Python 3, NumPy and SciPy. Numerical checks corroborate the
analytic Chebyshev and spectral-perturbation proofs; they do not prove them.
"""
import math
import numpy as np
from scipy.linalg import eigvals, expm
from scipy.special import eval_chebyt, eval_chebyu, i0


def hamiltonian(n, J, gamma, phi):
    H = np.zeros((n, n), dtype=np.complex128)
    phase = np.exp(1j * phi / n)
    for j in range(n):
        H[(j + 1) % n, j] += J * phase
        H[j, (j + 1) % n] += J * phase.conjugate()
    H[0, 0] -= 0.5j * gamma
    return H


def secular(n, J, gamma, phi, z):
    x = z / (2 * J)
    return (2 * J**n) * (eval_chebyt(n, x) - np.cos(phi)
                            + (1j * gamma / (4 * J)) * eval_chebyu(n - 1, x))


def scaled_survival(n, J, gamma, delta, tau):
    t = gamma * n * tau / (8 * J * J * delta * delta)
    v = expm(-1j * hamiltonian(n, J, gamma, np.pi + delta) * t)[:, n // 2]
    return float(np.vdot(v, v).real)


def finite_mixture(n, tau):
    theta = (2 * np.arange(n // 2) + 1) * np.pi / n
    return float((2 / n) * np.exp(-tau * np.sin(theta)**2).sum())


def main():
    checks = 0
    J, gamma = 1.2, 1.7
    for n in (4, 6, 8, 10):
        for phi in (0.25, 1.1, np.pi, np.pi + 0.22):
            z = 1.6 + 0.43j
            det = np.linalg.det(z * np.eye(n) - hamiltonian(n, J, gamma, phi))
            sec = secular(n, J, gamma, phi, z)
            assert abs(det - sec) <= 1e-8 * max(1, abs(sec)), (n, phi, det, sec)
            checks += 1
        for k in range(n // 2):
            theta = (2 * k + 1) * np.pi / n
            E = 2 * J * np.cos(theta)
            c = 4 * J * J / (gamma * n) * np.sin(theta)**2
            for delta in (0.005, 0.002):
                vals = eigvals(hamiltonian(n, J, gamma, np.pi + delta))
                close = vals[np.argmin(abs(vals - E))]
                ratio = -close.imag / delta**2
                assert abs(ratio - c) / c < 0.013, (n, k, delta, ratio, c)
                checks += 1
        for tau in (0.5, 1.3, 2.0):
            for delta in (0.025, 0.015):
                measured = scaled_survival(n, J, gamma, delta, tau)
                predicted = finite_mixture(n, tau)
                assert abs(measured - predicted) < 0.004, (n, tau, delta, measured, predicted)
                checks += 1
    for tau in (0.0, 0.2, 1.0, 2.0, 5.0, 8.0):
        limit = np.exp(-tau / 2) * i0(tau / 2)
        mid = finite_mixture(300, tau)
        assert abs(mid - limit) < 2e-13, (tau, mid, limit)
        checks += 1
    for tau in (20.0, 50.0, 100.0):
        lhs = np.exp(-tau / 2) * i0(tau / 2)
        rhs = 1 / np.sqrt(np.pi * tau)
        assert 0 < lhs / rhs - 1 < 0.015, (tau, lhs, rhs)
        checks += 1
    print('PASS: {} numerical identity/perturbation/survival/Bessel checks'.format(checks))


if __name__ == '__main__':
    main()
