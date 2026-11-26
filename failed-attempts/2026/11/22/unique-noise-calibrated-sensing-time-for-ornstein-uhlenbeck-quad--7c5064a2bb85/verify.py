"""Reproduce symbolic and independent numerical checks for quadratic OU energy sampling."""
from math import exp, expm1, isfinite
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq

l, x = sp.symbols('l x', positive=True)
q = sp.exp(-2*l)
t = sp.Symbol('t', positive=True)
K1 = sp.exp(-l*x)*sp.sinh(l*t)/l
K2 = sp.exp(-l*t)*sp.sinh(l*x)/l
H_integrated = sp.integrate(K1**2, (t,0,x)) + sp.integrate(K2**2, (t,x,1))
H_closed = (2+2*q-(4*l*x+2+q)*sp.exp(-2*l*x)-q*sp.exp(2*l*x))/(8*l**3)
V = (1-sp.exp(-2*l*x))/(2*l)
D = (4*l*x+q-q*sp.exp(4*l*x))/(4*l**2)
varQ = (4*l+8*l*q-5+4*q+q*q)/(8*l**4)
assert sp.simplify(sp.expand((H_integrated-H_closed).rewrite(sp.exp))) == 0
assert sp.simplify(sp.diff(H_closed,x)-sp.diff(V,x)*D) == 0
assert sp.simplify(sp.diff(D,x)-(1-sp.exp(4*l*x-2*l))/l)==0
assert sp.simplify(2*sp.integrate(H_closed,(x,0,1))-varQ)==0
assert sp.limit(varQ,l,0)==sp.Rational(1,3)
assert sp.limit(H_closed,l,0)==x*x-sp.Rational(2,3)*x*x*x
assert sp.limit(V,l,0)==x


def values(lam, xpos):
    e=exp(-2*lam)
    v=-expm1(-2*lam*xpos)/(2*lam)
    h=(2+2*e-(4*lam*xpos+2+e)*exp(-2*lam*xpos)-e*exp(2*lam*xpos))/(8*lam**3)
    d=(4*lam*xpos+e-e*exp(4*lam*xpos))/(4*lam**2)
    return v,h,d


def knot(lam, eta):
    def g(z):
        v,h,d=values(lam,z)
        return (v+eta)*d-h
    return brentq(g,.5,1,xtol=2e-14)


def cov(lam, t, x):
    return (exp(-lam*abs(t-x))-exp(-lam*(t+x)))/(2*lam)

independent_integrals = 0
for lam in [.2,.7,1.,2.,5.]:
    for z in [.16,.37,.51,.73,.92]:
        h_num=quad(lambda tt:cov(lam,tt,z)**2,0,z,epsabs=2e-13)[0]+quad(lambda tt:cov(lam,tt,z)**2,z,1,epsabs=2e-13)[0]
        v,h,_=values(lam,z)
        assert abs(h-h_num) < 5e-11*max(1,h_num)
        independent_integrals+=1

checks=0
for lam in [.05,.1,.2,.4,.75,1.,1.5,2.,3.,4.,6.,10.]:
    previous=.5
    eta_grid=[0.,.0001,.001,.01,.05,.2,1.,4.,10.,100.,10000.]
    for eta in eta_grid:
        r=knot(lam,eta)
        assert .5<r<1 and r>previous-1e-12
        previous=r
        v,h,d=values(lam,r)
        if eta>0: assert d>0
        max_val=h/(v+eta)
        for xx in np.linspace(.02,1,151):
            vv,hh,_=values(lam,xx)
            assert max_val + 2e-10 >= hh/(vv+eta), (lam,eta,r,xx)
            checks+=1
    root_limit=brentq(lambda z:values(lam,z)[2],.5,1)
    assert knot(lam,1e6)<root_limit and root_limit-knot(lam,1e6)<1e-5

if __name__ == '__main__':
    print('PASS: exact OU covariance integration, derivative factorization, and quadratic-energy variance.')
    print(f'PASS: {independent_integrals} independent covariance integrals; {checks} global grid comparisons.')
    for eta in [0,.2,1]:
        z=knot(1,eta)
        v,h,_=values(1,z)
        q=exp(-2)
        total=(4+8*q-5+4*q+q*q)/8
        print(f'lambda=1, eta={eta:g}: x*={z:.12f}, Bayes risk={total-2*(h/(v+eta))**2:.12f}')
