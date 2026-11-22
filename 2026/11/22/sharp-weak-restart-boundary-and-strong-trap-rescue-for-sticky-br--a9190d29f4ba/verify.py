#!/usr/bin/env python3
"""Reproducibility checks for a sticky-boundary Brownian first-passage theorem.
Usage: python3 verify.py (requires SymPy, SciPy, NumPy).
These finite tests supplement, rather than replace, the analytic argument.
"""
import math
import numpy as np
import sympy as sp
from scipy.linalg import solve_banded
from scipy.optimize import brentq

checks=0
def check(condition, label):
    global checks
    assert condition, label
    checks+=1

z, x, nu, q=sp.symbols('z x nu q', real=True, nonnegative=True)
H=lambda w: sp.cosh(q*w)+nu*q*sp.sinh(q*w)
M=(1-x*x)/2+nu*(1-x)
poly=5*x**3+(5+20*nu)*x**2+(24*nu**2+8*nu-1)*x-(1+4*nu)
# Exact backward-equation solution at an absorbing right endpoint, sticky left endpoint.
phi=H(x)/H(1)
check(sp.simplify(sp.diff(phi,x,2)-q*q*phi)==0,'interior resolvent')
check(sp.simplify(sp.diff(phi,x).subs(x,0)-nu*q*q*phi.subs(x,0))==0,'Wentzell resolvent')
check(sp.simplify(phi.subs(x,1)-1)==0,'absorption boundary')
# Independent first two moments from the backward generator and sticky boundary.
M1=M
M2p0=-2*nu*M1.subs(x,0)
t=sp.symbols('t', real=True)
M2gen=M2p0*x+sp.integrate((x-t)*(-2*M1.subs(x,t)),(t,0,x))
M2=sp.factor(M2gen-M2gen.subs(x,1))
check(sp.simplify(sp.diff(M2,x,2)+2*M1)==0,'second moment ODE')
check(sp.simplify(sp.diff(M2,x).subs(x,0)-nu*sp.diff(M2,x,2).subs(x,0))==0,'second moment sticky boundary')
check(sp.simplify(M2.subs(x,1))==0,'second moment absorbing boundary')
check(sp.factor(M1*M1-M2/2+(1-x)*poly/24)==0,'sharp coefficient from moments')

# Maclaurin expansion independently from the Laplace solution.
Q=lambda y: sp.cosh(q*y)+nu*q*sp.sinh(q*y)
Tseries=sp.series((Q(1)-Q(x))/(q*q*Q(x)),q,0,4).removeO().expand()
check(sp.simplify(Tseries.subs(q,0)-M1)==0,'mean from Laplace transform')
check(sp.factor(Tseries.coeff(q,2)+(1-x)*poly/24)==0,'weak-reset derivative')
check(sp.factor(poly.subs(nu,0)-(x+1)*(5*x*x-1))==0,'non-sticky threshold')
check(sp.simplify(poly.subs(x,1)-24*nu**2-24*nu-8)==0,'positive endpoint')

# Strict root uniqueness is exact by Descartes signs (+,+,possibly +/-,-).
# Prove monotone stickiness ordering using one positive root in nu for x below 1/sqrt5.
for a in [0,0.05,0.2,1,10,100]:
    f=lambda y: 5*y**3+(5+20*a)*y*y+(24*a*a+8*a-1)*y-(1+4*a)
    rt=brentq(f,0,1,xtol=2e-15)
    check(0<rt<=1/math.sqrt(5)+1e-12,'root location')
    check(abs(f(rt))<5e-8,'root residual')
    if a>0:
        check(rt<1/math.sqrt(5),'sticky threshold shifts')
    if a>=10:
        check(abs(a*rt-1/6)<0.002,'large stickiness root asymptotic')

# Numerically independent finite-volume sticky generator, not its analytic formula.
def finite_volume_phi(n,a,initial,s):
    h=1/n
    # unknown values at nodes i=0,...,n-1, absorbing node n is fixed to 1
    ab=np.zeros((3,n),float)
    rhs=np.zeros(n,float)
    ab[1,0]=s+1/(a*h)
    ab[0,1]=-1/(a*h)
    for i in range(1,n):
        ab[1,i]=s+2/h**2
        ab[2,i-1]=-1/h**2
        if i<n-1: ab[0,i+1]=-1/h**2
        else: rhs[i]=1/h**2
    # laplace hitting-time transform is solution (s-L)phi=0
    y=solve_banded((1,1),ab,rhs)
    j=round(initial*n)
    return float(y[j])

for a in [0.2,1.0,4.0]:
    for s in [0.1,0.7,4.0]:
        for u in [0.25,0.5,0.75]:
            target=(math.cosh(math.sqrt(s)*u)+a*math.sqrt(s)*math.sinh(math.sqrt(s)*u))/(math.cosh(math.sqrt(s))+a*math.sqrt(s)*math.sinh(math.sqrt(s)))
            e1=abs(finite_volume_phi(200,a,u,s)-target)
            e2=abs(finite_volume_phi(400,a,u,s)-target)
            check(e2<e1*0.75+1e-12,'sticky finite-volume convergence')
            check(e2<0.003,'sticky finite-volume consistency')

# Match numerical small-rate derivatives to exact moment formula.
for a in [0,.1,1,10]:
 for u in [.05,.2,.5,.8]:
    if a==0:
        def Hf(y,t):return math.cosh(math.sqrt(t)*y)
    else:
        def Hf(y,t):return math.cosh(math.sqrt(t)*y)+a*math.sqrt(t)*math.sinh(math.sqrt(t)*y)
    exact=-(1-u)*(5*u**3+(5+20*a)*u*u+(24*a*a+8*a-1)*u-1-4*a)/24
    mean=(1-u*u)/2+a*(1-u)
    zrate=1e-4/(1+a)**2
    raw=(Hf(1,zrate)/Hf(u,zrate)-1)/zrate
    check(abs((raw-mean)/zrate-exact)<2e-3,'finite-rate slope')

# Strong-stickiness limit at fixed positive reset rate, and non-commuting r->0 limit.
for u in [.15,.4,.8]:
 for t in [.2,1,4]:
    y=math.sqrt(t)
    target=(math.sinh(y)/math.sinh(u*y)-1)/t
    for a in [500,2000]:
        approx=((math.cosh(y)+a*y*math.sinh(y))/(math.cosh(u*y)+a*y*math.sinh(u*y))-1)/t
        check(abs(approx-target)<45/(a*u*u*(1+t*t)),'strong-stickiness limit')

print(f'PASS {checks} reproducibility checks; exact symbolic identities and separate finite-volume generator')
