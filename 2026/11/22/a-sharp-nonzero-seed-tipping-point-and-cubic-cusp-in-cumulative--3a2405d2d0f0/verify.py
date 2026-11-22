#!/usr/bin/env python3
"""Independent numerical and exact-arithmetic checks of a positive-seed contagion theorem."""
from __future__ import annotations
import math
from fractions import Fraction
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


def H(z, B, A):
    return (1-z)*math.exp(B*z + A*z*z/2)


def q(z, B, A):
    return B-1 + (A-B)*z - A*z*z


def final_root(eps, B, A):
    # The *first* zero is required: brentq on [0,1] alone is not sufficient.
    a_star = (1+math.sqrt(1-B))**2
    if A > a_star:
        disc=(A+B)**2-4*A
        u=(A-B-math.sqrt(disc))/(2*A)
        if H(u,B,A)<=1-eps:
            return brentq(lambda z:H(z,B,A)-(1-eps),0,u,xtol=1e-14)
        v=(A-B+math.sqrt(disc))/(2*A)
        return brentq(lambda z:H(z,B,A)-(1-eps),v,1,xtol=1e-14)
    return brentq(lambda z:H(z,B,A)-(1-eps),0,1,xtol=1e-14)


def verify():
    Bq=Fraction(1,2); Aq=Fraction(3)
    assert q(Fraction(1,3),Bq,Aq)==0
    assert q(Fraction(1,2),Bq,Aq)==0
    assert (Aq+Bq)**2-4*Aq==Fraction(1,4)
    # Exact rational verification of the double cusp root.
    Bc=Fraction(3,4); Ac=Fraction(9,4); zc=Fraction(1,3)
    assert q(zc,Bc,Ac)==0
    assert Ac-Bc-2*Ac*zc==0
    for zz in (0.1,0.25,0.4,0.6,0.8):
        h=1e-6
        num=(H(zz+h,.5,3)-H(zz-h,.5,3))/(2*h)
        target=H(zz,.5,3)*q(zz,.5,3)/(1-zz)
        assert abs(num-target)<1e-8
    B=.5; A=3.; u=1/3; v=.5
    epsc=1-H(u,B,A)
    w=brentq(lambda z:H(z,B,A)-H(u,B,A),v+1e-9,.999999)
    assert 0<epsc<1 and u<v<w<1
    assert abs(epsc-(1-2/3*math.exp(1/3)))<1e-14
    assert abs(epsc-0.06959171660927355)<1e-12
    assert abs(w-0.574237376735705)<1e-11
    assert H(v,B,A)>H(u,B,A)
    for eta in (1e-3,1e-4,1e-5):
        lo=final_root(epsc-eta,B,A)
        hi=final_root(epsc+eta,B,A)
        assert lo<u and hi>w and abs(lo-u)<0.12 and abs(hi-w)<0.12
    # Check actual dynamical trajectories against analytic first roots.
    mu=1.7; beta=B*mu; alpha=A*mu
    def ode(t,y):
        S,I,R=y
        inf=(beta+alpha*R)*S*I
        return [-inf,inf-mu*I,mu*I]
    for eps in (.025,.11):
        sol=solve_ivp(ode,(0,400),[1-eps,eps,0],rtol=2e-11,atol=2e-12,method='DOP853')
        assert sol.success
        assert abs(sol.y[2,-1]-final_root(eps,B,A))<2e-9
        assert abs(sol.y[1,-1])<1e-9
        assert abs(sum(sol.y[:,-1])-1)<1e-9
    # Cusp: both sides are governed by the *signed* real cube root.
    s=.5; B=1-s*s; A=(1+s)**2
    zstar=s/(1+s)
    estar=1-math.exp(s-s*s/2)/(1+s)
    coeff=(3/((1+s)**2*math.exp(s-s*s/2)))**(1/3)
    assert abs(estar-.030005723587865685)<1e-12
    for delta in (-1e-7,1e-7,-1e-8,1e-8):
        z=final_root(estar+delta,B,A)
        expected=zstar+coeff*math.copysign(abs(delta)**(1/3),delta)
        assert abs((z-zstar)/(expected-zstar)-1)<.015
    print('PASS exact discriminants, fold/cusp roots, phase jump, signed cube root, and independent ODE integration')

if __name__=='__main__':
    verify()
