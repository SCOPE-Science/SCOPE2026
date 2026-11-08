#!/usr/bin/env python3
"""Exact rational consistency checks for Brownian-kernel integral sampling."""
import sympy as s
u,v,w=s.symbols('u v w', real=True)
x=(1+v-u)**3
y=(1+w-v)**3
av=s.integrate(x,(u,0,1),(v,0,1))
assert av==s.Rational(3,2)
ex2=s.integrate(x**2,(u,0,1),(v,0,1))
exy=s.integrate(x*y,(u,0,1),(v,0,1),(w,0,1))
assert ex2==s.Rational(127,28)
assert exy==s.Rational(449,336)
var=ex2-av**2;cov=exy-av**2
assert var==s.Rational(16,7)
assert cov==-s.Rational(307,336)
assert var+2*cov==s.Rational(11,24)
assert (var+2*cov)/144==s.Rational(11,3456)
assert s.integrate(u**3,(u,0,1))==s.Rational(1,4)
for n in range(1,8):
    z=s.symbols('z', real=True)
    t=[s.Rational(2*i,2*n+1) for i in range(1,n+1)]
    gaps=[t[0]]+[t[i]-t[i-1] for i in range(1,n)]+[1-t[-1]]
    gapvar=sum(g**3 for g in gaps[:-1])/12+gaps[-1]**3/3
    assert gapvar==s.Rational(1,3*(2*n+1)**2)
    assert all(s.Rational(i-1,n)<t[i-1]<s.Rational(i,n) for i in range(1,n+1))
    K=s.Matrix([[min(a,b) for b in t] for a in t])
    c=s.Matrix([a-a*a/2 for a in t]); posterior=s.Rational(1,3)-(c.T*K.inv()*c)[0]
    assert posterior==gapvar
    mean=s.Rational(6*n-1,48*n**3)
    assert mean>=gapvar
    assert s.factor(mean/gapvar)==s.Rational((6*n-1)*(2*n+1)**2,16*n**3)
# Nonoptimal rational observation point verifies bridge-covariance identity.
for t in [(s.Rational(1,5),s.Rational(4,7)),(s.Rational(1,10),s.Rational(3,8),s.Rational(6,7))]:
    K=s.Matrix([[min(a,b) for b in t] for a in t]); c=s.Matrix([a-a*a/2 for a in t]);
    posterior=s.Rational(1,3)-(c.T*K.inv()*c)[0]
    gaps=[t[0]]+[t[i]-t[i-1] for i in range(1,len(t))]+[1-t[-1]]
    assert posterior==sum(g**3 for g in gaps[:-1])/12+gaps[-1]**3/3
print('PASS: uniform moments, long-run variance, optimal grids, exact covariance identities')
