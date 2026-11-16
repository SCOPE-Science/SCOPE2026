#!/usr/bin/env python3
"""Numerical consistency checks for the boundary-chirp Cesaro example.
Requires Python 3 and mpmath. Finite checks do not establish infinite claims.
"""
from math import comb
from fractions import Fraction
import mpmath as mp
mp.mp.dps = 46
checks = 0

def ok(condition, meaning):
    global checks
    assert condition, meaning
    checks += 1

s = mp.mpf('0.25')
eta = mp.exp(1j * mp.pi / 4)

def moment(n, sp=s):
    m = mp.sqrt(n + 1)
    # Numerically integrate only on the rigorously justified rotated ray.
    f = lambda y: (eta*y / (1 + eta*y))**n * (1 + eta*y)**(-sp-1) * mp.exp(1j * (1 + eta*y)) * eta
    return mp.quad(f, [0, m/3, m, 2*m, 4*m, mp.inf])

def asym(n, sp=s):
    return mp.sqrt(mp.pi) * n**(-sp/2-mp.mpf('0.25')) * mp.exp(-mp.sqrt(2*n) + 1j * (mp.sqrt(2*n) + mp.mpf('.5') + mp.pi*(mp.mpf('0.125')-sp/4)))

for n, tolerance in [(30, mp.mpf('.15')), (100,mp.mpf('.09')), (300,mp.mpf('.055')), (900,mp.mpf('.035'))]:
    rat = moment(n) / asym(n)
    ok(abs(rat-1) < tolerance, f'asymptotic ratio n={n}: {rat}')
    print(f'n={n} complex asymptotic ratio: {mp.nstr(rat,15)}')

# Exact lower-triangular matrix and the determinant identity at a finite order.
alpha = Fraction(0)
coeff = [Fraction(j+1) for j in range(6)] # (alpha+2)_j/j! = j+1
for n in range(6):
    for k in range(n+1):
        ok(coeff[n-k] == n-k+1, 'Bergman coefficients')
# Numerical triangular characteristic polynomial, small sizes.
ms = [moment(i) for i in range(5)]
for N in range(1,5):
    T = mp.matrix([[ms[n]*(n-k+1) if k<=n else 0 for k in range(N)] for n in range(N)])
    for z in [mp.mpf('.3'), mp.mpf('1.2')+0.2j]:
        d = mp.det(mp.eye(N) - z*T)
        product = mp.fprod([1-z*ms[i] for i in range(N)])
        ok(abs(d-product) < mp.mpf('1e-30'), f'finite determinant N={N}')
# Oscillatory incomplete-Gamma trace: both sides computed independently.
trace_integral = mp.quad(lambda y: mp.exp(1j*(1+eta*y)) * (1+eta*y)**(-s)*eta,
                        [0,1,3,10,mp.inf])
trace_gamma = (-1j)**(s-1) * mp.gammainc(1-s,-1j)
ok(abs(trace_integral-trace_gamma) < mp.mpf('1e-28'), 'trace incomplete Gamma')
# Positive-measure coefficient exponents cannot be square summable.
for a in [mp.mpf('0'),mp.mpf('-0.95'),mp.mpf('3')]:
    ok(2*(a+1-s)>-1,'positive-variation non-Hardy exponent')
print('PASS:',checks,'finite consistency assertions; analytical proof required for infinite conclusions')
