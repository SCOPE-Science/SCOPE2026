"""Exact checks of the two-component scalar quadratic reshuffling frontier."""
from fractions import Fraction
import sympy as s
z,t,u=s.symbols('z t u',real=True)
p=1-2*t+(1-z)*t*t
S=1-2*t+(1+z)*t*t
P=z*(1-z)**2*t**4+(1-z)*(1-3*z)*t**3+(-2*z*z+5*z-5)*t*t+(8-2*z)*t-4
R=224*z**7+896*z**6+96*z**5-3405*z**4+1956*z**3+350*z*z-148*z-17
RR=t**4*(z/(1-p)**2+1/(1-p*p))
WR=t*t/(1-S)
assert s.factor((RR/WR-1)-2*P/((2-(1-z)*t)**2*(2-2*t+(1-z)*t*t)))==0
assert s.factor(s.resultant(P,s.diff(P,t),t)+4*z**3*(z-1)**4*R)==0
assert s.factor(P.subs(t,1)-z*z*(z-1))==0
assert s.factor(P.subs(t,2/(1+z))+16*z*z*(1-z)**2/(1+z)**4)==0
assert s.factor(s.expand((1+u)**4*P.subs(t,1/(1+u)))-(-4*u**4-2*(z+4)*u**3-(2*z*z+z+5)*u*u-(z*z+1)*u+z*z*(z-1)))==0
H=s.factor((1+u)**4*(1+z)**4*P.subs(t,(1+2*u/(1+z))/(1+u)))
coefs=[z*z*(z-1)*(1+z)**4,(z-1)*(1+z)**3*(7*z*z-1),(1-z)*(1+z)**2*(2*z**3-19*z*z+4*z+1),2*z*(1-z)*(1+z)*(5*z*z-10*z+1),-16*z*z*(1-z)**2]
assert s.Poly(s.expand(H-s.Add(*(coefs[i]*u**i for i in range(5)))),u).is_zero
assert s.Poly(R,z).count_roots(0,1)==2
assert s.Poly(R,z).count_roots(s.Rational(315,1000),s.Rational(316,1000))==1
assert s.Poly(R,z).count_roots(s.Rational(819,1000),s.Rational(820,1000))==1
assert s.gcd(R,s.diff(R,z))==1
for v,n in [(s.Rational(1,4),2),(s.Rational(2,5),0),(s.Rational(9,10),0)]:
 assert s.Poly(P.subs(z,v),t).count_roots(1,2/(1+v))==n
assert s.factor(P.subs(z,0)-(t-1)*(t-2)**2)==0
u0=s.Rational(6,5);z0=s.Rational(1,4)
assert s.factor(RR.subs({t:u0,z:z0})-s.Rational(5364,2057))==0
assert s.factor(WR.subs({t:u0,z:z0})-s.Rational(12,5))==0
# Direct pairwise SGD affine-step propagation, independent polynomial recursion.
d=s.symbols('d',real=True)
a1=1-d;a2=1+d
q1=1-t*a1;q2=1-t*a2
s1=lambda x:q1*x-t
s2=lambda x:q2*x+t
x=s.symbols('x')
assert s.expand((s2(s1(x))-q1*q2*x)-t*t*(1+d))==0
assert s.expand((s1(s2(x))-q1*q2*x)-t*t*(d-1))==0
assert s.factor(s.expand((q1*q1+q2*q2)/2).subs(d*d,z)-S)==0
assert s.factor(s.expand((s1(x)**2+s2(x)**2)/2) -(s.expand(S.subs(z,d*d))*x*x+t*t-2*t*t*d*x))==0
sturm=s.sturm(R,z)
def variations(v):
 signs=[1 if term.subs(z,v)>0 else -1 for term in sturm]
 return sum(signs[i]!=signs[i+1] for i in range(len(signs)-1))
assert [variations(v) for v in [0,s.Rational(315,1000),s.Rational(316,1000),s.Rational(819,1000),s.Rational(820,1000),1]]==[4,4,3,3,2,2]
assert s.Poly(P.subs(z,s.Rational(1,3)),t).count_roots(1,s.Rational(3,2))==0
for dval in (s.Rational(0),s.Rational(1,5),s.Rational(1,2),s.Rational(4,5)):
 for tv in (s.Rational(1,10),s.Rational(9,10),s.Rational(6,5)):
  if tv>=2/(1+dval*dval):continue
  zval=dval*dval
  Pval=P.subs({z:zval,t:tv});gap=(RR-WR).subs({z:zval,t:tv})
  assert (Pval>0)==(gap>0) and (Pval<0)==(gap<0)
print('VERIFY_OK: exact rational identities, resultant, Sturm counts, scalar update, and risk-sign comparisons.')
