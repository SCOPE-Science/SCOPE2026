"""Exact algebra checks for paired relaxed row projections (two real rows)."""
import sympy as sp

c,h,q=sp.symbols('c h q',real=True)
a=sp.sqrt((1+c)/2)
b=sp.sqrt((1-c)/2)
u=sp.Matrix([a,b]); v=sp.Matrix([a,-b]); I=sp.eye(2)
T1=I-h*u*u.T; T2=I-h*v*v.T
S=(T1**4+T2**4)/2
D=(T1*T2**2*T1+T2*T1**2*T2)/2
r=(1-h)**4
K=h**2*(1-c**2)*(2-h)/2
ap=1+(r-1)*(1+c)/2
am=1+(r-1)*(1-c)/2
bp=sp.factor(ap+K*(h*(1+c)-2))
bm=sp.factor(am-K*(2-h*(1-c)))
checks=0
for M, entries in [(S,(ap,am)),(D,(bp,bm))]:
 for i in (0,1):
  assert sp.simplify(sp.expand(M[i,i]-entries[i]))==0,(M,i)
  checks+=1
 assert sp.simplify(sp.expand(M[0,1]))==0
 assert sp.simplify(sp.expand(M[1,0]))==0
 checks+=2
q0=(h*h-2*h+2)/(h*h*(1-c*c))
assert sp.factor((am-ap)/((bp-ap)-(bm-am))-q0)==0
checks+=1
assert sp.factor((bp-ap)-K*(h*(1+c)-2))==0
checks+=1
assert sp.factor((bm-am)+K*(2-h*(1-c)))==0
checks+=1
assert sp.factor((bp-bm)-c*h*(h-2)*(c*c*h*h-2*h+2))==0
checks+=1
assert sp.factor(q0.subs(h,sp.Rational(2,1)/(1+c))-(1+c*c)/(2*(1-c*c)))==0
checks+=1
assert sp.factor(q0.subs({h:sp.Rational(3,2),c:sp.Rational(1,2)})-sp.Rational(20,27))==0
checks+=1
for qq,expected in [(sp.Rational(0),sp.Rational(49,64)),(sp.Rational(1,2),sp.Rational(257,512)),(sp.Rational(20,27),sp.Rational(3,8)),(sp.Rational(1),sp.Rational(103,256))]:
 vals=[sp.factor((1-qq)*t+qq*s).subs({h:sp.Rational(3,2),c:sp.Rational(1,2)}) for t,s in [(ap,bp),(am,bm)]]
 assert max(vals)==expected,(qq,vals,expected)
 checks+=1

# Verify piecewise minimizer, including the nonunique transition case,
# by exact rational comparisons against a full rational grid of couplings.
from fractions import Fraction
cc=[Fraction(i,20) for i in range(1,20)]
hh=[Fraction(i,20) for i in range(1,40)]
qa=[Fraction(i,50) for i in range(51)]
def risk(c,h,q):
 r=(1-h)**4;K=h*h*(1-c*c)*(2-h)/2
 ap=1+(r-1)*(1+c)/2
 am=1+(r-1)*(1-c)/2
 return max(ap+q*K*(h*(1+c)-2),am-q*K*(2-h*(1-c)))
for cv in cc:
 for hv in hh:
  qv=(hv*hv-2*hv+2)/(hv*hv*(1-cv*cv))
  plus_slope=hv*(1+cv)-2
  if plus_slope>0 and qv<1: opt=qv
  elif plus_slope==0 and qv<1: opt=qv
  else: opt=Fraction(1)
  optval=risk(cv,hv,opt)
  assert all(optval<=risk(cv,hv,qq) for qq in qa)
  # Check the endpoint and exact crossover as independent candidates.
  assert optval<=risk(cv,hv,Fraction(0)) and optval<=risk(cv,hv,Fraction(1))
  if qv<1:
   assert optval<=risk(cv,hv,qv)
  checks+=len(qa)+2+(qv<1)
print(f'PASS: {checks} symbolic identities and exact-rational comparisons')
