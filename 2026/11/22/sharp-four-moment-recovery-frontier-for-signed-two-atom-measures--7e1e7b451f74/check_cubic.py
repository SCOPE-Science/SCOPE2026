"""Reproducible algebraic checks for cubic moment dipoles.
Requires Python 3, sympy; optionally scipy for discretized primal tests.
The exact symbolic identities are deductions; finite LP probes are diagnostic only.
"""
import sympy as S
from fractions import Fraction
x,a,b,L,R,d = S.symbols('x a b L R d',real=True)
t=S.symbols('t', real=True)
# Integrate from a to x with b=a+d to avoid symbolic-piecewise ambiguity.
y=S.symbols('y',real=True)
p=1+12/d**3*S.integrate(y*(y-d),(y,0,x-a))
p=S.factor(p)
assert S.simplify(p.subs(x,a)-1)==0
assert S.simplify(p.subs(x,a+d)+1)==0
assert S.simplify(S.diff(p,x)-12*(x-a)*(x-a-d)/d**3)==0
assert S.simplify(p.subs(x,a-L)+1-2*(d-2*L)*(d+L)**2/d**3)==0
assert S.simplify(1-p.subs(x,a+d+R)-2*(d-2*R)*(d+R)**2/d**3)==0
assert S.factor(p.subs(x,a+d)-p.subs(x,a)+2)==0
# Exact rational grid: classify endpoint boundedness by the simple two inequalities;
# additionally verify all stationary and endpoint values.
N=0
for ai in [S.Rational(i,12) for i in range(-11,11)]:
 for bi in [S.Rational(i,12) for i in range(-10,12) if S.Rational(i,12)>ai]:
  dd=bi-ai
  if dd<=0: continue
  pp=p.subs({a:ai,d:dd})
  values=[pp.subs(x,z) for z in [-1,ai,bi,1]]
  bounded=all(-1<=v<=1 for v in values)
  condition=(dd>=2*(ai+1) and dd>=2*(1-bi))
  assert bounded==condition, (ai,bi,values)
  N+=1
# A case inside and exactly on the two-sided boundary; another asymmetric sharp boundary.
assert S.factor(p.subs({a:S.Rational(-1,2),d:1})-(4*x**3-3*x))==0
for aa,bb,inside in [(-S.Rational(3,4),S.Rational(3,4),True),(-S.Rational(1,2),S.Rational(1,2),True),(-S.Rational(1,3),S.Rational(2,3),False),(0,S.Rational(3,4),False),(-S.Rational(4,5),S.Rational(2,5),True)]:
 aa=S.sympify(aa); bb=S.sympify(bb)
 dd=bb-aa
 cond=dd>=2*(aa+1) and dd>=2*(1-bb)
 assert cond==inside,(aa,bb,cond)
print('Exact symbolic identities and',N,'rational-location classifications passed.')

try:
 import numpy as np
 from scipy.optimize import linprog
 # Discretization includes the true two atoms; comparison probes only, NOT proof.
 for aa,bb in [(-.75,.75),(-.5,.5),(-.25,.5),(-.25,.25),(-.8,.5)]:
  z=np.unique(np.concatenate((np.linspace(-1,1,801),[aa,bb])))
  A=np.array([z**k for k in range(4)])
  m=np.array([aa**k - bb**k for k in range(4)])
  # signed measure = positive part minus negative part
  c=np.ones(2*len(z)); E=np.concatenate((A,-A),axis=1)
  sol=linprog(c,A_eq=E,b_eq=m,bounds=(0,None),method='highs')
  assert sol.success,sol.message
  opt=sol.fun
  cond=(bb-aa>=2*(aa+1)-1e-10 and bb-aa>=2*(1-bb)-1e-10)
  if cond:assert abs(opt-2)<1e-7,(aa,bb,opt)
  else:assert opt<2-1e-7,(aa,bb,opt)
  print('discrete LP diagnostic',aa,bb,'criterion',cond,'grid optimum',round(opt,9))
except ImportError:
 print('Optional scipy not installed: finite LP diagnostic skipped.')
