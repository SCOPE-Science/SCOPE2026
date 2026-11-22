#!/usr/bin/env python3
"""Exact algebra and finite supplementary checks for four-state reversible path design.
Run: python verify.py  (requires sympy and numpy).
"""
import math
import random
import numpy as np
import sympy as sp

T=sp.symbols('t',positive=True)
r=1+sp.sqrt(2)
d=r*r
low_rate=2*T/(T+d)
low_a=T*(2+sp.sqrt(2))/(T+d)
low_b=T*(T+1+sp.sqrt(2))/(T+d)
high_a=T/(1+T)
high_b=T/2
q=sp.Matrix([r,1,-1,-r])
M=sp.diag(1,T,T,1)

def chain(a,b,c):
 return sp.Matrix([[1-a,a,0,0],
                   [a/T,1-(a+b)/T,b/T,0],
                   [0,b/T,1-(b+c)/T,c/T],
                   [0,0,c,1-c]])

assert sp.simplify(low_a+low_b-T)==0
assert sp.simplify(low_rate-2*T/(T+r*r))==0
assert all(sp.simplify(z)==0 for z in (chain(low_a,low_b,low_a)*q-(1-low_rate)*q))
assert sp.simplify((q.T*M*q)[0]-2*(r*r+T))==0
assert sp.simplify((q.T*M*(sp.eye(4)-chain(low_a,low_b,low_a))*q)[0]-low_rate*(q.T*M*q)[0])==0
assert sp.simplify(high_a+high_b-T - (1-T)*T/(2*(1+T)))==0
# The two nontrivial parity spectra for a reflection-invariant chain.
a,b=sp.symbols('a b',positive=True)
K=sp.Matrix([[1-a,a/sp.sqrt(T)],[a/sp.sqrt(T),1-(a+2*b)/T]])
H=sp.eye(2)-K
p=sp.factor(H.charpoly().as_expr())
z=sp.symbols('lambda')
pz=sp.factor(p.subs(sp.Symbol('lambda'),z))
assert sp.simplify(pz-(z*z-(a+(a+2*b)/T)*z+2*a*b/T))==0
assert sp.simplify(pz.subs(z,a*(1+1/T))+2*a*b/T**2)==0
Khi=sp.simplify(K.subs({a:high_a,b:high_b}))
assert sp.simplify(Khi.trace())==0
assert sp.simplify(Khi*Khi-sp.eye(2)/(1+T))==sp.zeros(2)
assert sp.simplify(high_a.subs(T,1)-low_a.subs(T,1))==0
assert sp.simplify(high_b.subs(T,1)-low_b.subs(T,1))==0
assert sp.simplify((1-low_rate).subs(T,1)-1/sp.sqrt(2))==0
print('Exact symbolic identities: PASS')

def fast_mu(t,a,b,c):
 ms=np.array([1.,t,t,1.]); edges=[a,b,c]
 P=np.eye(4)
 for i,w in enumerate(edges):
  P[i,i]-=w/ms[i];P[i+1,i+1]-=w/ms[i+1]
  P[i,i+1]+=w/ms[i];P[i+1,i]+=w/ms[i+1]
 S=np.diag(np.sqrt(ms))@P@np.diag(1/np.sqrt(ms))
 vals=np.linalg.eigvalsh(S)
 return max(abs(vals[:3]))

def optimal(t):
 if t<=1:
  a=t*(2+math.sqrt(2))/(t+3+2*math.sqrt(2))
  b=t-a
  return a,b,1-2*t/(t+3+2*math.sqrt(2))
 return t/(1+t),t/2,1/math.sqrt(1+t)

rng=random.Random(36571)
counts=0
for t in (0.01,0.03,.1,.2,.5,.9,1.,1.1,2.,5.,20.,100.):
 a,b,mu=optimal(t)
 assert abs(fast_mu(t,a,b,a)-mu) < 1e-11,(t,mu,fast_mu(t,a,b,a))
 assert 0<a<1 and 0<b<t and a+b<=t+1e-11
 for trial in range(150):
  bb=t*rng.random()
  aa=min(1,t-bb)*rng.random()
  cc=min(1,t-bb)*rng.random()
  obs=fast_mu(t,aa,bb,cc)
  assert obs+1e-10>=mu,(t,aa,bb,cc,obs,mu)
  counts+=1
print('Feasible asymmetric numerical samples checked:',counts)
print('Endpoint and interior examples:')
for t in (.5,1.,2.):
 a,b,mu=optimal(t)
 print('t=',t,'edge flows=',(a,b,a),'SLEM=',mu)
print('ALL CHECKS PASS (numerical tests are supplementary, not an infinite proof).')
