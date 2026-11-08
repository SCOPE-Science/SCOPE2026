#!/usr/bin/env python3
"""Exact checks for the Gauss-fixed trace description of cyclic cubic hypersurfaces.

No external dependencies. A finite check supports the general algebraic proof;
it is not used as an infinite proof.
"""
from itertools import product


def monomials_f(n):
    out = []
    for i in range(n):
        e = [0] * n
        e[i] += 2
        e[(i + 1) % n] += 1
        out.append(tuple(e))
    return out


def squared_monomials(monomials):
    return {tuple(2 * z for z in m) for m in monomials}


def f_of_gradient_monomials(n):
    # dF/dX_i = X_(i-1)^2 in characteristic two.
    return {tuple(4 * int(j == (i - 1) % n) +
                  2 * int(j == i) for j in range(n))
            for i in range(n)}


def poly_mul(a, b):
    v = 0
    while b:
        if b & 1:
            v ^= a
        b >>= 1
        a <<= 1
    return v


def poly_rem(a, b):
    while a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length() - b.bit_length())
    return a


def gf_mul(a, b, mod=0b100101):  # u^5+u^2+1
    return poly_rem(poly_mul(a, b), mod)


def gf_pow(a, n):
    v = 1
    while n:
        if n & 1:
            v = gf_mul(v, a)
        a = gf_mul(a, a)
        n >>= 1
    return v


def trace(a):
    s = 0
    for i in range(5):
        s ^= gf_pow(a, 1 << i)
    return s


def frob_orbits(elements):
    left = set(elements)
    orbits = []
    while left:
        a = min(left)
        orb = []
        while a not in orb:
            orb.append(a)
            a = gf_mul(a, a)
        assert a == orb[0]
        assert set(orb) <= left
        left -= set(orb)
        orbits.append(orb)
    return orbits


def check():
    for n in range(3, 11):
        assert squared_monomials(monomials_f(n)) == f_of_gradient_monomials(n)
        # T_n^2 + T_n = a^(2^n) + a, as polynomial over F_2.
        t = sum(1 << (1 << i) for i in range(n))
        assert poly_mul(t, t) ^ t == ((1 << (1 << n)) ^ (1 << 1))
        # Every formal derivative of T_n is 1.
        assert (t & (1 << 1)) and all((1 << i) % 2 == 0 for i in range(1, n))
    print('FROBENIUS_AND_TRACE_POLYNOMIAL_IDENTITIES n=3..10 OK')

    # T_5(a)/a = a^15 + a^7 + a^3 + a + 1.
    p = sum(1 << ((1 << i) - 1) for i in range(5))
    assert p == ((1 << 15) | (1 << 7) | (1 << 3) | (1 << 1) | 1)
    factors = [(1 << 5) | (1 << 2) | 1,
               (1 << 5) | (1 << 3) | 1,
               (1 << 5) | (1 << 3) | (1 << 2) | (1 << 1) | 1]
    v = 1
    for f in factors:
        v = poly_mul(v, f)
        for degree in (1, 2):
            for low in range(1 << degree):
                candidate = (1 << degree) | low
                assert poly_rem(f, candidate) != 0
    assert v == p
    print('THREE_DISTINCT_IRREDUCIBLE_QUINTIC_FACTORS OK')

    roots = [a for a in range(1, 32) if trace(a) == 0]
    assert len(roots) == 15
    assert trace(1) == 1
    assert all(gf_pow(a, 31) == 1 for a in roots)
    for a in roots:
        point = [gf_pow(a, 1 << i) for i in range(5)]
        grad = [gf_mul(point[(i - 1) % 5], point[(i - 1) % 5])
                for i in range(5)]
        assert grad == point
        f_val = 0
        for i in range(5):
            f_val ^= gf_mul(gf_mul(point[i], point[i]), point[(i + 1) % 5])
        assert f_val == 0
    orbits = frob_orbits(roots)
    assert sorted(map(len, orbits)) == [5, 5, 5]
    print('F32_TRACE_ZERO_NONZERO=15 FROBENIUS_ORBITS=[5,5,5] OK')
    print('VERIFY_OK')


if __name__ == '__main__':
    check()
