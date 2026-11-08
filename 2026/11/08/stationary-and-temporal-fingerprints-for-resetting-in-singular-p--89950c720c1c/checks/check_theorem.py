#!/usr/bin/env python3
"""Numerical and symbolic spot checks of the stated radial theorem.

Run with: python checks/check_theorem.py
Requires sympy, scipy, numpy. These checks corroborate, not replace, the proof.
"""
import math
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import gamma, kv, digamma

R, D, a, reset, k = sp.symbols('R D a reset k', positive=True)
y = R**4/(16*D)

def L(g):
    return D/R**2 * sp.diff(g,R,2) + (1-2*a)*D/R**3 * sp.diff(g,R)

assert sp.simplify(L(y) - (1-a/2)) == 0
assert sp.simplify(L(y*y) - 2*(2-a/2)*y) == 0
# The reset contribution is -r*f(y) for f(0)=0.
assert sp.simplify((L(y)-reset*y) - (1-a/2-reset*y)) == 0
assert sp.simplify((L(y*y)-reset*y*y) - (2*(2-a/2)*y-reset*y*y)) == 0

# Exact stationary moments of S=R^4/(16D) for all k>0.
def exact_m(p, shape, lam=0.8, dif=1.7):
    return (16*dif/lam)**(p/4) * gamma(1+p/4)*gamma(shape+p/4)/gamma(shape)

def density_s(s, shape, lam=0.8):
    z=2*math.sqrt(lam*s)
    return 2*lam**((shape+1)/2) / gamma(shape) * s**((shape-1)/2)*kv(shape-1,z)

# Density integrals and moments, compared with independently evaluated gamma formulas.
for shape in [0.5,0.75,1.0,0.63,0.91]:
    lam=0.8
    total=quad(lambda u:2*u*density_s(u*u,shape,lam),1e-11,math.sqrt(500),epsabs=2e-10)[0]
    assert abs(total-1)<1e-8,(shape,total)
    for power in [1,2]:
        got=quad(lambda u:2*u*(u*u)**power*density_s(u*u,shape,lam),1e-11,math.sqrt(500),epsabs=2e-9)[0]
        want=gamma(shape+power)/gamma(shape)*gamma(1+power)/lam**power
        assert abs(got-want)<1e-7*want,(shape,power,got,want)
    chi=exact_m(4,shape)/exact_m(2,shape)**2
    assert abs(chi-(4/math.pi)*shape*(gamma(shape)/gamma(shape+.5))**2)<3e-13

# Strict likelihood-ratio growth on a broad grid is a check; the proof is analytic.
for lo,hi in [(0.5,0.75),(0.75,1.0),(0.5,1.0),(0.63,0.91)]:
    xs=np.logspace(-5,2.0,300)
    ratios=np.array([density_s(x,hi)/density_s(x,lo) for x in xs])
    assert np.all(np.diff(ratios)>0),(lo,hi)
    assert ratios[0]<1 and ratios[-1]>1,(lo,hi)

# The scale-free shape fingerprint is strictly decreasing in k.
for shape in np.linspace(.5,1.0,51):
    dlog=1/shape-2*(digamma(shape+.5)-digamma(shape))
    assert dlog<0

# A three-parameter population inverse round trip at non-endpoint shape.
shape0, lam0, dif0, t0 = .75, .83, 1.7, .71
m2 = exact_m(2,shape0,lam0,dif0)
m4 = exact_m(4,shape0,lam0,dif0)
C = math.exp(-lam0*t0)
measured_shape = m4/m2**2
shape_back = brentq(lambda z:(4/math.pi)*z*(gamma(z)/gamma(z+.5))**2-measured_shape,.5,1)
lam_back = -math.log(C)/t0
dif_back = lam_back*m4/(16*shape_back)
assert abs(shape_back-shape0)<1e-12
assert abs(lam_back-lam0)<1e-12
assert abs(dif_back-dif0)<1e-12

# A simulation uses exact BESQ transitions, not Euler steps.
gen=np.random.default_rng(61923)
size=230000
lag=0.71
lam=0.83
for shape in [.5,.75,1.0]:
    Y0=gen.gamma(shape,1,size=size)*gen.exponential(1/lam,size=size)
    noreset=gen.uniform(size=size)<math.exp(-lam*lag)
    Yt=np.empty(size)
    count=np.count_nonzero(noreset)
    if count:
        Yt[noreset]=lag/2*gen.noncentral_chisquare(2*shape,2*Y0[noreset]/lag,size=count)
    count=size-count
    if count:
        # Age since latest reset, conditioned on at least one event in (0,lag).
        age=-np.log1p(-gen.uniform(size=count)*(1-math.exp(-lam*lag)))/lam
        Yt[~noreset]=age*gen.gamma(shape,1,size=count)
    covariance=np.mean((Y0-Y0.mean())*(Yt-Yt.mean()))
    normalized=covariance/Y0.var()
    target=math.exp(-lam*lag)
    assert abs(normalized-target)<.035,(shape,normalized,target)
    assert abs(Y0.mean()-shape/lam)<.015
    assert abs(Y0.var()-shape*(shape+2)/lam**2)<.05*(shape*(shape+2)/lam**2)

print('PASS: symbolic generator, 15 stationary integrals, likelihood-ratio samples, shape ratio, exact BESQ-transition simulation (3 conventions)')
