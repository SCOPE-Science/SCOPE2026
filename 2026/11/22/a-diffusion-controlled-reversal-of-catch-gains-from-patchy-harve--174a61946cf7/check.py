#!/usr/bin/env python3
"""Reproduce spectral perturbation identities and independent stationary checks."""
from fractions import Fraction as F
import sympy as s
import numpy as np
from scipy.fft import dct,idct
from scipy.optimize import root
D=s.symbols('D', positive=True)
a,b,m,eta,u0=s.Integer(4),s.Integer(1),s.Rational(1,2),s.Integer(1),s.Rational(3,2)
h=m+eta*u0
q=a/h-b
r=b*h/a
c=h*(1-r)
assert (h,q,r,c)==(2,1,s.Rational(1,2),1)
A=c+D
# For the unnormalized perturbation v=cos(x), mean v^2=1/2.
stock=s.factor((eta**2*q/c)*(1/A-r*c/A**2)/2)
catch=s.factor(eta**2*q/(2*A)*((b*h**2/a-m)/c-(h-m)*r/A))
assert s.simplify(stock-(2*D+1)/(4*(1+D)**2))==0
assert s.simplify(catch-(2*D-1)/(8*(1+D)**2))==0
Dstar=s.factor(h*m*(1-r)**2/(b*h**2/a-m))
assert Dstar==s.Rational(1,2)
assert s.simplify(catch.subs(D,Dstar))==0
# The core quadratic identities in arbitrary physical parameters.
H,M,R,C,Z=s.symbols('H M R C Z', positive=True)
# Eliminate the steady-budget relation H=C/(1-R) from the general catch bracket.
assert s.simplify((((H-M)/C)*(1-R*C/Z)-1 - ((H*R-M)/C-(H-M)*R/Z)).subs(C,H*(1-R)))==0
# The unique spectral zero of the catch multiplier has the announced form.
K=(H*R-M)/C
H1=(H-M)*R
lam=s.symbols('lam', positive=True)
T=s.symbols('T', positive=True)
Astar=s.simplify(H1/K)
assert s.simplify(((Astar-C)/lam - M*(1-R)*C/(lam*(H*R-M))).subs(C,H*(1-R)))==0
# Direct finite collocation check of the full nonlinear stationary equation.
N=80
x=np.pi*(np.arange(N)+0.5)/N
v=np.cos(x)
weights=np.arange(N,dtype=float)**2

def solve(d,eps):
    def residual(B):
        return -d*idct(weights*dct(B,norm='ortho'),norm='ortho')+4*B/(1+B)-(2+eps*v)*B
    rr=root(residual,np.ones(N),tol=1e-10)
    err=np.max(np.abs(residual(rr.x)))
    assert err<1e-8, ('residual',d,eps,err)
    assert np.min(rr.x)>0
    return np.mean(rr.x),np.mean((1.5+eps*v)*rr.x)

for d in (0.25,1.0):
    eps=.01
    bp,yp=solve(d,+eps)
    bm,ym=solve(d,-eps)
    observed_b=(bp+bm-2)/(2*eps**2)
    observed_y=(yp+ym-3)/(2*eps**2)
    expected_b=(2*d+1)/(4*(1+d)**2)
    expected_y=(2*d-1)/(8*(1+d)**2)
    assert abs(observed_b-expected_b)<1e-4,(d,observed_b,expected_b)
    assert abs(observed_y-expected_y)<1e-4,(d,observed_y,expected_y)
    assert observed_b>0
    assert observed_y*(2*d-1)>0
    print(f'D={d}: B2={observed_b:.10f}, Y2={observed_y:.10f}; expected ({expected_b:.10f},{expected_y:.10f})')
print('PASS: exact algebra, sharp threshold, independent nonlinear stationary consistency')
