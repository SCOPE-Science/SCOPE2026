#!/usr/bin/env python3
"""Self-contained exact algebra and independent Fourier-kernel checks."""
from fractions import Fraction as Q
import math
import random

# Exact arithmetic in Q(sqrt(2)), represented by pairs of Fractions.
def v(a, b=0):
    return (Q(a), Q(b))
def add(x, y):
    return (x[0] + y[0], x[1] + y[1])
def neg(x):
    return (-x[0], -x[1])
def sub(x, y):
    return add(x, neg(y))
def mul(x, y):
    return (x[0]*y[0] + 2*x[1]*y[1], x[0]*y[1] + x[1]*y[0])
def inv(x):
    d = x[0]*x[0] - 2*x[1]*x[1]
    return (x[0]/d, -x[1]/d)
def div(x, y):
    return mul(x, inv(y))

def g(z):
    return div(mul(sub(v(1), z), mul(add(mul(v(16), z), v(1)), add(mul(v(16), z), v(1)))), z)

zp = v(Q(1,4), Q(1,8))
zm = v(Q(1,4), Q(-1,8))
for root in (zp, zm):
    assert add(sub(mul(v(32),mul(root,root)),mul(v(16),root)),v(1)) == v(0)
assert g(zp) == v(71,8)
# Rational coefficient identity for the derivative numerator, descending powers.
# -(16z+1)(32z^2-16z+1) = -512z^3+224z^2-1.
assert (-16*32, 16*16-32, -16+16, -1) == (-512,224,0,-1)
assert (2-math.sqrt(2))/8 > 1/16
assert (2+math.sqrt(2))/8 < 1
print('EXACT_QUADRATIC_CRITICAL_POINTS_AND_RADICAL_IDENTITY_PASS')

TAU = 2*math.pi

def kernel(t):
    return 1+2*math.cos(t)+2*math.cos(2*t)

def antiderivative(t, delta):
    return 2*(math.sin(t)-math.sin(t-delta)) + math.sin(2*t)-math.sin(2*(t-delta))

def split_integral(delta):
    h = delta/2
    c = abs(math.cos(h))
    roots = [0., TAU, h % TAU, (h + math.pi) % TAU]
    if c > .25 + 1e-14:
        theta = math.acos(-1/(4*math.cos(h)))
        roots += [(h + theta) % TAU, (h + TAU-theta) % TAU]
    roots = sorted(set(round(t,14) for t in roots))
    return sum(abs(antiderivative(b,delta)-antiderivative(a,delta)) for a,b in zip(roots[:-1],roots[1:]))/(4*math.pi)

def predicted(delta):
    c=abs(math.cos(delta/2));s=abs(math.sin(delta/2))
    return 2*s/math.pi*(2 if c<=.25 else 4*c+1/(4*c))

critical = 2*math.acos(math.sqrt((2+math.sqrt(2))/8))
sharp = math.sqrt(71+8*math.sqrt(2))/(2*math.pi)
assert 0<critical<math.pi
for delta in (0.11,0.31,0.83,1.0,critical,2.17,2.9,math.pi,4.1):
    a,b=split_integral(delta),predicted(delta)
    assert abs(a-b)<5e-12, (delta,a,b)
assert abs(split_integral(critical)-sharp)<5e-12
assert abs(split_integral(math.pi)-4/math.pi)<5e-12
assert sharp>4/math.pi
print('INDEPENDENT_SIGN_SPLIT_KERNEL_INTEGRALS_PASS')

# Perturbation-stability sample: any zero-sum atomic derivative produces a
# finite circular BV input, whose projected derivative is a Dirichlet mixture.
rng=random.Random(60421)
N=4096
for case in range(120):
    k=rng.randrange(2,10)
    points=[rng.random()*TAU for _ in range(k)]
    masses=[rng.uniform(-2,2) for _ in range(k-1)]
    masses.append(-sum(masses))
    total=sum(abs(a) for a in masses)
    val=0.
    for j in range(N):
        t=TAU*(j+.5)/N
        d=sum(a*kernel(t-p) for a,p in zip(masses,points))/TAU
        val+=abs(d)*TAU/N
    assert val<=sharp*total+0.002, (case,val/total)
print('ATOMIC_BV_STRESS_TEST_PASS 120')
print('SHARP_CONSTANT',format(sharp,'.15f'))
print('NONANTIPODAL_JUMP_SEPARATION',format(critical,'.15f'))
print('ALL_BV_FOURIER_SECOND_CUTOFF_CHECKS_PASS')
