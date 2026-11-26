"""Reproduce the harmonic-resonance and exponential face-selection identities.

Requirements: Python 3, sympy, scipy, numpy. Run: python verification.py
All finite checks supplement, but do not replace, the algebraic proof.
"""
from fractions import Fraction as F
from math import exp, log
import random
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp


def G(n, q, p):
    r0, s0, t0, pp0, r1, s1, t1, pp1 = p
    return ((1-n)*(r0-t0) + n*(r1-t1))*q + ((1-n)*(s0-pp0)+n*(s1-pp1))*(1-q)


def rhs(t, v, theta, delta, payoffs):
    x, y, n1, n2, n12 = v
    th1, th2, th12 = theta
    return np.array([
        x*(1-x)*((1-delta)*G(n1,x,payoffs)+delta*G(n12,y,payoffs)),
        y*(1-y)*((1-delta)*G(n2,y,payoffs)+delta*G(n12,x,payoffs)),
        n1*(1-n1)*((1+th1)*x-1),
        n2*(1-n2)*((1+th2)*y-1),
        n12*(1-n12)*((1+th12)*(x+y)/2-1),
    ])


def coeff(theta):
    th1,th2,th12 = theta
    a=(1+th12)/(2*(1+th1))
    b=(1+th12)/(2*(1+th2))
    return a,b,a+b-1


def Q(v,theta):
    a,b,s=coeff(theta)
    n1,n2,n12 = v[2:]
    odds=lambda z:log(z/(1-z))
    return odds(n12)-a*odds(n1)-b*odds(n2)

# Independent symbolic computation, with no assumption on payoffs.
x,y,t1,t2,t12=sp.symbols('x y t1 t2 t12', real=True, positive=True)
a=(1+t12)/(2*(1+t1));b=(1+t12)/(2*(1+t2));sig=a+b-1
sym_deriv=sp.simplify((1+t12)*(x+y)/2-1-a*((1+t1)*x-1)-b*((1+t2)*y-1))
assert sp.simplify(sym_deriv-sig)==0
assert sp.factor(sig)==sp.factor((t12*(2+t1+t2)-(t1+t2+2*t1*t2))/(2*(1+t1)*(1+t2)))
res=(t1+t2+2*t1*t2)/(2+t1+t2)
assert sp.simplify(sig.subs(t12,res))==0
assert sp.simplify(1/(1+res)-(1/(1+t1)+1/(1+t2))/2)==0

# Exact-rational stress tests involving all five actual ODE components.
rng=random.Random(20241013)
for i in range(1800):
    th=tuple(F(rng.randrange(1,25),rng.randrange(1,15)) for _ in range(3))
    de=F(rng.randrange(1,19),20)
    p=(F(2),F(1),F(0),F(0),F(0),F(0),F(1),F(1))
    v=tuple(F(rng.randrange(1,50),50) for _ in range(5))
    rv=rhs(F(0),v,th,de,p)
    aa,bb,ss=coeff(th)
    direct=rv[4]/(v[4]*(1-v[4]))-aa*rv[2]/(v[2]*(1-v[2]))-bb*rv[3]/(v[3]*(1-v[3]))
    assert direct==ss, (i,direct,ss)

# The algebraic source-compliant interior-equilibrium witness on resonance.
pars=(F(1),F(3),F(5,3))
v=(F(1,2),F(1,4),F(1,2),F(1,2),F(1,2))
p=(F(1),F(1),F(0),F(0),F(0),F(0),F(1),F(1))
for delta in (F(1,10),F(1,3),F(1,2),F(9,10)):
    assert all(q==0 for q in rhs(F(0),v,pars,delta,p))
assert coeff(pars)[2]==0

# 2 off-resonance directions with distinct theta's, plus the resonant case.
examples=[((1.,3.,2.),0.37,[.41,.67,.24,.73,.36]),
          ((1.,3.,1.),0.68,[.7,.3,.47,.39,.64]),
          ((1.,3.,5./3.),0.23,[.31,.62,.21,.72,.46])]
for th,de,v0 in examples:
    sol=solve_ivp(lambda t,v:rhs(t,v,th,de,tuple(float(z) for z in p)),
        (0,10),v0,rtol=1e-11,atol=1e-13,dense_output=True, max_step=.025)
    assert sol.success
    aa,bb,ss=coeff(th)
    q0=Q(v0,th)
    for tt in np.linspace(0,10,101):
        v=sol.sol(tt)
        assert all(0<z<1 for z in v)
        assert abs(Q(v,th)-q0-ss*tt)<3e-9, (th,tt,Q(v,th)-q0-ss*tt)
        _,_,n1,n2,n12=v
        if ss>0:
            product=(1-n12)*n1**aa*n2**bb
            assert product <= exp(-q0-ss*tt)*(1+1e-10)
            assert min(1-n12,n1,n2) <= exp((-q0-ss*tt)/(1+aa+bb))*(1+1e-10)
        elif ss<0:
            product=n12*(1-n1)**aa*(1-n2)**bb
            assert product <= exp(q0+ss*tt)*(1+1e-10)
            assert min(n12,1-n1,1-n2) <= exp((q0+ss*tt)/(1+aa+bb))*(1+1e-10)
print('PASS: symbolic identities; 1,800 exact-rational full-system derivative checks;')
print('       four exact interior-equilibrium witnesses; 303 high-precision trajectory samples.')
