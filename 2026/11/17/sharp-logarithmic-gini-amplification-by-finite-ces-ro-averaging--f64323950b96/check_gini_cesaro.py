#!/usr/bin/env python3
"""Exact rational diagnostics for the finite Cesaro/Gini norm theorem.

The infinite-dimensional (all-n) step is proved by harmonic inequalities
in RESULT.md; this script checks precisely the finite base cases used there
and several independently derived identities. No dependencies beyond Python.
"""
from fractions import Fraction as Q
from itertools import combinations


def harmonic(n):
    return sum((Q(1, i) for i in range(1, n + 1)), Q(0))


def gini(x):
    return sum((abs(x[i] - x[j]) for i in range(len(x))
                for j in range(i + 1, len(x))), Q(0))


def cesaro(x):
    s = Q(0)
    out = []
    for i, v in enumerate(x, 1):
        s += v
        out.append(s / i)
    return out


def target(n):
    return ((n + 1) * harmonic(n) - 2 * n) / (n - 1)


def column_gini(n, j):
    z = [Q(0)] * (j - 1) + [Q(1, i) for i in range(j, n + 1)]
    val = gini(z)
    formula = (n + 2 * j - 1) * (harmonic(n) - harmonic(j - 1)) - 2 * (n - j + 1)
    assert val == formula
    return val


def normalized_triangle_gap(n, k):
    t = (n + 1) * harmonic(n) - 2 * n
    b = (n + k) * (harmonic(n) - harmonic(k)) - n + Q(3*k - 1, 2)
    return Q(n-k, n-1) * t - b


def main():
    small = {}
    checked_cuts = 0
    for n in range(2, 9):
        opt = Q(-1)
        masks = []
        for k in range(1, n):
            for subset in combinations(range(n), k):
                x = [Q(int(i in subset)) for i in range(n)]
                val = gini(cesaro(x)) / (k * (n-k))
                checked_cuts += 1
                if val > opt:
                    opt, masks = val, [subset]
                elif val == opt:
                    masks.append(subset)
        assert opt == target(n), (n, opt, target(n))
        assert (0,) in masks, (n, masks)
        small[n] = str(opt)
    print('ALL_SMALL_CUTS_EXHAUSTIVELY_VERIFIED', checked_cuts, small)

    base_cases = []
    for k in range(5, 22):
        gap = normalized_triangle_gap(2*k, k)
        assert gap > 0, (k, gap)
        base_cases.append((k, gap))
    print('EXACT_DIAGONAL_HARMONIC_BASE_CASES_VERIFIED', len(base_cases),
          'minimum', min(base_cases, key=lambda t:t[1]))

    for k in (2, 3, 4):
        gap = normalized_triangle_gap(9, k)
        assert gap > 0
    print('EXACT_LOW_K_ANCHORS_AT_NINE_VERIFIED')

    # Formula and first-order difference identity, checked independently on a grid.
    for n in range(2, 50):
        gs = [column_gini(n, j) for j in range(1, n+1)]
        assert all(gs[i] >= gs[i+1] for i in range(n-1))
        for k in range(1, n//2+1):
            S = sum(gs[:k], Q(0))
            f = Q(n-k, n-1) * gs[0] - S/k
            assert f == normalized_triangle_gap(n, k)
            if n >= 9 and k >= 2:
                assert f > 0, (n,k,f)
            if n >= 2*k and k >= 2:
                delta = (normalized_triangle_gap(n+1,k)
                         - normalized_triangle_gap(n,k))
                rhs = (harmonic(k)-1
                       -Q(2*(k-1),n-1)*(1-harmonic(n)/n))
                assert delta == rhs and rhs > 0, (n,k,delta,rhs)
    print('COLUMN_MONOTONICITY_SUM_IDENTITIES_AND_DIFFERENCE_GRID_VERIFIED')

    # Concrete signed vectors, not relying on the cut reduction.
    import random
    rng = random.Random(78421)
    trials = 0
    for n in range(2, 26):
        L = target(n)
        for _ in range(250):
            x = [Q(rng.randrange(-15,16),rng.randrange(1,8)) for _ in range(n)]
            assert gini(cesaro(x)) <= L*gini(x)
            trials += 1
    print('INDEPENDENT_SIGNED_SIGNAL_DIAGNOSTICS_VERIFIED', trials)
    print('FIRST_SPIKE_ATTAINMENT_VERIFIED_FOR_ALL_SMALL_DIMENSIONS')
    print('ALL_FINITE_CESARO_GINI_CHECKS_PASSED')


if __name__ == '__main__':
    main()
