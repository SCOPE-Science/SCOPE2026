#!/usr/bin/env python3
"""Numerical cross-checks for the stated Fourier-type dephasing theorem.

Requires Python 3 and NumPy. These tests supplement, not replace, the proof.
"""
import itertools
import math
import numpy as np


def fourier(d):
    w = np.exp(2j * np.pi / d)
    return np.array([[w ** (j * k) / math.sqrt(d) for k in range(d)]
                     for j in range(d)], dtype=complex)


def walsh4():
    return np.array([[1, 1, 1, 1], [1, -1, 1, -1],
                     [1, 1, -1, -1], [1, -1, -1, 1]], dtype=complex) / 2


def matrix_channel(U, p):
    d = len(U)
    out = np.empty((d*d, d*d), dtype=complex)
    for j in range(d*d):
        E = np.zeros((d, d), dtype=complex)
        E.flat[j] = 1
        Y = U @ E @ U.conj().T
        Y = (1-p)*Y + p*np.diag(np.diag(Y))
        out[:, j] = Y.reshape(-1)
    return out


def predicted(d, ps):
    odd = math.prod(1-p for k,p in enumerate(ps, 1) if k % 2)
    even = math.prod(1-p for k,p in enumerate(ps, 1) if not k % 2)
    return np.sort(np.array([1.] + [odd]*(d-1) + [even]*(d-1)
                            + [odd*even]*(d-1)**2, dtype=float))


def verify(U, ps):
    d = len(U)
    I = np.eye(d, dtype=complex)
    assert np.linalg.norm(U.conj().T @ U-I) < 5e-12
    assert np.max(abs(U)) - np.min(abs(U)) < 5e-12
    S = np.eye(d*d, dtype=complex)
    for p in ps:
        assert 0 <= p <= 1
        S = matrix_channel(U, p) @ S
    singular = np.sort(np.linalg.svd(S, compute_uv=False))
    theory = predicted(d, ps)
    assert np.max(np.abs(singular-theory)) < 8e-11, (d, ps, singular, theory)
    depol = np.outer(I.reshape(-1), I.reshape(-1)) / d
    odd = math.prod(1-p for k,p in enumerate(ps, 1) if k % 2)
    even = math.prod(1-p for k,p in enumerate(ps, 1) if not k % 2)
    actual = np.linalg.svd(S-depol, compute_uv=False)[0]
    assert abs(actual - max(odd,even)) < 8e-11, (d,ps,actual,odd,even)
    return 2


def grid_budget():
    checks = 0
    for t in [2, 3, 4, 5]:
        for b_units in range(0, 4*t+1, 2):
            budget = b_units / 4
            best = float('inf')
            for ticks in itertools.product(range(5), repeat=t):
                if sum(ticks) != b_units:
                    continue
                p = [x/4 for x in ticks]
                odd = math.prod(1-x for k,x in enumerate(p, 1) if k%2)
                even = math.prod(1-x for k,x in enumerate(p, 1) if k%2==0)
                best = min(best,max(odd,even))
            assert abs(best - max(0,1-budget/2)) < 1e-12, (t,budget,best)
            checks += 1
    return checks


def main():
    checks=0
    schedules = [[0.4], [0.4,0.7], [0.2,0.4,0.7],
                 [1.0,0.0], [1.0,1.0], [0.1,0.7,0.4,0.25],
                 [0.3,0.0,0.3,0.0,0.2], [0.0,1.0,0.0,1.0]]
    for U in [fourier(k) for k in (2,3,4,5,6)] + [walsh4()]:
        for ps in schedules:
            checks += verify(U,ps)
    checks += grid_budget()
    print('PASS:', checks, 'matrix-spectrum, contraction and grid-budget assertions')


if __name__=='__main__':
    main()
