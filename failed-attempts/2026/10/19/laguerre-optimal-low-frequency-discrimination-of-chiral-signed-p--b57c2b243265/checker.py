#!/usr/bin/env python3
"""Exact and high-precision independent evaluations for octahedral-orbit Fourier contrast."""
from itertools import permutations, product
from math import factorial
from functools import reduce
import sympy as sp
import mpmath as mp


def signed_permutation_group(n):
    for perm in permutations(range(n)):
        parity = (-1) ** sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        for signs in product((-1, 1), repeat=n):
            det = parity * reduce(lambda a, b: a * b, signs, 1)
            yield perm, signs, det


def h(x):
    a = sp.prod(x)
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            a *= x[j] ** 2 - x[i] ** 2
    return a


def fischer(n):
    return factorial(n) * sp.prod(factorial(2*j - 1) for j in range(1, n+1))


def exact_moment(n):
    v = tuple(range(1, n+1))
    omega = tuple((i+1)**2+1 for i in range(n))
    degree = n*n
    total = 0
    for perm, signs, det in signed_permutation_group(n):
        dot = sum(omega[i]*signs[i]*v[perm[i]] for i in range(n))
        total += det * dot**degree
    expected = factorial(degree)*(2**n)*factorial(n)*int(h(v))*int(h(omega))//int(fischer(n))
    assert total == expected, (n, total, expected)
    return len(tuple(signed_permutation_group(n))), len(str(abs(total)))


def polynomial_discriminant(n):
    z=sp.symbols('z')
    p=sp.Poly(sp.expand((-1)**n*factorial(n)*sp.laguerre(n,z)), z)
    disc=sp.discriminant(p.as_expr(), z) if n>=2 else sp.Integer(1)
    expected=sp.prod(j**(2*j-1) for j in range(2,n+1))
    assert disc == expected
    return disc


def high_precision_limit(n, r):
    mp.mp.dps=105
    z=sp.symbols('z')
    roots=sorted([float(sp.re(x)) for x in sp.nroots((-1)**n*factorial(n)*sp.laguerre(n,z))])
    a=[mp.sqrt(mp.mpf(str(x))/n**2) for x in roots]
    aa=mp.sqrt(sum(x*x for x in a))
    a=[x/aa for x in a]
    b=list(reversed(a))
    rr=mp.mpf(str(r))
    total=mp.mpc(0)
    for perm, signs, det in signed_permutation_group(n):
        dot=sum(b[i]*signs[i]*a[perm[i]] for i in range(n))
        total+=det *mp.exp(-2j*mp.pi*rr*dot)
    total*=mp.mpf(2)/(2**n*factorial(n))
    leading=mp.power(-2j*mp.pi*rr,n*n)*mp.mpf(2)/int(fischer(n))
    for t in (a,b):
        leading*=mp.mpf(str(h(t))) if n<=2 else mp.mpf(str(h(t)))
    return mp.nstr(total/leading, 18)


def main():
    print('Exact signed Fourier moments and Macdonald/Fischer normalization:')
    for n in range(1,5):
        count, digits=exact_moment(n)
        disc=polynomial_discriminant(n)
        M2=sp.factorial(n)*disc/sp.Integer(n)**(2*n*n)
        print(f'n={n}, group_size={count}, degree={n*n}, F={fischer(n)}, discriminant={disc}, sharp_M_squared={M2}, moment_digits={digits}, PASS')
    for n,r in [(3,sp.Rational(1,10)),(3,sp.Rational(1,20))]:
        print('Fourier-to-leading ratio n=',n,'r=',r,'value=',high_precision_limit(n,float(r)))
    print('ALL CHECKS PASSED; asymptotic uniformity and optimizer uniqueness require the analytic proof.')

if __name__ == '__main__': main()
