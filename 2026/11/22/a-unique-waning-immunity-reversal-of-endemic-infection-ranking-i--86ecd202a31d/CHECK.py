#!/usr/bin/env python3
"""Exact algebraic tests of the two-group SIRS prevalence-ranking theorem."""
import sympy as s
from fractions import Fraction

a,b,g,h,d=s.symbols('a b g h d', positive=True)
y=s.factor(d*(a*b-g*h)/(b*(d*(a+g)+g*(a+h))))
z=s.factor(d*(a*b-g*h)/(a*(d*(b+h)+h*(b+g))))
r1=g*y/d; r2=h*z/d
x1=s.factor(1-y-r1); x2=s.factor(1-z-r2)
assert s.factor(a*z*x1-g*y)==0
assert s.factor(b*y*x2-h*z)==0
assert s.factor(g*y-d*r1)==0
assert s.factor(h*z-d*r2)==0
U=s.factor(1/y); V=s.factor(1/z)
assert s.factor(U-g*V/a-(1+g/d))==0
assert s.factor(V-h*U/b-(1+h/d))==0
A=a*h-b*g
B=a*b*(h-g)+g*h*(a-b)
D1=b*(d*(a+g)+g*(a+h))
D2=a*(d*(b+h)+h*(b+g))
assert s.factor((y-z)*D1*D2/(d*(a*b-g*h))-(A*d+B))==0
assert s.factor(s.diff(y,d)- (a*b-g*h)*g*(a+h)/(b*(d*(a+g)+g*(a+h))**2))==0
assert s.factor(s.diff(z,d)- (a*b-g*h)*h*(b+g)/(a*(d*(b+h)+h*(b+g))**2))==0
w={a:s.Integer(2),b:s.Integer(5),g:s.Integer(1),h:s.Integer(2)}
assert s.simplify((A*d+B).subs(w))==4-d
for delta,expect1,expect2 in [(1,s.Rational(8,35),s.Rational(4,19)),(4,s.Rational(2,5),s.Rational(2,5)),(10,s.Rational(8,17),s.Rational(20,41))]:
 subs={**w,d:s.Integer(delta)}
 assert y.subs(subs)==expect1 and z.subs(subs)==expect2
 for q in [y,z,r1,r2,x1,x2]: assert 0<q.subs(subs)<1
 assert s.simplify((x1+y+r1).subs(subs))==1
 assert s.simplify((x2+z+r2).subs(subs))==1
count=0
for ai in (2,3,5):
 for bi in (3,5,7):
  for gi,hi in ((1,2),(2,1)):
   for di in (1,3):
    subs={a:ai,b:bi,g:gi,h:hi,d:di}
    if ai*bi<=gi*hi: continue
    vals=[s.cancel(v.subs(subs)) for v in (x1,y,r1,x2,z,r2)]
    assert all(0<v<1 for v in vals)
    assert sum(vals[:3])==sum(vals[3:])==1
    assert s.sign(vals[1]-vals[4])==s.sign((A*d+B).subs(subs))
    count+=1
assert count==36,count
print('PASS: exact symbolic equilibrium, derivative and ranking identities; rational witness; 36 independent parameter checks')
