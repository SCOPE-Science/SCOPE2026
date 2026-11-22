#!/usr/bin/env python3
"""Finite arithmetic diagnostics for an analytic weighted-composition theorem.

These tests do not prove the infinite-dimensional spectrum, strong limits, or
absence of norm convergence. Those follow from the accompanying proof.
"""
import math

checks = 0

def close(x, y, tol=1e-11):
    global checks
    checks += 1
    assert math.isclose(x, y, rel_tol=tol, abs_tol=tol), (x, y)

def weight(a, delta, y):
    return math.exp(-delta*y)

def qvalue(a, eta):
    return 1.0-eta+eta/a

# Polar powers and generalized Aluthge weight (pointwise on L^2(0,infinity)).
for a in (0.4, 0.8, 1.2, 2.5):
    for d in (0.05, 0.7, 2.0):
        for eta in (0.1, 0.5, 0.9, 1.0):
            q = qvalue(a, eta)
            for y in (0.0001, 0.03, 0.2, 1.5, 7.0):
                # |A|^eta * V_a * |A|^(1-eta): scalar factor at y.
                from_polar = math.exp(-eta*d*y/a) * math.exp(-(1-eta)*d*y)
                close(from_polar, weight(a, d*q, y))
                for n in (0, 1, 2, 4):
                    dn = d*q**n
                    next_weight = math.exp(-eta*dn*y/a)*math.exp(-(1-eta)*dn*y)
                    close(next_weight, weight(a, d*q**(n+1), y))

# Unitarly conjugate all positive damping parameters by half-line dilations.
for a in (0.4, 0.8, 1.2, 2.5):
    for d in (0.01, 1.0, 8.0):
        for c in (0.2, 0.6, 2.0, 5.0):
            for y in (0.01, 1.0, 10.0):
                close(math.exp(-d*y/c), math.exp(-(d/c)*y))

# Sharp sup of two exponential weights; compare critical point to dense grids.
for a in (0.4, 0.8, 1.2, 2.5):
    for eta in (0.1, 0.5, 1.0):
        q = qvalue(a, eta)
        z = math.log(q)/(q-1)
        theo = abs(1-q)*q**(-q/(q-1))
        close(abs(math.exp(-z)-math.exp(-q*z)), theo)
        for i in range(1001):
            zi = z * (i+1)/300
            checks += 1
            assert abs(math.exp(-zi)-math.exp(-q*zi)) <= theo + 1e-13
    t = a*math.log(a)/(a-1)
    theo = abs(a-1)/a * a**(-a/(a-1))
    close(abs(math.exp(-t/a)-math.exp(-t))/a, theo)
    for i in range(1001):
        ti = t*(i+1)/300
        checks += 1
        assert abs(math.exp(-ti/a)-math.exp(-ti))/a <= theo+1e-13

# Exponentially small finite-shift residual witnesses to the inner disk.
# The continuous multiplicity comes from the direct integral, not finite tests.
for a in (0.5, 2.0):
    mu = 0.5
    h = math.log(a)
    xi = 0.07
    ws = {k: math.exp(-min(745.0,math.exp(xi+k*h))) for k in range(-30, 31)}
    xs = {0:1.0}
    if a < 1:
        # W x = mu x, W x[k] = w[k] x[k+1].
        for k in range(0, 30):
            xs[k+1] = xs[k] * mu / ws[k]
        for k in range(-1, -31, -1):
            xs[k] = xs[k+1] * ws[k] / mu
        residual = sum((ws[k]*xs.get(k+1,0.0)-mu*xs[k])**2 for k in range(-30, 31))
    else:
        # W* x = mu x, W* x[k] = w[k-1] x[k-1].
        for k in range(1,31):
            xs[k] = xs[k-1]*ws[k-1]/mu
        for k in range(-1,-31,-1):
            xs[k] = xs[k+1]*mu/ws[k]
        residual = sum((ws.get(k-1,0)*xs.get(k-1,0)-mu*xs[k])**2 for k in range(-30,31))
    normalized = (residual / sum(x*x for x in xs.values()))**.5
    checks += 1
    assert normalized < 1e-6, (a, normalized)

print(f'CHECKS_OK {checks}')
