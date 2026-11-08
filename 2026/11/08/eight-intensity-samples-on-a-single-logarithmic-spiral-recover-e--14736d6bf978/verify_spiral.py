"""Exact eight-sample certificate for quadratic polynomial intensity phase retrieval."""
import sympy as sp
I = sp.I
z = [sp.expand((1+I)**j) for j in range(8)]

def row(v):
    q = sp.expand(v*sp.conjugate(v))
    return [sp.Integer(1), q, sp.expand(q*q),
            2*sp.re(v), -2*sp.im(v),
            2*sp.re(sp.expand(v**2)), -2*sp.im(sp.expand(v**2)),
            2*q*sp.re(v), -2*q*sp.im(v)]
M = sp.Matrix([row(v) for v in z])
assert M.rank()==8
u = sp.Matrix([256, -150, 2, -48, -96, 3, 3, -9, 3])
assert M*u == sp.zeros(8,1)
d0,d1,d2,a,b,c,d,e,f = list(u)
H=sp.Matrix([[d0,a+I*b,c+I*d], [a-I*b,d1,e+I*f], [c-I*d,e-I*f,d2]])
assert H.det()==-111540
for zz in z:
    v=sp.Matrix([1,zz,zz**2])
    assert sp.simplify((sp.conjugate(v).T*H*v)[0])==0
assert M[:,0:8].det()!=0
print('EIGHT_SPIRAL_PASS rank=8 determinant_H=-111540 minor=',M[:,0:8].det())
