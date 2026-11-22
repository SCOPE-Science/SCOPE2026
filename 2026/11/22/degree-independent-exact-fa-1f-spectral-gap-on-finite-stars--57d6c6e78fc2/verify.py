#!/usr/bin/env python3
"""Reproduce finite-state checks for the FA-1f star spectral-gap formula.

Exact eigenvector and detailed-balance tests use only Python's standard library.
Optional spectral checks use NumPy and SciPy when available.
"""
from fractions import Fraction
from math import sqrt


def transitions(n, s, q):
    """State bits equal 1 for vacancies; bit 0 is the hub; state 0 excluded."""
    p = 1 - q
    for v in range(n + 1):
        facilitated = bool(s >> 1) if v == 0 else bool(s & 1)
        if not facilitated:
            continue
        t = s ^ (1 << v)
        assert t != 0
        rate = p if (s & (1 << v)) else q
        yield t, rate


def check_exact(n, vac_root):
    s0 = Fraction(vac_root)
    q = 1 - s0 * s0
    lam = 1 - s0
    assert 0 < lam < q < 1
    factor = q / (q - lam)
    weighted = lambda state: q ** state.bit_count() * (1 - q) ** (n + 1 - state.bit_count())
    check_count = 0
    for i, j in {(1, 2), (1, n)}:
        def f(state):
            contrast = ((state >> i) & 1) - ((state >> j) & 1)
            return Fraction(contrast) * (Fraction(1) if (state & 1) else factor)
        for state in range(1, 1 << (n + 1)):
            qf = Fraction(0)
            for target, rate in transitions(n, state, q):
                assert weighted(state) * rate == weighted(target) * next(
                    rev for other, rev in transitions(n, target, q) if other == state
                )
                qf += rate * (f(target) - f(state))
                check_count += 1
            assert qf == -lam * f(state), (n, q, state, i, j, qf, f(state))
    return check_count


def check_numerical(n, q):
    import numpy as np
    from scipy.sparse import lil_matrix
    from scipy.sparse.linalg import eigsh
    states = list(range(1, 1 << (n + 1)))
    idx = {state: j for j, state in enumerate(states)}
    mat = lil_matrix((len(states), len(states)), dtype=float)
    for state in states:
        i = idx[state]
        for target, rate in transitions(n, state, q):
            j = idx[target]
            mat[i, i] += float(rate)
            mat[i, j] = -sqrt(q * (1 - q))
    ev = np.linalg.eigvalsh(mat.toarray())
    expected = (1-sqrt(1-q)) if n >= 2 else q
    assert abs(ev[0]) < 2e-9, (n, q, ev)
    assert abs(ev[1] - expected) < 2e-8, (n, q, ev, expected)
    if n >= 3:
        for k in range(1, min(n, len(ev))):
            assert abs(ev[k] - expected) < 2e-8, (n, q, k, ev)
    return float(ev[1])


def main():
    exact_edges = 0
    for n in range(2, 10):
        for root in [Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)]:
            exact_edges += check_exact(n, root)
    print('EXACT_EIGENVECTOR_AND_REVERSIBILITY_PASSED', 'directed_edges=', exact_edges)
    numerical = 0
    try:
        import numpy
        import scipy
    except ImportError:
        print('NUMERICAL_SPECTRA_NOT_RUN: NumPy/SciPy unavailable')
    else:
        for n in range(1, 8):
            for q in [0.125, 0.5, 0.875]:
                check_numerical(n, q)
                numerical += 1
        print('FINITE_SPECTRAL_GAPS_PASSED', numerical)


if __name__ == '__main__':
    main()
