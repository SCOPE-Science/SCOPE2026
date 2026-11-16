"""Exact symbolic verification of the cubic harmonic concentration operator on a quarter-lune."""
from functools import lru_cache
import sympy as sp
x,y,z=sp.symbols('x y z')
P=[z*(5*z*z-3), z*(x*x-y*y), 2*x*y*z, x*(5*z*z-1), y*(5*z*z-1), x*(x*x-3*y*y), y*(3*x*x-y*y)]
@lru_cache(None)
def lune_moment(a,b,c):
    if c % 2: return sp.Integer(0)
    return sp.gamma(sp.Rational(a+1,2))*sp.gamma(sp.Rational(b+1,2))*sp.gamma(sp.Rational(c+1,2))/(2*sp.gamma(sp.Rational(a+b+c+3,2)))
def sphere_moment(a,b,c):
    if a%2 or b%2 or c%2:return sp.Integer(0)
    return 4*lune_moment(a,b,c)
def integrate(f,fun):
    return sum(v*fun(*mon) for mon,v in sp.Poly(sp.expand(f),x,y,z).terms())
L=sp.Matrix(7,7,lambda i,j:sp.expand(integrate(P[i]*P[j],lune_moment)))
B=sp.Matrix(7,7,lambda i,j:sp.expand(integrate(P[i]*P[j],sphere_moment)))
assert B == sp.diag(*B.diagonal())
assert list(B.diagonal()) == [16*sp.pi/7,16*sp.pi/105,16*sp.pi/105,32*sp.pi/21,32*sp.pi/21,32*sp.pi/35,32*sp.pi/35]
Q=sp.diag(*[1/sp.sqrt(B[j,j]) for j in range(7)])
C=sp.simplify(Q*L*Q)
T=sp.Rational(1,4)*sp.eye(7)
T[0,2]=T[2,0]=-sp.sqrt(15)/(10*sp.pi)
T[3,4]=T[4,3]=1/(2*sp.pi)
T[3,6]=T[6,3]=-sp.sqrt(15)/(30*sp.pi)
T[4,5]=T[5,4]=sp.sqrt(15)/(30*sp.pi)
T[5,6]=T[6,5]=1/(6*sp.pi)
assert C==T,(C-T)
a=(5+sp.sqrt(115))/(30*sp.pi)
b=(sp.sqrt(115)-5)/(30*sp.pi)
c=sp.sqrt(15)/(10*sp.pi)
expected={sp.Rational(1,4):1,sp.Rational(1,4)+a:1,sp.Rational(1,4)-a:1,sp.Rational(1,4)+b:1,sp.Rational(1,4)-b:1,sp.Rational(1,4)+c:1,sp.Rational(1,4)-c:1}
lam=sp.symbols("lam")
assert sp.simplify(C.charpoly(lam).as_expr()-sp.expand(sp.prod(lam-v for v in expected)))==0
assert sp.N(a)>sp.N(c)>sp.N(b)>0
assert sp.N(sp.Rational(1,4)-a)>0
print('PASS exact orthogonal norms, regional matrix, all seven simple eigenvalues and sharp ordering')
