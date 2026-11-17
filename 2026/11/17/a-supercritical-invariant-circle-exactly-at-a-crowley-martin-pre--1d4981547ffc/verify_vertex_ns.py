"""Exact algebraic checks for a nullcline-vertex Neimark--Sacker bifurcation.

Run with Python 3 and SymPy: python verify_vertex_ns.py
"""
import sympy as sp

x, y, h = sp.symbols('x y h', real=True)
R = sp.Rational
f = sp.Matrix([
    3*x*(1-x/3) - 4*x*y/((1+x)*(1+y/2)),
    4*x*y/((1+x)*(1+y/2)) - y
])
variables = (x,y)
point = {x:R(1), y:R(2)}
assert f.subs(point) == sp.zeros(2,1)

# The prey nullcline is y = g(x) with an interior maximum at x=1.
H = (3-x)*(1+x)
g = H/(4-H/2)
assert sp.simplify(g.subs(x,1)-2) == 0
assert sp.simplify(sp.diff(g,x).subs(x,1)) == 0
assert sp.diff(g,x,2).subs(x,1) < 0

J = sp.simplify(f.jacobian(variables).subs(point))
A = sp.eye(2)+J
assert J == sp.Matrix([[0,-R(1,2)],[1,-R(1,2)]])
assert A == sp.Matrix([[1,-R(1,2)],[1,R(1,2)]])
assert sp.simplify((sp.eye(2)+h*J).det()-(1-h*R(1,2)+h*h*R(1,2))) == 0
assert A.det()==1 and A.trace()==R(3,2)

lam = (3+sp.I*sp.sqrt(7))/4
q = sp.Matrix([1, 2*(1-lam)])
left = sp.Matrix([[1,lam-1]])
left /= (left*q)[0]
qbar = sp.conjugate(q)
assert sp.simplify(A*q-lam*q)==sp.zeros(2,1)
assert sp.simplify(left*A-lam*left)==sp.zeros(1,2)
assert sp.simplify((left*q)[0]-1)==0

Btensor = [
  [[sp.diff(f[i],variables[j],variables[k]).subs(point)
    for k in range(2)] for j in range(2)] for i in range(2)
]
Ctensor = [
  [[[sp.diff(f[i],variables[j],variables[k],variables[l]).subs(point)
    for l in range(2)] for k in range(2)] for j in range(2)] for i in range(2)
]
def B(u,v):
    return sp.Matrix([sum(Btensor[i][j][k]*u[j]*v[k]
                     for j in range(2) for k in range(2)) for i in range(2)])
def C(u,v,w):
    return sp.Matrix([sum(Ctensor[i][j][k][l]*u[j]*v[k]*w[l]
                     for j in range(2) for k in range(2) for l in range(2))
                      for i in range(2)])

h11 = (sp.eye(2)-A).inv()*B(q,qbar)
h20 = (lam**2*sp.eye(2)-A).inv()*B(q,q)
G = sp.simplify((left*(C(q,q,qbar)/2+B(q,h11)+B(qbar,h20)/2))[0])
assert sp.simplify(G-(-R(7,20)+sp.I*sp.sqrt(7)/140))==0
ell = sp.simplify(sp.re(sp.conjugate(lam)*G))
assert ell == -R(1,4)

# This is a genuine transverse unit-circle crossing, not merely a neutral pair.
D = sp.factor((sp.eye(2)+h*J).det())
assert sp.diff(D,h).subs(h,1) == R(1,2)
assert sp.simplify(sp.diff(sp.sqrt(D),h).subs(h,1)) == R(1,4)
for j in range(1,5):
    assert sp.simplify(lam**j-1) != 0

print('nullcline vertex: (1,2); g\'(1)=0, g\'\'(1)<0')
print('flow Jacobian:', J)
print('map Jacobian at h=1:', A)
print('unit roots:', lam, sp.conjugate(lam))
print('determinant as function of h:', D)
print('normal-form cubic term:', sp.simplify(sp.expand_complex(G)))
print('radial cubic coefficient:', ell)
print('crossing derivative:', sp.diff(sp.sqrt(D),h).subs(h,1))
print('ALL EXACT CHECKS PASSED')
