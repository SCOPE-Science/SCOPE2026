#!/usr/bin/env python3
"""Reproducibility diagnostics for exact physical-time radial asymptotics."""
import mpmath as mp
import sympy as sp
mp.mp.dps = 45
x, y, a, b = sp.symbols('x y a b', real=True)
R = x*x+y*y
fx = -a*R*x + b*(x*x-y*y)*x-R*y
fy = -a*R*y + b*(x*x-y*y)*y+R*x
assert sp.expand(x*fx+y*fy+a*R*R-b*(x*x-y*y)*R)==0
assert sp.expand(x*fy-y*fx-R*R)==0

def G(theta,a,b):
    return mp.quad(lambda u: mp.exp(-2*a*u-b*mp.sin(2*(theta-u))),[0,mp.pi])/(1-mp.exp(-2*a*mp.pi))
def I(theta,a,b):
    return mp.exp(2*a*theta)*G(theta,a,b)
def F(theta,a,b):
    return mp.exp(b*mp.sin(2*theta))*G(theta,a,b)

checks=2
for aa,bb in [(mp.mpf('1'),mp.mpf('5')),(mp.mpf('0.7'),mp.mpf('-2.3')),(mp.mpf('2'),mp.mpf('0'))]:
    for theta in [mp.mpf('0.2'),mp.mpf('1.15'),mp.mpf('2.8')]:
        assert mp.almosteq(F(theta+mp.pi,aa,bb),F(theta,aa,bb),rel_eps=mp.mpf('1e-35'))
        assert mp.almosteq(I(theta+mp.pi,aa,bb)/I(theta,aa,bb),mp.exp(2*aa*mp.pi),rel_eps=mp.mpf('1e-35'))
        checks+=2
    theta0=mp.mpf('0.3'); r0=mp.mpf('0.8')
    C=r0*r0*mp.exp(-bb*mp.sin(2*theta0)+2*aa*theta0)
    I0=I(theta0,aa,bb)
    for k in [1,2,4,7]:
        theta=theta0+k
        t=(I(theta,aa,bb)-I0)/C
        rsq=C*mp.exp(-2*aa*theta+bb*mp.sin(2*theta))
        assert t>0 and rsq>0
        assert mp.almosteq(t*rsq,(1-I0/I(theta,aa,bb))*F(theta,aa,bb),rel_eps=mp.mpf('1e-35'))
        checks+=1
assert abs(F(mp.mpf('0'),1,5)-F(mp.pi/4,1,5))>mp.mpf('0.01')
checks+=1
for aa in [mp.mpf('0.4'),mp.mpf('3')]:
    assert mp.almosteq(F(mp.mpf('1.7'),aa,0),1/(2*aa),rel_eps=mp.mpf('1e-35'))
    checks+=1
print('CHECK_OK: polynomial polar identities, I/F periodicity, physical-time trajectory identity, b=0 and nonconstant b=5 profile; checks=',checks)
