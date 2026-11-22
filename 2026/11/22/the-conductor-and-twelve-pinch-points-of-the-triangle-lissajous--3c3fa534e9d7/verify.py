"""Exact symbolic checks for the shifted triangle Lissajous sextic.

Run with Python 3 and SymPy: python verify.py
"""
import sympy as S
x,y,z=S.symbols('x y z')
s2=1-y*y; t2=1-z*z
F=x**4+y**4+z**4-2*(x*x*y*y+x*x*z*z+y*y*z*z)+4*x*x*y*y*z*z
basis=[(0,0),(1,0),(0,1),(1,1)]
def mul(p,q):
    out=[0]*4
    for i,(a,b) in enumerate(basis):
        for j,(c,d) in enumerate(basis):
            e=a+c;f=b+d
            out[basis.index((e%2,f%2))]+=p[i]*q[j]*s2**(e//2)*t2**(f//2)
    return S.Matrix([S.expand(v) for v in out])
one=S.Matrix([1,0,0,0]);s=S.Matrix([0,1,0,0]);t=S.Matrix([0,0,1,0]);st=S.Matrix([0,0,0,1])
X=z*s+y*t
X2=mul(X,X);X3=mul(X2,X);X4=mul(X3,X)
C=y*y+z*z-2*y*y*z*z
assert S.simplify(X2[0]-C)==0
assert S.simplify(X2[3]-2*y*z)==0
assert all(S.expand(k)==0 for k in X4+F.subs(x,0)*one+(-2*C)*X2)  # F(X)=0
M=S.Matrix.hstack(one,X,X2,X3)
assert S.factor(M.det())==4*y*y*z*z*(y-z)*(y+z)
Q=M.inv()
for r,target in [(one,2*y*z*x),(s,y*(x*x-y*y+z*z)),(t,z*(x*x+y*y-z*z)),(st,x*(x*x-y*y-z*z+2*y*y*z*z))]:
    coeff=Q*mul(y*z*X,r)*2
    asserted=S.Poly(S.expand(target),x)
    have=S.Poly(sum(S.cancel(a)*x**i for i,a in enumerate(coeff)),x)
    assert S.simplify(have.as_expr()-asserted.as_expr())==0
# The six singular lines are respectively y=0,x=+-z;
# z=0,x=+-y; x=0,y=+-z.
partials=[S.diff(F,v) for v in (x,y,z)]
for i,(a,b,c) in enumerate(((z,0,z),(-z,0,z),(y,y,0),(-y,y,0),(0,z,z),(0,-z,z))):
    assert S.expand(F.subs({x:a,y:b,z:c},simultaneous=True))==0
    for f in partials: assert S.expand(f.subs({x:a,y:b,z:c},simultaneous=True))==0
# The origin has four distinct linear tangent factors.
tangent=S.expand(F-4*x*x*y*y*z*z)
assert S.expand(tangent-(x-y-z)*(x-y+z)*(x+y-z)*(x+y+z))==0
# The 12 pinch points lie on the singular locus.
import itertools
pinches=set()
for axis in range(3):
    for a,b in itertools.product((-1,1),repeat=2):
        p=[a,b];p.insert(axis,0)
        pinches.add(tuple(p))
assert len(pinches)==12
for p in pinches:
    subs=dict(zip((x,y,z),p))
    assert F.subs(subs)==0 and all(f.subs(subs)==0 for f in partials)
print('PASS: F, quartic basis, conductor, six singular lines, fourfold tangent cone, twelve pinch points')
