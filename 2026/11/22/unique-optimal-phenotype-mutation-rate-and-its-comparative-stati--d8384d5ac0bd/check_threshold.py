#!/usr/bin/env python3
"""Reproduce symbolic and numerical checks for the binary phenotype mutation threshold."""
import math
import sympy as sp
from scipy.optimize import brentq

m, z, v = sp.symbols('m z v', positive=True)

def lap(c):
    # One-coordinate Laplace transform for two phenotype states.
    return 2*v*((1-z)/c + z/(c+4*v))

L1, L2, L3 = lap(1), lap(1+2*m), lap(3+2*m)
raw = sp.factor(((1+2*m)**2*L1 + m*(3+2*m)*L3 -
                 (1+m)*(1+2*m)*L2) /
                ((1+m)*(1+2*m)*L2 + m*(3+2*m)*L3 - (1+2*m)*L1))
A = (2*m+1)/(2*(m+1))
B = (2*m+1)*(2*m+3)/(8*(m+1))
formula = (4*(1-z)*v + 2*m*(1-z) + 3-2*z)/z - (2*m+1)/(4*z*(m+1)*(m+2*v+1)) + B/(z*v)
d1 = (4*(1-z) + A/(m+2*v+1)**2 - B/v**2)/z
d2 = (-4*A/(m+2*v+1)**3 + 2*B/v**3)/z
for desc, diff in [
    ('exact threshold simplification', raw-formula),
    ('exact first derivative', sp.diff(raw,v)-d1),
    ('exact second derivative', sp.diff(raw,v,2)-d2),
    ('bound coefficient', B-A/4-(2*m+1)/4),
    ('strategy-mutation comparative-statics coefficient', sp.diff(A,m)/4-sp.diff(B,m)+sp.Rational(1,2)),
]:
    assert sp.simplify(diff)==0, desc
    print('PASS:', desc)

F = sp.lambdify((m,z,v), z*d1, 'math')
V = sp.lambdify((m,z,v), formula, 'math')

def optimum(mm,zz):
    lo,hi=1e-9,1000.0
    assert F(mm,zz,lo)<0<F(mm,zz,hi)
    x=brentq(lambda vv:F(mm,zz,vv),lo,hi,xtol=1e-13)
    left=math.sqrt((2*mm+1)/(16*(1-zz)))
    right=math.sqrt((2*mm+1)*(2*mm+3)/(32*(mm+1)*(1-zz)))
    assert left < x < right
    assert V(mm,zz,x) < V(mm,zz,x/2)
    assert V(mm,zz,x) < V(mm,zz,x*2)
    return x,V(mm,zz,x)

for mm in (0.25,0.5,1.,4.):
    vals=[]
    for zz in (0.125,0.25,0.375,0.49):
        x,y=optimum(mm,zz); vals.append(x)
        print(f'mu={mm:.4g}, z={zz:.4g}, nu_star={x:.12f}, beta_star={y:.12f}')
    assert all(a<b for a,b in zip(vals,vals[1:])), 'discrimination monotonicity'
for zz in (0.125,0.25,0.375):
    vals=[optimum(mm,zz)[0] for mm in (0.25,0.5,1.,4.)]
    assert all(a<b for a,b in zip(vals,vals[1:])), 'strategy-mutation monotonicity'
x,y=optimum(0.5,0.25)
assert abs(x-0.46274575270921886)<1e-10
assert abs(y-23.76593598346907)<1e-9
print('PASS: all numerical checks, root bracketing, and comparative statics')
