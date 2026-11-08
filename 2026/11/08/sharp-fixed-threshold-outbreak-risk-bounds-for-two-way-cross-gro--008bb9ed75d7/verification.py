#!/usr/bin/env python3
"""Standalone finite diagnostics for a two-type cross-transmission epidemic model.

The universal convexity and branching arguments are proven in RESULT.md;
these numerical/exact checks do not replace their infinite-domain proofs.
"""
import math
from fractions import Fraction

checks = 0

def check(b):
    global checks
    assert b
    checks += 1

def scalar_survival(rate):
    if rate <= 1:
        return 0.0
    lo, hi = 1e-12, 1.0
    for _ in range(100):
        mid = (lo + hi) / 2
        value = -math.expm1(-rate * mid) - mid
        if value > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

def two_type_survival(a, b):
    assert a > 0 and b > 0 and a*b > 1
    lo, hi = 1e-12, 1.0
    for _ in range(100):
        mid = (lo + hi) / 2
        child_b = -math.expm1(-b * mid)
        residual = -math.expm1(-a * child_b) - mid
        if residual > 0:
            lo = mid
        else:
            hi = mid
    x = (lo + hi) / 2
    y = -math.expm1(-b*x)
    return x, y

# Exact coefficient monotonicity used for the key analytic convexity lemma.
# c_n=(2**n-2)/n!, c_2=c_3=1, c_{n+1}<c_n for n>=3.
coeffs = {n: Fraction(2**n-2, math.factorial(n)) for n in range(2,121)}
check(coeffs[2] == 1)
check(coeffs[3] == 1)
for n in range(4,121):
    check(coeffs[n-1] > coeffs[n])

# A second exact identity: expected total progeny for the subcritical process.
for R in [Fraction(1,5), Fraction(1,2), Fraction(3,4), Fraction(9,10)]:
    for ratio in [Fraction(1),Fraction(3,2),Fraction(2),Fraction(5),Fraction(20)]:
        a, b = R*ratio, R/ratio
        # Expected A seed total=(1+a)/(1-ab); B seed=(1+b)/(1-ab)
        expected = ((1+a)+(1+b))/(2*(1-a*b))
        formula = (2+a+b)/(2*(1-R*R))
        check(expected == formula)
        check(expected >= Fraction(1,1)/(1-R))
        check((expected == 1/(1-R)) == (ratio == 1))
        # The Perron eigenvalue of [[0,a],[b,0]] is R since ab=R^2.
        check(a*b == R*R)

# Analytic inverse-map curvature is positive at all grid values.
for i in range(1,1000):
    x = i/1000
    L = -math.log1p(-x)
    second = 1/(x*x) + (L-1)/((1-x)**2*L*L)
    check(second > 0)

# Nonextinction equations and sharp bounds for fixed cross-type R0.
for R in [1.1, 1.2, 1.5, 2., 3., 5.]:
    optimum = scalar_survival(R)
    infimum = scalar_survival(R*R)/2
    previous = 2
    for imbalance in [1, 1.01, 1.1, 1.5, 2, 3, 5, 10, 30, 100, 500]:
        a = R * imbalance
        b = R / imbalance
        x,y = two_type_survival(a,b)
        p = (x+y)/2
        check(abs(x - (-math.expm1(-a*y))) < 2e-13)
        check(abs(y - (-math.expm1(-b*x))) < 2e-13)
        check(abs(a*b-R*R) < 2e-12*R*R)
        check(infimum < p + 1e-12)
        check(p < optimum + 1e-12)
        check(p <= previous + 1e-12)
        check((imbalance == 1) == (abs(p-optimum) < 1e-10))
        previous = p

# Asymptotic lower bound is achieved as a limit, not at finite rates.
for R in [1.1,1.5,2.,3.]:
    a, b = R*1e7, R/1e7
    x,y = two_type_survival(a,b)
    bound = scalar_survival(R*R)/2
    check(abs((x+y)/2-bound) < 2e-6)

print(f'PASS {checks} deterministic assertions; no random trials')
