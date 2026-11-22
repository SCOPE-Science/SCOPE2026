"""Exact local-stability checks for a two-stage three-species directed cycle."""
import sympy as s
x,L,z=s.symbols('x L z')
cycle=s.Matrix([[0,6,0],[0,0,6],[6,0,0]])
assert s.expand(cycle.charpoly(x).as_expr())==x**3-216
for a,b in [(1,3),(3,1)]:
    D=s.Matrix([[-1-a*L,-1+a*L],[-1+b*L,-1-b*L]])
    B=s.Matrix([[1,0],[-1,0]])
    J=s.kronecker_product(s.eye(3),D)+s.kronecker_product(cycle,B)
    assert all(J[i,j] == (-1-a*L if i==j and i%2==0 else J[i,j]) for i in range(6) for j in range(6))
    cp=s.factor(J.subs(L,50).charpoly(x).as_expr())
    mode=s.factor((x*s.eye(2)-D-z*B).det())
    assert s.factor(mode-(x*x+(2+4*L-z)*x+L*(8+(a-b)*z)-2*z)) == 0
    assert s.simplify(cp - s.factor(mode.subs({L:50,z:6})*s.resultant(mode,z*z+6*z+36,z).subs(L,50)))==0
    if (a,b)==(1,3):
        assert s.factor(cp).has(x**2+196*x-212)
        # A strictly positive root exists because the real-mode determinant is negative.
        assert mode.subs({L:50,z:6,x:0})==-212
    else:
        q=x**4+410*x**3+42264*x**2+38168*x+270544
        assert s.factor(cp)==(x*x+196*x+988)*q
        A,Bc,C,Dc,E=s.Poly(q,x).all_coeffs()
        assert Bc*C-A*Dc==17290072>0
        assert Bc*C*Dc-A*Dc*Dc-Bc*Bc*E==614449021696>0
print('PASS: exact 6x6 factorization, slow-mode identity, real-root sign, quartic Hurwitz determinants')
