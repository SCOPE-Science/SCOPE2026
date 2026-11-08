#!/usr/bin/env python3
"""Exact finite tests for Fourier spectra of pairs of matrices with zero product.
Uses only Python standard library. Coefficients are calculated as integers,
including an exact Eisenstein-integer DFT for characteristic three.
"""
from itertools import product
from math import prod


def gf_mul(a, b, q):
    if q in (2, 3):
        return (a * b) % q
    assert q == 4
    x = 0
    for i in range(2):
        if (b >> i) & 1:
            x ^= a << i
    if x & 8:
        x ^= 0b1100  # x^3 -> x^2+x via x^2=x+1
    if x & 4:
        x ^= 0b111   # x^2 -> x+1
    return x


def field_add(a, b, q):
    return (a + b) % q if q == 3 else a ^ b


def matrix_zero_product(A, B, n, q):
    for i in range(n):
        for j in range(n):
            t = 0
            for k in range(n):
                t = field_add(t, gf_mul(A[n*i+k], B[n*k+j], q), q)
            if t:
                return False
    return True


def fwt_binary(a):
    a = list(a)
    h = 1
    while h < len(a):
        for i in range(0, len(a), h*2):
            for j in range(h):
                u, v = a[i+j], a[i+j+h]
                a[i+j] = u+v
                a[i+j+h] = u-v
        h *= 2
    return a


def fft3_exact(a, dim):
    # Store c0+c1*zeta_3 as a pair; zeta_3^2=-1-zeta_3.
    a = [(z, 0) for z in a]
    stride = 1
    mul_zeta = lambda x: (-x[1], x[0]-x[1])
    plus = lambda x, y: (x[0]+y[0], x[1]+y[1])
    for _ in range(dim):
        for base in range(0, len(a), stride*3):
            for tail in range(stride):
                i = base+tail
                u, v, w = a[i], a[i+stride], a[i+2*stride]
                a[i] = plus(plus(u,v),w)
                a[i+stride] = plus(plus(u,mul_zeta(v)),mul_zeta(mul_zeta(w)))
                a[i+2*stride] = plus(plus(u,mul_zeta(mul_zeta(v))),mul_zeta(w))
        stride *= 3
    return a


def encode_binary(entries, q):
    bits = 1 if q == 2 else 2
    return sum(x << (bits*i) for i,x in enumerate(entries))


def encode_ternary(entries):
    z = 0
    for e in reversed(entries):
        z = z*3+e
    return z


def count_rank_matrices(n, q, r):
    return prod((q**n-q**i)**2 for i in range(r)) // prod(q**r-q**i for i in range(r))


def run_case(n, q):
    mat = list(product(range(q), repeat=n*n))
    dim = 2*n*n
    freq_count = q**dim
    f = [0]*freq_count
    for A in mat:
        for B in mat:
            if matrix_zero_product(A,B,n,q):
                key = encode_ternary(A+B) if q == 3 else encode_binary(A+B,q)
                f[key] = 1
    expected_card = sum(count_rank_matrices(n,q,r)*q**(n*(n-r)) for r in range(n+1))
    assert sum(f) == expected_card, (n,q,sum(f),expected_card)
    if q == 3:
        transformed = fft3_exact(f, dim)
        assert all(b == 0 for a,b in transformed)
        coeffs = [a for a,b in transformed]
    else:
        coeffs = fwt_binary(f)
    fac = q**(n*(n-1)//2)
    assert all(z % (q*fac) == ((-1)**n * fac) % (q*fac) for z in coeffs)
    assert min(abs(z) for z in coeffs) == fac
    assert max(abs(z) for z in coeffs) == expected_card
    assert all(z for z in coeffs)
    print('PASS', 'n='+str(n), 'q='+str(q), 'frequencies='+str(freq_count),
          'incidence_size='+str(expected_card), 'minimum_abs='+str(fac),
          'unique_values='+str(len(set(coeffs))), 'zero_coefficients=0')


if __name__ == '__main__':
    for args in [(2,2),(2,3),(2,4),(3,2)]:
        run_case(*args)
    print('ALL_ZERO_PRODUCT_FOURIER_CHECKS_OK')
