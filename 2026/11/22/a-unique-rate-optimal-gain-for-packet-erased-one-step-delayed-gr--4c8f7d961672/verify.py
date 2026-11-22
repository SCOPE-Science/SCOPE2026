"""Reproduce exact second-moment identities for delayed, intermittently delivered descent.

Python >=3.10; requires sympy and numpy. Finite tests supplement, not replace,
the all-parameter proof in RESULT.md.
"""
import math
from fractions import Fraction
import numpy as np
import sympy as s

p,h,r=s.symbols('p h r', positive=True)
M=s.Matrix([[1,-2*p*h,p*h*h],[1,-p*h,0],[1,0,0]])
f=s.expand((r*s.eye(3)-M).det())
assert s.expand(f-(r**3+(p*h-1)*r**2+p*h*(1-h)*r-p*p*h**3))==0
assert s.expand(f.subs(r,1)-p*h*(2-h-p*h*h))==0
Q=(1-p)**2*h**3-8*(1+p)*h*h+8*h-1
stationary=s.diff(f,h)/p
res=s.factor(s.resultant(f,stationary,r))
assert s.simplify(res/(h**3*p**2*Q))==4
assert s.factor(Q.subs(h,s.Rational(1,4)))==(p-1)*(p-33)/64
assert s.factor(Q.subs(p,(2-h)/h**2))==(h-4)*(h**3-2*h*h+5*h-1)/h
assert s.factor(64*f.subs(r,s.Rational(1,4)).subs(h,s.Symbol('z')/p) -(-3+20*s.Symbol('z')-16*s.Symbol('z')**2/p-64*s.Symbol('z')**3/p))==0
# A map's exact covariance transfer, evaluated at rational states
X,Y=s.symbols('X Y')
right=(1-p)*X**2+p*(X-h*Y)**2
left=s.Matrix([X**2,X*Y,Y**2]);assert s.expand((M*left)[0]-right)==0

# Independent rational path enumeration matches matrix recurrence exactly.
for pp in [s.Rational(1,5),s.Rational(1,2),s.Rational(4,5)]:
 for hh in [s.Rational(1,7),s.Rational(1,3),s.Rational(3,4)]:
  for a,b in [(s.Rational(1),s.Rational(1)),(s.Rational(0),s.Rational(2)),(s.Rational(3),s.Rational(-2))]:
   moments=s.Matrix([b*b,a*b,a*a]) # state initially (x_0,x_{-1})=(b,a)
   histories={(a,b):s.Integer(1)}
   for step in range(1,6):
    new={}
    for (old,cur),weight in histories.items():
     for success,w in [(False,1-pp),(True,pp)]:
      nxt=cur-hh*old if success else cur
      key=(cur,s.expand(nxt))
      new[key]=new.get(key,0)+weight*w
    histories=new
    moments=M.subs({p:pp,h:hh})*moments
    direct=sum(w*cur*cur for (_,cur),w in histories.items())
    assert s.simplify(direct-moments[0])==0

# Check there is exactly one rate-optimal step above 1/4 in every sampled regime
from scipy.optimize import brentq, minimize_scalar
for pp in np.linspace(.01,.99,99):
 hc=4/(1+np.sqrt(1+8*pp))
 qq=lambda z:(1-pp)**2*z**3-8*(1+pp)*z*z+8*z-1
 hs=brentq(qq,.25,hc)
 def rate(z):
  W=np.array([[1.,-2*pp*z,pp*z*z],[1.,-pp*z,0],[1.,0.,0.]])
  return max(abs(np.linalg.eigvals(W)))
 for z in [1e-6,.1,.25,max(1e-6,hs-0.01),min(hc,hs+0.01),hc,1.3*hc]:
  if abs(z-hs)>1e-9: assert rate(hs)<rate(z)+2e-8,(pp,z,hs,rate(z))
 test=minimize_scalar(rate,bounds=(1e-8,hc),method='bounded',options={'xatol':1e-12})
 assert abs(test.x-hs)<2e-5,(pp,test.x,hs)

pp=.5
hc=4/(1+math.sqrt(1+8*pp))
hs=brentq(lambda z:(1-pp)**2*z**3-8*(1+pp)*z*z+8*z-1,.25,hc)
rt=max(abs(np.linalg.eigvals(np.array([[1,-2*pp*hs,pp*hs*hs],[1,-pp*hs,0],[1,0,0]]))))
assert hs>0.50800153 and hs<0.50800154
print('exact symbolic checks passed; rational enumeration: 405 test steps; 99 optimal-rate grids passed')
print(f'p=1/2, h*= {hs:.12f}, rate*= {rt:.12f}, stability_ceiling= {hc:.12f}')
