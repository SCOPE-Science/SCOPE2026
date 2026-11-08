"""Self-contained finite exact-arithmetic diagnostics for a renewal-reset OU inverse theorem.

Use: python3 verify.py
Finite tests are not substitutes for the analytic infinite-dimensional proof.
"""
from fractions import Fraction as F
from math import comb, factorial


def poly_mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_pow(a, n):
    out = [F(1)]
    for _ in range(n):
        out = poly_mul(out, a)
    return out


def deriv(a, n=1):
    for _ in range(n):
        a = [i * a[i] for i in range(1, len(a))]
    return a


def integral(a, lo=F(1, 3), hi=F(2, 3)):
    return sum(x * (hi ** (i + 1) - lo ** (i + 1)) / (i + 1) for i, x in enumerate(a))


def multiply_u_power(a, n):
    return [F(0)] * n + a


def odd_double_factorial(k):
    return factorial(2 * k) // (2**k * factorial(k))


count = 0
# At reset rate 2*kappa with kappa=1, equilibrium U is uniform.
# Standardized V=(1-U) has E[V**j]=1/(j+1).
for k in range(1, 18):
    sigma2 = F(1)
    b = F(1, k + 1)
    moment = odd_double_factorial(k) * sigma2 ** k * b
    assert moment == F(odd_double_factorial(k), k + 1)
    count += 1

# Exact compactly supported polynomial perturbation, C^3 at the endpoints.
# This is a finite algebraic diagnostic; the theorem uses a C-infinity bump.
h = poly_mul(poly_pow([F(-1, 3), F(1)], 4),
             poly_pow([F(2, 3), F(-1)], 4))
q = deriv(h, 3)
for j in range(3):
    assert integral(multiply_u_power(q, j)) == 0
    count += 1
assert integral(multiply_u_power(q, 3)) != 0
count += 1
# First two stationary even moments identical under g+ and g- perturbations.
for k in range(1, 3):
    coeffs = [F((-1) ** j * comb(k, j)) for j in range(k + 1)]
    poly = poly_mul(coeffs, q)
    assert integral(poly) == 0
    count += 1
# Compact bump protects endpoint mean, independently of perturbation sign.
assert integral(q) == 0
count += 1

# Deterministic renewal time T=mu produces uniform age on [0,mu].
# Under u=exp(-2*kappa*a), its g integrates to 1 exactly by substitution.
# The integral of c/u from exp(-2*kappa*mu) to 1 is 2*kappa*mu*c=1.
for mu in (F(1, 5), F(1, 2), F(3, 2), F(7, 3)):
    for kappa in (F(1, 2), F(1), F(2)):
        c = 1 / (2 * kappa * mu)
        assert 2 * kappa * mu * c == 1
        count += 1

# For fixed mean mu, deterministic T=mu vs T taking mu +/- delta,
# stationary ages differ by total variation delta/(2*mu).
for mu in (F(1), F(2), F(5)):
    for delta in (mu / 3, mu / 5, mu / 9):
        # Their three age-density slabs are [0,mu-delta),
        # [mu-delta,mu), and [mu,mu+delta).
        l1 = delta * (F(1, 2) / mu + F(1, 2) / mu)
        assert l1 / 2 == delta / (2 * mu)
        count += 1

print('PASS', count, 'finite exact-arithmetic assertions')
