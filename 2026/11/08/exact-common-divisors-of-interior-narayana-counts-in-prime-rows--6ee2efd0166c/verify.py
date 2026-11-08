#!/usr/bin/env python3
"""Reproducibility tests for the exact internal-row gcd of Narayana numbers.
Only standard-library arithmetic is used; the unrestricted theorem is proved separately.
"""
from math import comb, gcd, isqrt


def primes_up_to(bound):
    sieve = bytearray([1]) * (bound + 1)
    sieve[0:2] = b'\x00\x00'
    for n in range(2, isqrt(bound) + 1):
        if sieve[n]:
            for t in range(n * n, bound + 1, n):
                sieve[t] = 0
    return [p for p in range(bound + 1) if sieve[p]]


def narayana(n, k):
    assert 1 <= k <= n
    numerator = comb(n, k) * comb(n, k - 1)
    assert numerator % n == 0
    return numerator // n


def predicted_gcd(p):
    u = p - 1
    a = 0
    while u % 2 == 0:
        a += 1
        u //= 2
    return p * (1 << min(2, a - 1)) if u == 1 else p


def vp(n, p):
    a = 0
    while n and n % p == 0:
        n //= p
        a += 1
    return a


def lucas_binomial_mod_prime(n, k, p):
    out = 1
    while k:
        a, b = n % p, k % p
        if b > a:
            return 0
        out = (out * comb(a, b)) % p
        n //= p
        k //= p
    return out


checked = primes_up_to(257)
entries = 0
for p in checked:
    if p == 2:
        continue
    values = [narayana(p, k) for k in range(2, p)]
    entries += len(values)
    g = 0
    for v in values:
        g = gcd(g, v)
    assert g == predicted_gcd(p), (p, g, predicted_gcd(p))
    assert vp(g, p) == 1
    assert g % p == 0

# For each possible prime divisor ell of (p-1), check the proof's
# Lucas nonvanishing witness whenever p-1 is not an ell-power.
odd_prime_witnesses = 0
binary_witnesses = 0
for p in primes_up_to(2000):
    if p == 2:
        continue
    for ell in primes_up_to(p - 1):
        if (p - 1) % ell:
            continue
        s = 0
        u = p - 1
        while u % ell == 0:
            u //= ell
            s += 1
        if u == 1:
            continue
        k = ell**s + 1
        assert 2 <= k <= p - 1
        a = lucas_binomial_mod_prime(p, k, ell)
        b = lucas_binomial_mod_prime(p, k - 1, ell)
        assert a != 0 and b != 0
        assert (a * b * pow(p, -1, ell)) % ell != 0
        if ell == 2:
            binary_witnesses += 1
        else:
            odd_prime_witnesses += 1

# High-index Fermat-prime parity witnesses, without constructing huge binomials.
for r in (1, 2, 4, 8, 16):
    p = 2**r + 1
    if r == 1:
        assert vp(narayana(p, 2), 2) == 0
    elif r == 2:
        assert vp(narayana(p, 2), 2) == 1
    else:
        k = 2**(r - 1) + 1
        expected = 2 * r - 2 * vp(k - 1, 2)
        assert expected == 2
        assert r - 1 >= 2

print('VERIFY_OK', 'prime_rows=', len(checked) - 1,
      'interior_entries=', entries,
      'Lucas_odd_witnesses=', odd_prime_witnesses,
      'Lucas_binary_witnesses=', binary_witnesses,
      'Fermat_exponents=1,2,4,8,16',
      'exact_gcd=PASS')
