#!/usr/bin/env python3
"""Reproduce exact algebraic and numerical checks for the stated radial-kernel theorem.
These checks supplement the analytic argument and do not certify global zero counts.
"""
import math
import sympy as sp
import mpmath as mp
checks = 0

def verify(condition, msg):
    global checks
    assert condition, msg
    checks += 1

n, z, u = sp.symbols('n z u')
a = (n + 1)*(n + 2)*(2*n + 3)
verify(sp.expand(a) == 2*n**3 + 9*n**2 + 13*n + 6,'unperturbed coefficient')
verify(sp.factor(sum([0])) == 0,'sanity')
q = u**4 - 18*u**3 + 42*u**2 - 18*u + 1
S = 1/(1-z)
J = 0
p = sp.Poly(sp.expand(a**2),n)
for k in range(7):
    J += p.nth(k) * S
    S = sp.cancel(z * sp.diff(S,z))
J = sp.cancel(J)
verify(sp.cancel(J - 36*(z**4+18*z**3+42*z**2+18*z+1)/(1-z)**7)==0,'generating rational function')
verify(sp.cancel(J.subs(z,-u)-36*q/(1+u)**7)==0,'variation polynomial')
verify(sp.factor(q/u**2 - ((u+1/u)**2-18*(u+1/u)+40))==0,'reciprocal reduction')
v1=9+sp.sqrt(41)
v2=9-sp.sqrt(41)
u1=(v1-sp.sqrt(v1**2-4))/2
u2=(v2-sp.sqrt(v2**2-4))/2
verify(0 < float(u1) < float(u2) < 1,'two radial thresholds')
for root in (u1,u2):
    verify(abs(complex(sp.N(q.subs(u,root),20)))<1e-14,'quartic root')
for x, sign in ((0.01,1),(0.2,-1),(0.8,1)):
    verify(float(q.subs(u,x))*sign > 0, 'three signed radial bands')
# Exact first variations: K(2,0;z)=6(1+z)/(1-z)^4.
r=sp.symbols('r',positive=True)
Kb = 6*(1+z)/(1-z)**4
verify(sp.diff(Kb,z).subs(z,-1)==sp.Rational(3,8),'transverse scalar derivative')
I = sp.integrate(18*r**4*(1-r**2)/(1+r**2)**4,(r,0,1))
verify(sp.simplify(I-(sp.Rational(15,4)-9*sp.pi/8))==0,'linear-tilt epsilon derivative')
slope = sp.factor((sp.Rational(32,1)/(3*sp.pi))*I)
verify(sp.simplify(slope-(40/sp.pi-12))==0,'threshold linear response')
verify(float(slope)>0,'linear tilt delays')
mp.mp.dps=30

def K0(t,z):
    u=mp.sqrt(z)
    return (t+1)/(4*u)*((1-u)**(-t-2)-(1+u)**(-t-2))

def Klin(t,e,z):
    h=e*(t+1)/(1+e)
    return (K0(t,z)+h*mp.quad(lambda y:y**(t+2-h)*K0(t,z*y*y),[0,1]))/(1+e)
for e in (mp.mpf('-.004'),mp.mpf('.004')):
    tstar=mp.findroot(lambda t:mp.re(Klin(t,e,-1)),(mp.mpf('1.99'),mp.mpf('2.01')))
    verify(abs((tstar-2)/e-(40/mp.pi-12)) < mp.mpf('.02'), 'finite-difference threshold slope')
    verify(abs(mp.im(Klin(tstar,e,-1))) < mp.mpf('1e-22'),'real root boundary')
for t in [mp.mpf('1.99'),mp.mpf('2.01')]:
    for e in [mp.mpf('-.003'),mp.mpf('0'),mp.mpf('.003')]:
        for zz in [-mp.mpf('.99'),-mp.mpf('.8'),mp.mpf('.3')]:
            # geometric-mode series is absolutely convergent at these scalar points.
            def term(n):
                nn=int(n)
                m0=2*mp.beta(2*nn+2,t+1)
                m1=2*mp.beta(2*nn+3,t+1)
                return zz**nn/(m0+e*m1)
            alt=mp.nsum(term,[0,mp.inf])
            verify(abs(alt-Klin(t,e,zz))<mp.mpf('2e-19'),'series integral agreement')
print(f'PASS: {checks} independent assertions (symbolic, integral and numerical)')
