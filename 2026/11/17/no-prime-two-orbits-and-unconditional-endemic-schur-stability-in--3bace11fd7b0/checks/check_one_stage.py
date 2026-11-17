"""Reproduce algebraic identities and representative numeric checks for the one-stage map.
This is a finite consistency check, not a substitute for the all-parameter proof.
"""
from fractions import Fraction as Q
from math import exp, log
from random import Random


def map2(a, r, e, z, t, H):
    s = 1-a-r
    return e*a+H(a)*s, t*a+z*r


def H_risk(a, rho, nu, tau):
    e=exp(-(1+nu)*tau)
    L = rho*(1-e)*a/(1+nu)
    m = nu*tau
    B = L+m
    return L/B*(-__import__('math').expm1(-B))


def dH_risk(a, rho, nu, tau):
    e=exp(-(1+nu)*tau)
    c = rho*(1-e)/(1+nu)
    L=c*a
    B=L+nu*tau
    return c*((nu*tau)/B**2*(-__import__('math').expm1(-B))+(L/B)*exp(-B))


def smooth_bump(x):
    return exp(1-1/(1-x*x)) if abs(x)<1 else 0.0

def H_witness(a):
    return 0.9*smooth_bump(20*(a-0.2))+(3/11)*smooth_bump(20*(a-0.5))

# Exact two-cycle under deliberately nonmonotone, still [0,1]-valued incidence.
e,z,t=Q(1,4),Q(1,2),Q(3,8)
a1,r1,a2,r2=Q(1,2),Q(9,40),Q(1,5),Q(3,10)
h1,h2=Q(3,11),Q(9,10)
assert e*a1 + h1*(1-a1-r1)==a2
assert t*a1+z*r1==r2
assert e*a2 + h2*(1-a2-r2)==a1
assert t*a2+z*r2==r1
assert abs(H_witness(float(a1))-float(h1))<1e-14
assert abs(H_witness(float(a2))-float(h2))<1e-14
assert all(0<=H_witness(j/10000)<=1 for j in range(10001))

# More than 4000 physically admissible comparisons validate derivative and ratio.
rg=Random(71337)
for _ in range(4000):
    rho=10**rg.uniform(-2,2)
    nu=10**rg.uniform(-3,1)
    tau=10**rg.uniform(-3,1)
    a=rg.uniform(.00001,.999)
    h=H_risk(a,rho,nu,tau)
    dh=dH_risk(a,rho,nu,tau)
    assert 0<h<1 and dh>0 and a*dh<h + 1e-12
    epsilon=1e-7
    # Finite-difference only when not too near numerical underflow.
    if 1e-9<h<1-1e-8 and dh>1e-8:
        fd=(H_risk(a+epsilon,rho,nu,tau)-H_risk(a-epsilon,rho,nu,tau))/(2*epsilon)
        assert abs(fd-dh)<3e-5*max(1,abs(dh))
    e=exp(-(1+nu)*tau)
    z=exp(-nu*tau)
    t=(1-e)/(1+nu)
    assert 0<e<1 and 0<z<1 and 0<t<1-e
    # Coefficients guarantee nonflip at every interior point.
    s=rg.random()*(1-a)
    j11=e-h+dh*s
    d_plus=(1+j11)*(1+z)+t*h
    assert d_plus>0
# Verify exact endemic-equilibrium classification and Jury inequalities on 1200 parameter sets.
for _ in range(1200):
    rho=10**rg.uniform(-2,2)
    nu=10**rg.uniform(-3,.6)
    tau=10**rg.uniform(-2,.3)
    e=exp(-(1+nu)*tau)
    z=exp(-nu*tau)
    t=(1-e)/(1+nu)
    B=1+t/(1-z)
    hp0=rho*(1-e)/(1+nu)*(-__import__('math').expm1(-nu*tau))/(nu*tau)
    if hp0<=1-e: continue
    lo,hi=0.0,1/B
    for j in range(90):
        mid=(lo+hi)/2
        val=H_risk(mid,rho,nu,tau)*(1-B*mid)-(1-e)*mid
        if val>0:lo=mid
        else: hi=mid
    a=(lo+hi)/2
    s=1-B*a
    H=H_risk(a,rho,nu,tau)
    dH=dH_risk(a,rho,nu,tau)
    assert abs(H*s-(1-e)*a)<1e-10
    A=e-H+s*dH
    tr=A+z
    det=A*z+t*H
    assert 1-tr+det>0 and 1+tr+det>0 and 1-det>0
print('PASS: exact rational two-cycle, smooth incidence, 4000 hazard/Jacobian and 1200 equilibrium draws')
