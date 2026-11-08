#!/usr/bin/env python3
"""Exact scalar certificates for radius-one Schur masks of stars.

Requires only Python's standard library. The universal proof is analytic;
finite checks corroborate its rational and rank-two identities.
"""
from fractions import Fraction as F


def check(n):
    assert isinstance(n, int) and n >= 1
    denom = 3*n+1
    t = F(5*n-1, denom)
    x = F(2*(n-1), denom)
    d = 1-x
    q = F(n+1, denom)
    r = F(2, denom)
    count = 0
    def eq(a, b):
        nonlocal count
        assert a == b, (n, a, b)
        count += 1
    eq(t, 1+x)
    eq(q+n*r, 1)
    eq((q-r)**2+4*n*q*r, 1)
    eq((n-1)*r+1, t)
    eq((2*(n+1)+(n-1)+2*(n-1)), 5*n-1)
    eq(t-x-1, 0)  # leaf-orthogonal eigenvalue, H-M
    eq(t-x+1, 2)  # leaf-orthogonal eigenvalue, H+M
    eq((t-1)*(t+(n-1)*x-1)-n*(d-1)**2, 0)
    eq((t+1)*(t+(n-1)*x+1)-n*(d+1)**2, 0)
    eq(t-1 >= 0, True)
    eq(t+(n-1)*x-1 >= 0, True)
    eq(t+1 > 0, True)
    eq(t+(n-1)*x+1 > 0, True)
    eq(t, F(5, 3)-F(8, 3*(3*n+1)))
    eq(t >= 1, True)
    return count


def main():
    count = 0
    for n in range(1, 1025):
        count += check(n)
    print(f'STAR_BALL_EXACT_CERTIFICATES_OK {count}')


if __name__ == '__main__':
    main()
