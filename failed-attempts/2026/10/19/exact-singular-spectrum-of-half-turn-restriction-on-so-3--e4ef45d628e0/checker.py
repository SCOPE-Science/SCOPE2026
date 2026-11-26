"""Exact-arithmetic checks for the half-turn SO(3) Fourier restriction theorem.

The checker uses polynomial recurrences and rational integration;
finite tests corroborate but do not establish the all-bandwidth proof.
Requires only Python 3.9+ standard library.
"""
from fractions import Fraction as F
from math import comb


def add(a, b):
    return [(a[i] if i < len(a) else F(0)) +
            (b[i] if i < len(b) else F(0))
            for i in range(max(len(a), len(b)))]


def scale(a, c):
    return [c * v for v in a]


def shift(a):
    return [F(0)] + a


def mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            out[i + j] += u * v
    return out


def cheb_u(n):
    a, b = [F(1)], [F(0), F(2)]
    if n == 0:
        return a
    for _ in range(1, n):
        a, b = b, add(scale(shift(b), 2), scale(a, -1))
    return b


def legendre(n):
    a, b = [F(1)], [F(0), F(1)]
    if n == 0:
        return a
    for k in range(1, n):
        a, b = b, scale(add(scale(shift(b), 2*k+1),
                          scale(a, -k)), F(1, k+1))
    return b


def average(p):
    return sum((v/F(k+1) for k, v in enumerate(p)
                if k % 2 == 0), F(0))


def derivative(p):
    return [F(i) * p[i] for i in range(1, len(p))]


def check(L):
    kernel = [F(0)]
    for ell in range(L):
        kernel = add(kernel, scale(cheb_u(2*ell), 2*ell+1))
    assert kernel == scale(derivative(cheb_u(2*L-1)), F(1, 2))
    eig = [average(mul(kernel, legendre(2*j))) for j in range(L)]
    assert eig[0] == L
    assert all(eig[j] > eig[j+1] for j in range(L-1))
    assert eig[-1] == F((2*L-1)*2**(4*L-4),
                        (4*L-3)*comb(4*L-4, 2*L-2))
    assert sum(((4*j+1)*v for j,v in enumerate(eig)),F(0)) == \
        sum((2*k+1)**2 for k in range(L))
    assert sum(4*j+1 for j in range(L)) == 2*L*L-L
    return eig


if __name__ == '__main__':
    for L in range(1,13):
        ev = check(L)
        print('L=%d rank=%d max=%s min=%s cond2=%s' %
              (L, 2*L*L-L, ev[0], ev[-1], ev[0]/ev[-1]))
    print('Exact finite checks passed; the universal proof is in RESULT.md.')
