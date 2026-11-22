#!/usr/bin/env python3
"""Exact polynomial and local-jet checks for the projective infinity calculation."""
import sympy as s
x,y,z,c,W,t,u=s.symbols('x y z c W t u')
F=(c**4-4*c**3*x*y*z+4*c**2*(x*x*y*y+x*x*z*z+y*y*z*z)
   -2*c**2*(x*x+y*y+z*z)-4*c*x*y*z*(x*x+y*y+z*z)
   +8*c*x*y*z+x**4+y**4+z**4
   -2*(x*x*y*y+x*x*z*z+y*y*z*z)+4*x*x*y*y*z*z)
P=s.Poly(F,x,y,z)
H=s.expand(sum(coeff*x**a*y**b*z**d*W**(6-a-b-d) for (a,b,d),coeff in P.terms()))
assert s.expand(H.subs(W,0)-4*x*x*y*y*z*z)==0
for v in (x,y,z,W):
 assert s.expand(s.diff(H,v).subs({x:0,W:0}))==0
q=s.expand(4*t*t*u*u-4*c*t*(1+t*t)*u*W+((1-t*t)**2+4*c*c*t*t)*W*W)
disc=s.cancel(s.discriminant(q,u)/W**2)
assert s.factor(disc-16*t*t*(c*c-1)*(1-t*t)**2)==0
# Exact vanishing of all four first derivatives on representative affine singular line.
for p in (F,s.diff(F,x),s.diff(F,y),s.diff(F,z)):
 assert s.factor(p.subs({x:c,z:y}))==0
# Projective representative of affine singular line x=cW, z=y.
for p in (H,s.diff(H,x),s.diff(H,y),s.diff(H,z),s.diff(H,W)):
 assert s.factor(p.subs({x:c*W,z:y}))==0
# The local side crossing [0:1:1:0].
E=s.Poly(s.expand(H.subs({x:c*W+u,y:1,z:1+t})),u,W,t)
def jet(deg):
 return s.expand(sum(co*u**a*W**b*t**d for (a,b,d),co in E.terms() if a+b+d==deg))
assert s.expand(jet(2)-4*u*u)==0
assert s.expand(jet(3)-8*t*u*u)==0
assert s.factor(jet(4).subs(u,0)-4*(1-c*c)*t*t*W*W)==0
# At a vertex the critical-point elimination of W has quartic residual.
V=s.Poly(s.expand(H.subs(x,1)),y,z,W)
assert s.expand(sum(co*y**a*z**b*W**d for (a,b,d),co in V.terms() if a+b+d==2)-W*W)==0
assert s.expand(sum(co*y**a*z**b*W**d for (a,b,d),co in V.terms() if a+b+d==3)+4*c*y*z*W)==0
assert s.expand(sum(co*y**a*z**b*W**d for (a,b,d),co in V.terms() if a+b+d==4).subs(W,0)-4*y*y*z*z)==0
print('exact symbolic checks: PASS')
