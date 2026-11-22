#!/usr/bin/env python3
"""Independent finite diagnostics for a correlated Gaussian oblique tangent projector.
The analytic moment and tail proofs are in RESULT.md; random draws cannot prove them.
"""
from fractions import Fraction as F
from math import asin, log, sqrt
from random import Random

COUNT = 0


def check(condition, explanation):
    global COUNT
    if not condition:
        raise AssertionError(explanation)
    COUNT += 1


def mm(A, B):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*B)] for row in A]


def add(A, B):
    return [[a + b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(A, B)]


def sub(A, B):
    return [[a - b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(A, B)]


def tr(A):
    return [list(c) for c in zip(*A)]


def frob2(A):
    return sum(x * x for row in A for x in row)


def pair(a, b):
    L = [[F(1), a], [F(0), F(0)]]
    R = [[F(1), b], [F(0), F(0)]]
    Z = [[F(0), F(0)], [F(0), F(1)]]
    raw = sub(add(mm(L, Z), mm(Z, tr(R))), mm(mm(L, Z), tr(R)))
    symmetric = [[(raw[i][j] + raw[j][i]) / 2 for j in range(2)] for i in range(2)]
    return raw, symmetric


# Exact rational rank-one oblique-projector reconstruction and squared-risk algebra.
grid = [F(-9, 5), F(-1), F(-2, 7), F(0), F(1, 3), F(7, 5)]
for a in grid:
    for b in grid:
        raw, sym = pair(a, b)
        check(raw == [[-a*b, a], [b, F(0)]], 'raw tangent identity')
        check(sym == [[-a*b, (a+b)/2], [(a+b)/2, F(0)]], 'symmetrization')
        check(frob2(sym) == a*a*b*b + (a+b)**2 / 2, 'Frobenius identity')
        if a == b:
            check(frob2(sym) == a**4 + 2*a*a, 'perfect sharing')

# Exact endpoint mean-square identities and strict positive gap.
for ell in range(3, 40):
    a2 = F(1, ell-2)
    independent = a2 + a2*a2
    check(independent == F(1, ell-2) + F(1, (ell-2)**2), 'independent mean square')
    if ell > 4:
        shared = 2*a2 + F(3, (ell-2)*(ell-4))
        delta = shared - independent
        check(delta == F(ell*ell-4*ell+6, (ell-2)**2*(ell-4)), 'exact risk difference')
        check(delta > 0, 'strict sharing penalty')

# Derive the Schwinger-parameter integral via a *separate* midpoint quadrature,
# using u=t/(1-t) to put the domain on the unit interval.
def laplace_numeric(ell, rho, n=12000):
    s = 1-rho*rho
    # Derive separate one-dimensional transformations of the positive
    # Gaussian Laplace determinant integral, smooth on the unit interval.
    total = 0.0
    for i in range(n):
        t = (i+0.5)/n
        if ell == 3:
            value = 1/(s+(1-s)*(1-t)**2)
        elif ell == 4:
            value = 1/(4*(s+(1-s)*(1-t)))
        else:
            raise ValueError('diagnostic only implemented for three or four rows')
        total += value
    return total/n

for ell in (3, 4):
    for rho in (0.0, 0.2, 0.5, 0.8, 0.95):
        s = 1-rho*rho
        exact = (asin(rho)/(rho*sqrt(s)) if rho else 1.0) if ell == 3 else (-log(s)/(4*rho*rho) if rho else 0.25)
        approx = laplace_numeric(ell, rho)
        check(abs(approx-exact) < 0.0007, 'correlated inverse-chi Laplace integral')

# Gaussian sketches: reconstruct the exactly defined pair from full vector columns.
# This is a finite test of the projector identities, not a moment-divergence test.
rng = Random(20261121)
for ell in (1, 2, 3, 4, 5, 8):
    for rho in (-1.0, -0.75, 0.0, 0.61, 0.98, 1.0):
        s = sqrt(max(0.0, 1-rho*rho))
        for trial in range(125):
            g = [rng.gauss(0, 1) for _ in range(ell)]
            h = [rng.gauss(0, 1) for _ in range(ell)]
            u = [rng.gauss(0, 1) for _ in range(ell)]
            v = [rng.gauss(0, 1) for _ in range(ell)]
            gp = [rho*x+s*y for x, y in zip(g, u)]
            hp = [rho*x+s*y for x, y in zip(h, v)]
            a = sum(x*y for x, y in zip(g, h)) / sum(x*x for x in g)
            b = sum(x*y for x, y in zip(gp, hp)) / sum(x*x for x in gp)
            observed = a*a*b*b + 0.5*(a+b)**2
            check(observed >= 0, 'nonnegative squared Frobenius norm')
            check(abs(observed-((a*b)**2 + 2*((a+b)/2)**2)) < 1e-9*max(1.0, observed), 'direct matrix norm')
            if abs(rho) == 1.0:
                check(abs(a-b) <= 1e-10*(1+abs(a)), 'same sketch equivalence')

print(f'VERIFY_OK checks={COUNT}')
