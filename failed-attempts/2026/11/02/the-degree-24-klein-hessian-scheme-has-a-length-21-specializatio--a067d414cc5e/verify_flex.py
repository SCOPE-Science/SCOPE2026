#!/usr/bin/env python3
"""Exact integer and characteristic-seven Klein-flex intersection checks.

Run: python3 verify_flex.py
Requires SymPy. Algebraic-geometric Bezout/flatness implications
are proved in RESULT.md and are not inferred from finite samples.
"""
import sympy as sp
X,Y,Z=sp.symbols('X Y Z')
F=X**3*Y+Y**3*Z+Z**3*X
h=X**5*Z-5*X**2*Y**2*Z**2+X*Y**5+Y*Z**5
assert sp.expand(sp.hessian(F,(X,Y,Z)).det()+54*h)==0
# Nonzero in F_7[Y], so there is no common curve component in X!=0.
f=sp.expand(F.subs(X,1))
g=sp.expand(h.subs(X,1))
res=sp.Poly(sp.resultant(f,g,Z),Y,modulus=7)
assert res==sp.Poly(-Y*(Y-2)**21,Y,modulus=7)
# At Y=2, the gcd has only Z=4, even though the F polynomial
# itself has a second root. At Y=0, the only common root is Z=0.
for yy,root in [(0,0),(2,4)]:
 P=sp.Poly(f.subs(Y,yy),Z,modulus=7)
 Q=sp.Poly(g.subs(Y,yy),Z,modulus=7)
 gg=sp.gcd(P,Q)
 assert sp.factor(gg.monic().as_expr()-sp.Poly(Z-root,Z,modulus=7).monic().as_expr())==0 or (yy==2 and gg.degree()>1)
 # regardless of multiplicity, the gcd has no root except the named one
 assert gg.monic()==sp.Poly((Z-root)**gg.degree(),Z,modulus=7).monic()
# In X=0, only two coordinate vertices lie on F; both lie on h.
assert sp.expand(F.subs(X,0))==Y**3*Z
assert sp.expand(h.subs(X,0))==Y*Z**5
# All three coordinate vertices are transverse intersection points.
for pp in [(1,0,0),(0,1,0),(0,0,1)]:
 assert F.subs(dict(zip((X,Y,Z),pp)))==0 and h.subs(dict(zip((X,Y,Z),pp)))==0
 M=sp.Matrix([[sp.diff(P,V).subs(dict(zip((X,Y,Z),pp))) for V in (X,Y,Z)] for P in (F,h)])
 assert M.rank()==2
# Unique singular point on the curve in characteristic 7:
P=(1,2,4)
assert all(int(S.subs(dict(zip((X,Y,Z),P))))%7==0 for S in (F,sp.diff(F,X),sp.diff(F,Y),sp.diff(F,Z),h))
# Distinct support: three transverse coordinate points + P.
# Bezout degrees 4*6=24, so local length at P is 21.
print('KLEIN_FLEX_MOD7_21_AT_SINGULARITY_PLUS_3_SIMPLE_OK')
