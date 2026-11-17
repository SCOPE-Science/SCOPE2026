#!/usr/bin/env python3
"""Exact characteristic-two consistency checks for the specified cuspidal plane curves.

The symbolic proof of the all-n stabilizer theorem is in RESULT.md; this finite
checker verifies the normalizing polynomial identities and examples only.
"""
from math import gcd


def f2mul(a, b):
    c = 0
    while b:
        if b & 1:
            c ^= a
        a <<= 1
        b >>= 1
    return c


def f2pow(a, n):
    v = 1
    while n:
        if n & 1:
            v = f2mul(v, a)
        a = f2mul(a, a)
        n >>= 1
    return v


def field_mul(a, b, modulus, degree):
    ans = 0
    mask = (1 << degree) - 1
    while b:
        if b & 1:
            ans ^= a
        b >>= 1
        a <<= 1
        if a & (1 << degree):
            a ^= modulus
        a &= mask
    return ans


def field_pow(a, n, modulus, degree):
    out = 1
    while n:
        if n & 1:
            out = field_mul(out, a, modulus, degree)
        a = field_mul(a, a, modulus, degree)
        n >>= 1
    return out


def test_identity(n):
    q = 1 << n
    t = 0b10
    x, y = f2pow(t, q), f2pow(t, q + 2) ^ t
    assert f2pow(y, q) == f2pow(x, q + 2) ^ x
    recovered = f2pow(x, q)
    for j in range(n):
        recovered ^= f2mul(f2pow(x, (1 << j) - 1), f2pow(y, 1 << j))
    assert recovered == t, (n, recovered)


def test_field(n, modulus):
    q = 1 << n
    degree = 2*n
    size = 1 << degree
    roots = [a for a in range(1, size) if field_pow(a, q + 1, modulus, degree) == 1]
    assert len(roots) == q + 1, (n, roots)
    # For every field element on the parameter line, the derived diagonal action
    # matches parameter multiplication. This is finite consistency, not completeness.
    for a in roots:
        aq = field_pow(a, q, modulus, degree)
        for t in range(size):
            x = field_pow(t, q, modulus, degree)
            y = field_pow(t, q + 2, modulus, degree) ^ t
            X = field_mul(aq, x, modulus, degree)
            Y = field_mul(a, y, modulus, degree)
            T = field_mul(a, t, modulus, degree)
            assert X == field_pow(T, q, modulus, degree)
            assert Y == field_pow(T, q + 2, modulus, degree) ^ T
    for r in range(1, 2*n + 1):
        assert len([a for a in roots if field_pow(a, (1 << r) - 1, modulus, degree) == 1]) == gcd(q + 1, (1 << r) - 1)
    assert all(field_pow(a, (1 << r) - 1, modulus, degree) != 1
               for r in range(1, 2*n) for a in roots
               if all(field_pow(a, (q + 1)//p, modulus, degree) != 1
                      for p in prime_factors(q + 1)))
    print('FIELD_OK', 'n=', n, 'geometric_order=', len(roots), 'full_descent_degree=', 2*n)


def prime_factors(n):
    ans = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            ans.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        ans.append(n)
    return ans


if __name__ == '__main__':
    for n in range(2, 7):
        test_identity(n)
        print('POLYNOMIAL_OK', 'n=', n, 'q=', 1 << n)
    for n, irreducible in ((2, 0x13), (3, 0x43), (4, 0x11b)):
        test_field(n, irreducible)
    print('CERTIFICATE_OK')
