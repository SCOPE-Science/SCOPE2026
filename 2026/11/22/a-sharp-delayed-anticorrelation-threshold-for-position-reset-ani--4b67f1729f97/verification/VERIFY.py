#!/usr/bin/env python3
"""Reproducibility checks for cross-energy lag sign in resetting anisotropic diffusion.
All scientific claims, symbols and sources are specified in RESULT.md.
Uses the Python standard library only. Finite tests are not infinite proofs.
"""
from fractions import Fraction as F
from math import exp, expm1, log1p, sqrt, isclose

checks = 0

def check(condition, reason):
    global checks
    assert condition, reason
    checks += 1

def exact_moments(D, delta, r, w):
    # Stationarity L x^2=0, L (x^2 cos 2theta)=0,
    # L (xy sin 2theta)=0, and L (x^2 y^2)=0.
    m2 = 2 * D / r
    xc = delta / (r + w)
    yc = -xc
    xys = xc
    m22 = (2 * (D * m2 + delta * yc)
           + 2 * (D * m2 - delta * xc)
           + 8 * delta * xys) / r
    V = m22 - m2 * m2
    return m2, xc, yc, xys, m22, V

def threshold(b, w):
    u = b*b
    return w * (u + sqrt(u*u + 6*u + 4))/(2 + 3*u)

def H(rate, w, t):
    k = rate-w
    return t if k == 0 else expm1(k*t)/k

def bracket(D, delta, rate, w, t):
    V = 4*D*D/(rate*rate) + 4*delta*delta/(rate*(rate+w))
    A = 2*delta*delta/(rate+w)
    return V - A*H(rate,w,t)

def zero(D,delta,rate,w):
    V = 4*D*D/(rate*rate) + 4*delta*delta/(rate*(rate+w))
    A = 2*delta*delta/(rate+w)
    return V/A if rate==w else log1p((rate-w)*V/A)/(rate-w)

for D,delta,r,w in [(F(1),F(0),F(1),F(3)),
                     (F(2),F(1),F(2),F(1)),
                     (F(3),F(-2),F(5),F(4)),
                     (F(7,3),F(1,10),F(17,5),F(13,4))]:
    m2,xc,yc,xys,m22,V = exact_moments(D,delta,r,w)
    check(m2 == 2*D/r, 'second-moment normalization')
    check(xc+yc == 0, 'cosine anti-symmetry')
    check(xys == xc, 'sine mixed moment')
    check(r*m22 == 2*(D*m2+delta*yc)+2*(D*m2-delta*xc)+8*delta*xys,
          'independent mixed generator equation')
    check(m22 == 8*D*D/(r*r)+4*delta*delta/(r*(r+w)), 'mixed fourth moment')
    check(V == 4*D*D/(r*r)+4*delta*delta/(r*(r+w)), 'initial covariance')
    check(V>0, 'positive equal-time covariance')

for num in range(1,28):
    b=num/28
    w=1.75
    rc=threshold(b,w)
    check((1+sqrt(11))/5 < rc/w < 1, 'sharp interior threshold range')
    u=b*b; x=rc/w
    check(abs((2+3*u)*x*x-2*u*x-2)<1e-12,'quadratic threshold')
    for fac in (0.2,0.8,0.99):
        r=fac*rc
        check(r<w, 'subcritical r less than angular relaxation')
        V=bracket(1,b,r,w,0)
        A=2*b*b/(r+w)
        check(V - A/(w-r)>0, 'subcritical late-time bracket')
        for t in (0,.1,1,4,20):
            check(bracket(1,b,r,w,t)>0,'subcritical positive lag')
    for fac in (1.001,1.02,1.2,2,5):
        r=fac*rc
        t=zero(1,b,r,w)
        check(t>0,'positive crossing time')
        check(bracket(1,b,r,w,t*.6)>0, 'before crossing positive')
        check(bracket(1,b,r,w,t*1.4)<0, 'after crossing negative')
        check(abs(bracket(1,b,r,w,t))<1e-9*bracket(1,b,r,w,0),'crossing formula')
    # Strictly critical: the bracket is an exact exponentially-decaying positive function.
    r=rc
    V=bracket(1,b,r,w,0)
    for t in (0.05,.5,2,7,20):
        check(abs(bracket(1,b,r,w,t)-V*exp(-(w-r)*t))<1e-10*V,
              'critical strictly positive tail')
    # r=w resonant formula
    r=w; t=zero(1,b,r,w)
    check(abs(bracket(1,b,r,w,t))<1e-11,'resonant crossing')
    # Monotonicity in lag: normalized covariance bracket strictly decreases.
    for r in (rc/2,rc*1.05,2*w):
        times=(0,.2,1,3)
        values=[bracket(1,b,r,w,t) for t in times]
        check(all(v1>v2 for v1,v2 in zip(values,values[1:])), 'strict lag decay')

for b in (.13,.4,.95):
    old=threshold(b,1.0)
    for rate in (1e3,1e4):
        target=log1p(2+2/b**2)
        check(abs(rate*zero(1,b,rate,1)-target)<0.07,'high-reset scaled zero')
    check(threshold(b,1.0)==old,'deterministic threshold')

# Check exact covariance evolution independently against the differentiated semigroup.
for b in (.13,.4,.95):
    for r,w in ((.5,1.),(1.,1.),(1.6,1.)):
        D=1.; delta=b
        V=4*D*D/r**2+4*delta**2/(r*(r+w)); A=2*delta**2/(r+w)
        def C(t): return exp(-r*t)*bracket(D,delta,r,w,t)
        for t in (0,.05,.4,2):
            dt=1e-5
            der=(C(t+dt)-C(t-dt))/(2*dt) if t>=dt else (-3*C(t)+4*C(t+dt)-C(t+2*dt))/(2*dt)
            check(abs(der+r*C(t)+A*exp(-w*t))<5e-8,'two-time semigroup ODE')

print('PASS: {} standard-library exact-rational and numerical assertions'.format(checks))
print('FINITE CHECK LIMIT: all-parameter and all-time claims follow from the analytic proof.')
