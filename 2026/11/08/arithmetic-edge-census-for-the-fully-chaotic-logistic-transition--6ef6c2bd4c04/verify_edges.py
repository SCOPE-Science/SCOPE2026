#!/usr/bin/env python3
"""Exact arithmetic checks for positive-measure one-step logistic bin transitions.

All interval endpoints are integer numerators over m*m. The checker is
supplementary finite verification, not a proof for all resolutions.
"""
from math import gcd


def least_square_root_divisor(m):
    q = m // gcd(m, 4)
    fac = []
    p = 2
    while p*p <= q:
        if q % p == 0:
            e = 0
            while q % p == 0:
                q //= p
                e += 1
            fac.append((p, e))
        p += 1 if p == 2 else 2
    if q > 1:
        fac.append((q, 1))
    r = 1
    for p, e in fac:
        r *= p**((e+1)//2)
    return r


def direct_edge_count(m):
    result = 0
    for j in range(m):
        v0 = 4*j*(m-j)
        v1 = 4*(j+1)*(m-j-1)
        lo = min(v0, v1)
        hi = m*m if 2*j < m < 2*(j+1) else max(v0, v1)
        for k in range(m):
            result += max(lo, k*m) < min(hi, (k+1)*m)
    return result


def main():
    tested = 0
    for m in range(2, 513):
        r = least_square_root_divisor(m)
        assert m % r == 0
        q = m//gcd(m, 4)
        assert (r*r) % q == 0
        expected = 3*m - m//r - (m % 2)
        actual = direct_edge_count(m)
        assert actual == expected, (m,r,actual,expected)
        assert m <= 4*r*r  # exact sharp global deficit bound
        tested += 1
    for k in range(1, 101):
        m = 4*k*k
        assert least_square_root_divisor(m) == k
        assert 3*m - m//k == 12*k*k - 4*k
    for m in (2000, 1999, 4096, 9999, 123456):
        r = least_square_root_divisor(m)
        print('edge_formula',m,3*m-m//r-(m%2),'R',r)
    print('VERIFY_OK exact_integer_adjacency_resolutions=',tested,
          'sharp_square_family_cases=100')

if __name__ == '__main__':
    main()
