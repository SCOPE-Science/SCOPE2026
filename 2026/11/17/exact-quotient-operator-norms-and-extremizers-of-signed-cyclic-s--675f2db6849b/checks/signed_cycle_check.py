"""Supplementary finite-dimensional numerical diagnostics for signed cyclic shifts.

Requires numpy. Floating-point checks are not proofs for all dimensions.
"""
from math import pi, sin, tan
import numpy as np


def signed_cycle(n, mu):
    a = np.zeros((n, n), dtype=float)
    for j in range(n):
        edge = mu if j == n - 1 else 1
        a[j, (j+1) % n] = edge
        a[(j+1) % n, j] = edge
    return a


def predicted(n, mu):
    if n % 2:
        return n * sin(pi / (2 * n))
    if mu == (-1) ** (n // 2):
        return (n / 2) * tan(pi / n)
    return (n / 2) * sin(pi / n)


def main():
    count = 0
    for n in range(3, 65):
        for mu in (-1, 1):
            a = signed_cycle(n, mu)
            d, v = np.linalg.eigh(a)
            signed = np.where(d > 1e-8, 1., np.where(d < -1e-8, -1., 0.))
            s = (v * signed) @ v.T
            tau = 2. * n / np.abs(d).sum()
            tau_theory = predicted(n, mu)
            assert abs(tau - tau_theory) < 5e-10
            count += 1
            b0 = tau_theory * s
            assert abs(np.linalg.norm(b0, 2) - tau_theory) < 5e-10
            count += 1
            for j in range(n):
                edge = mu if j == n - 1 else 1
                assert abs(b0[j, (j+1) % n] - edge) < 5e-10
                count += 1
            ker = v[:, abs(d) < 1e-8]
            singular = (n % 2 == 0 and mu == (-1) ** (n // 2))
            assert ker.shape[1] == (2 if singular else 0)
            count += 1
            if singular:
                p = ker @ ker.T
                pe = np.diag([j % 2 == 0 for j in range(n)])
                po = np.eye(n) - pe
                ue = np.dot(pe, p[:, 0]); uo = np.dot(po, p[:, 1])
                if np.linalg.norm(ue) < 1e-9 or np.linalg.norm(uo) < 1e-9:
                    ue = np.dot(pe, p[:, 1]); uo = np.dot(po, p[:, 0])
                u, z = ue / np.linalg.norm(ue), uo / np.linalg.norm(uo)
                assert np.linalg.norm(a @ u) < 1e-8
                assert np.linalg.norm(a @ z) < 1e-8
                count += 2
                for alpha, beta in ((-1.,-1.), (1.,1.), (0.,0.), (.37,-.63)):
                    alt = b0 + tau * (alpha * np.outer(u,u) + beta * np.outer(z,z))
                    assert abs(np.linalg.norm(alt,2)-tau) < 1e-8
                    assert max(abs(alt[j,(j+1)%n]-(mu if j==n-1 else 1)) for j in range(n)) < 1e-8
                    count += 2
    print('SIGNED_CYCLE_OPERATOR_QUOTIENT_DIAGNOSTICS_OK', count)


if __name__ == '__main__':
    main()
