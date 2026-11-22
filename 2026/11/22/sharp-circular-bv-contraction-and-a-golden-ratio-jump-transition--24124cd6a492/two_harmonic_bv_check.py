#!/usr/bin/env python3
"""Independent finite checks for the two-harmonic circular BV coefficient.

No finite calculation here replaces the analytical all-parameter proof.
"""
import math
import random
import sympy as sp
import mpmath as mp

mp.mp.dps = 42
x = sp.sqrt(5)
s_star = (3-x)/2
q_star = sp.sqrt((11+5*x)/2)
assert sp.simplify(s_star*(1-2*s_star)*q_star**2 - 1) == 0
assert sp.simplify((1-s_star)**3/(1-2*s_star) - 1) == 0
assert sp.simplify(sp.diff((1-sp.Symbol('s'))**3/(1-2*sp.Symbol('s')),sp.Symbol('s')) - ((1-sp.Symbol('s'))**2*(4*sp.Symbol('s')-1)/(1-2*sp.Symbol('s'))**2)) == 0
print('EXACT_GOLDEN_RATIO_CROSSOVER_IDENTITIES_PASS')

def shift_tv(a,b,phi):
    c=mp.cos(phi/2)
    if 4*b*c <= a:
        return 4*a/mp.pi*mp.sin(phi/2)
    q=4*b/a
    return 2*a/mp.pi*mp.sin(phi/2)*(q*c+1/(q*c))

def coefficient(a,b):
    q=4*b/a
    qc=float(q_star)
    if q <= qc:
        return 4*a/mp.pi, mp.pi
    s=(1+mp.sqrt(1-8/q**2))/4
    c=mp.sqrt(s)
    return (2*a/mp.pi)*mp.sqrt(1-s)*(q*c+1/(q*c)), 2*mp.acos(c)

def kernel(a,b,theta):
    return (1+2*a*mp.cos(theta)+2*b*mp.cos(2*theta))/(2*mp.pi)

def direct_tv(a,b,phi):
    # Quadrature split at known zeroes of the difference when present.
    c=mp.cos(phi/2)
    roots=[-mp.pi,0,mp.pi]
    if 4*b*c>a:
        t=mp.acos(-a/(4*b*c))
        roots=sorted([-mp.pi,0,mp.pi,-t,t])
    integral=mp.fsum(mp.quad(lambda tt:abs(kernel(a,b,tt+phi/2)-kernel(a,b,tt-phi/2)),[roots[i],roots[i+1]]) for i in range(len(roots)-1))
    return integral/2

random.seed(5319)
for i in range(24):
    a=mp.mpf(random.randrange(1,140))/1000
    b=mp.mpf(random.randrange(1,140))/1000
    phi=mp.pi*mp.mpf(random.randrange(1,1000))/1000
    expected=shift_tv(a,b,phi)
    got=direct_tv(a,b,phi)
    assert abs(got-expected)<mp.mpf('1e-32'),(i,a,b,phi,got,expected)
print('DIRECT_TRANSLATE_DENSITY_INTEGRALS_MATCH_CLOSED_FORM_PASS',24)

for t in ['0.05','0.5','0.7','0.832547668','0.832547670','0.9','1','1.3','3']:
    a=mp.mpf('0.02')
    b=a*mp.mpf(t)
    exact,phi=coefficient(a,b)
    grid=max(shift_tv(a,b,mp.pi*mp.mpf(k)/6000) for k in range(1,6001))
    assert exact >= grid-mp.mpf('1e-25')
    assert abs(grid-exact)<mp.mpf('1e-7'),(t,exact,grid)
    assert abs(shift_tv(a,b,phi)-exact)<mp.mpf('1e-34')
print('INDEPENDENT_GLOBAL_SHIFT_GRID_AND_ANALYTIC_MAXIMIZERS_PASS')

# Fourier convolution powers: semigroup coefficients are exponentiated.
a=mp.mpf('0.1');b=mp.mpf('0.09')
for r in range(1,9):
    got,phi=coefficient(a**r,b**r)
    grid=max(shift_tv(a**r,b**r,mp.pi*mp.mpf(k)/3000) for k in range(1,3001))
    assert abs(grid-got)<mp.mpf('1e-7')*a**r
    if r==1: assert phi<mp.pi
    else: assert phi==mp.pi
print('ITERATION_MODE_SWITCH_FIRST_NONANTIPODAL_THEN_ANTIPODAL_PASS')

# A full-circle arc derivative is a positive and negative point mass; its
# output-variation ratio is precisely the shift-TV formula.
for t in ['0.2','0.7','0.9','1.0','1.4']:
    a=mp.mpf('0.09');b=a*mp.mpf(t)
    K, phi=coefficient(a,b)
    result=direct_tv(a,b,phi)
    assert abs(result-K)<mp.mpf('1e-32')
print('ATTAINING_SINGLE_ARC_STEP_WITNESSES_PASS')
print('ALL_TWO_HARMONIC_CIRCULAR_BV_FINITE_CHECKS_PASS')
