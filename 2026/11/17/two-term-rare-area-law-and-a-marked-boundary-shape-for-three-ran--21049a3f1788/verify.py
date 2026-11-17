"""Standalone numerical and algebraic checks for a spherical great-circle cell-area law.
Requires only the Python standard library. Not an independent proof.
"""
from fractions import Fraction as Q
from math import asin, cos, pi, sin, sqrt
import random

# Dirichlet(1/2,1/2,1/2) moments for the geometric density.
a, a0 = Q(1, 2), Q(3, 2)
pair = a*a/(a0*(a0+1))
triple = a*a*a/(a0*(a0+1)*(a0+2))
assert 3*pair-triple == Q(4, 21)
# (1/(64*pi))*(2*pi)*(4/21)*(1/4) = 1/672.
assert Q(1, 64)*2*Q(4, 21)*Q(1, 4)==Q(1, 672)

rng = random.Random(202611140731)
def unit():
    v = [rng.gauss(0, 1) for _ in range(3)]
    w = sqrt(sum(z*z for z in v))
    return [z/w for z in v]
def dot(u, v):
    return sum(a*b for a,b in zip(u,v))
for _ in range(1500):
    u,v,w=unit(),unit(),unit()
    x,y,z = dot(u,v), dot(u,w), dot(v,w)
    aa,bb,cc=asin(x),asin(y),asin(z)
    A=[pi/2+aa+bb+cc,pi/2+aa-bb-cc,
       pi/2-aa+bb-cc,pi/2-aa-bb+cc]
    assert all(k>0 for k in A), A
    determinant=1+2*x*y*z-x*x-y*y-z*z
    product=4
    for k in A: product *= sin(k/2)
    assert abs(determinant-product)<3e-12,(determinant,product)

# Importance sampler: analytical leading density, exact sine correction.
def sinc(x):
    return sin(x)/x if x else 1.0
for eps in (0.4,0.1):
    total=0.0
    draws=90000
    for _ in range(draws):
        t=[rng.gammavariate(.5,1) for i in range(3)]
        t=[x/sum(t) for x in t]
        eta=eps*rng.random()**.25 # normalized near-event radial law
        g=1
        for z in t: g *= (1-z)
        ratio=1
        for z in t: ratio *= sinc(eta*(1-z)/2)
        ratio /= sqrt(sinc(eta/2)*sinc(eta*t[0]/2)*sinc(eta*t[1]/2)*sinc(eta*t[2]/2))
        # E_Dirichlet[g/tprod^.5]=4/21; importance weight
        total += g*ratio
    rel=(total/draws)/float(Q(4,21))
    assert abs(rel-1)<0.008,(eps,rel)
print('SPHERICAL_MAX_CELL_MARKED_TAIL_CHECKS_OK')
