"""Exact symbolic checks for the characteristic-two 3x2x2 resultant singularity."""
import sympy as s
from itertools import combinations

a,b,c,d,x,y=s.symbols('a b c d x y')
N=s.Matrix([[-a,1,-(1+c),0],[-b,0,-d,1],[y,0,-x,0]])
mins=[]
for j in range(4):
    cols=[i for i in range(4) if i!=j]
    mins.append((-1)**j*N[:,cols].det())
p=s.Matrix(mins)
assert all(s.expand(v)==0 for v in N*p)
Q=lambda z:z[0]*z[3]-z[1]*z[2]
h=s.expand(Q(p))
expect=b*x*x+(d-a)*x*y-(1+c)*y*y
assert s.expand(h-expect)==0
# Jacobian in characteristic 2 as a monomial presentation.
partials=[s.diff(h,z) for z in [a,b,c,d,x,y]]
assert s.expand(partials[0]+x*y)==0
assert s.expand(partials[1]-x*x)==0
assert s.expand(partials[2]+y*y)==0
assert s.expand(partials[3]-x*y)==0
# characteristic-two derivatives reduce to (d-a)*y, (d-a)*x
assert s.Poly(partials[4]-(d-a)*y,x,y,a,b,c,d,modulus=2).is_zero
assert s.Poly(partials[5]-(d-a)*x,x,y,a,b,c,d,modulus=2).is_zero
# characteristic-two local Jacobian: (x^2, xy, y^2, (d-a)x, (d-a)y).
# at d=a these reduce to (x,y)^2, with vector basis 1,x,y.
G2=s.groebner([x*x,x*y,y*y], x,y,modulus=2)
assert not G2.reduce(s.Integer(1))[1] == 0
assert all(G2.reduce(z)[1]!=0 for z in [x,y])
assert all(G2.reduce(z)[1]==0 for z in [x*x,x*y,y*y])
# in odd characteristic at a=b=c=d=0, H=-y^2;
# derivatives span (x^2,y), yielding length two with basis 1,x.
local_odd=[s.expand(p.subs({a:0,b:0,c:0,d:0})) for p in partials]
Godd=s.groebner(local_odd,x,y)
assert Godd.reduce(x*x)[1]==0 and Godd.reduce(y)[1]==0
assert Godd.reduce(x)[1] !=0
# generic transversal: d-a is a unit, so x=y=0 reduced.
print('LOCAL_MINOR_IDENTITY=PASS')
print('CHAR2_JACOBIAN_IDEAL=PASS')
print('TANGENT_FIBER_LENGTH_3_IN_CHAR2=PASS')
print('TANGENT_FIBER_LENGTH_2_IN_ODD_CHAR=PASS')
print('ALL_CHECKS_PASSED')
