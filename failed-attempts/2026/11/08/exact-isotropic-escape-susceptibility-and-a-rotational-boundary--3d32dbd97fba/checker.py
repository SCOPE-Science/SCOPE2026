"""Numerical and symbolic consistency checks for a disk first-exit response theorem.

Requires Python 3 with numpy, scipy, sympy, and mpmath.
These finite checks supplement, but do not replace, the analytic argument.
"""
import math
import numpy as np
from scipy.special import iv, ive
from scipy.integrate import quad
from scipy.optimize import brentq
import sympy as sp


def f(beta, rho):
    if beta == 0:
        return rho * (rho*rho-1.0) / 16.0
    k = math.sqrt(beta)
    # Scaled Bessel ratio to prevent overflow.
    ratio = ive(1, k*rho) / ive(1, k) * math.exp(-k*(1-rho))
    return (ratio-rho) / (2*beta)


def g(beta, rho):
    if beta == 0:
        return -((1-rho*rho)**2)/128.0
    k=math.sqrt(beta)
    i0rat = ive(0,k*rho)/ive(0,k)*math.exp(-k*(1-rho))
    r = ive(0,k)/ive(1,k) * (1-i0rat)/k
    return (r-(1-rho*rho)/2.0)/(4*beta)


def g_independent(beta,rho):
    return quad(lambda s:0.5*f(beta,s),rho,1,epsabs=4e-14)[0]

# Direct second-order ODE and integral identity; no reliance on evolved simulations.
for beta in [0,0.01,0.1,1.0,4.0,100.0,800.0]:
    for rho in [0,0.07,0.23,0.55,0.84,0.97]:
        diff = abs(g(beta,rho)-g_independent(beta,rho))
        assert diff < 2e-9, (beta,rho,diff)
        if rho<1:
            assert g(beta,rho)<0, (beta,rho,g(beta,rho))

# Check the beta=0 ODE exactly.
r=sp.symbols('r',positive=True)
f0=r*(r**2-1)/16
g0=-(1-r**2)**2/128
assert sp.simplify(sp.diff(f0,r,2)+sp.diff(f0,r)/r-f0/r**2-r/2)==0
assert sp.simplify(sp.diff(g0,r,2)+sp.diff(g0,r)/r+(sp.diff(f0,r)+f0/r)/2)==0
assert g0.subs(r,1)==0
assert sp.diff(g0,r).subs(r,0)==0

# Second-order finite-speed response independently confirmed at beta=0
# by the exact constant-drift center-exit solution.
from scipy.special import iv, kv
for w in [0.05,0.10,0.15,0.20]:
    texact=iv(1,w/2)/(w*iv(0,w/2))
    t2=0.25+(w*w)*g(0,0)
    assert abs(texact-t2) < 3e-6, (w,texact,t2)

# An independent Green-function integral for the drifted disk center exit time.
for w in [0.3,0.8,1.7,3.9,8.0]:
    k=w/2.0
    green=quad(lambda r: r * (kv(0,k*r)-iv(0,k*r)*kv(0,k)/iv(0,k))
               *iv(0,k*r),0,1,epsabs=2e-11)[0]
    claimed=iv(1,k)/(w*iv(0,k))
    assert abs(green-claimed) < 1e-10, (w,green,claimed)

# Large-beta fixed-interior law and boundary-layer law.
for rho in [0.,0.2,0.6]:
    for k in [40.,70.,120.]:
        val=g(k*k,rho)*k*k
        target=-(1-rho*rho)/8
        assert abs(val-target)<0.007, (rho,k,val,target)
for z in [0.5,1.,2.,3.]:
    for k in [100.,300.,800.]:
        rho=1-z/k
        numerical=g(k*k,rho)*k**3
        expected=-(z-1+math.exp(-z))/4
        assert abs(numerical-expected)<0.032, (z,k,numerical,expected)

# A first-principles Taylor coefficient identity from Bessel generating series.
q=sp.symbols('q',real=True)
B0=lambda x: sum((q*x*x/4)**j/(sp.factorial(j)**2) for j in range(5))
B1ratio=lambda x: sum((q*x*x/4)**j/(sp.factorial(j)*sp.factorial(j+1)) for j in range(5))
ratio_series=sp.series((r*B1ratio(r)/B1ratio(1)-r)/(2*q),q,0,2).removeO()
assert sp.simplify(ratio_series.subs(q,0)-f0)==0

# Positivity/strict monotonicity spot checks as a sanity test.
for rho in [0.0,0.2,0.7]:
    vals=[g(b,rho) for b in [0,0.01,0.2,2,20,200]]
    assert all(y>x for x,y in zip(vals,vals[1:])), (rho, vals)

print('PASS: exact beta=0 ODE, 42 Bessel/integral checks, beta=0 drift expansion,')
print('      Green-kernel drift benchmark, high-rotation bulk/boundary asymptotics,')
print('      positivity and beta-monotonicity.')
print('Finite checks do not prove infinite-dimensional comparison or all-parameter claims.')
