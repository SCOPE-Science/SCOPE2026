"""Reproducibility checks for one-site fractional-Brownian-area design.

Requires sympy, scipy, and mpmath. Numerical grids only check consistency;
the universal optimality conclusion comes from the analytic inequalities in RESULT.md.
"""
import math
from fractions import Fraction
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar
import sympy as sp

b=sp.Rational(3,2)
t=sp.symbols('t',positive=True)
e=sp.symbols('e',nonnegative=True)
c=sp.Rational(1,2)*(t**b+(1-t**(b+1)-(1-t)**(b+1))/(b+1))
cp=sp.Rational(3,4)*sp.sqrt(t)+sp.Rational(1,2)*((1-t)**b-t**b)
cpp=-sp.Rational(3,4)*((t-sp.Rational(1,2))/sp.sqrt(t)+sp.sqrt(1-t))
assert sp.simplify(sp.diff(c,t)-cp)==0
assert sp.simplify(sp.diff(c,t,2)-cpp)==0
S=2*(t**b+e)*cp-b*t**(b-1)*c
Sprime=2*(t**b+e)*cpp+b*t**(b-1)*cp-b*(b-1)*t**(b-2)*c
assert sp.simplify(sp.diff(S,t)-Sprime)==0
assert sp.simplify(sp.limit(c,t,1)-sp.Rational(1,2))==0
assert sp.simplify(sp.limit(cp,t,1)-sp.Rational(1,4))==0
assert sp.simplify(sp.limit(S,t,1)-(e-sp.Rational(1,2))/2)==0

# Rigorous rational bounds used in the global proof.
assert Fraction(27,64)<Fraction(49,100) # ((3/4)^(3/2))^2 < (7/10)^2
assert Fraction(297,400)>Fraction(21,32)
assert Fraction(189,200)>Fraction(21,32)
assert Fraction(361,400)>Fraction(9,10)
assert Fraction(1,4)<Fraction(7,16)

def C(x):
    return .5*(x**1.5+(1-x**2.5-(1-x)**2.5)/2.5)
def risk(x,eta):
    if x==0:return 2/7
    return 2/7-C(x)**2/(x**1.5+eta)
def cov(x,s):
    return .5*(x**1.5+s**1.5-abs(x-s)**1.5)

# Direct covariance integrations not derived from the closed-form integral expression.
for x in np.linspace(.01,1,25):
    z=quad(lambda s:cov(float(x),s),0,1,points=[float(x)],epsabs=2e-12)[0]
    assert abs(z-C(float(x)))<3e-11

# Verify strict endpoint superiority for positive noise at and above the threshold,
# as well as nonendpoint improvement just below it; a grid is NOT the proof.
for eta in [.5,.51,.6,.75,1.,5.,100.]:
    endpoint=risk(1,eta)
    for x in np.linspace(0,.9999,901):
        assert risk(float(x),eta)>endpoint-2e-13,(x,eta)
for eta in [0,.01,.1,.25,.4,.49]:
    sol=minimize_scalar(lambda x:risk(x,eta),bounds=(.00001,1),method='bounded',options={'xatol':1e-12})
    assert sol.x<.999999 and sol.fun<risk(1,eta)-1e-10,(eta,sol.x,sol.fun)

# Exact threshold risk and nondegenerate endpoint comparisons.
assert abs(risk(1,.5)-5/42)<2e-15
print('PASS: symbolic covariance derivatives, 5 exact inequalities, 25 direct integrals, 6307 grid and 6 interior checks')
