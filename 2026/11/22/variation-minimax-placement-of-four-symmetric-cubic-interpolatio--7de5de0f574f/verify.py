#!/usr/bin/env python3
"""Exact identities and rational enclosures for symmetric cubic interpolation variation."""
from fractions import Fraction as F
from math import isqrt
from random import Random
import sympy as sp

z, a = sp.symbols('z a', real=True)
nodes = [-1, -a, a, 1]
cardinals = [sp.cancel(sp.prod((z - t)/(v - t) for j,t in enumerate(nodes) if j!=i)) for i,v in enumerate(nodes)]
assert sp.simplify(sum(cardinals) - 1) == 0
steps = [sp.factor(sum(cardinals[k:])) for k in (1,2,3)]
T = (z+1)*(z*z-a*a)/(2*(1-a*a))
U = sp.Rational(1,2)+z*(1+a+a*a-z*z)/(2*a*(1+a))
assert sp.simplify(steps[0]-(1-T.subs(z,-z)))==0
assert sp.simplify(steps[1]-U)==0
assert sp.simplify(steps[2]-T)==0
assert sp.simplify(sp.diff(steps[0],z)-(3*z*z-2*z-a*a)/(2*(1-a*a)))==0
assert sp.simplify(sp.diff(steps[1],z)-(1+a+a*a-3*z*z)/(2*a*(1+a)))==0
print('EXACT_FOUR_NODE_CARDINAL_AND_STEP_IDENTITIES_PASS')

s = sp.sqrt(1+3*a*a)
r_minus, r_plus = (1-s)/3,(1+s)/3
Kouter = 1+4*(1+3*a*a)**sp.Rational(3,2)/(27*(1-a*a))
assert sp.simplify(1+2*(steps[0].subs(z,r_minus)-steps[0].subs(z,r_plus))-Kouter)==0
q=1+a+a*a
r=sp.sqrt(q/3)
Kmiddle=4*(q/3)**sp.Rational(3,2)/(a*(1+a))-1
assert sp.simplify(2*(U.subs(z,r)-U.subs(z,-r))-1-Kmiddle)==0
assert sp.simplify(sp.diff(sp.log((Kmiddle+1)),a)-(1+2*a)*(a*a+a-2)/(2*a*(a+1)*q))==0
print('EXACT_TOTAL_VARIATION_AND_MONOTONICITY_IDENTITIES_PASS')

def sqrt_bounds(v,scale=10**38):
    assert v>0
    k=isqrt(v.numerator*scale*scale//v.denominator)
    return F(k,scale),F(k+1,scale)

def branch_intervals(x):
    assert 0<x<1
    ss=sqrt_bounds(1+3*x*x)
    rr=sqrt_bounds((1+x+x*x)/3)
    outer=(1+F(4,27)*ss[0]**3/(1-x*x), 1+F(4,27)*ss[1]**3/(1-x*x))
    middle=(4*rr[0]**3/(x*(1+x))-1,4*rr[1]**3/(x*(1+x))-1)
    return outer,middle

def cross_interval(x):
    o,m=branch_intervals(x)
    return o[0]-m[1],o[1]-m[0]

left=F(48013692628,10**11)
right=F(48013692629,10**11)
assert cross_interval(left)[1]<0, cross_interval(left)
assert cross_interval(right)[0]>0, cross_interval(right)
lb=branch_intervals(left)[0][0]
ub=branch_intervals(right)[0][1]
assert F(14235939250,10**10)<lb and ub<F(14235939251,10**10)
print('EXACT_RATIONAL_UNIQUE_MINIMIZER_BRACKET_PASS', str(left),str(right))
print('EXACT_RATIONAL_SHARP_NORM_BRACKET_PASS')

# Exact comparison against ordinary equally spaced and Chebyshev-Lobatto nodes.
for t in [F(1,3),F(1,2)]:
    o,m=branch_intervals(t)
    assert max(o[0],m[0])>ub
print('EXACT_STANDARD_NODE_COMPARISONS_PASS')

# Supplementary independent numerical integration using raw Lagrange polynomials.
import numpy as np
from numpy.polynomial import Polynomial as P
rng=Random(42)
for case in range(4000):
    aa=float(rng.uniform(.02,.98)); data=np.array([rng.uniform(-2,2) for _ in range(4)])
    nds=[-1.,-aa,aa,1.]
    poly=P([0.])
    for j,y in enumerate(data):
        term=P([float(y)])
        for k,t in enumerate(nds):
            if j!=k: term=term*P([-t,1.])/(nds[j]-t)
        poly+=term
    roots=poly.deriv().roots()
    pts=[-1.]+sorted(float(v.real) for v in roots if abs(v.imag)<1e-10 and -1<v.real<1)+[1.]
    variation=sum(abs(poly(v)-poly(u)) for u,v in zip(pts,pts[1:]))
    input_var=sum(abs(np.diff(data)))
    kval1=1+4*(1+3*aa*aa)**1.5/(27*(1-aa*aa))
    kval2=4*((1+aa+aa*aa)/3)**1.5/(aa*(1+aa))-1
    assert variation<=max(kval1,kval2)*input_var+1e-7
print('INDEPENDENT_RANDOM_POLYNOMIAL_VARIATION_STRESS_PASS 4000')
print('ALL_SYMMETRIC_CUBIC_INTERPOLATION_VARIATION_CHECKS_PASS')
