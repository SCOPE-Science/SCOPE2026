"""Exact symbolic and independent finite checks for the extinction-hazard theorem.
Run: python verify.py. Dependencies: sympy, numpy, scipy.
"""
import sympy as sp
import numpy as np
from scipy.linalg import expm

c,z=sp.symbols('c z',real=True)
T=sp.Matrix([[-1-2*c,2*c,0],[2,-2-2*c,2*c],[0,3,-3]])
w=sp.Matrix([[sp.Rational(1,2),0,sp.Rational(1,2)]])
D=sp.expand((z*sp.eye(3)-T).det())
V=sp.expand((w*(z*sp.eye(3)-T).adjugate()*sp.ones(3,1))[0])
assert sp.simplify(D-(z**3+(6+4*c)*z**2+(11+8*c+4*c*c)*z+6))==0
assert sp.simplify(2*V-(2*z*z+(11+8*c)*z+17+14*c+8*c*c))==0
assert sp.simplify(sp.resultant(D,V,z)+(c-1)*(4*c*c+5*c+6))==0
assert sp.factor(D.subs(c,1))==(z+3)*(z*z+7*z+2)
assert sp.factor(2*V.subs(c,1))==(z+3)*(2*z+13)
q=sp.symbols('q',positive=True)
S=2*q-sp.Rational(3,2)*q*q+sp.Rational(1,2)*q**3
H=sp.cancel(q*sp.diff(S,q)/S)
assert sp.simplify(H-(3*q*q-6*q+4)/(q*q-3*q+4))==0
assert sp.simplify(-q*sp.diff(H,q)-q*(3*q*q-16*q+12)/(q*q-3*q+4)**2)==0
assert (-q*sp.diff(H,q)).subs(q,1)==-sp.Rational(1,4)
assert sp.simplify((-q*sp.diff(H,q)).subs(q,sp.Rational(1,2))-sp.Rational(38,121))==0

# The seven-state labelled occupancy generator is formed independently; its
# count distribution is compared to the three-state generator.
from itertools import combinations
states=[tuple(int(i in cset) for i in range(3)) for k in (1,2,3) for cset in combinations(range(3),k)]
Q=np.zeros((7,7)); count=lambda s:sum(s)
for rate in [0,0.01,0.1,0.5,1,2,5]:
 Q[:]=0
 for i,s in enumerate(states):
  for v in range(3):
   if s[v]:
    y=list(s); y[v]=0
    if any(y): Q[i,states.index(tuple(y))]+=1
    Q[i,i]-=1
   else:
    k=count(s)
    if k:
     y=list(s);y[v]=1
     Q[i,states.index(tuple(y))]+=rate*k
     Q[i,i]-=rate*k
 Tnum=np.array(T.subs(c,rate)).astype(float)
 for t in [0,.03,.1,.2,.5,1,2,4]:
  p7=np.zeros(7)
  p7[0]=.5/3;p7[1]=.5/3;p7[2]=.5/3;p7[-1]=.5
  r7=p7@expm(Q*t)
  init=np.array([.5,0,.5]);r3=init@expm(Tnum*t)
  grouped=np.array([sum(r7[i] for i in range(7) if count(states[i])==k) for k in (1,2,3)])
  assert np.allclose(grouped,r3,rtol=1e-12,atol=1e-12),(rate,t,grouped,r3)
  hprime=((r3@Tnum@np.ones(3))**2-sum(r3)*(r3@Tnum@Tnum@np.ones(3)))/sum(r3)**2
  if rate<1 and t==0: assert hprime<0
  if rate>=1 and t>0: assert hprime<1e-7
  if rate<1 and t==1: assert hprime>0
print('PASS: characteristic polynomial, rational resolvent, resultant, critical cancellation, derivative, 56 independently grouped CTMC comparisons (168 state-probability entries), and sampled hazards')
