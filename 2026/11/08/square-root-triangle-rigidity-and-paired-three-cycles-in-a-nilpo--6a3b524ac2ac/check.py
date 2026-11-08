#!/usr/bin/env python3
"""Exact algebraic checks for the triangular height spectrum."""
import sympy as S
x,y,z,A=S.symbols('x y z A')
p=S.Function('p')
H=p(y+A*x*x)
F=S.Matrix([H,z-2*A*x*H,A*H**2])
J=F.jacobian([x,y,z])
assert S.simplify(S.trace(J)) == 0
assert S.simplify(S.trace(J*J)) == 0
assert S.simplify(J.det()) == 0
assert S.simplify(J**3) == S.zeros(3)
P=lambda t: (-3*t*t+35*t-32)/S.Integer(20)
assert [P(i) for i in (1,4,9)]==[0,3,2]
def step(v):
 a,b,c=v; h=P(b+a*a)
 return (S.simplify(h),S.simplify(c-2*a*h),S.simplify(h*h))
first=[(2,-3,4),(0,4,0),(3,0,9)]
second=[(3,-8,9),(0,9,0),(2,0,4)]
for cyc in [first,second]:
 for j in range(3): assert step(cyc[j]) == cyc[(j+1)%3]
 assert len(set(cyc))==3
assert set(first).isdisjoint(set(second))
assert [v[1]+v[0]**2 for v in first]==[1,4,9]
assert [v[1]+v[0]**2 for v in second]==[1,9,4]
# Additional exact rational heights and Lagrange interpolation constructions.
for r,s in ((S.Rational(1,2),S.Rational(3,2)),(1,2),(2,5),(3,4),(S.Rational(2,3),S.Rational(5,4))):
 t=r+s
 Q=S.interpolate([(r*r,0),(s*s,t),(t*t,s)],x)
 assert S.degree(Q,x)==2
 q=S.lambdify(x,Q,'sympy')
 assert S.simplify(Q.subs(x,s*s)-Q.subs(x,t*t))==r
 assert S.simplify(Q.subs(x,t*t)-Q.subs(x,r*r))==s
 assert S.simplify(Q.subs(x,r*r)-Q.subs(x,s*s))==-t
 print('pair',r,s,'polynomial',Q)
print('PASS: nilpotent Jacobian identities, two disjoint exact 3-cycles, five interpolation examples')
