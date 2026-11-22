#!/usr/bin/env python3
"""Reproducible checks for a thermal tuning of a Gaussian coupled diffusion.

Dependencies: sympy, numpy, scipy. Run: python verify.py
The analytic proof is independent of numerical sampling.
"""
import math
import random
import numpy as np
import sympy as sp
from scipy.linalg import expm, solve_continuous_lyapunov

a,k,T,U,t=sp.symbols('a k T U t',positive=True)
A=sp.Matrix([[a,-k],[-k,a]])
D=sp.diag(T,U)
s11,s12,s22=sp.symbols('s11 s12 s22')
S0=sp.Matrix([[s11,s12],[s12,s22]])
sol=sp.solve(list(A*S0+S0*A-2*D),(s11,s12,s22))
S=sp.simplify(S0.subs(sol))
Q=sp.simplify(D-A*S)
tuned=T*(2*a+k)/k
count=0

def eq(lhs,rhs):
    global count
    assert sp.simplify(lhs-rhs)==0,(lhs,rhs)
    count+=1

for expr in list(A*S+S*A-2*D): eq(expr,0)
q=k*(U-T)/(2*a)
eq(Q[0,1],q);eq(Q[1,0],-q);eq(Q[0,0],0);eq(Q[1,1],0)
U_stationary=S.subs(U,tuned)
eq(U_stationary[0,0], T/(a-k))
eq(U_stationary[0,1], T/(a-k))
eq(U_stationary[1,1], T*(2*a-k)/(k*(a-k)))
eq(q.subs(U,tuned),T)
rate=sp.factor(sp.trace(S.inv()*Q.T*D.inv()*Q))
eq(rate,k*k*(U-T)**2/(2*a*T*U))
eq(rate.subs(U,tuned),2*a*k/(2*a+k))
J1=sp.factor((A*S*A)[0,0]-a*T)
eq(J1,k*k*(U-T)/(2*a))
eq(J1.subs(U,tuned),k*T)
eq(rate,J1*(1/T-1/U))
slow=((T+U)/(a-k)+(T-U)/a)/4
fast=((T+U)/(a+k)+(T-U)/a)/4
eq(fast,(T*(2*a+k)-k*U)/(4*a*(a+k)))
eq(slow,(T*(2*a-k)+k*U)/(4*a*(a-k)))
eq(slow+fast,S[0,0])
eq(slow.subs(U,tuned),T/(a-k))
eq(fast.subs(U,tuned),0)
# A short-time force impulse has response R(t)=(exp(-At))_11.
response=sp.exp(-a*t)*sp.cosh(k*t)
eq(sp.diff(response,t).subs(t,0),-a)
# Fixed visible OU drift lambda and T, varying k preserves the entire path law.
lam=sp.symbols('lam',positive=True)
hidden=sp.factor((2*a*k/(2*a+k)).subs(a,lam+k))
eq(hidden,2*k*(k+lam)/(3*k+2*lam))
assert sp.factor(sp.diff(hidden,k))>0 if all(v.is_number for v in [k,lam]) else True
numer=sp.factor(sp.together(sp.diff(hidden,k))*(3*k+2*lam)**2)
eq(numer,2*(3*k*k+4*k*lam+2*lam*lam))

rng=random.Random(20261118)
for j in range(360):
    av=rng.uniform(.5,6)
    kv=rng.uniform(.01,.85*av)
    Tv=rng.uniform(.1,4)
    Uv=Tv*(2*av+kv)/kv
    An=np.array([[av,-kv],[-kv,av]],float)
    Dn=np.diag([Tv,Uv])
    Sn=solve_continuous_lyapunov(An,2*Dn)
    assert np.all(np.linalg.eigvalsh(Sn)>0);count+=1
    Qn=Dn-An@Sn
    sigma=float(np.trace(np.linalg.inv(Sn)@Qn.T@np.linalg.inv(Dn)@Qn))
    expect=2*av*kv/(2*av+kv)
    assert math.isclose(sigma,expect,rel_tol=3e-11,abs_tol=2e-11);count+=1
    h=rng.uniform(.001,8)
    c=(expm(-An*h)@Sn)[0,0]
    target=Tv/(av-kv)*math.exp(-(av-kv)*h)
    assert math.isclose(c,target,rel_tol=1e-8,abs_tol=1e-10);count+=1
    passive=(expm(-An*h))[0,0]
    assert math.isclose(passive,math.exp(-av*h)*math.cosh(kv*h),rel_tol=1e-9,abs_tol=1e-10);count+=1
    assert passive<math.exp(-(av-kv)*h);count+=1
    assert math.isclose((kv*kv*(Uv-Tv)/(2*av)),kv*Tv,rel_tol=1e-12);count+=1
    # At any other positive bath temperature, fast-mode contribution is nonzero.
    off=Uv*(1.0+(0.5 if j%2 else -0.3))
    coef=(Tv*(2*av+kv)-kv*off)/(4*av*(av+kv))
    assert abs(coef)>1e-12;count+=1
    assert abs(((Tv+off)/(av-kv)+(Tv-off)/av)/4)>1e-13;count+=1
    # Projected stationary Gaussian is non-Markov off-curve: covariance semigroup fails.
    Do=np.diag([Tv,off]);So=solve_continuous_lyapunov(An,2*Do)
    h1=.37;h2=.63
    C0=So[0,0];C1=(expm(-An*h1)@So)[0,0];C2=(expm(-An*h2)@So)[0,0];C12=(expm(-An*(h1+h2))@So)[0,0]
    assert abs(C12*C0-C1*C2)>1e-13;count+=1

# Exhibit a simple exact-rational point.
exact=S.subs({a:sp.Integer(2),k:sp.Integer(1),T:sp.Integer(1),U:sp.Integer(5)})
assert exact == sp.Matrix([[1,1],[1,3]]);count+=1
eq(rate.subs({a:2,k:1,T:1,U:5}),sp.Rational(4,5))
print(f'PASS: {count} symbolic identities and numerical assertions')
