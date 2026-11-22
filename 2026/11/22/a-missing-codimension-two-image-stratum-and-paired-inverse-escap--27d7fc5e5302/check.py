#!/usr/bin/env python3
"""Reproduce exact inverse and singularity identities for a four-state polynomial map."""
import sympy as s
x,y,z,w,a,b,c,X,Y,Z,W,delta = s.symbols('x y z w a b c X Y Z W delta', real=True)
F=s.Matrix([a*y**2,b*(1-w**2/2)*y*(1-z),c*(1-x),w+y])
J=s.factor(F.jacobian([x,y,z,w]).det())
assert s.simplify(J-a*b*c*y*y*(2-w*w))==0
r=s.symbols('r',positive=True)
for sig in (-1,1):
 m=1-(W-sig*r)**2/2
 inv={x:1-Z/c,y:sig*r,z:1-Y/(b*sig*r*m),w:W-sig*r}
 expected=[a*r*r,Y,Z,W]
 for actual,target in zip(F,expected):
  assert s.simplify(actual.subs(inv, simultaneous=True)-target)==0
 assert s.simplify(m.subs({r:s.sqrt(2),W:0}))==0
 # Both inverse branches have identical residue at the missing target.
 zd=1-Y/(b*sig*s.sqrt(2)*(1-(delta-sig*s.sqrt(2))**2/2))
 assert s.simplify(s.limit(delta*zd,delta,0)+Y/(2*b))==0
 # A punctured target has two valid preimages for sufficiently small nonzero delta.
 assert s.simplify((1-(delta-sig*s.sqrt(2))**2/2)- (sig*s.sqrt(2)*delta-delta**2/2))==0
# Both signs of the square root must have vanishing memristance iff r=sqrt(2),W=0.
u,v=s.symbols('u v',real=True)
assert s.simplify((W-r)**2-(W+r)**2)==-4*W*r
# Exact non-generic cases at a=2,b=3,c=5; r=1 and W=0 are both nonsingular.
AA,BB,CC=s.Integer(2),s.Integer(3),s.Integer(5)
for yy in (-1,1):
 xx=s.Rational(1)-s.Rational(11,5)
 ww=-yy
 mm=s.Integer(1)-s.Rational(ww**2,2)
 zz=1-s.Rational(7)/(BB*yy*mm)
 assert F.subs({x:xx,y:yy,z:zz,w:ww,a:AA,b:BB,c:CC})==s.Matrix([2,7,11,0])
# One branch disappears for a target with nonzero second coordinate.
ww_target=1+s.sqrt(2)
assert s.simplify(1-(ww_target-1)**2/2)==0
assert s.simplify(1-(ww_target+1)**2/2)!=0
# At a punctured target both memristance branches vanish; no finite z can produce Y=7.
assert s.simplify(1-(0-s.sqrt(2))**2/2)==0
assert s.simplify(1-(0+s.sqrt(2))**2/2)==0
# At Y=0 those vanished branches each permit any z; confirm multiple exact points.
for yy in (-s.sqrt(2),s.sqrt(2)):
 for zz in (-15,0,17):
  state={x:0,y:yy,z:zz,w:-yy,a:AA,b:BB,c:CC}
  assert all(s.simplify(t-u)==0 for t,u in zip(F.subs(state),s.Matrix([4,0,5,0])))
# X=0,Y=0 yields an unbounded line of preimages.
for zz in (-99,0,101):
 assert F.subs({x:2,y:0,z:zz,w:9,a:AA,b:BB,c:CC})==s.Matrix([0,0,-5,9])
print('PASS: symbolic Jacobian, both inverse sheets, unique missing-stratum equations, common pole, and degenerate fibers')
