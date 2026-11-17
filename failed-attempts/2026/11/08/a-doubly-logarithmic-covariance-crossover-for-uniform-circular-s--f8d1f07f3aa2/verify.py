#!/usr/bin/env python3
"""Independent reproducibility checks for a Dirichlet-gap covariance crossover.
Uses only Python's standard library and mpmath for optional quadrature.
No finite computation is a substitute for the general proof in RESULT.md.
"""
from fractions import Fraction as F
from math import comb, log, exp, log1p


def harmonic(n):
    return sum((F(1, k) for k in range(1, n + 1)), F(0))


def exact_covariance(n, t):
    assert n >= 2 and F(0) < t < F(1)
    p = (1 - t) ** (n - 1)
    total = p * ((n - 1) * t - harmonic(n) + 1)
    for j in range(1, n):
        q = 1 - (j + 1) * t
        if q > 0:
            total += F((-1) ** (j + 1) * comb(n - 1, j), j * (j + 1)) * q ** n
    return total


def low_threshold_covariance(n, t):
    assert F(0) <= t <= F(1, n)
    return F(1, n) * (1 - (1 - t) ** (n - 1) * (1 + n * t * harmonic(n - 1)))


checks = 0
for n in range(2, 15):
    for d in (2*n+1, 3*n+1, 5*n+1, 11*n+1):
        t = F(1, d)
        assert exact_covariance(n, t) == low_threshold_covariance(n, t)
        checks += 1

# Sign checks for the low-threshold expansion, plus endpoint cases.
for n in range(2, 11):
    t = F(1, 100*n)
    assert exact_covariance(n, t) < 0
    assert exact_covariance(n, F(3, 4)) > 0
    checks += 2
assert exact_covariance(2, F(1, 2)) == 0
checks += 1

# The new double-iterated-log crossover is checked through a rigorous explicit
# nonnegative upper bound on the remainder eta, not by truncating an infinite sum.
# For n=10**k, moderate k suffices to make the tail bound tiny; log n is k log 10.
# Use the true elementary expression with H_{n-1} bounded between log(n-1)
# and 1+log(n-1), so the resulting uncertainty is <= u*p.
for k in (8, 10, 14):
    n = 10 ** k
    L = k * log(10)
    for z in (-2.0, -1.0, 0.0, 1.0, 2.0):
        u = log(L) + log(log(L)) + z
        t = u / n
        # Evaluate the exact beta tail probability using log1p (no subtraction
        # of two nearly equal floating-point numbers).
        p = exp((n - 1)*log1p(-t))
        eta_bound = n*n*(exp(n*log(2/exp(1))) + exp(-n*exp(-2*u)))
        # Integral bounds: log(n) <= H_(n-1) <= 1+log(n-1).
        # Identity (1) consequently proves these rigorous real-number bounds
        # (the float evaluation only checks their signs numerically).
        lower = 1 - eta_bound - p*(1 + u*(1+log(n-1)))
        upper = 1 - p*(1 + u*L)
        assert lower < upper
        # Determine that the scaled sign follows the claimed crossover
        # well to either side, allowing finite-n corrections.
        if abs(z) >= 1.0:
            assert (lower > 0) if z > 0 else (upper < 0)
        checks += 1

# Optional independent direct Beta-density quadrature for the finite formula.
try:
    import mpmath as mp
except ImportError:
    print(f"PASS: {checks} exact and explicit-bound assertions (mpmath absent)")
else:
    mp.mp.dps = 45
    for n in range(2, 7):
        m = n - 1
        def g(x):
            a = x / (1 - x) if x < 1 else mp.inf
            extra = mp.mpf(0)
            for j in range(1, m + 1):
                y = max(mp.mpf(0), 1-j*a)
                extra += (-1)**(j+1)*comb(m,j)*y**m/(j*m)
            return x+(1-x)*extra
        for tfrac in (F(1, 7), F(1, 3), F(3, 5)):
            t = mp.mpf(tfrac.numerator) / tfrac.denominator
            knots = [t]+[mp.mpf(1)/k for k in range(2,n+1) if t<mp.mpf(1)/k<1]+[mp.mpf(1)]
            knots.sort()
            mixed = sum(mp.quad(lambda x: (n-1)*(1-x)**(n-2)*g(x), [a,b]) for a,b in zip(knots,knots[1:]))
            p = (1-t)**(n-1)
            cov_quad = n*mixed-mp.mpf(harmonic(n).numerator)/harmonic(n).denominator*p
            cov_exact=exact_covariance(n,tfrac)
            expected=mp.mpf(cov_exact.numerator)/cov_exact.denominator
            assert abs(cov_quad-expected)<mp.mpf('1e-30'),(n,tfrac,cov_quad,expected)
            checks += 1
    print(f"PASS: {checks} exact, bound, and independent integral checks")
