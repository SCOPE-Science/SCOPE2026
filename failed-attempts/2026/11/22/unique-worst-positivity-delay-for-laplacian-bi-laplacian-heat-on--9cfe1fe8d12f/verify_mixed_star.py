#!/usr/bin/env python3
"""Numerical consistency checks for exact mixed-heat positivity horizons on stars."""
import math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq

def laplacian(m):
 L=np.zeros((m+1,m+1))
 L[0,0]=m
 for k in range(1,m+1):
  L[0,k]=L[k,0]=-1
  L[k,k]=1
 return L

def kernel(m,eta,t):
 a,b=1+eta,(m+1)*(1+(m+1)*eta)
 v,w=math.exp(-a*t), math.exp(-b*t)
 P=np.empty((m+1,m+1))
 P[0,0]=(1+m*w)/(m+1)
 P[0,1:]=P[1:,0]=(1-w)/(m+1)
 off=1/(m+1)-v/m+w/(m*(m+1))
 diag=off+v
 P[1:,1:]=off
 for k in range(1,m+1): P[k,k]=diag
 return P

def horizon(m,eta):
 a,b=1+eta,(m+1)*(1+(m+1)*eta)
 r=b/a
 def f(h): return m-(m+1)*math.exp(-h)+math.exp(-r*h)
 # Bracket excluding trivial h=0, using small h below the unique positive root.
 slope=r-(m+1)
 lo=min(1e-7,slope/(10*r*r))
 assert f(lo)<0,(m,eta,f(lo),lo)
 h=brentq(f,lo,math.log1p(1/m),xtol=1e-14)
 return h/a

def optimum(m):
 h=math.log((m+2)/(m+1))
 r=1+math.log(m+1)/h
 eta=(r-(m+1))/((m+1)**2-r)
 T=(m*(m+2)*h-math.log(m+1))/(m*(m+1))
 return eta,T

trials=0
for m in [2,3,4,5,7,10,16,30]:
 L=laplacian(m)
 for eta in [.003,.01,.1,.25,1.,3.,10.]:
  T=horizon(m,eta)
  etastar,Tstar=optimum(m)
  assert 0<T<=Tstar+1e-12,(m,eta,T,Tstar)
  for q in [.17,.7,1.,1.2,4.]:
   t=q*T
   P=kernel(m,eta,t)
   Q=expm(-t*(L+eta*(L@L)))
   assert np.max(np.abs(P-Q))<5e-12,(m,eta,t,np.max(np.abs(P-Q)))
   assert np.max(np.abs(P.sum(axis=1)-1))<1e-12
   assert np.min(P[0,:])>0
   assert np.min(np.diag(P))>0
   if q<1:assert P[1,2]<-5e-15,(m,eta,q,P[1,2])
   if q>1:assert P[1,2]>5e-15,(m,eta,q,P[1,2])
   if q==1:assert abs(P[1,2])<5e-14
   trials+=1
 assert abs(horizon(m,etastar)-Tstar)<1e-12
 for d in [.01,.12,.5]:
  assert horizon(m,etastar*math.exp(d))<Tstar
  assert horizon(m,etastar*math.exp(-d))<Tstar

# Asymptotic predictions: m*Tmax tends to 1 and m*eta*/log(m) tends to 1.
for m in [100,1000,10000]:
 e,t=optimum(m)
 assert 0<m*t<1
 assert .5<m*e/math.log(m)<1.1
print('INDEPENDENT_MATRICES_AND_HORIZON_SIGNS_PASS',trials)
print('OPTIMAL_STRENGTH_AND_LARGE_STAR_LIMITS_PASS',11)
for m in [2,3,5,10,100]:
 print('STAR',m,'ETA_STAR',format(optimum(m)[0],'.14g'),'MAX_TIME',format(optimum(m)[1],'.14g'))
