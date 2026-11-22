"""Exact arithmetic checks for the real Keller-map lineability theorem.

The all-dimensional assertion is proved using the classical Hurwitz--Radon
and Adams--Lax--Phillips theorems; the computations here check source data
and a quaternionic dimension-four witness, not the topological theorem.
"""
from fractions import Fraction
import sympy as sp

x, y, z = sp.symbols('x y z')
t = 1 + x*y
F0 = sp.Matrix([
    t**3*z + y**2*t*(4+3*x*y),
    y + 3*x*t**2*z + 3*x*y**2*(4+3*x*y),
    2*x - 3*x**2*y - x**3*z,
])
assert sp.factor(F0.jacobian([x, y, z]).det()) == -2
inputs = [(0,0,sp.Rational(-1,4)),
          (1,sp.Rational(-3,2),sp.Rational(13,2)),
          (-1,sp.Rational(3,2),sp.Rational(13,2))]
for values in inputs:
    assert F0.subs(dict(zip((x,y,z),values))) == sp.Matrix([-sp.Rational(1,4),0,0])

I = sp.eye(4)
i = sp.Matrix([[0,-1,0,0],[1,0,0,0],[0,0,0,-1],[0,0,1,0]])
j = sp.Matrix([[0,0,-1,0],[0,0,0,1],[1,0,0,0],[0,-1,0,0]])
k = i*j
for J in (i,j,k):
    assert J.T == -J and J.T*J == I
for J,K in ((i,j),(j,k),(k,i)):
    assert J*K+K*J == sp.zeros(4)
a,b,c,d=sp.symbols('a b c d',real=True)
A=a*I+b*i+c*j+d*k
assert sp.simplify(A.T*A-(a*a+b*b+c*c+d*d)*I) == sp.zeros(4)
assert sp.factor(A.det())==(a*a+b*b+c*c+d*d)**2
F4=sp.Matrix([*F0,sp.Symbol('w')]); w=sp.Symbol('w')
assert sp.factor(F4.jacobian([x,y,z,w]).det())==-2
assert sp.factor((A*F4).jacobian([x,y,z,w]).det()) == -2*(a*a+b*b+c*c+d*d)**2

def rho(n):
    b=0
    while n%2==0:
        n//=2
        b+=1
    q,r=divmod(b,4)
    return 8*q+(1<<r)
assert [(n,rho(n)) for n in (3,4,5,6,7,8,12,16,32)] == [
    (3,1),(4,4),(5,1),(6,2),(7,1),(8,8),(12,4),(16,9),(32,10)]
print('PASS: rational collision, Jacobian -2, quaternionic rho(4)=4 witness, and rho table')
