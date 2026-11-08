#!/usr/bin/env python3
"""Numerical corroboration of Gaussian-annulus Hermite-mode formulas.

No packages outside the Python standard library. Finite checks do not replace
proofs of statements for all radii or all nonnegative Hermite indices.
"""
import math

checks = 0

def check(condition, description):
    global checks
    if not condition:
        raise AssertionError(description)
    checks += 1

def intensity(k, x):
    if x == 0:
        return 1.0 if k == 0 else 0.0
    return math.exp(k * math.log(x) - x - math.lgamma(k + 1))

def eigenvalue(k, s, L, divisions=1024):
    """Composite Simpson integral; not used for analytical assertions."""
    h = L / divisions
    acc = intensity(k, s) + intensity(k, s + L)
    for j in range(1, divisions):
        acc += (4 if j % 2 else 2) * intensity(k, s + j*h)
    return acc * h / 3.0

def logmean(s, L):
    if s == 0:
        return 0.0
    return L / math.log1p(L/s)

def transition(n, L):
    return L / math.expm1(L/(n+1))

def asymptotic(s, L):
    rho = logmean(s, L)
    fraction = rho-math.floor(rho)
    constant = L*L/24 + L/4 - 1/24
    return (L/math.sqrt(2*math.pi*s) *
            (1-(constant + (fraction-0.5)**2/2)/s))

# Direct evaluation of the Poisson-density integrals, independent of mode rule.
for L in (0.15, 0.5, 1.0, 2.0, 5.0, 11.0):
    for s in (0.0, 0.02, 0.1, 0.3, 1.0, 2.5, 9.0, 20.0, 60.0, 150.0, 500.0):
        rho = logmean(s, L)
        m = math.floor(rho)
        lo, hi = max(0, m-7), m+8
        values = {k: eigenvalue(k, s, L) for k in range(lo,hi+1)}
        check(all(v>0 for v in values.values()), f'positive {s=}, {L=}')
        check(values[m] >= max(values.values())-1e-13,
              f'maximum at {m}, {s=}, {L=}')
        if m>lo:
            check(values[m] > values[m-1]+1e-13,
                  f'rising before {m}, {s=}, {L=}')
        check(values[m] > values[m+1]+1e-13,
              f'decreasing after {m}, {s=}, {L=}')
        for k in range(lo,hi):
            b=s+L
            diff=intensity(k+1,s)-intensity(k+1,b)
            if diff is not None:
                check(abs((values[k+1]-values[k])-diff)<1e-8,
                      f'integration by parts {k=}, {s=}, {L=}')

# Closed-form switching locations, pairwise equality, and sharp derivative jump.
for L in (0.3, 1.0, 3.0, 7.0):
    previous=0.0
    for k in range(14):
        s=transition(k,L)
        check(s>previous, f'increasing switches {L=}, {k=}')
        check(abs((k+1)*math.log1p(L/s)-L) < 3e-12,
              f'exact switch equation {k=}, {L=}')
        check(abs(logmean(s,L)-(k+1)) < 5e-11,
              f'logmean switch {k=}, {L=}')
        left=eigenvalue(k,s,L,4096)
        right=eigenvalue(k+1,s,L,4096)
        check(abs(left-right)<5e-11, f'tie {k=}, {L=}')
        h=1e-4
        def d(ss):
            return eigenvalue(k+1,ss,L,4096)-eigenvalue(k,ss,L,4096)
        numerical=(d(s+h)-d(s-h))/(2*h)
        predicted=L*intensity(k,s)/(s+L)
        check(abs(numerical-predicted)<2e-7,
              f'cusp slope {k=}, {L=}, {numerical=}, {predicted=}')
        previous=s

# Fixed-width high-radius second-order expansion. Compare to direct quadrature.
for L in (0.5, 1.0, 3.0, 7.0):
    for s in (100.0, 200.0, 400.0, 800.0, 1600.0):
        m=math.floor(logmean(s,L))
        actual=eigenvalue(m,s,L)
        predicted=asymptotic(s,L)
        relative=abs(actual-predicted)/(L/math.sqrt(2*math.pi*s))
        check(relative*s*s < 75*(1+L)**5,
              f'uniform second-order remainder {s=}, {L=}, {relative=}')

print(f'ANNULUS_MODE_CHECKS_PASS {checks}')
