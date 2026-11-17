#!/usr/bin/env python3
"""Reproducible supplementary finite-dimensional checks for the stated planar model.
The analytic proof, not finite calculations, establishes the universal claims.
Requires numpy, scipy, mpmath; pure Python standard-library checks are used where possible.
"""
import math
from itertools import product
import numpy as np
from scipy.linalg import expm
from mpmath import mp

COUNT = 0

def close(x,y,rtol=5e-10,atol=1e-12):
    global COUNT
    assert np.isclose(x,y,rtol=rtol,atol=atol), (x,y)
    COUNT += 1

def base(a,b,k,t):
    B=np.array([[-a,k],[0.,-b]])
    Q=-(B+B.T)
    C=expm(t*B)
    assert np.linalg.eigvalsh(Q)[0]>0
    assert np.linalg.svd(C,compute_uv=False)[0]<1
    r= t*math.exp(-a*t) if abs(a-b)<1e-13 else (math.exp(-a*t)-math.exp(-b*t))/(b-a)
    return C,r

def sym_sector(C,n):
    if n==0: return np.ones((1,1))
    # Normalized symmetrized bitstring vectors span Sym^n(C^2).
    N=2**n
    S=np.zeros((N,n+1))
    for bitstr in product((0,1),repeat=n):
        ones=sum(bitstr); i=sum(bit << (n-1-j) for j,bit in enumerate(bitstr))
        S[i,ones]=1./math.sqrt(math.comb(n,ones))
    T=C.copy()
    for _ in range(1,n): T=np.kron(T,C)
    return S.T@T@S

for a,b in [(1.,1.),(.7,2.8),(3.,.9),(2.,2.01)]:
 for frac in [0.,.25,.7,.999]:
  k=frac*2*math.sqrt(a*b)
  for t in [.05,.3,1.5]:
   C,r=base(a,b,k,t)
   u=math.exp(-a*t);v=math.exp(-b*t)
   close(C[0,0],u);close(C[1,1],v);close(C[0,1],k*r)
   s1,s2=np.linalg.svd(C,compute_uv=False)
   F=u*u+v*v+(k*r)**2
   close(s1*s1+s2*s2,F)
   close(s1*s2,u*v)
   D=(1-u*u)*(1-v*v)-(k*r)**2
   close(D,np.linalg.det(np.eye(2)-C@C.T),atol=1e-15)
   for p in [.5,1.,2.,3.]:
    val=math.exp(-p*(a+b)*t)/((1-s1**p)*(1-s2**p))
    if p==2:
     close(val,math.exp(-2*(a+b)*t)/D)
    assert val>0
   if t==.3:
    for n in range(6):
     S=sym_sector(C,n)
     actual=np.linalg.svd(S,compute_uv=False)
     expected=sorted([s1**j*s2**(n-j) for j in range(n+1)],reverse=True)
     for x,y in zip(actual,expected): close(x,y)

for a,b,t in [(.7,2.8,.2),(1.,1.,.4),(3.,.9,1.2)]:
 ks=np.linspace(0,2*math.sqrt(a*b)*.9999,61)
 for p in [.5,1.,2.,5.]:
  vals=[]
  for k in ks:
   C,_=base(a,b,k,t)
   sigma=np.linalg.svd(C,compute_uv=False)
   vals.append(math.exp(-p*(a+b)*t)/np.prod(1-sigma**p))
  for x,y in zip(vals,vals[1:]):
   assert y>x-1e-13
   COUNT+=1

# High precision check of the ellipticity-edge constant, avoiding cancellation.
mp.dps=85
for a,b in [(1,1),(mp.mpf('0.8'),mp.mpf('2.6'))]:
    for xi in ['0','1','7']:
        xi=mp.mpf(xi)
        predicted=1/(xi+a*b*(a+b)**2/3)
        for tstr in ['0.01','0.002']:
            t=mp.mpf(tstr)
            delta=xi*t*t if xi else t**6
            k=mp.sqrt(4*a*b-delta)
            u=mp.exp(-a*t);v=mp.exp(-b*t)
            r=mp.exp(-a*t)*t if a==b else (u-v)/(b-a)
            D=-mp.expm1(-2*a*t)*-mp.expm1(-2*b*t)-(k*r)**2
            value=t**4*mp.exp(-2*(a+b)*t)/D
            assert mp.fabs(value/predicted-1)<mp.mpf('.09'), (a,b,xi,t,value,predicted)
            COUNT+=1

print('PLANAR_INVERSE_OU_DIAGNOSTICS_OK',COUNT)
