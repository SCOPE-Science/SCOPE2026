"""Finite-chain generator cross-check of a rare-departure counting theorem.

Usage: python CHECKER.py. Requires numpy and scipy.
Numerical finite-size evidence does not substitute for the all-size proof.
"""
import numpy as np
from scipy.linalg import solve


def current_and_fano(length, injection, extraction, reset):
    n = 1 << length
    q = np.zeros((n, n), dtype=float)
    b = np.zeros((n, n), dtype=float)
    for state in range(n):
        def jump(dest, rate, marked=False):
            q[state, dest] += rate
            q[state, state] -= rate
            if marked:
                b[state, dest] += rate
        if not (state & 1):
            jump(state | 1, injection)
        if state & (1 << (length-1)):
            jump(state ^ (1 << (length-1)), extraction, True)
        for i in range(length-1):
            if (state & (1 << i)) and not (state & (1 << (i+1))):
                jump(state ^ (1 << i) ^ (1 << (i+1)), 1.)
        if not (state & 1):
            for i in range(1, length):
                if state & (1 << i):
                    jump(state ^ (1 << i) ^ 1, reset)
    assert np.max(np.abs(q.sum(axis=1))) < 1e-8
    qt = q.T.copy()
    qt[-1, :] = 1.
    rhs = np.zeros(n)
    rhs[-1] = 1.
    pi = solve(qt, rhs)
    assert np.min(pi) > -1e-8 and abs(pi.sum()-1.) < 1e-8
    jvec = b @ np.ones(n)
    j = pi @ jvec
    a = q.copy()
    a[-1, :] = pi
    y = j*np.ones(n) - jvec
    y[-1] = 0.
    h = solve(a, y)
    assert np.max(np.abs(q@h - (j*np.ones(n)-jvec))) < 1e-3
    variance_rate = j + 2*pi @ b @ h
    return j, variance_rate/j, pi


def main():
    cases = [(1.,1.),(.2,.8),(2.,.3)]
    tested = 0
    for length in (2,3,4):
        for injection, extraction in cases:
            c = injection + extraction if length == 2 else injection
            old_err = None
            old_fano = None
            for r in (100., 300., 1000.):
                mean, fano, pi = current_and_fano(length, injection, extraction, r)
                err = abs(r*mean/c-1.)
                ferr = abs(fano-1.)
                assert np.isfinite(mean) and np.isfinite(fano)
                assert mean>0 and fano>0
                assert err < .28, (length, injection, extraction, r, err)
                assert ferr < .32, (length, injection, extraction, r, ferr)
                assert old_err is None or err < old_err, (length, injection, extraction, r, err, old_err)
                assert old_fano is None or ferr < old_fano, (length, injection, extraction, r, ferr, old_fano)
                old_err, old_fano = err, ferr
                tested += 6
    # Exact two-site mean current, independently obtained by stationary elimination.
    for a,b,r in ((1.,1.,1.),(.2,.8,10.),(2.,.3,100.)):
        exact = a*b*(a+b)/(a*a*b + a*a + a*b*b + a*b*r + a*b + b*b)
        mean, _, _ = current_and_fano(2,a,b,r)
        assert abs(mean-exact) < 1e-10
        tested += 1
    print(f'PASS: {tested} deterministic generator, cumulant and convergence assertions; dimensions 2 through 4.')

if __name__ == '__main__':
    main()
