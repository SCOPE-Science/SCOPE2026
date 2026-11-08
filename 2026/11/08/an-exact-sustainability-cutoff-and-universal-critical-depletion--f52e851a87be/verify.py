import math
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

b=sp.Rational(7,10);d=sp.Integer(2);c=sp.Rational(1,2)
k=sp.symbols('k',real=True,positive=True)
q=sp.simplify((1-b)/(d-b))
K=sp.log((d-1)/(1-b))/c
pp=sp.simplify(K*q*(1-q))
kappa=sp.simplify(1+(d-b)*pp)
# Exact normalization and critical-coefficient checks
print('q=',q,'kc=',K,'kappa=',kappa)
assert q==sp.Rational(3,13)
assert sp.simplify(kappa-(1+sp.Rational(6,13)*sp.log(sp.Rational(10,3))))==0
RR=sp.symbols('R',real=True)
p=1/(1+sp.exp(-K*(RR-c)))
assert sp.simplify(p.subs(RR,0)-q)==0
assert sp.simplify(sp.diff(p,RR).subs(RR,0)-pp)==0
for kval in (1.0,float(K),5.0):
 def sigmoid(R):
  return 1/(1+math.exp(-kval*(R-.5)))
 def rhs(t,z):
  x,R=z
  return [1-x-sigmoid(R),R*(1-2+1.3*x-R)]
 lam=1-.7-1.3*sigmoid(0)
 if lam>0:
  root=brentq(lambda R:1-.7-1.3*sigmoid(R)-R,0,1)
 else:root=0
 print('k=',kval,'lambda=',lam,'R_star=',root)
 if abs(kval-float(K))<1e-12:
  for init in ([.1,.5],[.9,.03]):
   sol=solve_ivp(rhs,(0,30000),init,method='BDF',rtol=2e-11,atol=2e-13,dense_output=True)
   assert sol.success,sol.message
   for t in (100,1000,10000,30000):
    x,R=sol.sol(t)
    print('t=',t,'tR=',t*R,'t(x-x0)=',t*(x-float(1-q)))
  assert abs(30000*sol.y[1,-1]-float(1/kappa))<0.003
 else:
  sol=solve_ivp(rhs,(0,1000),[.5,.5],method='BDF',rtol=1e-10,atol=1e-12)
  assert sol.success
  assert abs(sol.y[1,-1]-root)<1e-6,(kval,sol.y[1,-1],root)
print('VERIFY_OK')
