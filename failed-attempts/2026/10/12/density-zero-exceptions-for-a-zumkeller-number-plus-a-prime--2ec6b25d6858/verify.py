#!/usr/bin/env python3
"""Small exact arithmetic checks supporting a separately proved density theorem.

Uses the Python standard library only. Finite tests do not establish any infinite claim.
"""
from math import gcd, isqrt

def prime(n):
    if n < 2: return False
    return all(n % p for p in range(2, isqrt(n) + 1))

def divisors(n):
    out = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n: out.append(n // d)
    return sorted(out)

def zumkeller(n):
    D = divisors(n)
    S = sum(D)
    if S & 1: return False
    bits = 1
    for d in D:
        bits |= bits << d
    return bool((bits >> (S // 2)) & 1)

assert zumkeller(6) and zumkeller(945) and zumkeller(15015)
for t in range(101):
    w = 1 + 6 * t
    assert gcd(6, w) == 1
    assert zumkeller(6 * w)
print('small_coprime_Zumkeller_closure_101_cases=PASS')

z = 6
m = z * z
reduced = [a for a in range(m) if gcd(a, z) == 1]
reps = {}
for a in reduced:
    q = 2
    while (q - (a - z)) % m or not prime(q):
        q += 1
    reps[a] = q
B = z + max(reps.values())
for n in range(B + 1, 10001):
    if gcd(n, z) != 1: continue
    q = reps[n % m]
    t, rem = divmod(n - q - z, m)
    assert rem == 0 and t >= 0 and prime(q)
    assert zumkeller(n - q)
print('reduced_residue_classes_mod_36=%d_PASS' % len(reduced))
print('fixed_modulus_representation_n_le_10000=PASS')
print('example_odd_prime_block_15015_zumkeller=PASS')
print('finite_checks_do_not_certify_density_limit')
