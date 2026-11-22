"""Reproduce checks for the two-temperature cardinal-response optimization theorem.

Uses only the Python standard library; the global theorem is analytical.
"""
from fractions import Fraction
from math import exp, tanh, isclose, sqrt

checks = 0

def check(value, description):
    global checks
    checks += 1
    if not value:
        raise AssertionError(description)

def response(p, x):
    if -1e-13 < x < 0.0:
        x = 0.0  # floating-point endpoint roundoff, not model extrapolation
    return x ** p * (1.0 - x)

def objective(p, m, a):
    return (response(p, m - a) + response(p, m + a)) / 2.0

def candidate(p, m):
    assert p > 0 and 0 < m < 1
    if p <= 1:
        return 0.0
    if p == 2:
        return min(m, 1-m) if m < Fraction(1,3) else 0.0
    if p < 2:
        mc = (2 ** (p - 1) - 1) / (2 ** p - 1)
        return m if m < mc else 0.0
    b, i = p / (2 * (p+1)), (p-1)/(p+1)
    if m <= b:
        return m
    if m >= i:
        return 0.0
    def position(z):
        if z < 1e-9:
            return i
        return p / (p + 1) / (1 + tanh(z) / tanh((p-1)*z))
    low, high = 0.0, 50.0
    for _ in range(100):
        mid = (low + high) / 2
        if position(mid) > m:
            low = mid
        else:
            high = mid
    return m * tanh((low + high)/2)

# Exact p=2 identity over all selected rational parameters and amplitudes.
for j in range(1, 50):
    m = Fraction(j, 50)
    for k in range(50):
        a = min(m, 1-m) * Fraction(k, 49)
        f = lambda x: x*x*(1-x)
        J = (f(m-a)+f(m+a))/2
        target = f(m)+(1-3*m)*a*a
        check(J == target, 'exact quadratic degeneracy')

# Exact p=3 example and optimality by an elementary quartic completion.
m = Fraction(2, 5)
a2 = Fraction(3, 25)
f3 = lambda x: x*x*x*(1-x)
base = f3(m)
opt = base + Fraction(6,25)*a2 - a2*a2
check(base == Fraction(24,625), 'constant-temperature response')
check(opt == Fraction(33,625), 'optimal mean response')
check(opt/base == Fraction(11,8), 'exact 37.5 percent benefit')
check(isclose(candidate(3, .4), sqrt(3)/5, abs_tol=1e-12), 'exact interior amplitude')

# Global numerical stress test: compare theorem-selected amplitudes with
# a fine independent mesh of every admissible gap. This is not a proof.
exponents = (.2, .5, .95, 1, 1.01, 1.1, 1.3, 1.5, 1.9, 1.99,
             2, 2.01, 2.1, 2.5, 3, 4, 5, 8, 12, 25)
for p in exponents:
    for j in range(1, 100):
        m = j / 100
        a = candidate(p, m)
        bound = min(m, 1-m)
        check(-1e-12 <= a <= bound + 1e-12, 'feasibility')
        selected = objective(p, m, a)
        for k in range(121):
            trial = bound*k/120
            check(selected + 2e-12 >= objective(p, m, trial), 'global optimality grid')

# Boundary uniqueness and phase transition checks.
for p in (1.1, 1.4, 1.8):
    mc = (2**(p-1)-1)/(2**p-1)
    check(isclose(objective(p, mc, 0), objective(p, mc, mc), abs_tol=1e-13), 'jump tie')
    check(candidate(p, mc*.99) > 0, 'below sharp jump')
    check(candidate(p, mc*1.01) == 0, 'above sharp jump')
for p in (2.1, 3, 5, 15):
    b = p/(2*(p+1))
    i = (p-1)/(p+1)
    check(isclose(candidate(p, b), b, abs_tol=1e-12), 'continuous onset at lower boundary')
    check(candidate(p, i) == 0, 'continuous disappearance at upper boundary')
    for u in (.01,.03,.10):
        m = i - u*(i-b)
        a = candidate(p,m)
        ratio = a*a / (i-m)
        target = 3*i/(p-2)
        if u == .01:
            check(abs(ratio/target-1) < .08, 'square-root asymptotic sample')

print('PASS', checks, 'assertions')
