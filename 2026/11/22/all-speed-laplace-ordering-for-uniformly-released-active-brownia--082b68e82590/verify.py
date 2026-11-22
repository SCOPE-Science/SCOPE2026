"""Deterministic numerical checks for the discounted active-escape Stieltjes law.

The proof is analytic; these tests diagnose sign, scaling and normalization.
Run: python verify.py  (requires numpy, scipy, mpmath)
"""
import math
import numpy as np
from scipy.linalg import eigh, solve
from mpmath import mp


def operators(nx=8, nt=12, D=1.3, Dr=0.45, L=1.0):
    h = 2.0 * L / (nx + 1)
    th = 2.0 * math.pi / nt
    Ax = np.diag(np.full(nx, 2 * D / h**2))
    Ax += np.diag(np.full(nx - 1, -D / h**2), 1)
    Ax += np.diag(np.full(nx - 1, -D / h**2), -1)
    D1 = np.diag(np.full(nx - 1, 1 / (2 * h)), 1)
    D1 += np.diag(np.full(nx - 1, -1 / (2 * h)), -1)
    At = np.diag(np.full(nt, 2 * Dr / th**2))
    for i in range(nt):
        At[i, (i + 1) % nt] -= Dr / th**2
        At[i, (i - 1) % nt] -= Dr / th**2
    A = np.kron(np.eye(nt), Ax) + np.kron(At, np.eye(nx))
    angles = np.arange(nt) * th
    B = np.kron(np.diag(np.cos(angles)), D1)
    return A, B


def run():
    n_checks = 0
    for Dr in (0.0, 0.45):
        A, B = operators(Dr=Dr)
        eye = np.eye(len(A))
        one = np.ones(len(A)) / math.sqrt(len(A))
        assert np.linalg.norm(A - A.T, ord=np.inf) < 1e-12
        assert np.linalg.norm(B + B.T, ord=np.inf) < 1e-12
        n_checks += 2
        for q in (0.0, 0.7, 3.0):
            Aq = A + q * eye
            lam, U = eigh(Aq)
            assert lam.min() > 0
            invroot = (U / np.sqrt(lam)) @ U.T
            K = invroot @ B @ invroot
            C = K.T @ K
            z = invroot @ one
            ev, W = eigh(C)
            assert ev.min() > -1e-9
            weights = (W.T @ z) ** 2
            assert np.count_nonzero(weights > 1e-12) > 1
            assert np.sum(weights * ev) > 0
            n_checks += 4
            prev = np.inf
            for v in (0.0, 0.05, 0.2, 0.5, 1.0, 2.0, 5.0):
                exact = one @ solve(Aq - v * B, one, assume_a='gen')
                via_spectrum = np.sum(weights / (1 + v * v * ev))
                assert abs(exact - via_spectrum) < 5e-11, (Dr, q, v, exact, via_spectrum)
                assert exact <= prev + 1e-10
                prev = exact
                n_checks += 2
                s = v * v
                f = np.sum(weights / (1 + s * ev))
                fp = -np.sum(weights * ev / (1 + s * ev)**2)
                fpp = 2 * np.sum(weights * ev * ev / (1 + s * ev)**3)
                assert fp < 0 and fpp > 0
                assert f * fpp >= 2 * fp * fp - 1e-11
                n_checks += 2
                for order in (1, 2, 3, 4, 5):
                    signed_derivative = math.factorial(order) * np.sum(
                        weights * ev**order / (1 + s * ev)**(order + 1)
                    )
                    assert signed_derivative > 0
                    n_checks += 1
    # Distinct exact check: one-dimensional absorbing interval, frozen planar
    # heading; mean over initial position and headings, continuous in both.
    mp.dps = 45
    L = mp.mpf(1)
    D = mp.mpf('1.3')
    def one_angle_mean(b):
        z = b * L / D
        if abs(z) < mp.mpf('0.002'):
            return L**2 / D * (mp.mpf(1)/3 - z*z/45 + 2*z**4/945 - z**6/4725 + 2*z**8/93555)
        return (L / b) * mp.coth(z) - D / (b*b)
    for v in (mp.mpf('0.05'), mp.mpf('0.2'), mp.mpf('0.6'), mp.mpf('1')):
        m = mp.quad(lambda t: one_angle_mean(v * mp.cos(t)), [0, mp.pi/2]) * 2 / mp.pi
        assert m > 0 and m < L**2/(3*D)
        n_checks += 2
    h = mp.mpf('0.0004')
    m = mp.quad(lambda t: one_angle_mean(h * mp.cos(t)), [0, mp.pi/2]) * 2/mp.pi
    c = (m - L**2/(3*D))/h**2
    expected = -L**4/(90*D**3)
    assert abs(c/expected - 1) < mp.mpf('0.000001')
    n_checks += 1
    print('PASS: %d deterministic assertions' % n_checks)

if __name__ == '__main__':
    run()
