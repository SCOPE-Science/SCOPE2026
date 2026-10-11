#!/usr/bin/env python3
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def vp(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v

def sigma_prime_power(q, a):
    return (q ** (a + 1) - 1) // (q - 1)

def floor_log_prime_power(p, q, a):
    # exact integer floor of log_p(q^a)
    target = q ** a
    v = 0
    t = 1
    while t * p <= target:
        t *= p
        v += 1
    return v

for p in (3, 5):
    for q in range(p + 1, 500):
        if not is_prime(q):
            continue
        for a in range(1, 81):
            v = vp(sigma_prime_power(q, a), p)
            assert v <= floor_log_prime_power(p, q, a), (p, q, a, v)

# Exact checks of the key elementary inequalities at their boundary cases.
assert (5 + 1) // 2 < 5
assert 4 <= 5 ** 2
assert (7 * 7 + 1) // 2 < 7 * 7
assert 4 <= 7

print("VERIFY_OK")
