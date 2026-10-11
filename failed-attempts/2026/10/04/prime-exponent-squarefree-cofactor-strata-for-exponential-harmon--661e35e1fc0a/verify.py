#!/usr/bin/env python3
from math import gcd


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


def factor(n):
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def divisors(n):
    ds = []
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0:
            ds.append(d)
            if d * d != n:
                ds.append(n // d)
    return sorted(ds)


def squarefree(n):
    return all(e == 1 for e in factor(n).values())


def e_harmonic_flags(n):
    fac = factor(n)
    d_e = 1
    sigma_e = 1
    S_e = 1
    for p, a in fac.items():
        ds = divisors(a)
        d_e *= len(ds)
        sigma_e *= sum(p ** d for d in ds)
        S_e *= sum(p ** (a - d) for d in ds)
    return (n * d_e) % sigma_e == 0, (n * d_e) % S_e == 0


primes = [p for p in range(2, 60) if is_prime(p)]
prime_exponents = [ell for ell in range(2, 12) if is_prime(ell)]
checked = 0
type2_hits = []
for p in primes:
    for ell in prime_exponents:
        for m in range(1, 1001):
            if gcd(p, m) != 1 or not squarefree(m):
                continue
            n = p ** ell * m
            t1, t2 = e_harmonic_flags(n)
            predicted_t1 = False
            predicted_t2 = (2 * m) % (p ** (ell - 1) + 1) == 0
            assert t1 == predicted_t1, (p, ell, m, n, t1)
            assert t2 == predicted_t2, (p, ell, m, n, t2, predicted_t2)
            checked += 1
            if t2 and len(type2_hits) < 12:
                type2_hits.append(n)

expected = [12, 18, 40, 60, 75, 84, 132, 135, 156, 204]
for n in expected:
    assert e_harmonic_flags(n)[1]

print("VERIFY_OK checked=%d sample_type2=%s" % (checked, type2_hits))
