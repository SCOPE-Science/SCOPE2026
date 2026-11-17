"""Exact identities and example checks for an axially symmetric quadratic map.
Runs using Python 3 and SymPy, without data files or network access.
"""
import sympy as s

v1,v2,v3,a,b=s.symbols('v1 v2 v3 a b',real=True)
c=1-v1
d=1+v3
e=1-v3
z=-(a*a+v3*b*b)/(1-v3*v3)
w=-(b*b+v3*a*a)/(1-v3*v3)
assert s.factor(w-v3*z+b*b)==0
assert s.factor(z-v3*w+a*a)==0
res1=c*a-b*(v2+z)
res2=c*b-a*(v2+w)
assert s.simplify(a*res1-b*res2-(a*a-b*b)*(c+a*b/d))==0
print('SYMBOLIC_BRANCH_IDENTITY_OK')

# Coordinates and reconstruction of the antisymmetric orbit.
r=e*(c+v2)
z_anti=-(c+v2)
A=s.symbols('A',real=True)
assert s.factor(res1.subs({a:A,b:-A}).subs(A**2,r))==0
assert s.factor(res2.subs({a:A,b:-A}).subs(A**2,r))==0
assert s.simplify((c+v2)-r/e)==0
assert s.simplify(z_anti+r/e)==0
print('ANTISYMMETRIC_BRANCH_OK')

S=(1-v3*v3)*v2/v3
P=-c*d
V2crit=2*c*v3/e
assert s.factor(S.subs(v2,V2crit)-2*c*d)==0
assert s.simplify(S+2*P-(1-v3*v3)/v3*(v2-V2crit))==0
assert s.factor(V2crit-c-c*(3*v3-1)/e)==0
print('SYMMETRY_BREAK_THRESHOLD_OK')

# An exact rational witness for the 3-cycle regime (one anticycle + two reflected nonanticycles).
params={v1:s.Rational(1,2),v3:s.Rational(1,2),v2:s.Rational(25,24)}
for A0,B0 in [(s.Rational(1),s.Rational(-3,4)),(-s.Rational(1),s.Rational(3,4))]:
 Z=s.simplify(z.subs(params).subs({a:A0,b:B0}))
 W=s.simplify(w.subs(params).subs({a:A0,b:B0}))
 def f(x,y,z0):return (y,params[v1]*x+params[v2]*y+y*z0,params[v3]*z0-y*y)
 X=(A0,B0,Z)
 Y=f(*X)
 assert Y==(B0,A0,W),(Y,B0,A0,W)
 assert f(*Y)==X
 assert X!=Y
print('RATIONAL_THREE_ORBIT_WITNESS_OK')

# A second exact witness, with three distinct primitive two-cycles but only one fixed point.
params2={v1:s.Rational(-1,2),v3:s.Rational(1,4),v2:s.Rational(61,60)}
assert s.simplify(V2crit.subs(params2))==1
assert params2[v2]<1-params2[v1]
for A0,B0 in [(s.Rational(3,2),-s.Rational(5,4)),(-s.Rational(3,2),s.Rational(5,4))]:
 Z=s.simplify(z.subs(params2).subs({a:A0,b:B0}))
 W=s.simplify(w.subs(params2).subs({a:A0,b:B0}))
 def f2(x,y,z0):return (y,params2[v1]*x+params2[v2]*y+y*z0,params2[v3]*z0-y*y)
 X=(A0,B0,Z)
 Y=f2(*X)
 assert Y==(B0,A0,W)
 assert f2(*Y)==X and X!=Y
print('THREE_CYCLES_ONE_FIXED_POINT_WITNESS_OK')

# Algebraic sample at the strict threshold; the only new parameter roots are duplicate anticycle points.
assert V2crit.subs(params)==1
At=s.sqrt(s.Rational(3,4));Zt=s.Rational(-3,2)
def f_boundary(x,y,z0):return (y,s.Rational(1,2)*x+y+y*z0,s.Rational(1,2)*z0-y*y)
X=(At,-At,Zt);assert f_boundary(*f_boundary(*X))==X
print('EXACT_THRESHOLD_COLLISION_OK')

# Check fixed points: a=b, z=w=-a^2/(1-v3), with a^2=e*(v2-c).
assert s.factor(s.simplify(res1.subs(b,a).subs(v2,c+a*a/e)))==0
print('FIXED_POINT_BRANCH_OK')
print('ALL_CHECKS_PASSED')
