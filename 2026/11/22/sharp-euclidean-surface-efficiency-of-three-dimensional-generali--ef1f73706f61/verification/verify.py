"""Reproduce the exact formulas and finite convex-hull diagnostics.

Run: python verify.py. Requires sympy, numpy, scipy.
The analytic proof of the all-dimensional statement is in RESULT.md;
finite hull tests are diagnostics, not an infinite proof.
"""
from itertools import permutations
from math import isclose, sqrt
import numpy as np
import sympy as sp
from scipy.spatial import ConvexHull

t = sp.symbols('t', nonnegative=True)
AL = (t+2)**2 - sp.Rational(1, 2)
AU = (t+1)**2 - sp.Rational(1, 2)
AP = sp.sqrt(2)*t
AT = 3*sp.sqrt(3)
S = sp.expand(3*AL+3*AU+3*AP+AT)
V = sp.expand((t+2)*AU+t*(2*t+3)+3*(t+1))
assert sp.simplify(S-(6*t**2+(18+3*sp.sqrt(2))*t+12+3*sp.sqrt(3))) == 0
assert sp.simplify(V-(t**3+6*t**2+sp.Rational(21,2)*t+4)) == 0
D = sp.expand(3*V*sp.diff(S,t)-2*S*sp.diff(V,t))
coeff = sp.Poly(D,t).all_coeffs()
assert [sp.sign(sp.N(c,40)) for c in coeff] == [1,1,-1,-1]
assert sp.N(D.subs(t,sp.Rational(252596,100000)),40)<0
assert sp.N(D.subs(t,sp.Rational(252597,100000)),40)>0
roots = [float(sp.re(r)) for r in sp.nroots(D) if abs(float(sp.im(r))) < 1e-10 and float(sp.re(r))>0]
assert len(roots)==1
star=roots[0]
Q=lambda z: float((S**3/V**2).subs(t,z).evalf(20))
assert isclose(star,2.5259646581068329,rel_tol=0,abs_tol=1e-10)
assert isclose(Q(star),193.0568124144038546,rel_tol=0,abs_tol=1e-9)
assert Q(0)>216 and Q(star)<216 and Q(10)<216
# The crossing of the equal-volume cube's normalized quotient.
F=sp.expand(S**3-216*V**2)
posroots=[float(sp.re(r)) for r in sp.nroots(F,maxsteps=100) if abs(float(sp.im(r)))<1e-10 and float(sp.re(r))>0]
assert len(posroots)==1 and isclose(posroots[0],0.629939681219772,abs_tol=1e-9)

# Independent hull geometry from the vertex orbits, not the facet area derivation.
def verts(v):
    families=[(v,v+1,v+2),(0,v+1,v+2),(0,0,v+2),(0,0,0)]
    return np.array(sorted(set(tuple(map(float,p)) for a in families for p in permutations(a))),dtype=float)

def halfspaces_hold(z,v):
    return all(x>=-1e-9 and x<=v+2+1e-9 for x in z) and all(z[i]+z[j]<=2*v+3+1e-9 for i in range(3) for j in range(i+1,3)) and sum(z)<=3*v+3+1e-9

for v in [0,0.25,0.5,1,2,3,5,8,12]:
    points=verts(v)
    assert len(points)==(10 if v==0 else 16)
    assert all(halfspaces_hold(z,v) for z in points)
    hull=ConvexHull(points)
    assert isclose(hull.volume,float(V.subs(t,v)),rel_tol=1e-10,abs_tol=1e-8),(v,hull.volume,V.subs(t,v))
    assert isclose(hull.area,float(S.subs(t,v)),rel_tol=1e-10,abs_tol=1e-8),(v,hull.area,S.subs(t,v))
print('PARKING_SURFACE_SHARP_QUOTIENT_PASS',len(roots),'positive extremum',len(posroots),'cube crossing','9 convex hulls')
