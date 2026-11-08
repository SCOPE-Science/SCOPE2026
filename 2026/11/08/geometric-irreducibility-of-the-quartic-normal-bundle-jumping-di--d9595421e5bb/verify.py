"""Reproducible exact computations for the quartic normal-bundle jump divisor.
Requires Python 3 and SymPy 1.14. No remote services or external data.
"""
import random
import sympy as S

A,B,C=S.symbols('A B C')
x,y,z=S.symbols('x y z')
p=101

def toe(coeff,rows,cols):
    e=cols-rows
    assert len(coeff)==e+1
    return S.Matrix(rows,cols,lambda i,j: coeff[j-i] if 0<=j-i<=e else 0)

def block(poly,sign=1):
    deg=len(poly)-1
    m=6-deg
    fs=[(deg-j)*poly[j] for j in range(deg)]
    ft=[(j+1)*poly[j+1] for j in range(deg)]
    return toe([sign*t for t in poly],m,6).row_join(toe(fs,m,5)).row_join(toe(ft,m,5))

def theta(u0,u1,v2,v3,w):
    def ublock(poly):
        T=block(poly)
        T[:,0:6]=S.zeros(2,6)
        return T
    M=ublock(u0).col_join(ublock(u1))
    for poly,sign in ((v2,1),(v3,1),(w,-1)):
        M=M.col_join(block(poly,sign))
    assert M.shape==(16,16)
    return M

# Nonvanishing witnesses on the normalized degree-two target pencil.
va=(1,0,0); vb=(0,0,1); w=(A,B,C)
P1=S.factor(theta((1,0,0,0,0),(0,0,0,0,1),va,vb,w).det())
P2=S.factor(theta((0,1,0,0,0),(0,0,0,1,0),va,vb,w).det())
P3=S.factor(theta((1,0,0,0,1),(0,1,0,1,0),va,vb,w).det())
assert S.expand(P1-16384*B**2*(A*C-B**2))==0
assert S.expand(P2+16384*A**2*C**2)==0
assert S.expand(P3+16384*(A**4 + A**2*B**2+2*A**2*C**2-2*A*B**2*C+B**2*C**2+C**4))==0
# Common affine zero set is only A=B=C=0, via the stated elementary case split.
assert P3.subs({A:1,B:0,C:0})==-16384
assert P3.subs({A:0,B:0,C:1})==-16384
print('VERTICAL_WITNESSES_OK')

# A concrete ternary plane section through the ten quartic coefficients.
v2=(1,0,1);v3=(1,1,0);w=(1,2,3)
random.seed(19)
lin=[sum(random.randrange(101)*v for v in (x,y,z)) for j in range(10)]
expected_lin=[(86,5,100),(66,15,65),(25,50,44),(67,37,74),(18,76,33),
              (13,33,52),(41,34,13),(98,41,39),(2,72,79),(25,9,25)]
assert [tuple(int(e.coeff(v)) for v in (x,y,z)) for e in lin]==expected_lin
F=(x**4-19*x**3*y-17*x**3*z+10*x**2*y**2+8*x**2*y*z+38*x**2*z**2
    -22*x*y**3-12*x*y**2*z-35*x*y*z**2-27*x*z**3-22*y**4+39*y**3*z
    +45*y**2*z**2+32*y*z**3-24*z**4)
# Both sides are ternary forms of degree four, and 15 triangular-grid values are unisolvent.
for i in range(5):
    for j in range(5-i):
        pt={x:1,y:i,z:j}
        lu=[int(t.subs(pt)) for t in lin]
        dm=int(theta(lu[:5],lu[5:],v2,v3,w).det(method='domain-ge'))%p
        fp=int(47*F.subs(pt))%p
        assert dm==fp,(i,j,dm,fp)
print('TERNARY_SECTION_IDENTITY_OK')
# Verify the entire geometric singular scheme of the quartic modulo 101.
grad=[S.diff(F,v) for v in (x,y,z)]
G=S.groebner([q.subs(x,1) for q in grad],y,z,modulus=p)
expected=[y+41*z*z+33*z+40,z**3+25*z*z-48*z+15]
assert len(G.polys)==2
assert all(S.Poly(e-q.as_expr(),y,z,modulus=p).is_zero for q,e in zip(G.polys,expected))
for fixed,other in ((y,z),(z,y)):
    h=S.groebner([q.subs({x:0,fixed:1}) for q in grad],other,modulus=p)
    assert len(h.polys)==1 and h.polys[0].as_expr()==1
cubic=S.Poly(expected[1],z,modulus=p)
assert S.gcd(cubic,cubic.diff()).degree()==0
Y=-(41*z*z+33*z+40)
H=S.diff(F.subs(x,1),y,2)*S.diff(F.subs(x,1),z,2)-S.diff(F.subs(x,1),y,z)**2
hess=S.Poly(S.rem(H.subs(y,Y),cubic.as_expr(),z),z,modulus=p)
assert S.gcd(hess,cubic).degree()==0
# The singular points are [1:Y(z):z] and not collinear: 1,Y,z independent mod cubic.
coeffs=S.Matrix([[1,0,0],[-40,-33,-41],[0,1,0]])
assert coeffs.det()%p==41
print('THREE_DISTINCT_NONCOLLINEAR_NODES_OK')
print('CERTIFICATE_OK')
