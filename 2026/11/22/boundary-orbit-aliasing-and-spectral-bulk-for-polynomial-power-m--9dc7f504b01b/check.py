#!/usr/bin/env python3
"""Finite, supplementary checks for the polynomial power-map companion theorem.

Uses only the Python standard library. Does not certify infinite-dimensional assertions.
Run: python3 check.py
"""
import cmath
import math
import random
from fractions import Fraction

TESTS = 0

def check(flag, message):
    global TESTS
    TESTS += 1
    if not flag:
        raise AssertionError(message)


def normalization(n, alpha):
    if alpha == -1:  # H^2 endpoint
        return 1.0
    return math.exp(0.5 * (math.lgamma(n + alpha + 2) -
                           math.lgamma(alpha + 2) - math.lgamma(n + 1)))


def column(n, k, coeffs, alpha):
    if n == 0:
        return {}
    bn = normalization(n, alpha)
    return {k*n+j: a*n/(k*n+j)*bn/normalization(k*n+j, alpha)
            for j, a in enumerate(coeffs) if a != 0}


def gram(n, m, k, coeffs, alpha):
    a = column(n, k, coeffs, alpha)
    b = column(m, k, coeffs, alpha)
    return sum(x.conjugate()*b.get(j, 0) for j, x in a.items())


def residue_symbol(theta, k, coeffs):
    w = cmath.exp(1j*theta)
    return sum(abs(sum(a * w**j for j, a in enumerate(coeffs[r::k])))**2
               for r in range(k))


def orbit_symbol(theta, k, coeffs):
    return sum(abs(sum(a*cmath.exp(1j*(theta+2*math.pi*r)*j/k)
                       for j, a in enumerate(coeffs)))**2
               for r in range(k))/k


def toeplitz_coefficient(r, k, coeffs):
    # Fourier coefficient of F_k at index r, e^{irt} convention.
    return sum(coeffs[j+k*r]*coeffs[j].conjugate()
               for j in range(len(coeffs)) if 0 <= j+k*r < len(coeffs))


rng = random.Random(20261117)
for k in (2, 3, 4, 5):
    for _ in range(12):
        coeffs = [complex(rng.randint(-3, 3), rng.randint(-2, 2))
                  for _ in range(rng.randint(1, 2*k+4))]
        if all(a == 0 for a in coeffs):
            coeffs[0] = 1
        for i in range(12):
            theta = (i+0.37)*2*math.pi/13
            check(abs(residue_symbol(theta,k,coeffs)-
                      orbit_symbol(theta,k,coeffs))<1e-9,
                  'cyclic Fourier alias identity')
        for r in range(-2,3):
            n = 2000
            m = n-r
            if m >= 1:
                for alpha in (-1, 0, 2):
                    theoretical = k**(-(alpha+3))*toeplitz_coefficient(r,k,coeffs)
                    actual = gram(n,m,k,coeffs,alpha)
                    check(abs(actual-theoretical) < 0.13,
                          'tail Gram coefficient, alpha=%s, k=%s, r=%s, diff=%s'
                          %(alpha,k,r,abs(actual-theoretical)))

# For a monomial g=z^j, the positive diagonal is an exact rational number.
for k in (2,3,4,5):
    for j in range(0,2*k+1):
        for n in range(1,28):
            a = [0]*j + [1]
            actual = abs(next(iter(column(n,k,a,0).values())))**2
            exact = Fraction(n*n*(n+1), (k*n+j)**2*(k*n+j+1))
            check(abs(actual-float(exact))<1e-11,'exact rational monomial norm')

# k=2: g=1-z has disjoint output supports and a single essential Gram value 1/4.
for n in range(1,100):
    for m in (n-1,n+1):
        if m>=1:
            check(abs(gram(n,m,2,[1,-1],0))<1e-12,'disjoint output supports')
for n in (100, 500, 2000, 10000):
    check(abs(gram(n,n,2,[1,-1],0)-0.25)<0.003,'singleton essential Gram limit')

# k=2: g=1-z^2 has a full boundary root orbit; normalized long blocks
# at high modes give approximate null sequences (not a closed-range proof).
def packet_sq_norm(start, length, coeffs):
    out = {}
    for n in range(start,start+length):
        for j,v in column(n,2,coeffs,0).items():
            out[j] = out.get(j,0)+v/math.sqrt(length)
    return sum(abs(v)**2 for v in out.values())
for length in (50,100,200):
    check(packet_sq_norm(5000,length,[1,0,-1])<0.015,
          'approximate null packet')

# A two-step Gram Toeplitz section of g=1-z^2 has limiting first two
# normalized trace moments 2/8 and 6/64, respectively.
for N in (150, 300):
    diagonal = [gram(n,n,2,[1,0,-1],0).real for n in range(1,N+1)]
    off = [gram(n,n+1,2,[1,0,-1],0) for n in range(1,N)]
    m1 = sum(diagonal)/N
    m2 = (sum(x*x for x in diagonal)+2*sum(abs(x)**2 for x in off))/N
    check(abs(m1-0.25)<0.025,'first moment finite-section limit')
    check(abs(m2-6/64)<0.025,'second moment finite-section limit')
print('POLYNOMIAL_ALIAS_COMPANION_FINITE_CHECK_OK',TESTS)
