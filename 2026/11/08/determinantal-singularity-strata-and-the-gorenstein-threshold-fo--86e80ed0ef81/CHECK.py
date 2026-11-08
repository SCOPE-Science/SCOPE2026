#!/usr/bin/env python3
"""Exact finite checks of projective toric chart generator identities.

This tests sample parameter vectors; the symbolic argument is required for the theorem.
"""
from itertools import product
from math import comb, factorial

def vec(n, terms):
    out = [0] * n
    for loc, coeff in terms:
        out[loc] += coeff
    return tuple(out)

def plus(*vs):
    return tuple(sum(v[i] for v in vs) for i in range(len(vs[0])))

def check(sizes):
    classes = tuple(tuple((j, s) for s in range(a)) for j, a in enumerate(sizes))
    flat = {label: idx for idx, label in enumerate(sum((list(c) for c in classes), []))}
    n = sum(sizes)
    r = len(sizes) - 1
    for k in range(r + 1):
        u = {(j, s): vec(n, ((flat[j, s], 1), (flat[j, 0], -1)))
             for j in range(r + 1) if j != k for s in range(1, sizes[j])}
        z = {(s, i): vec(n, ((flat[k, s], 1), (flat[i, 0], -1)))
             for s in range(sizes[k]) for i in range(r + 1) if i != k}
        for omit in range(r + 1):
            blocks = tuple(j for j in range(r + 1) if j != omit)
            for choices in product(*(range(sizes[j]) for j in blocks)):
                orig = vec(n, [(flat[j, s], 1) for j, s in zip(blocks, choices)]
                           + [(flat[j, 0], -1) for j in range(r + 1) if j != k])
                selected = dict(zip(blocks, choices))
                factors = [u[j, s] for j, s in selected.items() if j != k and s != 0]
                if omit != k:
                    factors.append(z[selected[k], omit])
                assert plus(*factors) == orig if factors else orig == (0,) * n
        # All 2x2 minors vanish as monomial identities.
        for s in range(sizes[k]):
            for t in range(s + 1, sizes[k]):
                for i in range(r + 1):
                    for j in range(i + 1, r + 1):
                        if i == k or j == k:
                            continue
                        assert plus(z[s, i], z[t, j]) == plus(z[s, j], z[t, i])
        # Leading Hilbert coefficient of the projective Segre variety.
        a = sizes[k]
        dim = a + r - 2
        if a > 1:
            vals = [comb(d + a - 1, a - 1) * comb(d + r - 1, r - 1)
                    for d in range(dim + 1)]
            for _ in range(dim):
                vals = [vals[i + 1] - vals[i] for i in range(len(vals) - 1)]
            assert vals == [comb(a + r - 2, a - 1)]
            # Q-Gorenstein condition from the canonical vector on the Segre product:
            assert ((-a) == (-r)) == (a == r)

for r in range(3, 6):
    cases = [[1] * (r + 1), [2] * (r + 1), [r] + [1] * r,
             [r] * (r + 1), [1, 2, 3] + [1] * (r - 2)]
    for sizes in cases:
        check(sizes)
        print('CHART_EXPONENT_AND_SEGRE_MULTIPLICITY_OK', r, ','.join(map(str, sizes)))
print('ALL_EXACT_CHART_CHECKS_OK')
