"""Reproduce exact algebra and independent Gaussian-conditioning checks."""
from fractions import Fraction
import random
import sympy as S

a,b,p,q,d=S.symbols('a b p q d',real=True)
f=lambda t:t**3+(1-t)**3
g=lambda x,y:x**3+(y-x)**3+(1-y)**3
F=(1-2*p+q)+(p-q)*(f(a)+f(b))+q*g(a,b)
assert S.factor(F.subs({a:S.Rational(1,2)-d,b:S.Rational(1,2)+d})-((1-2*p+q)+(p-q)*(S.Rational(1,2)+6*d*d)+q*(S.Rational(1,4)-S.Rational(3,2)*d+3*d*d+6*d**3)))==0
assert S.factor(S.diff(F.subs({a:S.Rational(1,2)-d,b:S.Rational(1,2)+d}),d) - S.Rational(3,2)*(12*q*d*d+(8*p-4*q)*d-q))==0
assert S.factor(1-f(a)-f(b)+g(a,b)-3*a*(1-b)*(1+b-a))==0
H=S.hessian(g(a,b),(a,b)); assert S.simplify(H[0,0]-6*b)==0 and S.simplify(H[1,1]-6*(1-a))==0
assert S.factor(S.diff(8*d/(1+4*d-12*d*d),d) - 8*(1+12*d*d)/(1+4*d-12*d*d)**2)==0

# Exact verification of posterior integral variance from Gaussian covariance.
def cov(x,y): return min(x,y)-x*y
for x,y in [(S.Rational(1,7),S.Rational(3,5)),(S.Rational(2,9),S.Rational(2,3)),(S.Rational(1,2),S.Rational(1,2)),(S.Rational(1,3),S.Rational(2,3))]:
 for ts in [[],[x],[y],[x,y]]:
  r=sum([t**3 for t in [x,y-x,1-y]])/12 if len(ts)==2 else (f(ts[0])/12 if len(ts)==1 else S.Rational(1,12))
  # drop coincident duplicate coordinates
  zz=list(dict.fromkeys(ts));
  if len(zz)!=len(ts):r=f(zz[0])/12
  K=S.Matrix([[cov(i,j) for j in zz] for i in zz]);k=S.Matrix([i*(1-i)/2 for i in zz]);
  direct=S.Rational(1,12)-(k.T*K.inv()*k)[0] if zz else S.Rational(1,12)
  assert S.simplify(direct-r)==0,(x,y,ts,direct,r)

# Formula, uniqueness and positivity of the marginal-correlation effect on valid parameter grids.
for pp in [S.Rational(1,10),S.Rational(2,5),S.Rational(1,2),S.Rational(3,4),S.Integer(1)]:
 for qq in [max(S.Integer(0),2*pp-1), pp/2,pp]:
  if qq < max(0,2*pp-1) or qq>pp:continue
  dd=S.Integer(0) if qq==0 else qq/(2*((2*pp-qq)+S.sqrt((2*pp-qq)**2+3*qq**2)))
  assert 0<=float(dd)<=1/6+1e-12
  assert abs(float((12*qq*dd**2+(8*pp-4*qq)*dd-qq)))<1e-12
  af,bf=float(.5-dd),float(.5+dd)
  best=float(F.subs({a:af,b:bf,p:pp,q:qq}))
  for i in range(21):
   for j in range(i,21):
    av=i/20;bv=j/20
    v=float(F.subs({a:av,b:bv,p:pp,q:qq}))
    assert v>=best-1e-10,(pp,qq,av,bv,v,best)

# Pure combinatorial endpoint cases and a compact exact benchmark.
pp=S.Rational(1,2);qq=S.Rational(1,4);dd=S.sqrt(3)/3-S.Rational(1,2)
assert S.simplify(12*qq*dd**2+(8*pp-4*qq)*dd-qq)==0
rstar=S.simplify(F.subs({a:S.Rational(1,2)-dd,b:S.Rational(1,2)+dd,p:pp,q:qq})/12)
assert rstar == S.Rational(1,12)-S.sqrt(3)/36
print('PASS: exact conditioning, convexity algebra, all tested parameter-grid candidates and benchmark')
print('p=1/2 q=1/4 nodes',float(S.Rational(1,2)-dd),float(S.Rational(1,2)+dd),'risk',float(rstar))
