#!/usr/bin/env python3
"""Reproduce finite and asymptotic consistency checks for a two-mode matched BB1 iteration."""
from fractions import Fraction
import math

R = math.sqrt(2.0)
THETA = math.acos(1.0/(2.0*R))

def b(phi):
    return math.cos(phi) - 3.0/math.sqrt(7.0)*math.sin(phi)

def u(phi, terms=115):
    return sum(R**(-m)*max(0.0, b(phi-m*THETA)) for m in range(2, terms+2))

def h(phi, terms=115):
    return min(u(phi, terms), u(phi+math.pi, terms))

def log_add(x,y):
    return max(x,y)+math.log1p(math.exp(-abs(x-y)))

def asymptotic_log_norm(n, L, ell, t):
    # The logarithms are safe even when the actual gradient underflows.
    lh = t/2.0
    ll = 0.0
    a0,a1=1,-1
    hist=[a0,a1]
    for j in range(2,n):
        hist.append(hist[-1]-2*hist[-2])
    for k in range(n):
        idx=0 if k<2 else k-1
        z=t*hist[idx]
        w=log_add(0.0,math.log(L/ell)+z)
        c=math.log((L-ell)/ell)-w
        lh+=c
        ll+=c+z
    return log_add(2*lh,2*ll)/2

def check_exact():
    count=0
    for L,ell in [(Fraction(9),Fraction(1)),(Fraction(13,3),Fraction(2,3)),(Fraction(5,2),Fraction(1,2))]:
        for h0,v0 in [(Fraction(2),Fraction(1)),(Fraction(1),Fraction(3)),(Fraction(5,3),Fraction(4,7))]:
            rh,rl=h0,v0
            eps0=(rh/rl)**2
            eps_history=[]
            for k in range(7):
                eps=(rh/rl)**2
                if k==0: alpha=(rh*rh+rl*rl)/(L*rh*rh+ell*rl*rl)
                else: alpha=(1+eps_history[k-1])/(L*eps_history[k-1]+ell)
                nh=(1-L*alpha)*rh
                nl=(1-ell*alpha)*rl
                eps_history.append(eps)
                if k==0: assert (nh/nl)**2 == 1/eps0
                elif k>=1: assert (nh/nl)**2 == eps/(eps_history[k-1]**2)
                # Exact factor identity (critical, not a floating simulation).
                base_eps=eps_history[0] if k<=1 else eps_history[k-1]
                assert nh == -(L-ell)/(L*base_eps+ell)*rh
                assert nl == (L-ell)*base_eps/(L*base_eps+ell)*rl
                rh,rl=nh,nl
                count+=4
    return count

def check_asymptotics():
    count=0
    assert abs((u(0.0)-u(math.pi)) + 0.5)<1e-13
    assert abs(h(-2*THETA)-2*h(0))<1e-12
    count+=2
    for t in [-1.0,-0.7,0.35,1.1]:
        for L,ell in [(9.0,1.0),(11.0,2.0),(3.0,1.0)]:
            for n in [34,38,42,46]:
                actual = -asymptotic_log_norm(n,L,ell,t)/(R**n)
                expected=abs(t)*h(n*THETA)
                assert abs(actual-expected)<0.001, (n,L,ell,t,actual,expected)
                count+=1
    return count

if __name__=='__main__':
    exact=check_exact(); approx=check_asymptotics()
    print('PASS exact-rational identities:',exact)
    print('PASS asymptotic / phase numeric checks:',approx)
    print('H(0) ~',format(h(0),'.14f'),'H(-2theta) ~',format(h(-2*THETA),'.14f'))
    print('The analytic proof is required for all infinite-time conclusions.')
