"""Reproduce symbolic and numerical checks of the two-person eco-evolutionary model.

Requires Python with SymPy, SciPy, NumPy. Numerical trajectories only corroborate;
the nonexistence and periodicity theorems use the analytical proof.
"""
import math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from numpy.polynomial.legendre import leggauss

x, p, r, ds, dd, eps, th = sp.symbols('x p r ds dd eps th', positive=True)
q = ds-(ds+dd)*p
ax = (th+1)*x-1
f = x*(1-x)*(r*(1+x*q)/2-1)
g = eps*p*(1-p)*ax
m = 1/(x**2*(1-x)*p*(1-p))
H = ds*sp.log(p)+dd*sp.log(1-p) -eps*(th*sp.log(x/(1-x))+1/x)
assert sp.simplify((sp.diff(H,x)*f+sp.diff(H,p)*g).subs(r,2))==0
assert sp.simplify(sp.diff(m*f,x)+sp.diff(m*g,p)+(r/2-1)/(x**2*p*(1-p)))==0
assert sp.simplify(sp.diff(sp.log(p/(1-p)),p)*g-eps*ax)==0
Q=sp.log(x/(1-x))-1/x
assert sp.simplify((sp.diff(Q,x)*f-q).subs(r,2))==0
assert sp.simplify((sp.diff(sp.log(x/(1-x)),x)*f-x*q).subs(r,2))==0
print('symbolic conservation, Dulac, three mean identities: PASS')


def critical_flow(t,y,ds,dd,eps,th):
    x,p=y
    return (x*x*(1-x)*(ds-(ds+dd)*p),eps*p*(1-p)*((th+1)*x-1))


def orbit_check(ds,dd,eps,th,offset):
    xstar=1/(1+th); pstar=ds/(ds+dd)
    x0=xstar+offset
    assert 0<x0<1
    def evt(t,y): return y[1]-pstar
    evt.direction=1
    evt.terminal=False
    sol=solve_ivp(lambda t,y: critical_flow(t,y,ds,dd,eps,th),(0,700),(x0,pstar),rtol=2e-12,atol=2e-13,max_step=0.1,events=evt,dense_output=True)
    assert sol.success and len(sol.t_events[0])>=2,sol.message
    times=sol.t_events[0]
    T=next(float(t) for t in times if t>1e-3)
    Xend=sol.sol(T)
    assert np.linalg.norm(Xend-[x0,pstar])<3e-9, (T,Xend)
    ns=1500
    grid,weights=leggauss(ns)
    ts=(grid+1)*T/2
    ys=sol.sol(ts)
    mx=np.dot(weights,ys[0])/2
    mp=np.dot(weights,ys[1])/2
    mxp=np.dot(weights,ys[0]*ys[1])/2
    assert abs(mx-xstar)<2e-9,(mx,xstar)
    assert abs(mp-pstar)<2e-9,(mp,pstar)
    assert abs(mxp-mx*mp)<2e-9,(mxp,mx*mp)
    def h(xx,pp): return ds*math.log(pp)+dd*math.log(1-pp)-eps*(th*math.log(xx/(1-xx))+1/xx)
    Hs=np.array([h(xx,pp) for xx,pp in ys.T])
    assert np.max(np.abs(Hs-Hs[0]))<3e-9,np.max(np.abs(Hs-Hs[0]))
    print('asymmetry',ds,dd,'theta',th,'epsilon',eps,'period',format(T,'.9f'),
          'means',tuple(format(v,'.9f') for v in (mx,mp,mxp)),
          'covariance',format(mxp-mx*mp,'.2e'),'energy range',format(float(np.ptp(Hs)),'.2e'))


orbit_check(.75,.25,.3,2,.12)
orbit_check(.4,.4,.6,1.4,.16)
orbit_check(.25,.8,.2,3,.08)
print('three periodic-orbit numerical quadrature experiments: PASS')
