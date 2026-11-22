#!/usr/bin/env python3
"""Independent small-cube verification of harmonic-face spectral formulas.

Requires Python >=3.9 and NumPy. Does not use any document or data file.
The finite tests supplement, but do not replace, the all-dimensional proof.
"""
import math
from fractions import Fraction
import numpy as np


def predicted(h, t):
    if t == 0:
        return Fraction(2 ** h)
    a = sum((Fraction(math.comb(h, j), j + t) for j in range(h + 1)), Fraction(0))
    b = sum((Fraction(math.comb(h, j), (j + t)**2) for j in range(h + 1)), Fraction(0))
    return Fraction(2 ** h) * b / (a * a)


def harmonic_extension(k, h):
    n = k + h
    size = 1 << n
    # First k bits are boundary coordinates, last h bits must be zero.
    bd = [u for u in range(1 << k)]
    interior = [u for u in range(size) if u not in bd]
    ix = {u: j for j, u in enumerate(interior)}
    mat = np.zeros((len(interior), len(interior)))
    force = np.zeros((len(interior), len(bd)))
    for i, u in enumerate(interior):
        mat[i, i] = n
        for bit in range(n):
            v = u ^ (1 << bit)
            if v in ix:
                mat[i, ix[v]] -= 1
            else:
                force[i, v] += 1
    ext = np.zeros((size, len(bd)))
    for j, v in enumerate(bd):
        ext[v, j] = 1
    if interior:
        ext[interior, :] = np.linalg.solve(mat, force)
    return ext


def walsh(k):
    size = 1 << k
    return np.array([[(-1)**((x & s).bit_count()) for s in range(size)]
                     for x in range(size)], dtype=float) / math.sqrt(size)


def tests():
    count = 0
    maxerr = 0.0
    for k in range(1, 4):
        for h in range(1, 6):
            if k + h > 7:
                continue
            ext = harmonic_extension(k, h)
            w = walsh(k)
            gram = w.T @ ext.T @ ext @ w
            expected = np.diag([float(predicted(h, s.bit_count())) for s in range(1 << k)])
            err = float(np.max(np.abs(gram - expected)))
            maxerr = max(maxerr, err)
            assert err < 2e-10, (k, h, err)
            count += 1
    # Exact rational recurrence and finite exceptions used in the proof.
    vals = [predicted(h, 1) for h in range(1, 16)]
    assert vals[3] == Fraction(3548, 2883)
    assert vals[0] < vals[1] < vals[2] < vals[3]
    assert all(vals[j] > vals[j+1] for j in range(3, len(vals)-1))
    for h in range(1, 20):
        assert all(predicted(h, t) > predicted(h, t+1) for t in range(1, 10))
    print('PASS: %d full Dirichlet matrix/Walsh spectral comparisons; max entry error %.3g' % (count, maxerr))
    print('PASS: rational universal maximum 3548/2883 and finite monotonicity checks')
    print('Note: infinite-dimensional assertions rely on the analytic proof.')


if __name__ == '__main__':
    tests()
