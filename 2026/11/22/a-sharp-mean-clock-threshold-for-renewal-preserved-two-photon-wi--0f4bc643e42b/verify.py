#!/usr/bin/env python3
"""Independent algebraic and numerical checks for a renewal-controlled Fock-state phase-space theorem.

This finite checker corroborates the theorem; its all-clock conclusion uses the analytic proof.
Only Python, SymPy, NumPy, and SciPy are required.
"""
import math
import numpy as np
import sympy as s
from scipy.integrate import quad
from scipy.optimize import brentq

T, A, B, z, r, x = s.symbols('T A B z r x', positive=True)
P = 1 + (8*x-4)*A/T + (8*x*x-16*x+4)*B/(2*T)
Phi = lambda a,b: 4*a*a/b -4*a +2*b
pmin = s.factor(P.subs(x,1-A/B))
assert s.simplify(pmin -(1-Phi(A,B)/T))==0
assert s.simplify(s.diff(P,x).subs(x,1-A/B))==0
assert s.factor(s.diff(P,x,2)-8*B/T)==0
phi = s.factor(Phi(1-z,1-z*z))
assert s.factor(phi-2*(1-z)*(1+z*z)/(1+z))==0
q = s.factor(z*s.diff(z*s.diff(phi,z),z))
quart = 2*z**4+5*z**3+3*z**2-3*z+1
assert s.factor(q+4*z*quart/(1+z)**3)==0
assert s.factor(Phi(1/(r+1),2/(r+2))-r**-1 - (r**3-r-2)/(r*(r+1)**2*(r+2)))==0
assert s.simplify(s.det(s.hessian(Phi(A,B), (A,B)))) == 0
assert s.simplify(s.diff(Phi(A,B),A,2)-8/B)==0
assert s.simplify(s.diff(Phi(A,B),B,2)-8*A*A/B**3)==0
assert s.simplify(s.diff(Phi(A,B),A,B)+8*A/B**2)==0
count = 12
phi_fun = lambda t: 2*(-math.expm1(-t))*(1+math.exp(-2*t))/(1+math.exp(-t))
root=brentq(lambda t: phi_fun(t)-t,.2,2,xtol=2e-14)
assert abs(root-1.130359548845188)<1e-12
count+=1
from numpy.random import default_rng
rng=default_rng(126374)
for k in range(280):
    n=int(rng.integers(2,11))
    w=rng.dirichlet(np.ones(n))
    times=np.exp(rng.normal(0,1.2,n))
    mean=float(np.dot(w,times))
    e=np.exp(-times)
    a=float(np.dot(w,1-e));b=float(np.dot(w,1-e*e))
    value=4*a*a/b-4*a+2*b
    assert value <= phi_fun(mean)+2e-13
    assert value <= np.dot(w,[phi_fun(t) for t in times])+2e-13
    m1=a/mean;m2=b/(2*mean)
    peak=1-a/b
    assert 0<peak<.5
    ys=[1+(8*u-4)*m1+(8*u*u-16*u+4)*m2 for u in (0,peak,2)]
    assert ys[1]<=ys[0]+1e-12 and ys[1]<=ys[2]+1e-12
    assert abs(ys[1]-(1-value/mean))<3e-12
    # Independent equilibrium-age integration of loss for a finite mixture of deterministic intervals.
    u=float(rng.uniform(0,2))
    def wigner_at_age(tt):
        eta=math.exp(-tt)
        p0=(1-eta)**2; p1=2*eta*(1-eta);p2=eta**2
        L0=1;L1=1-4*u;L2=1-8*u+8*u*u
        return p0*L0-p1*L1+p2*L2
    integ=sum(float(wj)*quad(wigner_at_age,0,float(tj),epsabs=2e-12)[0] for wj,tj in zip(w,times))/mean
    direct=1+(8*u-4)*m1+(8*u*u-16*u+4)*m2
    assert abs(integ-direct)<2e-10
    count+=7
for rho in (.1,.4,1,1.3,1.5213797068045676,2,4,10):
    mean=1/rho
    a=1/(rho+1);b=2/(rho+2)
    val=4*a*a/b-4*a+2*b
    sign=(rho**3-rho-2)/(rho*(rho+1)**2*(rho+2))
    assert abs(val-mean-sign)<2e-12
    count+=1
# Example in which a fixed-period clock preserves negativity but exponential clock does not.
mean=.9
assert phi_fun(mean)>mean
rho=1/mean
a=1/(rho+1);b=2/(rho+2)
assert 4*a*a/b-4*a+2*b<mean
count+=2
print(f'PASS: {count} algebraic and numerical checks; threshold={root:.15f}; period-0.9 example verified')
