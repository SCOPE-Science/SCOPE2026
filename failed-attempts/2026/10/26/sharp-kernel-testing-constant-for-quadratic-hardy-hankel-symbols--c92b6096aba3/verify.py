#!/usr/bin/env python3
"""Finite checks for the exact quadratic Hardy-Hankel kernel-testing theorem.
Run with Python 3; no third-party packages are required.
These finite checks supplement the analytical argument in RESULT.md.
"""
import math
import cmath
import random
from fractions import Fraction

checks = 0
R = random.Random(20261024)

def close(x, y, tol=2e-10):
    global checks
    assert abs(x-y) <= tol * (1 + abs(x) + abs(y)), (x, y)
    checks += 1

def bisection_root(t):
    lo, hi = 0.0, 1.0
    for _ in range(85):
        r = (lo + hi)/2
        p = 2*r**3+3*t*r*r+t*t*r-t
        if p <= 0: lo = r
        else: hi = r
    return (lo + hi)/2

# Exact rational certificate tests; the displayed polynomial identity in
# RESULT.md is an independent symbolic proof rather than an inference
# drawn from finitely many evaluations.
for j in range(1, 251):
    tau = Fraction(j, 250)
    F = (1-tau/4)*(1+tau*tau/4)
    right = Fraction(25,27) + (8-3*tau)*(3*tau-2)**2/Fraction(432)
    assert F == right and F >= Fraction(25,27)
    checks += 1

for _ in range(1600):
    t = 10**R.uniform(-4, 4)
    lam = (t + math.hypot(t, 2))/2
    tau = lam**-2
    r = 0.5/lam
    def F(x): return (1-x*x)*((t+x)**2+1)
    ratio_witness = F(r)/(lam*lam)
    close(ratio_witness, (1-tau/4)*(1+tau*tau/4))
    root = bisection_root(t)
    close(2*root**3+3*t*root**2+t*t*root-t, 0.0, 5e-8)
    assert F(root)+1e-7 >= F(r)
    checks += 1
    assert F(root)/(lam*lam) + 1e-8 >= 25/27
    checks += 1
    # Complex phases can be aligned by one choice of a reproducing kernel.
    alpha, beta = R.uniform(-math.pi, math.pi), R.uniform(-math.pi, math.pi)
    a, b = t*cmath.exp(1j*alpha), cmath.exp(1j*beta)
    w = root*cmath.exp(1j*(alpha-beta))
    squared_kernel = (1-root*root)*(abs(a+b*w)**2+abs(b)**2)
    close(squared_kernel, F(root), 3e-9)
    # The singular value of the finite Hankel corner agrees with lam.
    tr = abs(a)**2+2*abs(b)**2
    det = abs(b)**4
    spectral = math.sqrt((tr+math.sqrt(tr*tr-4*det))/2)
    close(spectral, lam, 4e-9)

teq = 1/math.sqrt(6)
lameq = math.sqrt(3/2)
req = teq
close((teq+math.sqrt(teq*teq+4))/2, lameq)
close(2*req**3+3*teq*req**2+teq*teq*req-teq, 0)
close(math.sqrt((1-req*req)*((teq+req)**2+1))/lameq, 5/(3*math.sqrt(3)))
print(f"PASS: {checks} independent finite arithmetic/algebra tests; analytic proof required for universal statement")
