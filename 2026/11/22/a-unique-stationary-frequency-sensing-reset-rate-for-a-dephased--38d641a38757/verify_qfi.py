"""Exact and independent numerical checks for stationary phase sensing with resets.

Dependencies: Python >= 3.10, sympy, numpy, scipy.
Run: python verify_qfi.py

This is an auxiliary checker; analytic arguments establish global assertions.
"""
import math
import sympy as S
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

u,t,r,g,w=S.symbols('u t r g w', real=True)
Q=(r+g)**2+w**2
sx=r*(r+g)/Q
sy=r*w/Q
bloch=S.simplify(sx**2+sy**2)
FB=S.factor(S.diff(sx,w)**2+S.diff(sy,w)**2 +
            (sx*S.diff(sx,w)+sy*S.diff(sy,w))**2/(1-bloch))
claimed=(r*r*(g*g+g*r+w*w)*(g*g+3*g*r+2*r*r+w*w)/
         ((g*g+2*g*r+w*w)*Q**3))
assert S.cancel(FB-claimed)==0
f=u*u*(1+u+t)*(1+3*u+2*u*u+t)/((1+2*u+t)*((u+1)**2+t)**3)
P=(1+t)**4+(6+18*t+18*t*t+6*t**3)*u+(
    12+26*t+16*t*t+2*t**3)*u**2+(6+8*t+2*t*t)*u**3-(
    9+11*t+2*t*t)*u**4-(12+7*t)*u**5-4*u**6
pred=2*u*P/((1+2*u+t)**2*((1+u)**2+t)**4)
assert S.cancel(S.diff(f,u)-pred)==0
assert S.expand(P.subs(t,0)+(u-1)*(u+1)**3*(2*u+1)**2)==0
assert S.expand(P.subs(t,u*u-1)-u**5*(u-1)*(u+1)**2)==0
assert S.diff(P,t).subs({u:1,t:0})==38
assert S.diff(P,u).subs({u:1,t:0})==-72
c2=(1+S.sqrt(3))/2
assert S.simplify(c2*(2*c2+1)/(1+c2)**3-2*S.sqrt(3)/9)==0

# Independent stationary-state calculation through the reset-age integral,
# and independent symmetric logarithmic derivative (a matrix linear solve).
paulis=[np.array([[0,1],[1,0]],complex),
        np.array([[0,-1j],[1j,0]],complex)]
I=np.eye(2,dtype=complex)

def stationary_integral(rr,gg,ww):
    ex=quad(lambda a:rr*math.exp(-(rr+gg)*a)*math.cos(ww*a),
            0,np.inf,epsabs=2e-12,epsrel=2e-12)[0]
    ey=quad(lambda a:rr*math.exp(-(rr+gg)*a)*math.sin(ww*a),
            0,np.inf,epsabs=2e-12,epsrel=2e-12)[0]
    return (I+ex*paulis[0]+ey*paulis[1])/2

def qfi_sld(rr,gg,ww):
    h=1e-5*max(1.0,abs(ww))
    rho=stationary_integral(rr,gg,ww)
    drho=(stationary_integral(rr,gg,ww+h)-
          stationary_integral(rr,gg,ww-h))/(2*h)
    M=np.kron(I,rho)+np.kron(rho.T,I)
    Lop=np.linalg.solve(M,(2*drho).flatten(order='F')).reshape((2,2),order='F')
    return np.trace(rho@Lop@Lop).real

def closed(rr,gg,ww):
    return float(claimed.subs({r:rr,g:gg,w:ww}))

ct=0
for gg in [0.4,1.0,2.3]:
    for ww in [-3.0,-0.8,0.0,0.6,4.4]:
        for rr in [0.2,1.0,3.2]:
            val=qfi_sld(rr,gg,ww)
            rhs=closed(rr,gg,ww)
            assert abs(val-rhs)<1e-8*max(1,rhs),(gg,ww,rr,val,rhs)
            ct+=1

pf=S.lambdify((u,t),P,'numpy')
ff=S.lambdify((u,t),f,'numpy')
for v in [0.0,0.05,0.3,1,2,5,10,100]:
    v2=v*v
    root=brentq(lambda z:pf(z,v2),1e-8,1000*max(1,v))
    assert root>=math.sqrt(1+v*v)-1e-10
    if v>0: assert root>math.sqrt(1+v*v)
    assert pf(root*.98,v2)>0 and pf(root*1.02,v2)<0
    assert ff(root,v2)>ff(root*.98,v2)
    assert ff(root,v2)>ff(root*1.02,v2)
    print('omega/gamma=',v,'r_star/gamma=',root,'gamma^2 F_star=',ff(root,v2))
print('PASS: exact identities; %d independent quadrature/SLD QFI checks; 8 optimum crosschecks.'%ct)
