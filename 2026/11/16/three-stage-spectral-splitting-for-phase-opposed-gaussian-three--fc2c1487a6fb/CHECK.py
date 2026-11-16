#!/usr/bin/env python3
"""Finite symbolic and numerical checks for a three-tone Gaussian Fourier phase diagram."""
import math
from scipy.optimize import brentq
import numpy as np
import sympy as sp

checks=0
x,s,a=sp.symbols('x s a', positive=True, real=True)
d=sp.sqrt(s)
c=sp.exp(-s/2)
F=sp.exp(-x*x/2)*(2*c*sp.cosh(d*x)-a)
# Direct derivative in the Gaussian-sum representation.
Fdirect=sp.exp(-(x-d)**2/2)+sp.exp(-(x+d)**2/2)-a*sp.exp(-x*x/2)
assert sp.simplify(sp.expand((Fdirect-F)*sp.exp((x*x+s)/2)).rewrite(sp.exp))==0
checks+=1
fp=sp.diff(F,x)
H=2*c*(sp.cosh(d*x)-d*sp.sinh(d*x)/x)
assert sp.simplify(fp-x*sp.exp(-x*x/2)*(a-H))==0
checks+=1
assert sp.simplify(sp.limit(H,x,0)-2*c*(1-s))==0
checks+=1
assert sp.simplify(sp.limit(sp.diff(F,x,2),x,0)-(a-2*c*(1-s)))==0
checks+=1
# Expand H in x^2 and check sign coefficients.
for k in range(1,12):
    term=2*c*s**k*(1-s/sp.Integer(2*k+1))/sp.factorial(2*k)
    actual=sp.diff(H,x,2*k).subs(x,0)/sp.factorial(2*k)
    # Direct substitution may return nan because removable singular; use series.
    actual=sp.series(H,x,0,2*k+2).removeO().coeff(x,2*k)
    assert sp.simplify(actual-term)==0
    checks+=1

sq=brentq(lambda u:2*math.exp(-u/2)*(1-u)-1,0,1,xtol=1e-14)
assert abs(sq-0.3917979837736633)<1e-12;checks+=1
s1=2*math.log(2)
assert sq<s1;checks+=1

def Hnum(s,x):
    d=math.sqrt(s); c=math.exp(-s/2)
    if abs(x)<1.e-8:
        return 2*c*(1-s)
    z=d*x
    return 2*c*(math.cosh(z)-d*math.sinh(z)/x)

def Fn(s,a,x):
    return (math.exp(-(x-math.sqrt(s))**2/2)+math.exp(-(x+math.sqrt(s))**2/2)
            -a*math.exp(-x*x/2))

def expected(s,a):
    h0=2*math.exp(-s/2)*(1-s)
    if a<=h0: return 1
    if a<=2*math.exp(-s/2): return 2
    return 3

# Four exact regimes; stable numerical grid find_peaks independently of root counting.
from scipy.signal import find_peaks
for s0,a0 in [(0.2,.6),(.5,1.),(2.,1.),(.2,2.1),(.4,1.2),(.8,.7),(1.5,.2),(2.,.3),(4.,1.),(4.,.08),(6.,.05)]:
    X=np.linspace(-12,12,80001)
    Y=(np.exp(-(X-math.sqrt(s0))**2/2)+np.exp(-(X+math.sqrt(s0))**2/2)
       -a0*np.exp(-X**2/2))**2
    inds,_=find_peaks(Y,prominence=1e-10)
    n=len(inds)
    assert n==expected(s0,a0), (s0,a0,n,expected(s0,a0))
    checks+=1

# Root uniqueness and derivative sign tests, in nondegenerate parameter regions.
for s0 in [0.05,.1,.2,.4,.8,1.,1.5,2.5,4.5,8.]:
    for a0 in [.05,.25,.5,1.,1.5,2.,3.]:
        h0=Hnum(s0,0)
        if a0 <= h0: continue
        root=brentq(lambda z:Hnum(s0,z)-a0,1e-6,30.,xtol=1e-12)
        assert root>0 and Fn(s0,a0,root)>0
        assert Hnum(s0,root/2)<a0 and Hnum(s0,root*1.5)>a0
        if a0>2*math.exp(-s0/2):
            assert Fn(s0,a0,0)<0 and Fn(s0,a0,root)>0
        checks+=3

# Distinct critical scales, unique solution of first one for several amplitudes.
for a0 in [0.01,.07,.25,.5,.85,1.,1.3,1.6,1.9,1.999]:
    first=brentq(lambda z:2*math.exp(-z/2)*(1-z)-a0,0,1)
    second=2*math.log(2/a0)
    assert 0<first<1 and second>first
    assert abs(2*math.exp(-first/2)*(1-first)-a0)<1.e-12
    checks+=2

# Universal square-root side-peak onset at fixed a=1.
for eps in [2e-5,4e-5,8e-5,1.6e-4]:
    root=brentq(lambda z:Hnum(sq+eps,z)-1,1.e-8,4.)
    ratio=root**2 / (3*eps/sq)
    assert abs(ratio-1)<0.003,(eps,ratio)
    checks+=1

# Quadratic onset of the new central peak.
for eps in [1e-4,3e-4,1e-3,3e-3]:
    F0=Fn(s1+eps,1.,0.)
    assert abs(F0**2 / (eps**2/4)-1)<eps*2
    checks+=1

# Direct Gaussian Fourier integral as an independent normalization check.
from scipy.integrate import quad
for s0,a0,x0 in [(0.5,1.0,0.1),(.8,.7,2.0),(2.1,1.2,-.4)]:
    d0=math.sqrt(s0)
    re=quad(lambda t:math.exp(-t*t/2)/math.sqrt(2*math.pi)*(2*math.cos(d0*t)-a0)*math.cos(x0*t),-18,18,epsabs=1e-11)[0]
    im=quad(lambda t:math.exp(-t*t/2)/math.sqrt(2*math.pi)*(2*math.cos(d0*t)-a0)*math.sin(x0*t),-18,18,epsabs=1e-11)[0]
    assert abs(re-Fn(s0,a0,x0))<1e-10 and abs(im)<1e-10
    checks+=1
print('THREE_TONE_GAUSSIAN_CHECKS_PASSED',checks)
