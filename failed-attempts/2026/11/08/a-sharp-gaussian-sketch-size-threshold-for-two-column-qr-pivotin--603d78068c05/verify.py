#!/usr/bin/env python3
"""Finite supplementary diagnostic checks for the two-column sketched-QR pivot law.

All mathematical claims, including the continuum bounds, are proved analytically
in RESULT.md. These diagnostics are not an infinite-domain certificate.
Requires only Python >=3.10 standard library.
"""
import math
import random
from fractions import Fraction as F

COUNT=0

def check(condition, message=''):
    global COUNT
    COUNT+=1
    if not condition:
        raise AssertionError(message or 'check failed')

def close(x,y,atol=1e-10,rtol=1e-9):
    check(abs(x-y)<=atol+rtol*abs(y), f'not close: {x}, {y}')

def beta_cdf(k,z):
    """Numerical regularized beta CDF, integrating x=s**2 to avoid 0 singularity."""
    if z<=0: return 0.
    if z>=1: return 1.
    a=k/2
    c=2*math.exp(math.lgamma(2*a)-2*math.lgamma(a))
    b=math.sqrt(z)
    n=1024
    dx=b/n
    def f(j):
        x=j*dx
        return c*x**(k-1)*(1-x*x)**(a-1)
    s=f(0)+f(n)
    for j in range(1,n):
        s+=(4 if j%2 else 2)*f(j)
    return s*dx/3

def theta(t,rho):
    w=t*t
    d=math.hypot(w-1,2*t*math.sqrt(1-rho*rho))
    return (d+1-w)/(2*d)

def wrong_pivot(k,t,rho):
    return beta_cdf(k,theta(t,rho))

def risk(k,t,rho):
    return 1+(t*t-1)*wrong_pivot(k,t,rho)

def exact_orthogonal_k2(w):
    w=F(w)
    return 2*w/(w+1)

def exact_orthogonal_k4(w):
    w=F(w)
    return w*(w*w+6*w+1)/(w+1)**3

# Exact rational formulas from chi-square/beta CDF specializations.
for w in range(2,101):
    u=F(1,w+1)
    lhs=1+(w-1)*u
    check(lhs==exact_orthogonal_k2(w))
    lhs=1+(w-1)*(3*u*u-2*u**3)
    check(lhs==exact_orthogonal_k4(w))
    # Derivative of the rational four-row risk from the quotient rule.
    N=F(w**3+6*w*w+w)
    Np=F(3*w*w+12*w+1)
    check(Np*(w+1)-3*N == -3*w*w+10*w+1)

# Critical point and exact optimal value to floating precision.
wstar=(5+2*math.sqrt(7))/3
opt=(17+7*math.sqrt(7))/27
close(float(exact_orthogonal_k4(F.from_float(wstar))),opt)
close(-3*wstar**2+10*wstar+1,0)
for w in (1.01,1.2,2,3,4,10,100,1000):
    check(float(exact_orthogonal_k4(F.from_float(w)))<=opt+1e-12)

# Check trace and determinant of correlated quadratic form, and eigenvalue signs.
for t in (1.01,1.2,2,3,10,100):
    for rho in (-0.999,-0.9,-0.5,0.,0.5,0.9,0.999):
        s=math.sqrt(1-rho*rho)
        d=math.hypot(t*t-1,2*t*s)
        lam_plus=(1-t*t+d)/2
        lam_minus=(1-t*t-d)/2
        check(lam_plus>0 and lam_minus<0)
        close(lam_plus+lam_minus,1-t*t)
        close(lam_plus*lam_minus,-t*t*s*s)
        close(lam_plus/d,theta(t,rho),atol=1e-12)

# Gaussian-sketched column norms and their beta prediction (seeded Monte Carlo).
rng=random.Random(20261107)
for k,t,rho in [(1,2.,0.),(1,4.,.7),(2,1.5,-.5),(2,4.,0.),
                (3,2.,.7),(4,2.,0.),(4,3.,.8),(6,1.2,-.9)]:
    count=0
    N=25000
    s=math.sqrt(1-rho*rho)
    for _ in range(N):
        g=[rng.gauss(0,1) for _ in range(k)]
        h=[rng.gauss(0,1) for _ in range(k)]
        if sum(v*v for v in g)>t*t*sum((rho*x+s*y)**2 for x,y in zip(g,h)):
            count+=1
    p=wrong_pivot(k,t,rho)
    check(abs(count/N-p)<0.018, f'simulation mismatch k={k}, t={t}, rho={rho}: {count/N} vs {p}')

# Exact low-dimensional beta CDF versus independent beta quadrature.
for w in (1.01,1.5,2,3,4,12,100):
    z=1/(1+w)
    close(beta_cdf(2,z),z,atol=1e-11)
    close(beta_cdf(4,z),3*z*z-2*z*z*z,atol=1e-11)

# Coherence extremality and universal mean ratio on a finite stress grid.
for k in range(1,11):
    for t in (1.001,1.02,1.2,1.7,2,3,5,10,30):
        r0=risk(k,t,0)
        for rho in (-.999,-.97,-.7,-.3,.3,.7,.97,.999):
            check(risk(k,t,rho)<=r0+1e-10)
        if k>=2:
            check(r0<2)

# Full asymptotic orders at large contrast, checked against proven constants.
for k in (1,2,3,4,5,6):
    for rho in (0,.4,.8):
        t=300.
        p=wrong_pivot(k,t,rho)
        C=2*math.exp(math.lgamma(k)-2*math.lgamma(k/2))/k
        predicted=C*(1-rho*rho)**(k/2)*t**(-k)
        check(abs(p/predicted-1)<.004,(k,rho,p,predicted))

print(f'PASS: {COUNT} diagnostic assertions; standard library only.')
