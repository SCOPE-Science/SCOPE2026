import sympy as sp

a,b,c,x,y,z = sp.symbols('a b c x y z', nonzero=True)
Fx = a*(y-x)
Fy = x*(c-z)
Fz = x*y-b*z

def L(f):
    return sp.expand(sp.diff(f,x)*Fx + sp.diff(f,y)*Fy + sp.diff(f,z)*Fz)

checks = {
    'L_x2_2': (L(x**2/2), a*(x*y-x**2)),
    'L_z': (L(z), x*y-b*z),
    'L_y2_2': (L(y**2/2), c*x*y-x*y*z),
    'L_z2_2': (L(z**2/2), x*y*z-b*z**2),
}
for name,(lhs,rhs) in checks.items():
    assert sp.simplify(lhs-rhs)==0, (name,lhs,rhs)

# Stationary identities: <xy>=<x^2>, <xy>=b<z>,
# c<xy>=<xyz>, <xyz>=b<z^2>.
X2, XY, Z1, XYZ, Z2 = sp.symbols('X2 XY Z1 XYZ Z2')
rels = [sp.Eq(XY,X2), sp.Eq(XY,b*Z1), sp.Eq(XYZ,c*XY), sp.Eq(XYZ,b*Z2)]
sol = sp.solve([r.lhs-r.rhs for r in rels], [XY,X2,XYZ,Z2], dict=True)
assert sol
s=sol[0]
assert sp.simplify(s[X2]-b*Z1)==0
assert sp.simplify(s[Z2]-c*Z1)==0
var = sp.expand(s[Z2]-Z1**2)
assert sp.factor(var-Z1*(c-Z1))==0

# Equilibria for a,b,c>0.
# Solve algebraically under x'=y'=z'=0: y=x; x(c-z)=0; x*y=b*z.
# Branch x=0 gives origin; x!=0 gives z=c and x^2=bc.
assert sp.simplify(Fx.subs({y:x}))==0
assert sp.simplify(Fy.subs({z:c}))==0
assert sp.simplify(Fz.subs({y:x,z:c})-(x**2-b*c))==0

print('VERIFY_OK')
