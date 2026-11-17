#!/usr/bin/env python3
"""Symbolic and numerical checks of a conserved quantity in a risk-feedback game."""
from fractions import Fraction
from math import comb, log, exp, sqrt, pi
import sympy as sp
from scipy.integrate import solve_ivp, quad
import numpy as np

x,r,b,c,e=sp.symbols('x r b c e',positive=True)
checks=0
for m in range(1,6):
    for n in range(1,6):
        d=m+n
        gamma=sp.binomial(d,m)*x**m*(1-x)**n
        f=x*(1-x)*(b*r*gamma-c)/e
        g=r*(1-r)*(sp.Rational(m,n)-(sp.Rational(d,n))*x)
        Y=1/gamma
        a=sp.Rational(n)*c/e
        q=sp.Rational(n)*b/e
        lhs=sp.factor(sp.diff(Y,x)*f-(a*Y-q*r)*g/(r*(1-r)))
        assert lhs==0,(m,n,lhs)
        checks+=1
        xx=sp.Rational(m,d)
        gg=sp.factor(gamma.subs(x,xx))
        rr=c/(b*gg)
        f_r=sp.diff(f,r).subs({x:xx,r:rr})
        g_x=sp.diff(g,x).subs({x:xx,r:rr})
        assert sp.factor(-f_r*g_x-sp.Rational(m,d)*c*(1-rr)/e)==0
        checks+=1
        curvature=sp.factor((sp.diff(Y,x,2)).subs(x,xx))
        expect=sp.factor((1/gg)*(sp.Rational(m)/xx**2+sp.Rational(n)/(1-xx)**2))
        assert sp.factor(curvature-expect)==0
        checks+=1
# Critical examples, H exact integration in logit coordinate
m,n=2,3
N=m+n+1
b0=1.0;c0=0.1;e0=0.1
Gamma=lambda z: comb(m+n,m)*z**m*(1-z)**n
xe=m/(m+n)
re=c0/(b0*Gamma(xe))
assert 0<re<1
ss=log(re/(1-re))
a=n*c0/e0;q=n*b0/e0
sig=lambda s: 1/(1+np.exp(-s))
def H(xv,rv):
    s=log(rv/(1-rv))
    integral=quad(lambda v: np.exp(-a*v)*sig(v),ss,s,epsabs=1e-12,epsrel=1e-12)[0]
    return np.exp(-a*s)/Gamma(xv)+q*integral

def f(t,z):
    xx,rr=z
    return [xx*(1-xx)*(b0*rr*Gamma(xx)-c0)/e0,rr*(1-rr)*(m/n-(m+n)/n*xx)]
start=[xe+0.025,re]
trajectory=solve_ivp(f,(0,60),start,rtol=4e-11,atol=1e-12,max_step=0.035,dense_output=True)
assert trajectory.success
hv=np.array([H(xx,rr) for xx,rr in trajectory.y.T[::20]])
maxdrift=float(np.max(np.abs(hv-hv[0])))
assert maxdrift<1e-6,maxdrift
omega=sqrt(m*c0/(m+n)/e0*(1-re))
assert 0<omega<10
print('VERIFY_OK',checks,'symbolic identities; first-integral numerical drift',maxdrift,'critical_equilibrium',xe,re,'small_period',2*pi/omega)
