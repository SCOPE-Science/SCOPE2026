#!/usr/bin/env python3
"""Reproduce finite-dimensional checks for a renewal Brownian work model.

Run: python check.py. This script tests exact algebra and finite quadrature;
the stable/normal limit theorems require the analytical proof.
"""
import math
import numpy as np
from scipy.integrate import quad

NTEST=0

def check(p, desc):
    global NTEST
    NTEST+=1
    if not bool(p):
        raise AssertionError(desc)

def expect_close(a,b,tol=1e-9):
    check(math.isclose(float(a),float(b),rel_tol=tol,abs_tol=tol),f'{a} vs {b}')

def normal_pdf(z):
    return math.exp(-z*z/2)/math.sqrt(2*math.pi)

def tail_coefficients(q, c, lam=1., D=1., mu=1., delta=.5):
    v=lam*D*mu/(mu+delta)
    cut=math.sqrt(v/(lam*D))
    cp=2*c*quad(lambda z:(lam*D*z*z-v)**q*normal_pdf(z),cut,18,epsabs=1e-11)[0]
    cm=2*c*quad(lambda z:(v-lam*D*z*z)**q*normal_pdf(z),0,cut,epsabs=1e-11)[0]
    return cp,cm

def exact_tail_at_x(q, x, mu=1., delta=.5, lam=1., D=1.):
    # Exact when the return preparation is concentrated at the origin.
    # T is Lomax(q, (q-1)*mu); xi=T*(lam*D*Z^2-v)-v*delta.
    theta=(q-1)*mu
    v=lam*D*mu/(mu+delta)
    cut=math.sqrt(v/(lam*D))
    plus=2*quad(lambda z:normal_pdf(z)*(1+(x+v*delta)/(theta*(lam*D*z*z-v)))**(-q),cut,18,epsabs=1e-13)[0]
    minus=2*quad(lambda z:normal_pdf(z)*(1+(x-v*delta)/(theta*(v-lam*D*z*z)))**(-q),0,cut,epsabs=1e-13)[0]
    return plus,minus

for q in (1.25,1.5,1.8,2.,2.6):
    mu=1.; delta=.5; lam=1.; D=1.
    theta=(q-1)*mu
    c=theta**q
    cp,cm=tail_coefficients(q,c,lam,D,mu,delta)
    check(cp>0 and cm>0, 'Both tail coefficients positive')
    # For q=2 the sum is the closed-form leading truncated-second-moment constant.
    if q==2.:
        v=mu/(mu+delta)
        expect_close(cp+cm,c*(3-2*v+v*v),1e-10)
    for x in (1e4,1e6):
        ep,em=exact_tail_at_x(q,x,mu,delta,lam,D)
        expect_close(ep*x**q,cp,1e-2 if x==1e4 else 4e-4)
        expect_close(em*x**q,cm,1e-2 if x==1e4 else 4e-4)
    # Increased deterministic reset overhead lowers the negative coefficient
    # and raises the positive coefficient (the work-rate threshold decreases).
    cp2,cm2=tail_coefficients(q,c,lam,D,mu,1.5)
    check(cp2>cp and cm2<cm, 'Strict one-sided coefficient monotonicity')

# Independent direct variance computation for finite-second-moment clocks:
for q in (2.5,3.5,6.,15.):
  for delta in (0.,.25,1.,4.):
    mu=1.1; lam=1.7; D=.8; sig2=.7
    theta=(q-1)*mu
    E_T2=2*theta**2/((q-1)*(q-2))
    variance_T=E_T2-mu**2
    m=mu+delta
    v=lam*D*mu/m
    # E[w^2 | T] = lambda^2(2 sigma^2 D T + 3 D^2 T^2).
    E_w2=lam**2*(2*sig2*D*mu+3*D*D*E_T2)
    E_wT=lam*D*E_T2
    # expand E[(w-v(T+delta))^2] from mixed moments:
    direct=E_w2-2*v*(E_wT+delta*lam*D*mu)+v*v*(E_T2+2*delta*mu+delta*delta)
    formula=lam**2*(2*D**2*E_T2+2*D*sig2*mu)+((lam*D*delta/m)**2)*variance_T
    expect_close(direct,formula,1e-10)
    check(formula>0,'Nondegenerate normal variance')

# Exact negative-work bound at every T follows algebraically:
for x0 in (-3., -1., 0., 2.5):
    for bm in (-4.,-2.,-.5,0.,1.,3.):
        w=.7/2*((x0+bm)**2-x0*x0)
        check(w>=-.7*x0*x0/2-1e-12,'Pointwise lower bound for one-cycle work')

print('PASS:',NTEST,'deterministic quadrature, finite-variance and inequality checks')
print('Illustrative Pareto q=3/2, mu=lambda=D=1, return overhead=1/2:')
q=1.5;c=(q-1)**q
cp,cm=tail_coefficients(q,c)
print('  v=',1/(1+.5),'c_+=',format(cp,'.12f'),'c_-=',format(cm,'.12f'))
print('  Stable-Levy one-sided coefficients per unit time: ',cp/1.5,cm/1.5)
print('No numerical calculation is treated as proof of an asymptotic limit.')
