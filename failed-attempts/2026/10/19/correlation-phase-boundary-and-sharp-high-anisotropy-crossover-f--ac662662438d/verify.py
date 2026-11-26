#!/usr/bin/env python3
"""Deterministic reproducibility checks for planar correlated-Gaussian range finding.
Standard-library only; the proof in RESULT.md establishes all continuum claims.
"""
import math
from fractions import Fraction

checks = 0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1


def exact_risk(a, b, c1, c2, rho):
    delta = math.sqrt(max(0.0, 1.0-rho*rho))
    d = a*b*math.sqrt(c1*c2)*delta
    return (a*a*b*b*(c1+c2)+(a*a+b*b)*d)/(a*a*c1+b*b*c2+2*d)


def quadrature_risk(a,b,c1,c2,rho,n=32768):
    delta = math.sqrt(max(0.0,1.0-rho*rho))
    x_scale, y_scale = math.sqrt(c1), math.sqrt(c2)
    acc = 0.0
    for j in range(n):
        theta = 2.0*math.pi*(j+0.5)/n
        x = x_scale*math.cos(theta)
        y = y_scale*(rho*math.cos(theta)+delta*math.sin(theta))
        den = a*a*x*x+b*b*y*y
        acc += a*a*b*b*(x*x+y*y)/den
    return acc/n

# Exact rational verification of derivative numerator and the covariance phase boundary.
for ai in (2,3,5,9):
    for bi in (1,2,3):
        if ai<=bi: continue
        for c1i in (1,2,3,4,7):
            for c2i in (1,2,3,5,11):
                a,b,c1,c2=map(Fraction,(ai,bi,c1i,c2i))
                u=a*a*b*b*(c1+c2)
                v=a*a+b*b
                w=a*a*c1+b*b*c2
                left=v*w-2*u
                right=(a*a-b*b)*(a*a*c1-b*b*c2)
                check(left==right,'derivative factorization')
                for di in (0,1,4):
                    d=Fraction(di)
                    r=(u+v*d)/(w+2*d)
                    check(b*b <= r <=a*a,'geometric bounds')

# The closed-form expected error matches a separate polar-angle integral.
settings=[(2.,1.,1.,1.,0.),(2.,1.,1.,1.,0.7),
          (10.,1.,1.,1.,0.),(10.,1.,1.,1.,0.9),
          (3.,1.,0.01,1.,0.7),(3.,1.,1./9.,1.,0.9),
          (1.3,0.8,1.7,0.6,-0.6),(9.,2.,2.,1.,-0.7)]
for s in settings:
    prediction=exact_risk(*s)
    integration=quadrature_risk(*s)
    check(abs(prediction-integration)<1e-8,
          f'angular integral mismatch: {s}: {prediction} vs {integration}')
    print('angle',repr(s),'closed',f'{prediction:.12g}','integral',f'{integration:.12g}')

# For fixed diagonal variances, the direction of correlation sensitivity is sharp.
for a,b,c1,c2 in [(3.,1.,1.,1.),(3.,1.,0.01,1.),(3.,1.,1./9.,1.)]:
    v0=exact_risk(a,b,c1,c2,0.0)
    v1=exact_risk(a,b,c1,c2,0.8)
    sign=(a*a-b*b)*(a*a*c1-b*b*c2)
    check((v1<v0) if sign>1e-12 else ((v1>v0) if sign< -1e-12 else abs(v1-v0)<1e-12),
          'correlation sensitivity sign')

# Exact algebraic decomposition of the equal-variance, one-spike error.
for k in (2.,5.,20.,100.):
    for rho in (0.,0.4,0.8,0.99):
        delta=math.sqrt(1-rho*rho)
        direct=exact_risk(k,1.,1.,1.,rho)
        split=k*delta+2*k*k*rho*rho/(k*k+1+2*k*delta)
        check(abs(direct-split)<5e-13*max(1,direct),'sharp crossover identity')

# A double scaling with k*sqrt(1-rho^2) -> tau yields risk -> 2+tau.
for tau in (0.,0.5,2.,5.):
    for k in (10000.,100000.):
        delta=tau/k
        rho=math.sqrt(1-delta*delta)
        risk=exact_risk(k,1.,1.,1.,rho)
        check(abs(risk-(2+tau))<0.003,'double-scaling limit')

print('PASS:',checks,'deterministic checks; not a replacement for the analytic proof')
