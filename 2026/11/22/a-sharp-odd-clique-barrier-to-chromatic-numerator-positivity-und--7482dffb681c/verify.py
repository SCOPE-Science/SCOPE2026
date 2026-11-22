#!/usr/bin/env python3
"""Exact standard-library checks for signed-clique tree extensions."""
from fractions import Fraction
from math import comb, factorial
from itertools import product
from functools import lru_cache


@lru_cache(None)
def stirling(n, k):
    values = [[0] * (n + 1) for _ in range(n + 1)]
    values[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            values[i][j] = values[i-1][j-1] + j * values[i-1][j]
    return values[n][k]


@lru_cache(None)
def clique_z(n, q):
    out = 0
    for j in range(1, n+1):
        term = 1
        for k in range(j):
            term *= (q-2*k)
        out += stirling(n,j) * term
    return out


def h_coeffs(n, r):
    N = n+r
    # chi(q)=Z(q-1)(q-2)^r, with 0**0=1 at r=0.
    chi = lambda q: clique_z(n, q-1) * (q-2)**r
    return [0]+[sum((-1)**j*comb(N+1,j)*chi(i-j) for j in range(i)) for i in range(1,N+2)]


def direct_even_colors(n, q):
    palette = list(range(1, q//2+1)) + list(range(-1, -q//2-1, -1))
    count = 0
    for w in product(palette, repeat=n):
        if all(w[i] != -w[j] for i in range(n) for j in range(i+1,n)):
            count += 1
    return count


def a(j):
    coeff = Fraction(1)
    for i in range(1,j+1):
        coeff *= Fraction(5-2*i,2*i)
    return (-1)**j * coeff / 2**j


def main():
    for n in (3,4,5):
        for q in (2,4,6):
            assert clique_z(n,q) == direct_even_colors(n,q), (n,q)
    print('DIRECT_SIGNED_COLOR_COUNTS n=3,4,5 q=2,4,6 PASS')

    expected = {
        3: [0,0,0,2,8,14],
        5: [0,0,0,2,22,162,82,452],
    }
    for n, profile in expected.items():
        assert h_coeffs(n,1) == profile, (n,h_coeffs(n,1))
        assert sum(profile) == factorial(n+1)
        for r in range(1,17):
            N=n+r
            h=h_coeffs(n,r)
            assert all(c>=0 for c in h)
            if r<16:
                nxt=h_coeffs(n,r+1)
                assert all(nxt[i] == (i-2)*(h[i] if i<len(h) else 0)+(N+4-i)*h[i-1] for i in range(1,len(nxt)))
    print('LOW_ODD_CASES_AND_BRIDGE_RECURRENCE r=1..16 PASS')

    finite_bound = sum(a(j)*Fraction(2*j-3,3)**7 for j in range(3,9))
    assert finite_bound == Fraction(731229629,679477248) and finite_bound > 1
    assert a(1)==Fraction(-3,4) and all(a(j)>0 for j in range(2,80))
    print('RATIONAL_EGF_SIGN_CERTIFICATE',str(finite_bound),'PASS')

    for n in range(7,32,2):
        assert clique_z(n,3) < 0
        assert clique_z(n,1) > 0
        assert h_coeffs(n,0)[3] < 0
        for r in range(1,6):
            h=h_coeffs(n,r)
            assert h[4] == 2**r*clique_z(n,3)-2*(n+r+1) < 0
    print('ODD_SIGN_AND_NUMERATOR_CHECKS n=7..31 r=0..5 PASS')
    for n in (3,5):
        assert h_coeffs(n,0)[3] < 0
    print('NO_BRIDGE_BASE_CASES PASS')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
