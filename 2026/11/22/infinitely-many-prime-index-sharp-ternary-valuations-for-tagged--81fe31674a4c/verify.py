#!/usr/bin/env python3
"""Exact finite arithmetic checks for a tagged odd-part partition theorem.

This diagnostic does not replace the analytic modular-form and prime-Hecke proof.
Run: python3 verify.py
"""
from fractions import Fraction
from math import gcd, isqrt


def sigma_1(n):
    total = 0
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            total += d
            if d * d != n:
                total += n // d
    return total


def eta_product(limit, exponents):
    """Exact q^0..q^limit terms in product_{d>=1} E(q^d)^e_d."""
    logarithm = [0] * (limit + 1)
    for d, exponent in exponents.items():
        for k in range(d, limit + 1, d):
            logarithm[k] -= exponent * d * sigma_1(k // d)
    coefficients = [1] + [0] * limit
    for n in range(1, limit + 1):
        value = sum(logarithm[k] * coefficients[n - k] for k in range(1, n + 1))
        assert value % n == 0
        coefficients[n] = value // n
    return coefficients


def isprime(n):
    if n < 2:
        return False
    return all(n % d for d in range(2, isqrt(n) + 1))


h = eta_product(580, {1: -13, 2: 8, 3: 7})
t = eta_product(800, {1: -2, 2: 1, 3: 2, 6: -1, 12: 2})
for n in range(1, 101):
    assert t[8*n-1] == 36 * h[n-1]
for n in range(1, 34):
    assert t[24*n-1] % 27 == 0
    assert ((t[24*n-1] // 27) + (t[8*n-1] // 9)) % 3 == 0

# Finite-order eta-cusp criterion, with exact rational arithmetic.
N = 18
exponents = {1: -13, 2: 8, 3: 7}
assert sum(exponents.values()) == 2
assert sum(d*e for d,e in exponents.items()) == 24
assert sum((N//d)*e for d,e in exponents.items()) == -120
orders = []
for c in (1, 2, 3, 6, 9, 18):
    inner = sum((Fraction(e * gcd(c, d)**2, d) for d,e in exponents.items()), Fraction(0))
    orders.append(Fraction(N, 24*gcd(c*c,N))*inner)
assert orders == [-5,2,1,1,1,1]
assert [v+a for v,a in zip(orders, [6,3,0,0,0,0])] == [1,5,1,1,1,1]

# The Eisenstein difference has a_0=-80 and all later coefficients divisible by 3.
# At a fixed q^n the 3-adic congruence F=H*A = H follows.
assert -80 % 3 == 1
for n in range(1, 100):
    sn = sum(d**3 for d in range(1,n+1) if n%d==0)
    tn = sum(d**3 for d in range(1,n//3+1) if n%3==0 and (n//3)%d==0)
    assert (240*sn-19440*tn)%3 == 0

sample_primes=[p for p in range(2,581) if p%54==1 and isprime(p)]
assert sample_primes == [109,163,271,379,433,487,541]
for p in sample_primes:
    assert h[p-1]%3 == 2
print('TAGGED_PRIME_SHARPNESS_FINITE_OK 100 33 6',len(sample_primes))
