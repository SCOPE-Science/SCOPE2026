#!/usr/bin/env python3
"""Independent finite checks of exchangeable minibatch covariance and stability formulas.

The mathematical arguments in RESULT.md, not these finite tests, prove the
parameter-uniform result. Requires Python 3.10+, SymPy, NumPy.
"""
from itertools import combinations
from math import comb, floor, sqrt
import sympy as s
import numpy as np

n, c, p, q, h = s.symbols('n c p q h', positive=True)
a = 1-c
L = 1+(n-1)*c
G = 1+(n-2)*c
K = a*L
T=s.Matrix([
 [1-2*h*p*L+h*h*L*L*(p+(n-1)*q)/n, h*h*(n-1)*a*a*(p-q)/n],
 [h*h*L*L*(p-q)/n, 1-2*h*p*a+h*h*a*a*((n-1)*p+q)/n]
])
S=p+q*G
F=4*p-2*S*h+q*K*h*h
assert s.factor((s.eye(2)-T).det()-p*h*h*K*F)==0
assert s.factor(F.subs(h,2)+4*q*(n-1)*c*c)==0
hd=2*p/(p+(n-1)*c*q)
assert s.factor(F.subs(h,hd)-4*c*p*q*(1-c)*(n-1)*(p-q)/(p+(n-1)*c*q)**2)==0
checks=3

# Reconstruct E[M X M^T] independently from every equally likely subset
# of each fixed size. Both eigenprojectors span all exchangeable covariances.
for nn in (2,3,4):
 for cc in (s.Rational(1,3),s.Rational(2,3)):
  HH=(1-cc)*s.eye(nn)+cc*s.ones(nn)
  UU=s.ones(nn)/nn
  for hh in (s.Rational(2,5),s.Rational(6,5),s.Rational(11,5)):
   for b in range(nn+1):
    pp=s.Rational(b,nn)
    qq=s.Rational(b*(b-1),nn*(nn-1))
    TT=T.subs({n:nn,c:cc,p:pp,q:qq,h:hh})
    masks=list(combinations(range(nn),b))
    for col,X in enumerate((UU,s.eye(nn)-UU)):
     Y=s.zeros(nn)
     for subset in masks:
      D=s.diag(*[int(i in subset) for i in range(nn)])
      M=s.eye(nn)-hh*D*HH
      Y += M*X*M.T
     Y=Y/len(masks)
     rr=s.simplify(s.trace(UU*Y))
     ss=s.simplify(s.trace((s.eye(nn)-UU)*Y)/(nn-1))
     assert s.simplify(rr-TT[0,col])==0, ('r',nn,cc,hh,b,col)
     assert s.simplify(ss-TT[1,col])==0, ('s',nn,cc,hh,b,col)
     checks+=2

# Fixed-mean exchangeable batch laws: min pair incidence at adjacent sizes,
# strict improvement over binomial and inclusion-induced sharp stability root.
def limit(nv,cv,pv,qv):
 lv=1+(nv-1)*cv
 kv=(1-cv)*lv
 gv=1+(nv-2)*cv
 ss=pv+qv*gv
 if abs(qv)<1e-13: return 2.0
 disc=ss*ss-4*pv*qv*kv
 return 4*pv/(ss+sqrt(max(0,disc)))

for nn in range(2,13):
 for cv in (0.17,0.5,0.89):
  for mu in (0.23,0.8,1.0,1.6,2.25,nn-0.35):
   if mu>=nn: continue
   pv=mu/nn
   m=floor(mu); theta=mu-m
   qmin=(m*(m-1)+2*m*theta)/(nn*(nn-1))
   qbin=pv*pv
   assert qmin+1e-12<qbin
   g1=limit(nn,cv,pv,qmin)
   g2=limit(nn,cv,pv,qbin)
   g3=limit(nn,cv,pv,pv)
   assert g1>g2 and g2>g3 and abs(g3-2/(1+(nn-1)*cv))<1e-11
   for qv in (qmin,qbin,pv):
    thr=limit(nn,cv,pv,qv)
    for testh in (0.7*thr,1.3*thr):
     tt=np.array(T.subs({n:nn,c:cv,p:pv,q:qv,h:testh}),dtype=float)
     eig=max(abs(np.linalg.eigvals(tt)))
     if testh<thr:assert eig<1-1e-9
     else: assert eig>1+1e-9
     checks+=1
   checks+=4

# Standalone transparent numerical example.
fixed=limit(4,.5,.5,1/6)
binomial=limit(4,.5,.5,.25)
assert abs(fixed-12/(5+sqrt(10)))<1e-12
assert binomial<fixed
print('PASS',checks,'exact symbolic / rational-mask / numerical assertions')
print('n=4,c=1/2,p=1/2: two-site fixed-size threshold:',fixed)
print('independent Bernoulli threshold:',binomial)
print('fixed-size one-step expected-descent ceiling:',4/3)
