#!/usr/bin/env python3
"""Standalone consistency checker for four-knot natural cubic interpolation."""
from fractions import Fraction as F
from math import sqrt
from random import Random

def curvature(y):
    # Invert [[4,1],[1,4]] over rational numbers.
    a=6*(y[2]-2*y[1]+y[0]); b=6*(y[3]-2*y[2]+y[1])
    return [F(0),(4*a-b)/15,(4*b-a)/15,F(0)]

def derivatives(y):
    m=curvature(y)
    out=[]
    for i in range(3):
        # -(m_i/2)(1-u)^2 + (m_{i+1}/2)u^2 + delta - (m_{i+1}-m_i)/6
        a=y[i+1]-y[i]-(m[i+1]-m[i])/6-m[i]/2
        b=m[i]
        c=(m[i+1]-m[i])/2
        out.append((a,b,c))
    return out

def antiderivative(p,u):
    a,b,c=map(float,p)
    return a*u+b*u*u/2+c*u*u*u/3

def roots(p):
    a,b,c=map(float,p)
    if abs(c)>1e-15:
        disc=b*b-4*c*a
        if disc<0:return []
        return [r for r in ((-b-sqrt(disc))/(2*c),(-b+sqrt(disc))/(2*c)) if 0<r<1]
    if abs(b)>1e-15:
        r=-a/b
        return [r] if 0<r<1 else []
    return []

def variation(y):
    total=0.0
    for p in derivatives(y):
        cuts=[0.0]+sorted(roots(p))+[1.0]
        total += sum(abs(antiderivative(p,v)-antiderivative(p,u)) for u,v in zip(cuts,cuts[1:]))
    return total

h1=[F(0),F(1),F(1),F(1)]
h2=[F(0),F(0),F(1),F(1)]
h3=[F(0),F(0),F(0),F(1)]
assert curvature(h1)==[F(0),F(-8,5),F(2,5),F(0)]
assert curvature(h2)==[F(0),F(2),F(-2),F(0)]
assert derivatives(h1)==[(F(19,15),F(0),F(-4,5)),(F(7,15),F(-8,5),F(1)),(F(-2,15),F(2,5),F(-1,5))]
assert derivatives(h2)==[(F(-1,3),F(0),F(1)),(F(2,3),F(2),F(-2)),(F(2,3),F(-2),F(1))]
K1=F(133,125)+4*sqrt(3)/135+52*sqrt(39)/3375
K2=1+8/(9*sqrt(3))
for step,expect in [(h1,K1),(h2,K2),(h3,K1)]:
    v=variation(step)
    assert abs(v-expect)<1e-12,(step,v,expect)
assert K1 < 1.25 < 1.5 < K2
rng=Random(20261114)
for k in range(2000):
    y=[F(rng.randint(-100,100),rng.randint(1,40)) for _ in range(4)]
    vd=sum(abs(y[i+1]-y[i]) for i in range(3))
    if vd: assert variation(y)<=K2*float(vd)+1e-9,(k,y,variation(y),float(vd))
print('EXACT_RATIONAL_NATURAL_CURVATURE_AND_DERIVATIVES_PASS')
print('STEP_ROOTS_AND_ANALYTIC_GAIN_REPLAY_PASS')
print('ALL_2000_RATIONAL_INPUT_STRESS_TESTS_PASS')
print('SHARP_FOUR_KNOT_NATURAL_SPLINE_BV_GAIN',format(K2,'.15f'))
print('ALL_CHECKS_PASS')
