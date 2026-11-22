"""Numerical corroboration for the probit-feedback dynamics. Standard Python library only.

Finite checks complement, and cannot replace, the analytic theorem.
Run: python check_probit.py
"""
import math

SQ2 = math.sqrt(2.0)
PHI0 = 1.0 / math.sqrt(2.0 * math.pi)
AC = 2.0 / PHI0


def Phi(z):
    return 0.5 * math.erfc(-z / SQ2)


def density(z):
    return PHI0 * math.exp(-0.5 * z * z)


def centered_cdf(z):
    return 0.5 * math.erf(z / SQ2)


def step(a, z):
    return z - a * centered_cdf(z)


def bisect(f, lo, hi, n=160):
    flo = f(lo)
    fhi = f(hi)
    assert flo * fhi < 0, (lo, hi, flo, fhi)
    for _ in range(n):
        mid = 0.5 * (lo + hi)
        fm = f(mid)
        if fm == 0:
            return mid
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return 0.5 * (lo + hi)


def positive_two_cycle(a):
    assert a > AC
    # Above the nonzero root a*g(u)-2*u becomes negative.
    return bisect(lambda u: a * centered_cdf(u) - 2 * u, 1.0e-5, max(5.0, a / 3.0))


# Critical point, strict subcritical distance contraction on sample grid.
for a in (0.4, 2.0, AC):
    for z in (0.001, 0.08, 1.2, 3.3, 40.0):
        assert abs(step(a, z)) < abs(z), (a, z)

# Superattracting root: g(u)=2*u*phi(u), and gain=1/phi(u).
us = bisect(lambda u: centered_cdf(u) - 2*u*density(u), 0.8, 3.0)
ass = 1.0 / density(us)
assert 6.67 < ass < 6.69
assert abs(ass * centered_cdf(us) - 2*us) < 1.0e-12
assert abs(step(ass, us) + us) < 1.0e-12
assert abs(1 - ass * density(us)) < 1.0e-13

# The exact two-cycle is symmetric, distinct, and locally attracting.
for a in (5.05, 5.4, 6.0, ass, 8.0, 12.0, 20.0):
    u = positive_two_cycle(a)
    assert abs(step(a, u) + u) < 2e-11, (a, u)
    assert abs(step(a, -u) - u) < 2e-11
    mu = (1.0 - a * density(u))**2
    assert 0.0 <= mu < 1.0

# At the critical point, nonexceptional small initial data approach n*z_n^2=3/2.
z = 0.1
for n in range(1, 300001):
    z = step(AC, z)
assert abs(n * z * z - 1.5) < 0.015, (n, z, n*z*z)

# A nonzero finite-hit critical point exists (so it must be excluded from the law).
crit_hit = bisect(lambda z: step(AC, z), 1.0, 4.0)
assert crit_hit > 1.0
assert abs(step(AC, crit_hit)) < 1e-13

# High-gain non-neutral multiplier gap and endpoint scales.
for a in (12.0, 16.0, 20.0):
    u = positive_two_cycle(a)
    lower = 0.5 * math.erfc(u / SQ2)
    predicted_lower = (4.0/a) * density(a/4.0)
    mu = (1 - a*density(u))**2
    predicted_gap = 2 * a * density(a/4.0)
    assert 0.85 < lower / predicted_lower < 1.2
    assert 0.90 < (1 - mu) / predicted_gap < 1.1

print('PASS: critical threshold, unique numerical branches, superattracting gain,')
print('      finite hitting exception, critical relaxation and Gaussian tails')
print('critical gain:', format(AC, '.15f'))
print('superattracting u, gain:', format(us,'.15f'), format(ass,'.15f'))
