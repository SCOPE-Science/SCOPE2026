#!/usr/bin/env python3
"""Independent standard-library numerical corroboration of sharp affine Fock stability."""
import math, cmath, random
PI=math.pi
C0=math.sqrt(PI)/2
SHARP=math.sqrt(2/(2-math.sqrt(PI)))

def bessel01(x):
    # Direct series; x is restricted to <= 6 in checks.
    h=x/2.0
    term0=1.0; term1=h
    y0=term0; y1=term1
    for k in range(1,60):
        term0 *= h*h/(k*k)
        term1 *= h*h/(k*(k+1))
        y0 += term0; y1 += term1
    return y0,y1

def rice_formula(s):
    if s==1: return 1.0
    x=s*s/(2*(1-s*s))
    u,v=bessel01(x)
    return C0*math.sqrt(1-s*s)*math.exp(-x)*((1+2*x)*u+2*x*v)

def rice_quadrature(s,nr=230,na=160):
    # Independent polar-Gaussian integration (no Bessel function).
    step=5/nr
    b=math.sqrt(1-s*s)
    accum=0.0
    roots=[cmath.exp(2j*PI*(k+.5)/na) for k in range(na)]
    for j in range(nr):
        rad=(j+.5)*step
        mean=sum(abs(s+b*rad*e) for e in roots)/na
        accum += 2*rad*math.exp(-rad*rad)*mean*step
    return accum

def ratio_sq(s,t):
    m=rice_formula(s)
    return (t*t+1-2*t*s)/(t*t+1-2*t*m)

assert abs(SHARP-2.9646965828533536)<1e-12
for s in (0,.1,.25,.4,.6,.75,.85,.92):
    if abs(rice_formula(s)-rice_quadrature(s))>2.5e-4:
        raise AssertionError(('quadrature',s,rice_formula(s),rice_quadrature(s)))
    m=rice_formula(s)
    assert m <= C0+(1-C0)*s+1e-11
    assert m>=s
    for t in (.15,.6,1,1.6,3.0):
        assert ratio_sq(s,t)<=SHARP**2+2e-11
for x in (.001,.02,.1,.3,.8,1.5,3.0,6.0):
    u,v=bessel01(x)
    assert 2*x*u-(2*x+1)*v>0
assert abs(ratio_sq(0,1)-SHARP**2)<1e-12
# Strict scale maximum for nonconstant s; discrete independent check.
for s in (.2,.5,.8):
    assert ratio_sq(s,.5)<ratio_sq(s,1)
    assert ratio_sq(s,2)<ratio_sq(s,1)
print('AFFINE_FOCK_SHARP_STABILITY_CHECKS_PASSED')
