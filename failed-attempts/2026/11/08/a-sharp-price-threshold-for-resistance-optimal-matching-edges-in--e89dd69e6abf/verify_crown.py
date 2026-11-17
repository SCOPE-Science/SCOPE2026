#!/usr/bin/env python3
"""Independent reproducibility checks for a priced matching on a balanced bipartite network.
Requires sympy, numpy, scipy. Finite tests supplement the proof; they do not certify all n or prices.
"""
import math
import numpy as np
import sympy as sp
from scipy.optimize import brentq

checks=0
n,c,x,B=sp.symbols('n c x B', positive=True)
F=sp.Rational(1,2)/(x+n-1)+(n-1)/n+(n-1)/(2*x+n-2)
G=(c*x+n-1)*F
ct=n*n*(4*n*n-11*n+8)/(4*n**4-19*n**3+32*n*n-24*n+8)
assert sp.factor(sp.diff(G,x).subs(x,0).subs(c,ct))==0;checks+=1
assert sp.factor(sp.diff(G,x).subs(x,1)-(c-1)*(n-1)*(4*n-3)/(2*n*n))==0;checks+=1
assert sp.factor(ct-1-8*(n-1)**3/((n-2)*(4*n**3-11*n*n+10*n-4)))==0;checks+=1
assert sp.series(ct.subs(n,1/x),x,0,3).removeO()==1+2*x+sp.Rational(7,2)*x**2;checks+=1
assert sp.factor((2*n*n*(n-1)*F.subs(x,0)/B)-n*(4*n**3-11*n*n+10*n-4)/(B*(n-2)))==0;checks+=1
assert sp.factor((2*n*n*(n-1)*F.subs(x,0)/B).subs(B,n*(n-1))-(4*n+1+(5*n-6)/((n-1)*(n-2))))==0;checks+=1

for nn in range(3,8):
 for aa,bb in [(sp.Rational(0),sp.Rational(2,5)),(sp.Rational(1,4),sp.Rational(3,8)),(sp.Rational(7,6),sp.Rational(3,5))]:
  L=sp.zeros(2*nn)
  for i in range(nn):
   for j in range(nn):
    w=aa if i==j else bb
    L[i,i]+=w;L[nn+j,nn+j]+=w;L[i,nn+j]-=w;L[nn+j,i]-=w
  J=sp.ones(2*nn)/(2*nn)
  k_exact=2*nn*((L+J).inv().trace()-1)
  k_formula=2*nn*(1/(2*(aa+(nn-1)*bb))+(nn-1)/(nn*bb)+(nn-1)/(2*aa+(nn-2)*bb))
  assert sp.simplify(k_exact-k_formula)==0
  eig=L.eigenvals()
  expected={sp.Integer(0):1,2*(aa+(nn-1)*bb):1,nn*bb:nn-1,2*aa+(nn-2)*bb:nn-1}
  # combine collisions, e.g. aa=bb
  from collections import defaultdict
  combined=defaultdict(int)
  for eigen,mult in expected.items():combined[sp.factor(eigen)]+=mult
  assert dict(combined)==eig,(nn,aa,bb,eig,dict(combined))
  checks+=2

def critical(nn):return float(ct.subs(n,nn))
def ff(nn,xx):return .5/(xx+nn-1)+(nn-1)/nn+(nn-1)/(2*xx+nn-2)
def ffprime(nn,xx):return -.5/(xx+nn-1)**2-2*(nn-1)/(2*xx+nn-2)**2
def stationary(nn,price,xx):return price*ff(nn,xx)+(price*xx+nn-1)*ffprime(nn,xx)
def optimum(nn,price,budget=1.):
 if price>=critical(nn):xx=0.
 else:
  hi=1.
  while stationary(nn,price,hi)<0:hi*=2
  xx=brentq(lambda z:stationary(nn,price,z),0,hi,xtol=1e-12)
 bb=budget/(nn*(price*xx+nn-1))
 return xx*bb,bb

def index_from_weights(nn,w):
 L=np.zeros((2*nn,2*nn),dtype=float)
 for i in range(nn):
  for j in range(nn):
   wt=w[i,j]
   L[i,i]+=wt;L[nn+j,nn+j]+=wt;L[i,nn+j]-=wt;L[nn+j,i]-=wt
 eig=np.linalg.eigvalsh(L)[1:]
 return float(2*nn*np.sum(1/eig))

rng=np.random.default_rng(3812)
for nn in range(3,9):
 for price in [0.03,0.2,0.7,0.999,1.,1.001,1.2,critical(nn)*.95,critical(nn),critical(nn)*1.05,3.,15.]:
  aa,bb=optimum(nn,price,12.)
  w=np.full((nn,nn),bb);np.fill_diagonal(w,aa)
  k=index_from_weights(nn,w)
  fK=2*nn*(1/(2*(aa+(nn-1)*bb))+(nn-1)/(nn*bb)+(nn-1)/(2*aa+(nn-2)*bb))
  assert abs(k-fK)<3e-8;checks+=1
  assert abs(float(np.sum(w)*1+(price-1)*np.trace(w))-12.)<1e-8;checks+=1
  if price>=critical(nn):assert aa==0
  elif price<1:assert aa>bb
  elif price==1:assert abs(aa-bb)<1e-9
  else:assert 0<aa<bb
  checks+=1
  for _ in range(10):
   v=rng.uniform(0.01,4,size=(nn,nn))
   v*=12./(v.sum()+(price-1)*np.trace(v))
   assert index_from_weights(nn,v)>=k-1e-7,(nn,price,k,index_from_weights(nn,v))
   checks+=1
print('VERIFY_OK',checks)
