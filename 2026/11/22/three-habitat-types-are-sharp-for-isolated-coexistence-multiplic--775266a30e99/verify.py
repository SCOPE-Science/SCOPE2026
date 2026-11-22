"""Exact rational verification for separable-colonization equilibrium example.
Run with Python 3 and SymPy; all assertions use exact symbolic arithmetic.
"""
import sympy as sp
h=(sp.Integer(2),sp.Integer(1),sp.Integer(4))
k=(sp.Integer(4),sp.Integer(1),sp.Integer(2))
a=(sp.Rational(99,40),sp.Integer(2),sp.Rational(99,40))
b=(sp.Rational(33,20),sp.Rational(8,3),sp.Rational(33,20))
p=[sp.Rational(1,3)]*3
C=sp.Matrix([[3*h[i]*a[j]/h[j] for j in range(3)] for i in range(3)])
G=sp.Matrix([[3*k[i]*b[j]/k[j] for j in range(3)] for i in range(3)])
assert all(t>0 for t in C) and all(t>0 for t in G)
assert C.rank()==G.rank()==1
assert C==sp.Matrix([[sp.Rational(297,40),12,sp.Rational(297,80)],[sp.Rational(297,80),6,sp.Rational(297,160)],[sp.Rational(297,20),24,sp.Rational(297,40)]])
assert G==sp.Matrix([[sp.Rational(99,20),32,sp.Rational(99,10)],[sp.Rational(99,80),8,sp.Rational(99,40)],[sp.Rational(99,40),16,sp.Rational(99,20)]])
U=sp.symbols('U')
R=sp.factor((1/(13-2*U)+1/(7+2*U))-sp.Rational(20,99))
num,den=sp.fraction(R)
assert sp.factor(num+80*(U-1)*(U-2))==0
assert sp.solve(num,U)==[1,2]
x=sp.symbols('u0:3')
y=sp.symbols('v0:3')
z=sp.Matrix(list(x)+list(y))
f=sp.Matrix([-x[i]+(p[i]-x[i]-y[i])*sum(C[i,j]*x[j] for j in range(3)) for i in range(3)]+[-y[i]+(p[i]-x[i]-y[i])*sum(G[i,j]*y[j] for j in range(3)) for i in range(3)])
J=f.jacobian(z)
lam=sp.symbols('lambda')
quartics=[60*lam**4+1380*lam**3+9679*lam**2+19218*lam+80,15*lam**4+345*lam**3+2424*lam**2+4838*lam-20]
expected=[(sp.Rational(2,33),sp.Rational(1,12),sp.Rational(4,27),sp.Rational(8,33),sp.Rational(1,6),sp.Rational(4,27)),(sp.Rational(4,27),sp.Rational(1,6),sp.Rational(8,33),sp.Rational(4,27),sp.Rational(1,12),sp.Rational(2,33))]
for idx,(uu,vv) in enumerate([(1,2),(2,1)]):
    us=[p[i]*h[i]*uu/(1+h[i]*uu+k[i]*vv) for i in range(3)]
    vs=[p[i]*k[i]*vv/(1+h[i]*uu+k[i]*vv) for i in range(3)]
    assert tuple(us+vs)==expected[idx]
    assert all(t>0 for t in us+vs)
    assert all(p[i]-us[i]-vs[i]>0 for i in range(3))
    assert sp.simplify(sum(3*a[i]*us[i]/h[i] for i in range(3))-uu)==0
    assert sp.simplify(sum(3*b[i]*vs[i]/k[i] for i in range(3))-vv)==0
    d=dict(zip(z,us+vs))
    assert all(sp.simplify(q)==0 for q in f.subs(d))
    jj=J.subs(d)
    cp=jj.charpoly(lam).as_expr()
    assert sp.factor(cp-(lam+1)**2*quartics[idx]/(60 if idx==0 else 15))==0
    assert sp.factor(jj.det())==([sp.Rational(4,3),-sp.Rational(4,3)][idx])
    co=sp.Poly(quartics[idx],lam).all_coeffs()
    A,B,CC,D,E=co
    d2=B*CC-A*D
    d3=B*CC*D-A*D**2-B**2*E
    assert d2==[12203940,763710][idx]
    assert d3==[234382966920,3697209480][idx]
    assert all(q>0 for q in co[:4]) and d2>0 and d3>0
    assert (E>0) if idx==0 else (E<0)
print('PASS: positive rank-one matrices; exactly two scalar roots; feasible stationary points; full Jacobian characteristic polynomials; one sink and one saddle.')
