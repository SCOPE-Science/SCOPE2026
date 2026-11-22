#!/usr/bin/env python3
"""Independent finite checks for the canonical path enriched chain-polytope ellipsoids.

Usage: python3 verify.py
Only standard Python, fractions and optionally SciPy for an extra numerical optimization.
The mathematical all-n claims require the proofs in RESULT.md.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, isclose, log


def stable_sets(n):
    return [tuple(i for i in range(n) if mask >> i & 1) for mask in range(1 << n)
            if mask & (mask << 1) == 0]


def maximal_sets(sets):
    supports = [set(s) for s in sets]
    return [s for s in sets if not any(set(s) < t for t in supports)]


def axes(n):
    if n % 2 == 0:
        b = [Fraction(1, 2)] * n
        c = [Fraction(2, n)] * n
    else:
        m = n // 2
        b = [Fraction(m + 1 if i % 2 == 0 else m, n) for i in range(n)]
        c = [Fraction(1, m + 1 if i % 2 == 0 else m) for i in range(n)]
    return b, c


def exact_checks(n):
    sets = stable_sets(n)
    maxsets = maximal_sets(sets)
    b, c = axes(n)
    assert all(b[i] + b[i + 1] <= 1 for i in range(n - 1))
    assert all(b[i] + b[i + 1] == 1 for i in range(n - 1))
    assert all(sum((c[i] for i in s), Fraction(0)) <= 1 for s in sets)
    # The unique minimal-volume ellipsoid has reciprocal John axes, up to n.
    assert all(bi * ci * n == 1 for bi, ci in zip(b, c))
    # Every signed edge facet is tangent to the John ellipsoid.
    assert 4 * (n - 1) == sum(4 for i in range(n - 1) if b[i] + b[i + 1] == 1)
    # Lowner contact supports are maximal independent sets lying on the ellipsoid.
    contact = [s for s in maxsets if sum((c[i] for i in s), Fraction(0)) == 1]
    signed_contact_count = sum(2**len(s) for s in contact)
    if n % 2 == 0:
        m = n // 2
        assert len(contact) == m + 1
        assert all(len(s) == m for s in contact)
        assert signed_contact_count == (m + 1) * 2**m
        assert b == [Fraction(1, 2)] * n
        assert c == [Fraction(1, m)] * n
    else:
        m = n // 2
        assert {s for s in contact} == {tuple(range(0, n, 2)), tuple(range(1, n, 2))}
        assert signed_contact_count == 3 * 2**m
        # Strict KKT multipliers for the John determinant maximization.
        lam = []
        for k in range(1, m + 1):
            lam.extend([Fraction(n * (m + 1 - k), m * (m + 1)),
                        Fraction(n * k, m * (m + 1))])
        assert all(v > 0 for v in lam)
        assert all(sum((lam[j] for j in (i - 1, i) if 0 <= j < n - 1), Fraction(0)) == 1 / b[i]
                   for i in range(n))
    # Determinant volume comparisons and exact counting, not a general proof.
    assert len(stable_sets(n)) == sum(comb(n + 1 - k, k) for k in range((n + 1)//2 + 1))
    return len(sets), len(maxsets), len(contact), signed_contact_count


def optimization_checks():
    try:
        import numpy as np
        from scipy.optimize import minimize
    except ImportError:
        print('SciPy unavailable: exact arithmetic checks remain complete.')
        return 0
    cases = 0
    for n in range(3, 12):
        b, c = axes(n)
        ss = stable_sets(n)
        I = np.zeros((len(ss), n))
        for k, s in enumerate(ss):
            I[k, list(s)] = 1
        E = np.zeros((n - 1, n))
        for k in range(n - 1):
            E[k, k:k + 2] = 1
        for target, incidence in [(np.array(list(map(float, b))), E),
                                  (np.array(list(map(float, c))), I)]:
            result = minimize(lambda z: -float(np.log(z).sum()),
                              np.full(n, 0.48 if incidence is E else 0.4),
                              jac=lambda z: -1 / z,
                              bounds=[(1e-8, 3)] * n,
                              constraints=[{'type': 'ineq', 'fun': lambda z, mat=incidence: 1-mat@z,
                                            'jac': lambda z, mat=incidence: -mat}],
                              method='SLSQP', options={'ftol':1e-12, 'maxiter':2000})
            assert result.success, (n, result.message)
            assert np.max(np.abs(result.x - target)) < 2e-4, (n, result.x, target)
            assert np.max(incidence@target) <= 1 + 1e-10
            cases += 1
    return cases


if __name__ == '__main__':
    rows = [(n, *exact_checks(n)) for n in range(3, 17)]
    assert all(signed > 0 for (_, _, _, _, signed) in rows)
    numerical = optimization_checks()
    print('FENCE_EXTREMAL_ELLIPSOIDS_PASS exact_dimensions=14 numerical_programs=', numerical)
    print('small_case_contacts=', [(n, ct, sc) for n, _, _, ct, sc in rows[:7]])
