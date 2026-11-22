"""Reproducibility tests for magnetic position-reset memory transitions.

Uses independent real matrix-exponential and complex-resolvent representations.
Finite checks supplement, but do not replace, the analytic sign proof.
"""
import math
import cmath
import numpy as np
from scipy.linalg import expm
from scipy.integrate import quad


def formula(r,g,w,theta,t):
    z=complex(-g,w)
    b=theta/(complex(r+g,-w))
    ss=2*b.real/r
    return (ss*math.exp(-r*t)+
            (theta*cmath.exp(z*t)*1/((complex(r+g,-w))*(complex(r-g,w)))-
             theta*math.exp(-r*t)/((complex(r+g,-w))*(complex(r-g,w)))).real)

def matrix(r,g,w,theta,t):
    den=(r+g)**2+w*w
    b=np.array([theta*(r+g)/den,theta*w/den])
    cov=2*b[0]/r
    M=np.array([[-r,1.,0.],[0.,-g,-w],[0.,w,-g]])
    return float((expm(t*M)@np.array([cov,*b]))[0])

checks=0
for r in [0.25,0.9,1.,1.7,3.]:
    for g in [0.35,1.,2.]:
        for w in [0.07,0.6,2.1,5.3]:
            for t in [0,0.1,0.6,1.2,3.7,6.1]:
                a=formula(r,g,w,1.6,t)
                b=matrix(r,g,w,1.6,t)
                assert math.isclose(a,b,rel_tol=2e-10,abs_tol=1e-11),(r,g,w,t,a,b)
                checks+=1
            # Independent Laplace-transform identity for stationary position variance:
            # E X^2 = (2/r) int_0^infty e^{-ru} K(u) du.
            quadrature=quad(lambda t:math.exp(-(r+g)*t)*math.cos(w*t),0,np.inf,epsabs=1e-11)[0]*3.2/r
            assert math.isclose(formula(r,g,w,1.6,0),quadrature,rel_tol=1e-9)
            checks+=1
# The exceptional critical-rate line has a strictly negative trough only below w=g/sqrt(2).
for w in [0.2,0.5,0.7,1/math.sqrt(2),0.8,1.,2.]:
    g=r=1.
    minimum=3-math.sqrt(1+4/w**2)
    assert (minimum < -1e-10)==(w < 1/math.sqrt(2)-1e-10)
    checks+=1
# At r>g the tail, scaled by e^{g t}, alternates signs indefinitely
# through a nonzero harmonic; at r<g its scaled limiting prefactor is positive.
for r in [0.25,0.7,0.99]:
    for w in [0.2,0.6,1.7]:
        g=1.
        numerator=(r-g)*(r-2*g)*(r+g)+(r+2*g)*w*w
        assert numerator>0
        checks+=1
print('PASS:',checks,'matrix, integral, and sharp-boundary checks.')
