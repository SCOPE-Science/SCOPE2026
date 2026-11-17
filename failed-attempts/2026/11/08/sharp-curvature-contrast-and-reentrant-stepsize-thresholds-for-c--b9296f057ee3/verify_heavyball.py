"""Algebraic and numerical sanity tests for periodic-curvature HB."""
from fractions import Fraction as Q
import sympy as sp
import random

b,z,r=sp.symbols('b z r', positive=True)
c=1+b
A=lambda t:sp.Matrix([[c-t,-b],[1,0]])
P=sp.simplify(A(r*z)*A(z))
assert sp.simplify(sp.trace(P)-((c-z)*(c-r*z)-2*b))==0
assert sp.simplify(P.det()-b**2)==0
assert sp.simplify((1+b*b)+sp.trace(P)-((c-z)*(c-r*z)+(1-b)**2))==0
assert sp.factor((1+b*b)-sp.trace(P))==sp.factor(c**2-(c-z)*(c-r*z))
assert sp.simplify(sp.diff((c-z)*(c-r*z),z)-(2*r*z-c*(r+1)))==0
print('general monodromy:',P)
# exact rational example, stable again at larger step
def exact_poly(eta):
 C=Q(3,2)
 return (C-eta)*(C-2*eta)+Q(1,4)
for eta,sig in [(Q(1,2),1),(Q(1),0),(Q(9,8),-1),(Q(5,4),0),(Q(7,5),1)]:
 assert (exact_poly(eta)>0)-(exact_poly(eta)<0)==sig,(eta,exact_poly(eta))
Pex=sp.simplify(P.subs({b:sp.Rational(1,2),z:sp.Rational(9,8),r:2}))
assert Pex == sp.Matrix([[-sp.Rational(25,32),sp.Rational(3,8)],[sp.Rational(3,8),-sp.Rational(1,2)]])
assert sp.simplify(Pex.charpoly().as_expr()-(sp.Symbol('lambda')**2+sp.Rational(41,32)*sp.Symbol('lambda')+sp.Rational(1,4)))==0
eigens=Pex.eigenvals();assert len(eigens)==2
assert min(float(x) for x in eigens)<-1
assert Pex[0,0]+Pex[0,1] != Pex[1,0]+Pex[1,1]
print('example:',Pex, 'roots',eigens, 'criterion at 9/8',exact_poly(Q(9,8)))
# robust threshold regime via random crosschecks
import math
def threshold(beta):
 if beta == 0: return math.inf
 delta=(1-beta)/(1+beta)
 if beta > 2-math.sqrt(3): return (math.sqrt(1+delta**2)+delta)**2
 return (1+beta)**2/(2*beta)
def worst(beta,ratio):
 C=1+beta
 zv=C*(ratio+1)/(2*ratio)
 hi=2*C/ratio
 zz=min(zv,hi)
 return (C-zz)*(C-ratio*zz)+(1-beta)**2
rng=random.Random(723)
for _ in range(10000):
 beta=rng.uniform(.00001,.99999)
 ratio=1+10**rng.uniform(-3,3)
 dd=worst(beta,ratio)
 t=threshold(beta)
 if ratio>t*(1+1e-8): assert dd<0,(beta,ratio,dd,t)
 if ratio<t*(1-1e-8): assert dd>0,(beta,ratio,dd,t)
# dense discrete test against closed form signs on both branches
for beta in [0.01,.1,2-math.sqrt(3),.3,.5,.9,.99]:
 for ratio in [1.01,1.5,2,2.5,3,4,8,20,100,1000]:
  t=threshold(beta)
  dd=worst(beta,ratio)
  if abs(ratio-t)<1e-7:continue
  assert (dd<0)==(ratio>t), (beta,ratio,dd,t)
  M=0.0
  C=1+beta
  for j in range(1,2001):
   eta=2*C/ratio*j/2001
   poly=(C-eta)*(C-ratio*eta)+(1-beta)**2
   M=min(M,poly)
  if dd < -0.005: assert M<0,(beta,ratio,dd,M)
print('PASS 10000 randomized threshold checks, 70 grid checks, all exact algebra assertions')
# Full classification: reentrant stability exists iff beta>2-sqrt(3), R1<r<R2.
def has_reentry(beta,ratio):
 C=1+beta
 hi=2*C/ratio
 vertex=C*(ratio+1)/(2*ratio)
 if vertex>=hi: return False
 at_min=(C-vertex)*(C-ratio*vertex)+(1-beta)**2
 at_max=(C-hi)*(C-ratio*hi)+(1-beta)**2
 return at_min<0 and at_max>0
for beta in [0.01,.1,.25,.2679491924311227,.3,.5,.75,.9,.99]:
 rb=threshold(beta)
 r2=(1+beta)**2/(2*beta)
 for ratio in [1.01,1.1,1.5,1.9,2,2.1,2.2,2.5,2.9,3,3.1,4,7,20,100]:
  want=beta>2-math.sqrt(3) and rb<ratio<r2
  assert has_reentry(beta,ratio)==want,(beta,ratio,rb,r2)
print('PASS 135 reentrance classification tests')
