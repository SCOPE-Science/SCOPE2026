#!/usr/bin/env python3
"""Standalone numerical and exact-coefficient corroboration of the analytic theorem."""
import cmath
import math
from fractions import Fraction


def squared_norm(z, w):
    # z is [a,b,c], for frequencies [0, +w, -w].
    freqs = [0.0, w, -w]
    return sum(
        z[i] * z[j].conjugate() *
        (1.0 if i == j else math.sin(freqs[i] - freqs[j]) / (freqs[i] - freqs[j]))
        for i in range(3) for j in range(3)
    ).real


def sharp(w):
    s = math.sin(w) / w
    A = 0.5 * (1 + s * math.cos(w)) - s * s
    B = 0.5 * (1 - s * math.cos(w))
    return 1 + (math.cos(w) - s) ** 2 / A + math.sin(w) ** 2 / B


def kernel_coeffs(w):
    s = math.sin(w) / w
    A = 0.5 * (1 + s * math.cos(w)) - s * s
    B = 0.5 * (1 - s * math.cos(w))
    u = (math.cos(w) - s) / A
    v = math.sin(w) / B
    return [1 - s * u, 0.5 * (u - 1j * v), 0.5 * (u + 1j * v)]


def F(t):
    return t*t*(4-math.cos(t))+9*t*math.sin(t)-24*(1-math.cos(t))


def series_coefficient(n):
    # Coefficient of t^(2*n) in F, direct expansion (not just the desired formula).
    a = -Fraction((-1)**(n-1), math.factorial(2*n-2)) if n >= 1 else Fraction(4)
    # t^2 (4 - cos t): - (-1)^(n-1)/(2n-2)! for n>=2, plus 4t^2.
    if n == 1:
        a = Fraction(3)
    b = Fraction(9 * (-1)**(n-1), math.factorial(2*n-1))
    c = Fraction(-24 * (-1)**(n+1), math.factorial(2*n))
    return a + b + c

for n in range(1, 17):
    got=series_coefficient(n)
    want=Fraction(0) if n < 4 else Fraction(4*(-1)**n*(n-2)*(n-3), math.factorial(2*n))
    assert got==want,(n,got,want)

count=0
for w in [0.045, 0.08, 0.13, 0.25, 0.47, 0.7, 1, 1.5, 2.2, 3, 4.9, 6.4, 9, 13, 31]:
    K=sharp(w)
    assert 0<K<9, (w,K)
    c=kernel_coeffs(w)
    endpoint=sum(c[j]*cmath.exp(1j*[0,w,-w][j]) for j in range(3))
    energy=squared_norm(c,w)
    assert abs(energy-K)<3e-6*max(1,K),('energy',w,energy,K)
    assert abs(endpoint-K)<3e-6*max(1,K),('eval',w,endpoint,K)
    for k in range(16):
        a=complex(math.cos(1.7*k),math.sin(.9*k))
        b=complex(math.cos(.3*k+.8),math.sin(2.2*k))
        d=complex(math.sin(1.1*k+.5),math.cos(.7*k))
        z=[a,b,d]
        ev=sum(z[j]*cmath.exp(1j*[0,w,-w][j]) for j in range(3))
        den=squared_norm(z,w)
        assert abs(ev)**2<=(K+2e-7)*den, ('Cauchy',w,k,abs(ev)**2,den)
        count+=1
for t in [0.3,0.7,1,1.5,2,2.4,3,3.2,4,5,6,6.01,7,9,14,31,110]:
    assert t*(2+math.cos(t))-3*math.sin(t)>0
    if t>=1:
        assert F(t)>0
print('CHECK_OK independent_complex_checks=',count,' exact_fraction_series=',16,' gap_count=',15)
