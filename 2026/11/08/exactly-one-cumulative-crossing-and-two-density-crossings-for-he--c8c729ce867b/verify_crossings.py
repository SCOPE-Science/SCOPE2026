#!/usr/bin/env python3
"""Reproduce the finite calculations in the two-crossing diffusivity result.

The universal assertion is proved analytically in RESULT.md; this script
checks finite identities, numerical roots, and representative distributions.
"""
import math
import numpy as np
import sympy as sp
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq
from scipy.special import erfc

u,z=sp.symbols('u z',positive=True)
f=sp.erfc(z/sp.sqrt(u))
expected1=z*sp.exp(-z*z/u)/(sp.sqrt(sp.pi)*u**sp.Rational(3,2))
expected2=z*(2*z*z-3*u)*sp.exp(-z*z/u)/(2*sp.sqrt(sp.pi)*u**sp.Rational(7,2))
assert sp.simplify(sp.diff(f,u)-expected1)==0
assert sp.simplify(sp.diff(f,u,2)-expected2)==0

checks=2
rng=np.random.default_rng(10402026)
examples=[]

def check(ds,ps,label):
 global checks
 ds=np.asarray(ds,dtype=float);ps=np.asarray(ps,dtype=float);ps=ps/ps.sum()
 mu=float(np.dot(ps,ds))
 assert len(ds)>=2 and ds.min()>0 and ds.max()>ds.min() and abs(ps.sum()-1)<1.e-12
 def K(s):
  return float(np.dot(ps,ds**(-0.5)*np.exp(s*(1/mu-1/ds)))-mu**(-0.5))
 def Kp(s):
  a=1/mu-1/ds
  return float(np.dot(ps,ds**(-0.5)*a*np.exp(s*a)))
 def Delta(s):
  return float(np.dot(ps,erfc(np.sqrt(s/ds)))-erfc(np.sqrt(s/mu)))
 assert K(0)>0 and Kp(0)<0
 smin=brentq(Kp,0,100,xtol=1e-11)
 assert K(smin)<-1e-10,(label,K(smin))
 s1=brentq(K,0,smin,xtol=1e-11)
 s2=brentq(K,smin,100,xtol=1e-11)
 sc=brentq(Delta,s1,s2,xtol=1e-11)
 assert 0<s1<sc<s2
 assert 1.5*ds.min()<sc<1.5*ds.max(), (label,sc,ds.min(),ds.max())
 assert Delta(s1)<0 and Delta(s2)>0
 for s in (s1*0.5, (s1+sc)/2, (sc+s2)/2, s2+0.5):
  assert (Delta(s)>0)==(s>sc),(label,s,sc,Delta(s))
 checks+=10
 examples.append((label,round(sc,8),round(1/(4*sc),8),round(1/(4*s2),8),round(1/(4*s1),8)))

check([1,4],[1,1],'binary (1,4), equal weights')
for n in range(2,8):
 for k in range(30):
  ds=np.sort(rng.uniform(0.5,3.5,size=n))
  # Avoid near-point-mass numerical cancellation.
  if ds.max()-ds.min()<0.2:ds[-1]+=0.4
  ps=rng.uniform(0.2,1,size=n)
  check(ds,ps,f'random {n}-atom #{k}')
for n in (16,32,64,128):
 x,w=leggauss(n)
 ds=1.0+(x+1.0)*1.5
 check(ds,w,f'uniform [1,4] {n}-point Gauss-Legendre')
print('PASS, checks:',checks,'representative laws:',len(examples))
for r in [examples[0],examples[1],examples[31],examples[-1]]: print(r)
