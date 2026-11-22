#!/usr/bin/env python3
"""Supplementary elementary checks for the two-ball Fourier envelope.

No external packages required. This script is a finite numerical/algebraic
check of an explicit three-dimensional example, not a proof of the general
Bessel expansion or the infinite-dimensional torus statements.
"""
from fractions import Fraction
from math import cos, sin, acos, sqrt, pi, gcd, isclose

checks = 0

def verify(cond, message):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(message)

# Exact extremum of z + 4(2z-1)^2 on 0 <= z <= 1.
vertex = Fraction(15, 32)
quadratic = lambda z: z + 4*(2*z-1)**2
verify(quadratic(vertex) == Fraction(31,64), 'three-dimensional exact minimum')
verify(quadratic(Fraction(0)) == 4, 'lower endpoint')
verify(quadratic(Fraction(1)) == 5, 'upper endpoint')
verify(quadratic(Fraction(0)) > quadratic(vertex), 'vertex is below first endpoint')
verify(quadratic(Fraction(1)) > quadratic(vertex), 'vertex is below second endpoint')
# Completed square gives an exact global certificate.
for den in range(1,20):
    for num in range(den+1):
        z=Fraction(num,den)
        verify(quadratic(z)-Fraction(31,64) == 16*(z-vertex)**2, 'completed square')

# Direct modular check of the abstract (p-q)*(d+3)/4 criterion:
# finite modular exploration is illustrative, not its Bezout proof.
for d in range(2,22):
    for p in range(1,16):
        for q in range(1,16):
            if gcd(p,q)!=1: continue
            phase=Fraction(d+3,4)
            right=(p-q)*phase
            congruence=(right.denominator==1)
            verify(congruence==(((p-q)*(d+3))%4==0),'rational zero congruence')
            # Seek u in rational grid u = k/(4*p*q), sufficient if compatible
            if congruence:
                ok=False
                for k in range(4*p*q):
                    u=Fraction(k,4*p*q)
                    if (p*u-phase).denominator==1 and (q*u-phase).denominator==1:
                        ok=True;break
                verify(ok,'explicit two-phase simultaneous-zero solution')

# Exact three-dimensional Fourier transform of the radius-r ball.
def ball_transform_3d(r,R):
    w=2*pi*r*R
    return (sin(w)-w*cos(w))/(2*pi*pi*R**3)

def spherical_energy_3d(R, r1=1.0, r2=2.0, distance=4.0):
    assert distance>r1+r2 and R>0
    a,b=ball_transform_3d(r1,R),ball_transform_3d(r2,R)
    z=2*pi*distance*R
    return a*a+b*b+2*a*b*sin(z)/z

def scaled(R):
    return (pi*pi)*R**4*spherical_energy_3d(R)

# For integer R, the angular cross term and both Bessel lower terms
# vanish exactly in real arithmetic, giving the sharp upper envelope.
for R in (10.0,20.0,50.0,100.0,400.0):
    verify(abs(scaled(R)-5)<2e-11,'three-dimensional upper envelope')

# A sequence with first cosine-square approaching z=15/32
phi=acos(sqrt(15/32))
for M in (30,100,300,1000):
    R=M+phi/(2*pi)
    verify(abs(scaled(R)-31/64)<3/(M**0.8),'lower-envelope convergence')

print('PASS:',checks,'supplementary assertions')
