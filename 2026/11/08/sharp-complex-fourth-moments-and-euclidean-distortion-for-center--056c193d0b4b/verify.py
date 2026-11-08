#!/usr/bin/env python3
"""Exact finite checks of centered affine complex fourth moments on simplices.

The mathematical proof, not these finite tests, establishes universal statements.
Python 3 standard library only.
"""
from fractions import Fraction
from itertools import product
from math import factorial, pi, cos, sin


def rising(m, k):
    value = 1
    for j in range(k):
        value *= (m+j)
    return value


def direct_moments(coeffs):
    """Exact simplex integration of complex Gaussian-integer vertex values."""
    m = len(coeffs)
    second = 0j
    for a, b in product(range(m), repeat=2):
        count = [0] * m
        count[a] += 1; count[b] += 1
        multiplicity = 1
        for t in count:
            multiplicity *= factorial(t)
        second += coeffs[a] * coeffs[b].conjugate() * multiplicity
    fourth = 0j
    for i, j, k, l in product(range(m), repeat=4):
        count = [0] * m
        for t in (i,j,k,l):
            count[t] += 1
        multiplicity = 1
        for t in count:
            multiplicity *= factorial(t)
        fourth += (coeffs[i]*coeffs[j]*coeffs[k].conjugate()
                   *coeffs[l].conjugate()*multiplicity)
    assert abs(second.imag) == 0 and abs(fourth.imag) == 0
    return Fraction(int(second.real), rising(m,2)), Fraction(int(fourth.real),rising(m,4))


def invariant_moments(coeffs):
    m=len(coeffs)
    p=sum(t.real*t.real+t.imag*t.imag for t in coeffs)
    q=sum(t*t for t in coeffs)
    r=sum((t.real*t.real+t.imag*t.imag)**2 for t in coeffs)
    p=int(p); r=int(r); q2=int(round(q.real*q.real+q.imag*q.imag))
    return Fraction(p, rising(m,2)),Fraction(2*p*p+q2+6*r,rising(m,4))


def fourth_ratio(coeffs):
    v,w=invariant_moments(coeffs)
    return w/v**2


def low(m):
    return Fraction(2*(m+1),m+2)


def high(m):
    return Fraction(3*(m+1)*(3*m*m-7*m+6),(m-1)*(m+2)*(m+3))


profiles = [
    [1+2j, -2+3j, 1-5j],
    [3+1j, -1-4j, -2+3j],
    [1+0j, -1+0j, 0+0j],
    [1+1j,2-1j,-3+0j],
    [1+0j, 1+2j, -2-2j],
    [1+1j, -2+1j, 0-1j, 1-1j],
    [2+1j, -1+2j, 1-2j, -2-1j],
    [1+2j, -2+0j, 0-1j, 1-1j],
    [2+0j, 1+2j, -2+1j, 0-1j, -1-2j],
    [2+1j, -1+1j, -1-2j],
]
checked=0
for z in profiles:
    assert sum(z)==0, z
    assert direct_moments(z)==invariant_moments(z),z
    K=fourth_ratio(z)
    assert low(len(z)) <= K <= high(len(z))
    checked+=1
print('EXACT_DIRECT_DIRICHLET_FOURTH_MOMENTS_OK',checked)

for m in range(3,75):
    z=[complex(m-1,0)]+[complex(-1,0)]*(m-1)
    assert fourth_ratio(z)==high(m),m
    c=Fraction(m*(m+1),(m+2)*(m+3))
    p=m*(m-1)
    r=(m-1)**4+(m-1)
    assert Fraction(r,p*p)==Fraction(m*m-3*m+3,m*(m-1))
    assert high(m)/low(m)==Fraction(3*(3*m*m-7*m+6),2*(m-1)*(m+3))
print('EXACT_UPPER_ENDPOINT_AND_EUCLIDEAN_DISTORTION_OK',72)

for m in range(3,60):
    z=[complex(cos(2*pi*j/m),sin(2*pi*j/m)) for j in range(m)]
    p=sum(abs(t)**2 for t in z)
    q=sum(t*t for t in z)
    r=sum(abs(t)**4 for t in z)
    K=(m*(m+1)/((m+2)*(m+3)))*(2+abs(q)**2/p**2+6*r/p**2)
    assert abs(sum(z))<1e-10*m
    assert abs(K-float(low(m)))<1e-11,m
print('ROOT_OF_UNITY_LOWER_ENDPOINT_DIAGNOSTICS_OK',57)

# For m=3, the full real centered affine space has the same ratio 12/5.
for a in range(-6,7):
    for b in range(-6,7):
        if a==0 and b==0: continue
        assert fourth_ratio([complex(a,0),complex(b,0),complex(-a-b,0)])==Fraction(12,5)
print('REAL_TRIANGLE_CONSTANT_EXACT_OK',168)

# The lower deficit equals the sum of phase and modulus-variance terms.
for z in profiles:
    m=len(z)
    p=int(round(sum(t.real*t.real+t.imag*t.imag for t in z)))
    q=sum(t*t for t in z)
    r=int(round(sum((t.real*t.real+t.imag*t.imag)**2 for t in z)))
    c=Fraction(m*(m+1),(m+2)*(m+3))
    lhs=fourth_ratio(z)-low(m)
    rhs=c/Fraction(p*p)*(int(round(q.real*q.real+q.imag*q.imag))+6*(Fraction(r)-Fraction(p*p,m)))
    assert lhs==rhs, (z,lhs,rhs)
print('EXACT_NONNEGATIVE_STABILITY_IDENTITY_OK',len(profiles))
print('ALL_COMPLEX_SIMPLEX_FOURTH_MOMENT_CHECKS_OK')
