"""Reproducible checks for the sharp stationary Brownian resetting density envelope.

The analytic proof, not this finite check, establishes arbitrary-distribution bounds.
Requires Python 3 and scipy.
"""
from math import exp, erfc, pi, sqrt, isclose
from scipy.optimize import brentq
from scipy.integrate import quad

assertions = 0

def check(condition, message="check failed"):
    global assertions
    assert condition, message
    assertions += 1

def phi(t, x, sigma):
    return exp(-x*x/(2*sigma*sigma*t))/sqrt(2*pi*sigma*sigma*t)

def H(t, x, sigma):
    if t <= 0:
        return 0.0
    a = abs(x)/(sigma*sqrt(2*t))
    return 2*sqrt(t)*exp(-a*a)/(sigma*sqrt(2*pi)) - abs(x)*erfc(a)/(sigma*sigma)

def F(z):
    return 2*sqrt(pi*z)*exp(z)*erfc(sqrt(z))-1

zstar = brentq(F, .01, .49, xtol=1e-15)
check(0 < zstar < .5)
check(abs(F(zstar)) < 1e-13)
for x,sigma in ((1.0,1.0),(.4,1.0),(1.,2.),(2.,.7)):
    tstar = x*x/(2*sigma*sigma*zstar)
    check(isclose(H(tstar,x,sigma)/tstar,phi(tstar,x,sigma),rel_tol=1e-12))
    for t in [tstar*a for a in (.01,.1,.2,.5,.8,1.,1.2,2.,10.,100.)]:
        check(H(t,x,sigma)/t <= phi(tstar,x,sigma)*(1+1e-12))
        a, err = quad(lambda s: phi(s,x,sigma),0,t,epsabs=2e-10,epsrel=1e-10)
        check(abs(a-H(t,x,sigma)) <= 5e-9*max(1,a))
    for mu in (tstar*.25,tstar*.75,tstar,tstar*1.5,tstar*3.):
        optimum = phi(tstar,x,sigma) if mu < tstar else H(mu,x,sigma)/mu
        for a in (.001,.02,.1,.5,.95):
            e = a*mu
            for b in (max(1.01*mu,1.01*tstar),5*mu,20*mu):
                if b <= mu: continue
                w = (mu-e)/(b-e)
                val = ((1-w)*H(e,x,sigma)+w*H(b,x,sigma))/mu
                check(val<=optimum+1e-10)
        if mu < tstar:
            for e in (1e-2*mu,1e-4*mu,1e-6*mu):
                w=(mu-e)/(tstar-e)
                val=((1-w)*H(e,x,sigma)+w*H(tstar,x,sigma))/mu
                check(val<optimum)
            check(abs(val-optimum) < 1e-5)
        else:
            check(abs(H(mu,x,sigma)/mu-optimum) < 1e-12)

print('checks_passed',assertions)
print('zstar',format(zstar,'.15g'))
print('dimensionless_spatial_threshold',format(sqrt(2*zstar),'.15g'))
print('sstar_for_x1_sigma1',format(1/(2*zstar),'.15g'))
print('at_x1_sigma1_mu1_optimum',format(phi(1/(2*zstar),1,1),'.15g'))
print('at_x1_sigma1_mu1_deterministic',format(H(1,1,1),'.15g'))
