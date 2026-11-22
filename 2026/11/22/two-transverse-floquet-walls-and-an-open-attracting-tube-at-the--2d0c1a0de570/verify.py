"""Exact-algebra checks for a forward-Euler Chen map's axial two-cycle."""
import sympy as s

x, y, z, A = s.symbols('x y z A', real=True)
a, c, h = s.symbols('a c h', real=True, positive=True)
b = 2/h
F = s.Matrix((x + h*a*(y-x),
              y + h*((c-a)*x-x*z+c*y),
              z + h*(x*y-b*z)))
J = F.jacobian((x, y, z))
assert F.subs({x:0,y:0,z:A}) == s.Matrix((0,0,-A))
M0 = s.Matrix(((1-h*a, h*a),(h*(c-a),1+h*c)))
M = lambda z0: M0-s.Matrix(((0,0),(h*z0,0)))
assert s.simplify(J.subs({x:0,y:0,z:A})[:2,:2] - M(A)) == s.zeros(2)
P = s.simplify(M(-A)*M(A))
m = s.factor(M0.det()); T = s.factor(s.trace(M0*M0))
D = s.factor(P.det())
assert s.simplify(m-(1+h*(c-a)+h*h*a*(a-2*c)))==0
assert s.simplify(s.trace(P)-T)==0
assert s.simplify(D-(m*m-h**4*a*a*A*A))==0
assert s.factor(1-T+m*m)==s.factor(h*h*a*(a-2*c)*(4+2*h*(c-a)+h*h*a*(a-2*c)))

# The precise quadratic two-step drift also verifies the local contraction argument's order.
Fp = s.simplify(F.subs({x:F[0],y:F[1],z:F[2]}, simultaneous=True))
assert s.simplify(Fp[2]-z-h*(F[0]*F[1]-x*y))==0
for i in range(2):
    # The transverse difference from P(z)*(x,y) vanishes through degree 2.
    diff=s.Poly(s.expand(Fp[i]-(P.subs(A,z)*s.Matrix((x,y)))[i]),x,y)
    assert all(sum(power)>=3 for power,coeff in diff.terms() if coeff!=0)
assert s.simplify(Fp[2].subs({x:0,y:0})-z)==0

bench={a:s.Integer(3),c:s.Integer(1),h:s.Rational(1,10)}
mb=m.subs(bench); Tb=T.subs(bench); Db=s.factor(D.subs(bench))
assert mb==s.Rational(83,100)
assert Tb==s.Rational(79,50)
assert s.simplify(Db-(6889-9*A*A)/10000)==0
assert s.simplify((1-T+ D).subs(bench)-9*(121-A*A)/10000)==0
assert s.simplify((1+T+D).subs(bench)-(32689-9*A*A)/10000)==0
assert (1-T+D).subs(bench).subs(A,11)==0
assert s.simplify((1+T+D).subs(bench).subs(A,s.sqrt(32689)/3))==0

# Auxiliary eigenvalue diagnostics; exact algebra above, not this sampling, proves all amplitudes.
import math
for val,expected in [(1,'attracting'),(10,'attracting'),(12,'saddle'),(60,'saddle'),(61,'repelling'),(100,'repelling')]:
    d=float(Db.subs(A,val)); t=float(Tb)
    roots=[complex(v) for v in s.nroots(s.Symbol('L')**2-s.Rational(79,50)*s.Symbol('L')+Db.subs(A,val))]
    count=sum(abs(e)>1+1e-8 for e in roots)
    assert count=={'attracting':0,'saddle':1,'repelling':2}[expected],(val,roots)
print('PASS: exact axis, matrix, polynomial, factorization, drift and amplitude checks')
