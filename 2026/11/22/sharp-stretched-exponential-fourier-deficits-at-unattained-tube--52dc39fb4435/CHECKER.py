#!/usr/bin/env python3
"""Supplementary finite checks for a dyadic tube Fourier construction.

No finite check certifies the all-frequency or all-parameter theorem;
those parts follow from the analytic argument in RESULT.md.
"""
import cmath
import math

N_TESTS = 0

def check(condition, message):
    global N_TESTS
    N_TESTS += 1
    if not condition:
        raise AssertionError(message)

# Normalized character sums over a full dyadic cell: only level q=N survives.
for N in range(2, 10):
    for q in range(2, 11):
        for m in (0, 1, 7):
            count = 1 << q
            val = sum((-1) ** k * cmath.exp(2j * math.pi * (1 << (N-1)) * k / count)
                      for k in range(m*count, (m+1)*count)) / count
            expected = float(q == N)
            check(abs(val - expected) < 2e-10, f'character q={q},N={N},m={m}: {val}')

# The continuous critical point and its exact minimum in the quadratic case.
for m in (1, 2, 10, 80, 1000, 100000):
    u = (math.pi*m) ** (1/3)
    f = lambda r: r*r + 2*math.pi*m/r
    check(abs(f(u) - 3*(math.pi*m)**(2/3)) < 1e-8,
          f'critical value at m={m}')
    n = max(2, round(u))
    check(f(n) >= f(u) - 1e-9, f'convex min at m={m}')
    if u >= 3:
        check(f(n)-f(u) < 3, f'bounded lattice error at m={m}')

# Numerically quantify the error-to-main ratio in the selected Fourier cell.
# Small q level sums are computed as ordinary positive terms; not an infinite proof.
for m in (100, 1000, 10000, 100000):
    u = (math.pi*m) ** (1/3)
    n = round(u)
    f = lambda r: r*r + 2*math.pi*m/r
    weights = [math.exp(-(f(q)-f(u))) for q in range(2, max(80, int(4*u)+20))]
    qs = range(2, 2+len(weights))
    qweighted = sum(w/q for w,q in zip(weights,qs))
    mass = math.exp(-(f(n)-f(u)))
    check(0 < mass <= 1+1e-12, f'normalization m={m}')
    check(qweighted/mass < 0.7, f'normalized weighted moment m={m}')
    if m > 1000:
        check(qweighted/mass < 0.4, f'improved error m={m}')


# Direct finite cell transforms test the phase-cancellation selector without
# freezing the q-dependent factor.  These are truncated q sums, not proofs.
for m in (30, 100, 300):
    n = round((math.pi*m) ** (1/3))
    saddle = math.exp(-n*n - 2*math.pi*m/n)
    cell = 0j
    for q in range(2, 12):
        scale = 1 << q
        layer = 0j
        for k in range(m*scale, (m+1)*scale):
            x = k/scale
            multiplier = cmath.exp(2j*math.pi*(1 << (n-1))*x)
            layer += (-1)**k * multiplier * (
                math.exp(-2*math.pi*x/q) +
                math.exp(-2*math.pi*(2-1/q)*x))
        cell += math.exp(-q*q)*layer/scale
    ratio = cell/saddle
    check(ratio.real > 0.4, f'cell-character lower signal m={m}: {ratio}')
    check(abs(ratio.imag) < 0.02, f'cell-character imaginary m={m}: {ratio}')

print(f'PASS: {N_TESTS} supplementary finite assertions')
