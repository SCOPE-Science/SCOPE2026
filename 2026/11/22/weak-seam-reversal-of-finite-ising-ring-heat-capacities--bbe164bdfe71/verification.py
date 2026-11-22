#!/usr/bin/env python3
"""Reproduce finite-ring specific-heat checks and weak-seam crossover.

Requires Python 3 and mpmath (tested with 1.3.0); no data files.
All finite enumerations here are supporting checks, not all-size proofs.
"""
import itertools
import math
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 110
checks = 0


def uprod(K, n, r):
    return mp.tanh(K)**(n - 1) * mp.tanh(r * K)


def g(K, n, r):
    return mp.atanh(uprod(K, n, r))


def second(K, n, r):
    return mp.diff(lambda x: g(x, n, r), K, 2)


def heat_exact(n, r, K, frustrated):
    # Enumerate all spin configurations, using the dimensionless H/J.
    weights = []
    for spins in itertools.product((-1, 1), repeat=n):
        chain = sum(spins[j] * spins[j+1] for j in range(n-1))
        edge = spins[-1] * spins[0]
        energy = -chain + (r if frustrated else -r) * edge
        weights.append((mp.exp(-K * energy), energy))
    Z = mp.fsum(w for w, e in weights)
    e1 = mp.fsum(w * e for w, e in weights)/Z
    e2 = mp.fsum(w * e * e for w, e in weights)/Z
    return K*K*(e2 - e1*e1)


# Exact polynomial identity underpinning strict uniform-ring positivity.
for n in range(3, 27):
    B = [0] * (2*n + 1)
    for idx, val in [(0, n-1), (1, -(n+1)), (n, n+1), (n+1, -(n-1))]:
        B[idx] += val
    S = [(j+1)*(n-1-j) for j in range(n-1)]
    coeff = [0] * (n+2)
    for j, a in enumerate(S):
        for k, b in enumerate([1, -3, 3, -1]):
            coeff[j+k] += a*b
    assert B[:n+2] == coeff
    assert all(v == 0 for v in B[n+2:])
    checks += 1

# Independent finite-state Boltzmann enumeration validates normalization.
for n in range(3, 9):
    for r in [mp.mpf('0.22'), mp.mpf('0.6'), mp.mpf('0.96'), mp.mpf(1)]:
        for K in [mp.mpf('0.3'), mp.mpf('1.1'), mp.mpf('2.7')]:
            observed = heat_exact(n, r, K, False)-heat_exact(n, r, K, True)
            predicted = 2*K*K*second(K, n, r)
            assert mp.almosteq(observed, predicted, rel_eps=mp.mpf('1e-36'), abs_eps=mp.mpf('1e-36'))
            checks += 1

# Strict homogeneous positivity with analytic all-size polynomial certificate.
for n in [3, 4, 6, 10, 20]:
    for K in [mp.mpf('0.05'), mp.mpf('0.3'), mp.mpf('1.5'), mp.mpf('4.5')]:
        t = mp.tanh(K)
        S = mp.fsum((j+1)*(n-1-j)*t**(2*j) for j in range(n-1))
        predicted = n*t**(n-2)*(1-t*t)**4*S/(1-t**(2*n))**2
        assert mp.almosteq(second(K, n, 1), predicted, rel_eps=mp.mpf('1e-34'))
        assert predicted > 0
        checks += 1

# For each weak seam, detect the proved high/low-temperature sign reversal.
for n in [3, 4, 5, 8, 15]:
    for r in [mp.mpf('0.2'), mp.mpf('0.5'), mp.mpf('0.9')]:
        assert second(mp.mpf('0.025'), n, r) > 0
        Klarge = mp.mpf(8)/(1-r)
        assert second(Klarge, n, r) < 0
        checks += 1

# Crossovers converge to the sharp logarithmic weak-defect center.
for n in [3, 4, 8, 20]:
    s = mp.log(mp.mpf(4)*n*n*(n+1)/3)/4
    for eps in [mp.mpf('0.01'), mp.mpf('0.001'), mp.mpf('0.0001')]:
        center = -mp.log(eps)/2+s
        F = lambda x: second(x, n, 1-eps)
        root = mp.findroot(F, (center-mp.mpf('.15'), center+mp.mpf('.15')))
        # Error shrinks; use broad bounds since epsilon*log epsilon corrections.
        assert abs(root-center) < mp.mpf('.14')
        assert abs(F(root)) < mp.mpf('1e-35')
        checks += 1

print('SPECIFIC_HEAT_CHECKS_PASSED', checks)
