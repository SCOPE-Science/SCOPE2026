#!/usr/bin/env python3
"""Independent symbolic-algebra and numerical spot checks for a two-channel integrated-Wiener quadrature design.

This is supporting finite computation; the infinite-domain proof is in RESULT.md.
"""
import math
import sympy as s
import numpy as np
from scipy.optimize import minimize_scalar

z,P,t=s.symbols('z P t',positive=True)
K=s.Matrix([[z**3/s.Integer(3),z**2/2],[z**2/2,z]])
c=s.Matrix([z**2*(3-z)/6,z*(2-z)/2])
M=K+s.ones(2)/P
D=s.factor(M.det())
a,b=[s.factor(q) for q in M.inv()*c]
assert s.factor(a-(P*z**3-2*z**2+12*z-12)/(P*z**3+4*z**2-12*z+12))==0
assert s.factor(b-(-P*z**4+P*z**3+2*z**2-12*z+12)/(P*z**3+4*z**2-12*z+12))==0
V=s.factor((c.T*M.inv()*c)[0])
assert s.factor(V.subs(z,1)-(P+1)/(3*(P+4)))==0
u=s.factor(s.diff(V,z)*(P*z**3+4*z**2-12*z+12)**2)
A=z**6*(1-z)**2
L=2*z**3*(3*z**4-18*z**3+40*z**2-36*z+12)
C=4*(z**2-6*z+6)*(z**4-6*z**3+15*z**2-18*z+6)
assert s.simplify(u-(A*P**2+L*P+C))==0
H=s.Poly(s.cancel((1+t)**8*u.subs(z,t/(1+t))),t)
coeff=[144,576,816,24*(P+12),12*(4*P-41),32*(P-21),P**2+12*P-356,2*(3*P-44),2*(P-4)]
assert [s.expand(H.nth(j)-coeff[j]) for j in range(9)] == [0]*9
p0=(2*z*z-12*z+12)/z**3
w=s.symbols('w')
B=2*z**3*(z-2)*(5*z**3-24*z**2+30*z-12)
C0=4*(z-2)**2*(z**2-6*z+6)*(5*z**2-12*z+6)
assert s.expand(u.subs(P,p0+w)-(A*w*w+B*w+C0))==0
zc=(6-s.sqrt(6))/5
pc=s.simplify(p0.subs(z,zc))
assert s.simplify(u.subs({P:pc,z:zc}))==0
assert s.simplify(s.diff(u,z).subs({P:pc,z:zc}))==0
assert s.simplify(u.subs(z,1)-2*(P-4))==0
zp=(P-2+s.sqrt(P*P+8*P+4))/(3*P)
assert s.simplify((3*P*z**2-2*P*z+4*z-4).subs(z,zp))==0
assert s.simplify(((c[1]**2/(z+1/P))).subs(z,zp)-P*zp**2*(2-zp)**2/(4*(1+P*zp)))==0
assert s.simplify(a.subs(z,1)-(P-2)/(P+4))==0
assert s.simplify(b.subs(z,1)-2/(P+4))==0

from scipy.optimize import brentq
zf=s.lambdify(P,zp,'numpy')
def pure(Pv):
 zz=float(zf(Pv));return Pv*zz**2*(2-zz)**2/(4*(Pv*zz+1))
def end(Pv): return (Pv+1)/(3*(Pv+4))
star=brentq(lambda pp:pure(pp)-end(pp),8.5,9,xtol=1e-13)
assert 8.57<star<8.59
assert abs(float(pc)-12.5319726474218)<1e-10
print('threshold',format(star,'.15f'),'transition_site',format(float(zf(star)),'.15f'),'critical_P',float(pc))
# Direct Gaussian covariances and independent polynomial-kernel computations.
for zz in np.linspace(.1,1,21):
 cc=np.array([float(v.subs(z,zz)) for v in c]); KK=np.array(K.subs(z,zz),dtype=float)
 xx=np.linspace(0,1,10001)
 g=np.maximum(zz-xx,0);h=(xx<zz).astype(float);f=1-xx
 approx=np.trapezoid(np.vstack([f*g,f*h,g*g,g*h,h*h]),xx,axis=1)
 assert np.allclose(approx,np.array([cc[0],cc[1],KK[0,0],KK[0,1],KK[1,1]]),atol=6e-5,rtol=5e-5)

# Completely independent direct-conditioning scan over all time and precision choices.
for PP in [0.03,0.2,1,2,4,6,8,8.5,star,9,12,20,100]:
 envelope=max(pure(PP),end(PP) if PP>2 else -1)
 xs=np.linspace(.001,1,191)
 rs=np.linspace(0,1,53)
 for zz in xs:
  cc=np.array([float(v.subs(z,zz)) for v in c]); KK=np.array(K.subs(z,zz),dtype=float)
  for r in rs:
   pp=PP*r;qq=PP*(1-r)
   noise=np.diag([1/pp if pp>0 else 1e50,1/qq if qq>0 else 1e50])
   gain=float(cc@np.linalg.solve(KK+noise,cc))
   assert gain<=envelope+1e-10,(PP,zz,r,gain,envelope)
 # check optimal design from both branches:
 if PP<star:
  zz=float(zf(PP));cc=np.array([float(v.subs(z,zz)) for v in c]);KK=np.array(K.subs(z,zz),dtype=float)
  gg=cc[1]**2/(KK[1,1]+1/PP)
 else:
  zz=1.;cc=np.array([float(v.subs(z,zz)) for v in c]); KK=np.array(K.subs(z,zz),dtype=float)
  gg=float(cc@np.linalg.solve(KK+np.diag([1/(PP-2),1/2]),cc))
 assert abs(gg-envelope)<1e-10
print('PASS symbolic identities, covariance integrations, and',13*191*53,'supplementary comparisons')
