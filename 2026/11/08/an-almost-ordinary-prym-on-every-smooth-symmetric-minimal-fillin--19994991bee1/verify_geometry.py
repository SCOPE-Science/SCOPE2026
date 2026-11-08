"""Exact geometry of symmetric bidegree-(4,4) filling curves over F_3.
Run: python verify_geometry.py (requires sympy)."""
import itertools
import sympy as sp

p=3
X0,X1,Y0,Y1,S,T,U=sp.symbols('X0 X1 Y0 Y1 S T U')
x,y=sp.symbols('x y')
A=lambda a,b:a**4+a*b**3+2*b**4
E=lambda a,b:a**3*b-a*b**3
F=sp.expand(A(Y0,Y1)*E(X0,X1)+A(X0,X1)*E(Y0,Y1))
G=2*S**3*U-S**3*T+S**2*T*U+S*U**3+S*T**3+T*U**3+T**2*U**2

assert all(int(c)%3==0 for c in sp.Poly(sp.expand(G.subs({S:X0*Y1+X1*Y0,T:X0*Y0,U:X1*Y1})-F),X0,X1,Y0,Y1).coeffs())

def unit_ideal(f,vs):
    gb=sp.groebner([f]+[sp.diff(f,v) for v in vs],*vs,modulus=p)
    return len(gb.polys)==1 and gb.polys[0].total_degree()==0

for i,j in itertools.product((0,1),repeat=2):
    substitution={X0:1,X1:x} if i==0 else {X0:x,X1:1}
    substitution.update({Y0:1,Y1:y} if j==0 else {Y0:y,Y1:1})
    f=sp.expand(F.subs(substitution))
    assert unit_ideal(f,(x,y)),(i,j)
print('CURVE_SMOOTH_ALL_FOUR_CHARTS_PASS')

for k,t in enumerate((S,T,U)):
    other=[w for w in (S,T,U) if w!=t]
    g=sp.expand(G.subs({t:1}))
    assert unit_ideal(g,other),k
print('QUARTIC_QUOTIENT_SMOOTH_ALL_THREE_CHARTS_PASS')

z=sp.symbols('z')
a=sp.Poly(z**4+z+2,z,modulus=p)
e=sp.Poly(z-z**3,z,modulus=p)
assert sp.gcd(a,a.diff()).degree()==0 and sp.gcd(a,e).degree()==0
assert all(a.eval(t)%p for t in (0,1,2))
# E vanishes at 0, 1, -1 and at infinity; A is nonzero at infinity.
assert A(1,0)%3!=0
print('EIGHT_DISTINCT_RAMIFICATION_POINTS_PASS')

# A projective quartic has 5 coefficients. Normalize first nonzero to 1;
# smoothness check includes all four affine charts and is exhaustive.
def forms(a,t,chart):
    return sum(a[i]*t**(i if chart==0 else 4-i) for i in range(5))
def eqq(a,chart1,chart2):
    e1=x-x**3 if chart1==0 else x**3-x
    e2=y-y**3 if chart2==0 else y**3-y
    return sp.expand(forms(a,y,chart2)*e1+forms(a,x,chart1)*e2)

def no_rational_zero(a):
    return a[0]!=0 and a[4]!=0 and all(sum(a[i]*t**i for i in range(5))%3 for t in (1,2))

rootfree=[]; smooth=[]
for aa in itertools.product(range(3),repeat=5):
    if not no_rational_zero(aa):continue
    if next(t for t in aa if t)!=1:continue
    rootfree.append(aa)
    if all(unit_ideal(eqq(aa,i,j),(x,y)) for i,j in itertools.product((0,1),repeat=2)):
        smooth.append(aa)
assert len(rootfree)==24
expected={(1,0,0,1,2),(1,0,0,2,2),(1,1,0,0,2),(1,1,0,2,1),(1,2,0,0,2),(1,2,0,1,1)}
assert set(smooth)==expected

matrices=[]
for aa,bb,cc,dd in itertools.product(range(3),repeat=4):
    if (aa*dd-bb*cc)%3:
        matrix=(aa,bb,cc,dd)
        if tuple(2*v%3 for v in matrix) not in matrices: matrices.append(matrix)
assert len(matrices)==24

def transform(a,m):
    aa,bb,cc,dd=m
    h=sp.Poly(sum(a[i]*(aa*x+bb*y)**(4-i)*(cc*x+dd*y)**i for i in range(5)),x,y)
    v=tuple(int(h.coeff_monomial(x**(4-i)*y**i))%3 for i in range(5))
    z=next(w for w in v if w)
    return tuple(z*w%3 for w in v) # z^{-1}=z for F_3^*

orbit={transform((1,0,0,1,2),m) for m in matrices}
assert orbit==expected
print('SYMMETRIC_SMOOTH_QUARTIC_CENSUS_PASS 24 6 1_ORBIT')
# All sixteen rational pairs lie on every symmetric equation since E=0 there.
assert all(E(a,b)%3==0 for a,b in ((1,0),(0,1),(1,1),(1,2)))
print('SIXTEEN_RATIONAL_POINTS_FILLING_PASS')
