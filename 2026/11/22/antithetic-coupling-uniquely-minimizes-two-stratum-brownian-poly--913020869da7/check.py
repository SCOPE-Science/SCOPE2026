"""Reproduce exact two-stratum Brownian polynomial-moment quadrature identities.
Uses only Python 3 and SymPy; the proof in RESULT.md is analytic.
"""
import sympy as s
from fractions import Fraction as F
u,v=s.symbols('u v',real=True)
x=u/2; y=(1+v)/2
h=y-x; mid=(x+y)/2
bridge=lambda a,b: s.factor((b-a)**3*((a+b)/2-s.Rational(1,2))**2/12+(b-a)**5/s.Integer(720))
A=s.factor(bridge(0,x))
C=s.factor(bridge(x,y))
z=s.symbols('z',real=True)
T=s.factor(s.integrate(z*z*(1-z)**2/4,(z,y,1)))
Q=lambda t:t*t/s.Integer(4)-t**3/s.Integer(6)
assert s.factor(A+C+T-(s.Rational(1,120)-Q(x)**2/x-(Q(y)-Q(x))**2/(y-x)))==0
assert s.factor(C-((1-u)**5+v**5)/1440 - v*(1-u)*(1+v-u)*(u+v-1)**2/1152)==0
base=s.integrate(A,(u,0,1))+s.integrate(T,(v,0,1))
anti=s.factor(base+s.integrate(C.subs(v,1-u),(u,0,1)))
com=s.factor(base+s.integrate(C.subs(v,u),(u,0,1)))
iid=s.factor(base+s.integrate(s.integrate(C,(u,0,1)),(v,0,1)))
assert base==s.Rational(107,69120)
assert anti==s.Rational(41,23040)
assert com==iid==s.Rational(25,13824)
assert com-anti==s.Rational(1,34560)
assert s.Rational(1,120)>anti
check_count=0
for i in range(1,30):
 for j in range(1,30):
  p={u:s.Rational(i,30),v:s.Rational(j,30)}
  residual=s.factor((C-((1-u)**5+v**5)/1440).subs(p))
  assert residual>=0
  a=p[u]/2;b=(1+p[v])/2
  q=lambda t:t*t/s.Integer(4)-t**3/s.Integer(6)
  direct=s.Rational(1,120)-q(a)**2/a-(q(b)-q(a))**2/(b-a)
  assert s.factor((A+C+T).subs(p)-direct)==0
  check_count+=1
print('PASS: symbolic covariance, dual equality, risk integrals,',check_count,'exact rational grid points')
print('optimal',anti,'comonotone',com,'independent',iid,'improvement',com-anti)
