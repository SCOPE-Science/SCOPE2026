"""Numerical diagnostics for the exact two-grid operator-resolvent minimax theorem.

Finite tests supplement, and do not replace, the analytic global proof.
"""
import math


def coth(z):
    return 1.0 / math.tanh(z)


def langevin(z):
    return coth(z) - 1.0 / z


def jratio(z):
    c = math.cosh(z)
    return (c / z) ** 2 - coth(z) ** 2


def root_fn(z):
    return jratio(z) * (1.0 + math.tanh(z)) - 1.0 - langevin(z)


lo, hi = 1.10450, 1.10451
assert root_fn(lo) < 0 < root_fn(hi)
for _ in range(70):
    mid = (lo + hi) / 2
    if root_fn(mid) < 0:
        lo = mid
    else:
        hi = mid
zstar = (lo + hi) / 2
astar = jratio(zstar)
wstar = astar + 1
Cstar = (1 - astar) / 4
assert abs(zstar - 1.10450454618953) < 5e-12
assert abs(wstar - 1.74430841041328) < 5e-12
assert abs(Cstar - 0.0639228973966799) < 5e-12
checks = 4

# Check both the functional-calculus scalar identity and error bound on a broad finite grid.
h, lam = 0.2, 0.7
for k in range(1, 5001):
    z = 0.03 + 0.003 * k
    x = 4 * z / h - lam
    if x < 0:
        continue
    coarse = h / (-math.expm1(-h * (lam + x))) - h / 2
    fine = h / 2 / (-math.expm1(-h / 2 * (lam + x))) - h / 4
    lhs = (wstar * fine + (1 - wstar) * coarse - 1 / (lam + x)) / h
    rhs = (langevin(z) - astar * math.tanh(z)) / 4
    assert abs(lhs - rhs) < 4e-13
    assert abs(lhs) <= Cstar + 1e-11
    checks += 2

# Exact two equioscillating contacts; strict against perturbations in the coefficient.
assert abs((langevin(zstar) - astar * math.tanh(zstar)) / 4 + Cstar) < 2e-12
for perturb in [-0.1, -0.01, -0.0001, 0.0001, 0.01, 0.1]:
    a = astar + perturb
    err_at_contact = abs(langevin(zstar) - a * math.tanh(zstar)) / 4
    err_at_infinity = abs(1 - a) / 4
    assert max(err_at_contact, err_at_infinity) > Cstar + 1e-10
    checks += 1
print(f'MINIMAX_TWO_GRID_DIAGNOSTIC_OK {checks}; z={zstar:.15f}; w={wstar:.15f}; C={Cstar:.16f}')
