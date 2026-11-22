#!/usr/bin/env python3
"""Exact symbolic verification of a three-coordinate nonnegative ridge support path."""
import sympy as s
from itertools import combinations

t=s.symbols('t',real=True,nonnegative=True)
A=s.Matrix([[3,-1,s.Rational(3,2)],[-1,1,0],[s.Rational(3,2),0,4]])
b=s.Matrix([1,1,5]); I=s.eye(3); H=A+t*I
D=s.factor(H.det())
q=(t-s.Rational(1,2))*(t-1)
u=H.inv()*b
assert s.factor(u[0]-q/D)==0
assert s.factor(u[1]-(1+u[0])/(1+t))==0
assert s.factor(u[2]-(5-s.Rational(3,2)*u[0])/(4+t))==0
assert s.expand(D) == t**3+8*t**2+s.Rational(63,4)*t+s.Rational(23,4)
assert all(c>0 for c in s.Poly(D,t).all_coeffs())
assert all(c>0 for c in s.Poly(D+q,t).all_coeffs())
assert all(c>0 for c in s.Poly(D-q,t).all_coeffs())
assert all(A[:k,:k].det()>0 for k in (1,2,3))
xmid=s.Matrix([0,1/(t+1),5/(t+4)])
gmid=s.simplify(H*xmid-b)
assert s.factor(gmid[0]+q/((t+1)*(t+4)))==0
assert all(s.factor(gmid[i])==0 for i in (1,2))
assert s.factor(q.subs(t,0))==s.Rational(1,2)
assert s.factor(q.subs(t,s.Rational(3,4)))==-s.Rational(1,16)
assert s.factor(q.subs(t,2))==s.Rational(3,2)

# Enumerate all 8 candidate supports at exact sample parameters and test KKT.
def optimal_exact(T):
  G=A+T*I
  sols=[]
  for n in range(4):
    for S in combinations(range(3),n):
      x=s.zeros(3,1)
      if S:
        z=G.extract(S,S).inv()*b.extract(S,[0])
        for j,i in enumerate(S):x[i]=z[j]
      grad=G*x-b
      if all(x[i]>=0 for i in range(3)) and all(grad[i]>=0 for i in range(3)) and all(x[i]*grad[i]==0 for i in range(3)):
        sols.append(x)
  uniq=[]
  for x in sols:
    if x not in uniq:uniq.append(x)
  assert len(uniq)==1, (T,uniq)
  return uniq[0]
points=[s.Rational(0),s.Rational(1,4),s.Rational(1,2),s.Rational(3,4),s.Integer(1),s.Rational(3,2),s.Integer(2),s.Integer(10),s.Integer(100)]
for T in points:
  x=optimal_exact(T)
  assert (x[0]==0)==(s.Rational(1,2)<=T<=1)
  assert x[1]>0 and x[2]>0
  if s.Rational(1,2)<=T<=1:
    assert x==xmid.subs(t,T)
  else:
    assert x==u.subs(t,T)

# A universal two-coordinate zero-test follows from the KKT equations.
# For G=[[a+t,c],[c,d+t]], x_1=0 iff c*max(b_2,0)/(d+t)-b_1>=0.
# Since this expression is monotone or constant in t>=0, its zero set is an interval abutting an endpoint.
assert s.diff(s.symbols('c')*s.symbols('v')/(s.symbols('d')+t)-s.symbols('w'),t) == -s.symbols('c')*s.symbols('v')/(s.symbols('d')+t)**2
print('VERIFY_OK exact KKT, symmetric principal minors, reentry at 1/2 and 1, two-dimensional monotone boundary test, 9 support enumerations')
