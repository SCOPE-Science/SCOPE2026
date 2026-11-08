#!/usr/bin/env python3
"""Finite arithmetic and numerical checks of the exact two-row Krylov selection theorem.

Run: python verify_krylov.py
Requires Python 3, NumPy and SciPy.  The proof is in RESULT.md; these
finite experiments are consistency checks, not a substitute for that proof.
"""
from fractions import Fraction
from itertools import combinations
from math import sqrt
import numpy as np
from scipy.linalg import qr


def exact_row_selection(N):
    assert N >= 2
    eps2 = Fraction(1, N * N)
    big2 = 1 - eps2
    mid2 = big2 / N
    assert big2 > mid2 > eps2 > 0
    # A row is (supporting column index, squared nonzero entry).
    rows = [(0, big2), (0, eps2), (1, eps2)] + [(1, mid2)] * N
    minvals = {}
    ratios = {}
    for i, j in combinations(range(len(rows)), 2):
        (si, ai), (sj, aj) = rows[i], rows[j]
        if si == sj:
            minvals[(i, j)] = Fraction(0)
            continue
        minvals[(i, j)] = min(ai, aj)
        ratios[(i, j)] = max(ai, aj) / min(ai, aj)  # kappa squared
    top = max(minvals.values())
    winners = {pair for pair, value in minvals.items() if value == top}
    expected = {(0, j) for j in range(3, N + 3)}
    assert top == mid2
    assert winners == expected
    assert all(ratios[p] == N for p in winners)
    assert min(ratios.values()) == 1
    assert {p for p, ratio in ratios.items() if ratio == 1} == {(1, 2)}
    return len(minvals)


def numeric_algorithms(N):
    eps = 1.0 / N
    big = sqrt(1 - eps * eps)
    mid = big / sqrt(N)
    V = np.zeros((N + 3, 2), dtype=float)
    V[0, 0] = big
    V[1, 0] = eps
    V[2, 1] = eps
    V[3:, 1] = mid
    assert np.allclose(V.T @ V, np.eye(2), atol=1e-14)

    # DEIM, with a literal interpolation residual at the second step.
    p1 = int(np.argmax(np.abs(V[:, 0])))
    residual = V[:, 1] - V[:, 0] * (V[p1, 1] / V[p1, 0])
    p2 = int(np.argmax(np.abs(residual)))
    assert p1 == 0 and 3 <= p2 < N + 3

    # Q-DEIM, via column-pivoted QR of V^T, as in the original algorithm.
    _, _, piv = qr(V.T, mode='economic', pivoting=True)
    assert int(piv[0]) == 0 and 3 <= int(piv[1]) < N + 3
    for pair in ((p1, p2), tuple(piv[:2])):
        SV = V[list(pair), :]
        _, R = np.linalg.qr(SV)
        # The exact whitening condition is kappa(V R^-1)=kappa(SV).
        W = np.linalg.solve(R.T, V.T).T
        assert np.isclose(np.linalg.cond(W), np.linalg.cond(SV), rtol=1e-9)
        assert np.isclose(np.linalg.cond(SV), sqrt(N), rtol=1e-9)
    assert np.isclose(np.linalg.cond(V[[1, 2], :]), 1.0)

    # Realize V as an ordinary two-column Arnoldi basis of a uniformly SPD A.
    if N <= 24:
        u, v = V[:, 0], V[:, 1]
        A = 2 * np.eye(N + 3) + np.outer(u, v) + np.outer(v, u)
        evals = np.linalg.eigvalsh(A)
        assert np.isclose(evals[0], 1, atol=1e-10)
        assert np.isclose(evals[-1], 3, atol=1e-10)
        w = A @ u
        w = w - (u @ w) * u
        w = w / np.linalg.norm(w)
        assert np.allclose(w, v, atol=1e-12)
    return True


def main():
    pairs = sum(exact_row_selection(N) for N in range(2, 81))
    for N in [2, 3, 4, 8, 16, 24, 32, 64, 128, 256]:
        numeric_algorithms(N)
    print(f'CHECKS_OK; {pairs} exact row pairs over N=2..80; 10 numerical DEIM/QR/whitening tests; 6 SPD Arnoldi tests')


if __name__ == '__main__':
    main()
