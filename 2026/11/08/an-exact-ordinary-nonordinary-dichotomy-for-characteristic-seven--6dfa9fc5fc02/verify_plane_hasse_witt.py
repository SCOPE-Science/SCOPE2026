import sympy as S
from math import factorial
from itertools import product
x,a,b=S.symbols('x a b')
F=[((0,3,1),1),((4,0,0),-1),((2,0,2),-a),((1,0,3),-b),((0,0,4),-1)]
T=[]
for c0 in range(7):
 for c1 in range(7-c0):
  for c2 in range(7-c0-c1):
   for c3 in range(7-c0-c1-c2):
    c4=6-c0-c1-c2-c3;z=[c0,c1,c2,c3,c4];
    ex=tuple(sum(F[t][0][j]*z[t] for t in range(5)) for j in range(3))
    co=S.Integer(factorial(6));
    for k in z:co//=factorial(k)
    co*=S.prod(F[t][1]**z[t] for t in range(5))
    T.append((ex,co))
D={}
for ex,co in T:D[ex]=D.get(ex,0)+co
v=[(2,1,1),(1,2,1),(1,1,2)]
H=[]
for e in v:
 row=[]
 for f in v:
  ex=tuple(7*e[i]-f[i] for i in range(3))
  pol=S.Poly(S.expand(D.get(ex,0)),a,b,modulus=7).as_expr();row.append(pol)
 H.append(row)
print('H frobenius plane quartic')
for row in H:print(row)
print('det:',S.Poly(S.det(S.Matrix(H)),a,b,modulus=7).as_expr())
Hmat = S.Matrix(H)
expected = S.Matrix([[-a**2-3,0,-3*b],
                     [0,2*a,0],
                     [-2*a**2*b-3*a*b**3-2*b,0,-3*a**3-a**2*b**2-2*a-2*b**2]])
assert all(S.Poly(Hmat[i,j]-expected[i,j],a,b,modulus=7).is_zero
           for i in range(3) for j in range(3))
disc=2*a**4+3*a**3*b**2-2*a**2-3*a*b**2+b**4-3
assert S.Poly(S.det(Hmat)-3*a**2*disc,a,b,modulus=7).is_zero
R=Hmat.subs(a,0)
assert R == S.Matrix([[-3,0,-3*b],[0,0,0],[-2*b,0,-2*b**2]])
R7=R.applyfunc(lambda x:x.subs(b,b**7))
assert all(S.Poly((R*R7)[i,j],b,modulus=7).as_expr()==
           S.Poly(((2*b**8+3)*S.Matrix([[3,0,3*b**7],[0,0,0],[2*b,0,2*b**8]]))[i,j],b,modulus=7).as_expr()
           for i in range(3) for j in range(3))
print('PICARD7_PLANE_FROBENIUS_PASS det=3*a^2*discriminant; rank1 boundary and square criterion')
Rt=R.T
Rt7=Rt.applyfunc(lambda x:x.subs(b,b**7))
# Directly test the transpose's nonzero (X,Z)-block factor.
block=Rt.extract([0,2],[0,2]); block7=block.applyfunc(lambda x:x.subs(b,b**7))
factor=2*b**8+3
assert all(S.rem(S.Poly((block*block7)[i,j],b,modulus=7),
                 S.Poly(factor,b,modulus=7)).is_zero
           for i in range(2) for j in range(2))
