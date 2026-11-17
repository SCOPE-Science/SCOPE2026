#!/usr/bin/env python3
"""Standalone exact checks for a two-coset planar Voronoi profile.
Requires Python 3 and SymPy. Not an exhaustive substitute for the proof.
"""
import sympy as S

t = S.symbols('t', real=True)
u = S.symbols('u', real=True, nonnegative=True)
verts = [(-1,-t*t/2),(t,-1+t*t/2),(1,-t*t/2),
         (1,t*t/2),(t,1-t*t/2),(-1,t*t/2)]
D = 0
J = 0
for j, (x,y) in enumerate(verts):
    xx, yy = verts[(j+1) % len(verts)]
    det = S.expand(x*yy-xx*y)
    D += det
    J += det*(x*x+x*xx+xx*xx+y*y+y*yy+yy*yy)
assert S.simplify(D/2 - 2) == 0
assert S.simplify((J/12)/(D/2) - (4+2*t*t-t**4)/12) == 0
for x,y in verts:
    assert S.simplify(x*x+y*y-(1+t**4/4))==0

# Check halfspaces against exact rational samples, including farther sites.
for z in [S.Rational(1,6),S.Rational(1,3),S.Rational(1,2),S.Rational(3,4)]:
    V = [(S.factor(x.subs(t,z)) if isinstance(x,S.Basic) else S.Rational(x),
          S.factor(y.subs(t,z)) if isinstance(y,S.Basic) else S.Rational(y)) for x,y in verts]
    for x,y in V:
        R2=x*x+y*y
        for k in range(-3,4):
            for l in range(-3,4):
                for sx,sy in ((2*k,2*l),(2*k+1+z,2*l+1)):
                    if sx==sy==0: continue
                    assert S.simplify((x-sx)**2+(y-sy)**2-R2)>=0

w = S.sqrt(u*u+4)
q = S.sqrt(2*(u+2+w))
f = u+q-4*u/q
P = 2*f
# Verify radical identity against the geometrically computed perimeter.
a = S.sqrt((t-1)**2+1); b = S.sqrt((t+1)**2+1)
for z in [S.Rational(0),S.Rational(1,4),S.Rational(1,2),S.Rational(3,4),S.Rational(1)]:
    formula = 2*z*z+2*((1+z)*a.subs(t,z)+(1-z)*b.subs(t,z))
    radical = P.subs(u,z*z)
    assert abs(float(formula-radical))<1e-12

assert S.simplify(S.diff(f,u).subs(u,0)-(1-3*S.sqrt(2)/4))==0
assert abs(float(S.diff(f,u).subs(u,1)-(3-S.sqrt(5))/2))<1e-13
u_star = S.nsolve(S.diff(f,u), (S.Rational(1,10),S.Rational(1,5)), prec=45)
assert S.Rational(12475,100000) < u_star < S.Rational(12476,100000)
assert abs(float(S.sqrt(u_star))-.3532048086279578)<1e-12
assert float(P.subs(u,u_star)) < float(P.subs(u,0))
assert float(P.subs(u,u_star)) < float(P.subs(u,1))
# The global proof uses q''>0 and 0<u q'/q<1 on [0,1],
# which are established by rational interval bounds in RESULT.md.
print('STAGGERED_VORONOI_TRADEOFF_CHECKS_OK')
