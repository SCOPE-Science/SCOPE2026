#!/usr/bin/env python3
"""Finite exact and numerical checks for normalized Fibonacci tiling-shape laws.

This is a reproducible diagnostic, not a proof of the infinite-time theorem.
"""
import math
import random
from fractions import Fraction

checks = 0

def fib(d, length):
    f = [1] * d
    while len(f) < length:
        f.append(f[-1] + f[-d])
    return f


def root(d):
    lo, hi = 1.0, 2.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if (mid ** (d - 1)) * (mid - 1) < 1:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

# Verify the finite-coordinate length and one-step affine recursion exactly.
for d in range(2, 13):
    f = fib(d, 28 * d + d)
    for r in range(d):
        L = 1
        S = 0
        for m in range(1, 27):
            w = f[d - 1 + r + (m - 1) * d]
            old_L = L
            old_S = S
            L += w
            S += (m % 2) * w
            assert L == f[m * d + r]
            checks += 1
            assert Fraction(S, L) == (Fraction(old_L, L) * Fraction(old_S, old_L)
                                      + Fraction(w, L) * (m % 2))
            checks += 1

# Check every intermediate coordinate phase against the original growth rule.
for d in range(2, 10):
    f = fib(d, 21*d+d)
    lengths = [1]*d
    for n in range(1, 20*d+1):
        r=(n-1)%d
        lengths[r] += f[n+d-2]
        assert sorted(lengths) == sorted(f[n:n+d])
        checks += 1
        for j in range(d):
            updates=(n+d-1-j)//d
            expected=1+sum(f[d-1+j+k*d] for k in range(updates))
            assert lengths[j] == expected
            checks += 1

# Compare exact first and second moments (independent fair placement bits)
# with the limiting stationary Cantor-autoregression formulas.
for d in range(2, 10):
    f = fib(d, 50 * d + d)
    rho = root(d)
    lam = rho ** (-d)
    assert 0 < lam < 0.5
    checks += 1
    assert abs(lam - (1 - 1/rho)) < 1e-12
    checks += 1
    limiting_variance = (1 - lam) / (4 * (1 + lam))
    for r in range(d):
        L = 1
        squares = 0
        Ls, Sq = [1], [0]
        for m in range(1, 46):
            w = f[d - 1 + r + (m - 1) * d]
            L += w
            squares += w*w
            Ls.append(L)
            Sq.append(squares)
            mean = Fraction(L-1, 2*L)
            variance = Fraction(squares, 4*L*L)
            assert Fraction(0) <= mean <= Fraction(1,2)
            assert Fraction(0) <= variance <= Fraction(1,4)
            checks += 2
        assert abs(float(Fraction(Sq[45],4*Ls[45]**2)) - limiting_variance) < 2e-6
        checks += 1
        for h in range(0, 8):
            cov = Fraction(Sq[37],4*Ls[37]*Ls[37+h])
            assert abs(float(cov) - limiting_variance * lam**h) < 2e-5
            checks += 1

# Empirical distribution and lagged covariance for a single realization,
# computed with stable affine recurrences; finite-M Monte Carlo is illustrative.
rng = random.Random(20670518)
for d in (2, 3, 7):
    lam = root(d) ** (-d)
    y = [0.0]*d
    n = 120000
    saved = [[] for _ in range(d)]
    for k in range(n):
        for r in range(d):
            y[r] = lam*y[r] + (1-lam)*rng.randrange(2)
            saved[r].append(y[r])
    var_lim = (1-lam)/(4*(1+lam))
    for r in range(d):
        values = saved[r][1000:]
        mean = sum(values)/len(values)
        variance = sum((v-.5)**2 for v in values)/len(values)
        assert abs(mean-.5)<.012
        assert abs(variance-var_lim)<.013
        checks+=2
        for h in (1,2,3):
            cov = sum((values[k]-.5)*(values[k+h]-.5)
                      for k in range(len(values)-h))/(len(values)-h)
            assert abs(cov-var_lim*lam**h)<.012
            checks+=1

# Exact elementary separation and dimension assertions.
for d in range(2, 31):
    rho = root(d)
    lam = rho**(-d)
    dim = d*math.log(2)/math.log(1/lam)
    assert 0 < dim < d
    assert abs(dim-math.log(2)/math.log(rho))<1e-10
    assert (1-2*lam)>0
    checks += 3

print(f'PASS: {checks} exact/arithmetic and bounded numerical checks')
print('d=2:', 'rho', root(2), 'lambda', root(2)**(-2),
      'shape_dimension', math.log(2)/math.log(root(2)))
