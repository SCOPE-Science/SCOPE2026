#!/usr/bin/env python3
"""Reproducible algebra and numerical diagnostics for the alternating-edge SIS theorem.
Requires Python 3, SymPy, NumPy, SciPy; no external files.
"""
import numpy as np
import sympy as sp
from scipy.linalg import expm
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from numpy.polynomial.legendre import leggauss

# Exact characteristic polynomial of the undamped two-contact monodromy.
c,s=sp.symbols('c s', real=True);z=sp.symbols('z')
H=sp.Matrix([[c,s,0],[c*s,c*c,s],[s*s,c*s,c]])
cp=sp.factor(sp.Poly(H.charpoly(z).as_expr(),s).rem(sp.Poly(s*s-c*c+1,s)).as_expr())
assert sp.simplify(cp-(z-1)*(z*z-(c*c+2*c-1)*z+1))==0
assert sp.factor(sp.Poly(H.det(),s).rem(sp.Poly(s*s-c*c+1,s)).as_expr()) == 1
# Scalar derivative identity for f(x) = arccosh((1+cosh(x))/2).
x=sp.symbols('x',positive=True)
fprime=sp.sqrt((sp.cosh(x)+1)/(sp.cosh(x)+3))
assert sp.simplify(sp.diff(fprime,x)-sp.sinh(x)/(sp.sqrt(sp.cosh(x)+1)*(sp.cosh(x)+3)**sp.Rational(3,2)))==0

beta=1.0; gamma=0.8
A1=np.array([[0.,1.,0.],[1.,0.,0.],[0.,0.,0.]])
A2=np.array([[0.,0.,0.],[0.,0.,1.],[0.,1.,0.]])
f=lambda x: np.arccosh((1+np.cosh(x))/2)
h=brentq(lambda h: f(h)/h-gamma,0.01,15.,xtol=1e-13)
T=2*h
L1=-gamma*np.eye(3)+beta*A1
L2=-gamma*np.eye(3)+beta*A2
P=expm(L2*h)@expm(L1*h)
eig,V=np.linalg.eig(P)
i=np.argmax(eig.real)
assert abs(eig[i].imag)<1e-12 and abs(eig[i].real-1)<1e-12
v=V[:,i].real
if v.sum()<0:v=-v
v/=v.sum()
eigw,W=np.linalg.eig(P.T)
j=np.argmin(abs(eigw-1))
w=W[:,j].real
if w.sum()<0:w=-w
w/=(w@v)
assert np.all(v>0) and np.all(w>0)
assert abs(w@v-1)<1e-11
assert np.max(abs(P@v-v))<1e-11
assert np.max(abs(P.T@w-w))<1e-11

def U(t):
    if t<=h:return expm(L1*t)
    return expm(L2*(t-h))@expm(L1*h)

def q_integrand(t):
    z=U(t)@v
    A=A1 if t<h else A2
    # w(t)=Phi(T,t).T w = U(t).(-T) w, using monodromy invariance
    wt=np.linalg.solve(U(t).T,w)
    return beta*wt@(z*(A@z))

gp, gw=leggauss(96)
q=0.
for a,b in [(0.,h),(h,T)]:
    ts=(gp+1)*(b-a)/2+a
    q+=sum(wi*q_integrand(float(t)) for t,wi in zip(ts,gw))*(b-a)/2
assert q>0 and np.isfinite(q)
# Closed half-period reflection formula on the neutral surface.
r=np.exp(-gamma*h);c0=np.cosh(beta*h);s0=np.sinh(beta*h)
B=r*r*s0/(1-r*c0)
v0=np.array([r,B,1.]);v_exp=v0/v0.sum()
wbase=np.array([1.,s0/(c0-r),r])
w_exp=wbase/(wbase@v_exp)
assert np.max(abs(v-v_exp))<1e-10
assert np.max(abs(w-w_exp))<1e-10
assert np.max(abs(U(h)@v-np.array([v[2],v[1],v[0]])))<1e-10
D=beta-gamma; E=3*beta+gamma
Jplus=np.expm1(D*h)/D if abs(D)>1e-8 else h
Jminus=-np.expm1(-E*h)/E
Jcosh=(Jplus+Jminus)/2
Jsinh=(Jplus-Jminus)/2
q_closed=2*beta*(w[0]+w[1])*((v[0]**2+v[1]**2)*Jsinh/2+v[0]*v[1]*Jcosh)
assert abs(q-q_closed)<1e-9,(q,q_closed)

def flow(x0):
    cur=np.asarray(x0,dtype=float)
    for L,A in ((L1,A1),(L2,A2)):
        def rhs(t,x):return L@x-beta*x*(A@x)
        sol=solve_ivp(rhs,(0,h),cur,rtol=1e-10,atol=1e-12,method='DOP853')
        assert sol.success
        cur=sol.y[:,-1]
    return cur

p=np.array([.23,.47,.14])
for n in range(1,1501):
    p=flow(p)
assert np.all(p>0)
pred=v/q
observed=1501*p
rel=float(np.max(abs(observed/pred-1)))
assert rel<0.015, (rel,observed,pred)
assert abs((f(h)/h)-gamma)<1e-12
print('VERIFY_OK')
print('critical_half_period=',format(h,'.13f'))
print('period=',format(T,'.13f'))
print('P_eigs=',np.sort(eig.real)[::-1])
print('v=',v, 'w=',w)
print('quadratic_coefficient_q=',format(q,'.12f'))
print('closed_coefficient_q=',format(q_closed,'.12f'))
print('predicted_limit_n_times_x=',pred)
print('numerical_n_times_x=',observed)
print('relative_error=',rel)
