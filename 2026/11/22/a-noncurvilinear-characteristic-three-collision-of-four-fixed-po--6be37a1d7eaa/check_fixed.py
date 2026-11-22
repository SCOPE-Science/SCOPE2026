#!/usr/bin/env python3
"""Independent exact calculations for the 3-cycle on five-point moduli."""
import sympy as S
u,v=S.symbols('u v')
x,y=S.symbols('x y')
# Geometric 3-cycle (p1,p2,p3) -> (p2,p3,p1) normalized by p1=1.
x1,y1=y/x,1/x
x2,y2=S.factor(y1/x1),S.factor(1/x1)
x3,y3=S.factor(y2/x2),S.factor(1/x2)
assert S.simplify(x3-x)==0 and S.simplify(y3-y)==0
# Blow-up at (1,1): x=1+u, y=1+u*v.
U=S.factor((y/x-1).subs({x:1+u,y:1+u*v}))
V=S.factor(((1/x-1)/(y/x-1)).subs({x:1+u,y:1+u*v}))
assert S.simplify(U-u*(v-1)/(1+u))==0
assert S.simplify(V-1/(1-v))==0
F=v*v-v+1
G=u*(u+2-v)
assert S.simplify((V-v)*(1-v)-F)==0
assert S.simplify((U-u)*(1+u)+G)==0
# Degree-four free Z module: f monic in v, g monic in u.
assert S.Poly(F,v).LC()==1 and S.Poly(G,u).LC()==1
# Etale away from 3: discriminant f=-3, relative resultant of linear factors = norm(2-v)=3.
assert S.discriminant(F,v)==-3
assert S.resultant(F,2-v,v)==3
# Over char 3: v=-1+w, I=(w^2, u(u-w)); Hilbert function (1,2,1).
w=S.symbols('w')
assert S.Poly(S.expand(F.subs(v,w-1)),w,modulus=3)==S.Poly(w*w,w,modulus=3)
assert S.Poly(S.expand(G.subs(v,w-1)),u,w,modulus=3)==S.Poly(u*(u-w),u,w,modulus=3)
gb=S.groebner([w*w,u*(u-w)],u,w,order='lex', modulus=3)
for polynomial in [u**3,u*u*w,u*w*w,w**3]:
 assert gb.reduce(polynomial)[1]==0
assert gb.reduce(u*w)[1]!=0
# Local differential identity at the unique F3 fixed support point.
Jac=S.Matrix([U,V]).jacobian([u,v]); J=Jac.subs({u:0,v:-1})
assert all((int(S.Rational(t).p)*pow(int(S.Rational(t).q),-1,3))%3==int(e)%3 for t,e in zip(J,S.eye(2))), J
# second-order action is not identity in char3: u'=u+u*w-u^2+O(3)
assert S.Poly(S.expand((u*(1+w)*(1-u+u*u)-u)),u,w,modulus=3).terms()
# Check all geometric points in finite prime fields in chart. F fixed iff both equations vanish.
for p in (3,5,7,11,13,17):
 points=[(a,b) for a in range(p) for b in range(p)
         if (a*a+2*a-a*b)%p==0 and (b*b-b+1)%p==0]
 # no denominator vanishes on fixed locus
 assert all((1+a)%p and (1-b)%p for a,b in points)
 assert len(points)==(1 if p==3 else (4 if pow((-3)%p,(p-1)//2,p)==1 else 0)), (p,points)
 print('fixed geometric support over F_%d: %s'%(p,points))
print('M05_C3_INTEGRAL_FIXED_SCHEME_CHECKED degree=4 char3_Hilbert=(1,2,1) tangent=identity')
