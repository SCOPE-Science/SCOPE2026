#!/usr/bin/env python3
"""Exact finite-field spot checks for alternating Frobenius hypersurfaces.

The infinite-family statements require the mathematical proof; the tests
independently enumerate small extension fields and projective representatives.
"""
from itertools import product


def extension_field(p):
    """Return arithmetic in F_(p^2) as integer-coded pairs."""
    if p == 2:
        b, c = 1, 1  # u^2 = u + 1
    else:
        b = next(x for x in range(2, p) if pow(x, (p - 1) // 2, p) == p - 1)
        c = 0  # u^2 = b
    Q = p * p
    def mul(x, y):
        a0, a1 = x % p, x // p
        d0, d1 = y % p, y // p
        return (a0 * d0 + b * a1 * d1) % p + p * ((a0 * d1 + a1 * d0 + c * a1 * d1) % p)
    def power(x, exponent):
        out = 1
        while exponent:
            if exponent & 1:
                out = mul(out, x)
            x = mul(x, x)
            exponent >>= 1
        return out
    return Q, mul, power


def binary_extension(s):
    """Exact GF(2^s) arithmetic with fixed irreducible binary moduli."""
    moduli = {3: 0b1011, 4: 0b10011}
    modulus = moduli[s]
    Q = 1 << s
    def mul(x, y):
        out = 0
        while y:
            if y & 1:
                out ^= x
            x <<= 1
            if x & Q:
                x ^= modulus
            y >>= 1
        return out
    def power(x, exponent):
        out = 1
        while exponent:
            if exponent & 1:
                out = mul(out, x)
            x = mul(x, x)
            exponent >>= 1
        return out
    return Q, mul, power


def projective_points(Q, dimension):
    for first in range(dimension):
        for tail in product(range(Q), repeat=dimension - first - 1):
            yield (0,) * first + (1,) + tail


def count(p, m, extension_degree, rank=None):
    if extension_degree == 1:
        Q = p
        mul = lambda x, y: (x * y) % p
        power = lambda x, k: pow(x, k, p)
    elif extension_degree == 2:
        Q, mul, power = extension_field(p)
    elif p == 2 and extension_degree in (3, 4):
        Q, mul, power = binary_extension(extension_degree)
    else:
        raise ValueError("unsupported finite field")
    rank = m if rank is None else rank
    total = 0
    for v in projective_points(Q, 2 * m):
        F = 0
        for i in range(rank):
            x, y = v[2 * i], v[2 * i + 1]
            F = (F + 0)  # use finite-field addition on integer-coded pairs
            lhs = mul(power(x, p), y)
            rhs = mul(x, power(y, p))
            if extension_degree == 1:
                F = (F + lhs - rhs) % p
            elif p == 2 and extension_degree in (3, 4):
                F ^= lhs ^ rhs
            else:
                a = (F % p + lhs % p - rhs % p) % p
                b = (F // p + lhs // p - rhs // p) % p
                F = a + p * b
        if F == 0:
            total += 1
    return total


def predicted(p, m, s, rank=None):
    rank = m if rank is None else rank
    k = 2 * (m - rank)
    q_s = p**s
    b = (p**(2 * rank) + p) // (p + 1)
    a = (b + p**rank) // 2
    c = (b - p**rank) // 2
    smooth_count = sum(p**(i * s) for i in range(2 * rank - 1))
    smooth_count += p**((rank - 1) * s) * (a + ((-1) ** s) * c)
    return sum(q_s**i for i in range(k)) + q_s**k * smooth_count


def check():
    checks = [(2, 1, 1, None), (2, 2, 1, None), (2, 2, 2, None),
              (2, 3, 1, None), (2, 3, 2, None), (3, 2, 1, None),
              (3, 2, 2, None), (5, 2, 1, None), (5, 2, 2, None),
              (2, 2, 3, None), (2, 2, 4, None),
              (2, 2, 1, 1), (2, 2, 2, 1), (3, 2, 2, 1)]
    for p, m, s, rank in checks:
        got = count(p, m, s, rank)
        want = predicted(p, m, s, rank)
        assert got == want, (p, m, s, rank, got, want)
        print(f"PASS p={p} m={m} s={s} rank={rank or m}: {got}")
    print(f"PASS {len(checks)} exhaustive finite-field enumerations")


if __name__ == '__main__':
    check()
