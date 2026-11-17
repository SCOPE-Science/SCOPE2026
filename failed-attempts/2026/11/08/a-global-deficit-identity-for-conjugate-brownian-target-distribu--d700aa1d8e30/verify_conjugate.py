#!/usr/bin/env python3
"""Independent numerical spot checks for the explicit Brownian renewal identities.

The analytic proof of global optimality does not rely on these finite tests.
Execute: python verify_conjugate.py
Requires: Python 3, NumPy, SciPy.
"""
import math
from scipy.integrate import quad
from scipy.special import erfc

D = 1.0

def f_fixed(x, t):
    return erfc(x / (2 * math.sqrt(D * t)))

def g_fixed(x, t):
    a = x / (2 * math.sqrt(D))
    return (t * math.erf(a/math.sqrt(t))
            + (2*a*math.sqrt(t)/math.sqrt(math.pi))*math.exp(-a*a/t)
            -2*a*a*erfc(a/math.sqrt(t)))

def f_exp(x, rate):
    return math.exp(-x*math.sqrt(rate/D))

def g_exp(x, rate):
    return -math.expm1(-x*math.sqrt(rate/D))/rate

def f_mix(x, components):
    return sum(w*f_exp(x, r) for w, r in components)

def g_mix(x, components):
    return sum(w*g_exp(x, r) for w, r in components)

def avg_exp_target(components):
    # Conjugate target to exponential rate 1 at D=1: 2 exp(-2x).
    return quad(lambda x: 2*math.exp(-2*x)*g_mix(x,components)/f_mix(x,components),
                1e-9,160,epsabs=1e-10,epsrel=1e-10,limit=400)[0]

def g_kernel(x,tf):
    return quad(lambda y: min(x,y)*f_fixed(y,tf)/D,0,35,
                epsabs=1e-11,epsrel=1e-11,limit=250)[0]

checks=0
for tt in (0.25,0.8,2.0,5.0):
    for xx in (0.2,0.7,1.5,3.1):
        a,b = g_fixed(xx,tt),g_kernel(xx,tt)
        assert math.isclose(a,b,rel_tol=5e-9,abs_tol=3e-10),(xx,tt,a,b)
        checks+=1

for r in (0.25,0.5,0.8,1.0,1.2,2.0,3.0):
    actual=avg_exp_target([(1.,r)])
    k=math.sqrt(r)
    exact=1/(k*(2-k))
    assert math.isclose(actual, exact,rel_tol=1e-9,abs_tol=1e-9)
    assert actual>=1-1e-10
    checks+=2

# A non-exponential renewal law: a mixture of exponential resetting clocks.
components=[(.35,.5),(.65,2.)]
actual=avg_exp_target(components)
assert actual>1.01
checks+=1

# The nonnegative symmetric-kernel gap formula, evaluated numerically on a
# finite window with exponentially small tail for these clock mixtures.
f0=lambda x:math.exp(-x)
h=lambda x:f_mix(x,components)/f0(x)
L=35.
# Use symmetry and integrate the nonsingular region 0<y<x.
def inn(x):
    hx=h(x)
    def fn(y):
        hy=h(y)
        return (2.*f0(x)*f0(y)*y*(hx-hy)**2/(hx*hy))
    return quad(fn,1e-8,x,epsabs=1e-9,epsrel=1e-9,limit=180)[0]
# Factor 1/(2*D*Z) where Z=1/2, D=1, so factor=1;
gap=quad(inn,1e-8,L,epsabs=1e-8,epsrel=2e-8,limit=180)[0]
assert math.isclose(gap,actual-1,abs_tol=2e-7,rel_tol=2e-6),(gap,actual-1)
checks+=1

# For a sharp reference clock, verify global improvement is impossible among
# a sample of competing exponential rates; averaged target erfc(x/2)^2/Z.
Z=quad(lambda x:f_fixed(x,1.)**2,0,14,epsabs=1e-11)[0]
sharp_mean=quad(lambda x:f_fixed(x,1.)*g_fixed(x,1.)/Z,
                1e-9,14,epsabs=1e-10)[0]
for r in (0.25,.6,1.,1.8,3.):
    v=quad(lambda x: f_fixed(x,1.)**2*g_exp(x,r)/f_exp(x,r)/Z,
           1e-9,14,epsabs=1e-10)[0]
    assert v>sharp_mean+1e-5,(r,v,sharp_mean)
    checks+=1

print(f'PASS: {checks} numerical identities and strict sample comparisons')
print(f'Poisson-conjugate optimal mean: 1.000000000000')
print(f'Mixed-clock mean: {actual:.12f}; direct gap: {gap:.12f}')
print(f'Sharp-reference optimal mean: {sharp_mean:.12f}')
