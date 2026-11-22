#!/usr/bin/env python3
"""Independent numerical and exact-arithmetic diagnostics for a two-detector coverage theorem.

Only Python standard-library modules are required. All globally quantified
claims rely on the accompanying analytic proof, not on finite checks.
"""
import json
import math
import random
from fractions import Fraction as Q

checks = 0

def ck(value, message):
    global checks
    checks += 1
    if not value:
        raise AssertionError(message)

def threshold(k):
    return (1+2*k)/(1+k)**2

def critical_k(p):
    return (1-p+math.sqrt(1-p))/p

def L(k,p):
    return math.log(p/threshold(k))

def T(k):
    return 2*k*k/(2*k*k+4*k+1)

def radial(k,p,w=1.0):
    if p <= threshold(k):
        return 0.0
    return w*math.sqrt(2*(1+k)/(k*(1+2*k))*L(k,p))

def cover(s,p,r,w):
    a=2*p*r*r/(r*r+w*w)
    b=p*p*r*r/(r*r+2*w*w)
    return a*math.exp(-s*s/(2*(r*r+w*w)))-b*math.exp(-s*s/(r*r))

def quadrature(s,p,r,w,n=170):
    # Independent, convergent midpoint integration of the ORIGINAL spatial formula.
    width=7*w+3*r
    step=2*width/n
    out=0.0
    for i in range(n):
        x=-width+(i+0.5)*step
        xx=x*x
        dens_x=math.exp(-xx/(2*w*w))/(math.sqrt(2*math.pi)*w)
        a1=p*math.exp(-((x-s)**2)/(2*r*r))
        b1=p*math.exp(-((x+s)**2)/(2*r*r))
        for j in range(n):
            y=-width+(j+0.5)*step
            a=a1*math.exp(-y*y/(2*r*r))
            b=b1*math.exp(-y*y/(2*r*r))
            out += dens_x*math.exp(-y*y/(2*w*w))/(math.sqrt(2*math.pi)*w) * (a+b-a*b)
    return out*step*step

def bisect(f,left,right,n=110):
    ck(f(left)*f(right)<0,'root not bracketed')
    for _ in range(n):
        m=(left+right)/2
        if f(left)*f(m)<=0: right=m
        else: left=m
    return (left+right)/2

# Exact symbolic check of the key rational logarithmic derivative identity
# J'(k) = 2k P(k) / ((k+1)(2k+1)(2k²+4k+1)²).
for n in range(1,300):
    k=Q(n,23)
    Lp=2*k/((1+k)*(1+2*k))
    Tp=4*k*(2*k+1)/(2*k*k+4*k+1)**2
    P=4*k**4+8*k**3+4*k**2-2*k-1
    expected=2*k*P/((k+1)*(2*k+1)*(2*k*k+4*k+1)**2)
    ck(Lp-Tp==expected, 'exact rational derivative factorization')
    a=2*(1+k)/(k*(1+2*k))
    h=1/k+2/(1+2*k)-1/(1+k)
    ck(h>0 and Lp/h==2*k*k/(2*k*k+4*k+1),'exact rational T formula')

# P changes sign only once because its coefficients have one sign change.
# These are diagnostics for the strict sign and root bounds, not a proof of Descartes' rule.
P=lambda x: 4*x**4+8*x**3+4*x*x-2*x-1
kr=bisect(P,0,2)
ck(0<kr<2,'critical polynomial root')
for j in range(1,150):
    x=j/100
    ck((P(x)<0) == (x<kr), 'P sign profile')

# Exact parametrized phase boundary and unique finite best range.
results=[]
for p in [0.03,0.1,0.25,0.5,0.75,0.95]:
    k0=critical_k(p)
    ck(abs(threshold(k0)-p)<3e-13,'threshold identity')
    kmax=bisect(lambda k:L(k,p)-T(k),k0,1e8)
    ck(kmax>k0 and abs(L(kmax,p)-T(kmax))<3e-12,'range turning point')
    ck(radial(k0,p)<1e-6,'boundary co-location (floating tolerance)')
    ck(radial(kmax,p)>radial(1.00001*k0,p),'strict gain')
    for z in [0.2,0.5,0.99,1.01,2.,4.,8.]:
        k=kmax*z
        if k>k0:
            ck(radial(k,p)<=radial(kmax,p)*(1+2e-13),'global best range at bracket')
    results.append({'p':p,'critical_k':k0,'maximum_k':kmax,'critical_detection_radius_for_w_1':1/math.sqrt(k0),'radius_at_maximum_for_w_1':1/math.sqrt(kmax),'maximal_half_separation_for_w_1':radial(kmax,p)})

# Numerical global optimization checks at many fixed radii.
rng=random.Random(416315)
for _ in range(225):
    p=.05+.92*rng.random()
    w=.5+1.5*rng.random()
    r=.08+2*rng.random()
    k=(w/r)**2
    s=radial(k,p,w)
    predicted=cover(s,p,r,w)
    for j in range(45):
        sj=j*(max(2.5*w,5*r)/44)
        ck(predicted+3e-13>=cover(sj,p,r,w),'global radial grid')
    # The signed derivative must have the correct sign on either side of the optimum.
    if s>1e-5:
        eps=min(.0001*s,.0001)
        ck(cover(s,p,r,w)>cover(s+eps,p,r,w),'right radial drop')
        ck(cover(s,p,r,w)>cover(s-eps,p,r,w),'left radial drop')

# Independent 2D spatial integration, not the Gaussian moment formula.
for p,r,w in [(0.5,0.4,1.),(.8,.75,1.2),(.2,.2,.7)]:
    k=(w/r)**2
    for s in [0.,radial(k,p,w),0.6*w]:
        exact=cover(s,p,r,w)
        numerical=quadrature(s,p,r,w)
        ck(abs(exact-numerical)<1e-4, 'original 2d integration')

# The predicted rare-detection asymptotic s_max ~ r_max ~ w*sqrt(p/(2e)).
for p in [1e-3,2e-4,1e-5,1e-6]:
    k0=critical_k(p)
    km=bisect(lambda k:L(k,p)-T(k),k0,1e10)
    approx=math.sqrt(p/(2*math.e))
    ck(abs(1/math.sqrt(km)/approx-1)<.02,'small-p radius asymptotic')
    ck(abs(radial(km,p)/approx-1)<.02,'small-p half-spacing asymptotic')

print(json.dumps({'status':'ok','assertions':checks,'two_dimensional_original_integrals':9,'example_p_0_5':next(x for x in results if x['p']==.5),'numeric_models':225,'rare_detection_cases':4},indent=2))
