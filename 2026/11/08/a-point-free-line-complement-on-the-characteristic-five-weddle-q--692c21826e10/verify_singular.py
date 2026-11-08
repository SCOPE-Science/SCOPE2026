"""Exact algebraic singular-locus certificate; requires SymPy >=1.12."""
import sympy as s
A,B,C,D=s.symbols('a b c d')
q=[A*C-B*B,A*D-B*C,B*D-C*C,C*D-A*B]
f=A*A*B*D-A*A*C*C-A*B*B*C+A*C*D*D+B**4-B*B*D*D-B*C*C*D+C**4
M=s.Matrix([[s.diff(g,x) for x in (A,B,C,D)] for g in q])
assert s.expand(M.det()-2*f)==0

def gb_at(unit,variables,expected):
    h=s.expand(f.subs(unit,1))
    gb=s.groebner([h]+[s.diff(h,v) for v in variables],*variables,order='lex',modulus=5)
    polys=[s.Poly(p,*variables,modulus=5) for p in gb.exprs]
    target=[s.Poly(p,*variables,modulus=5) for p in expected]
    assert len(polys)==len(target)
    assert all(p==q for p,q in zip(polys,target)),(polys,target)
    assert gb.is_zero_dimensional

gb_at(A,(B,C,D),(B-D**3,C-D**2,D**5-D))
gb_at(D,(A,B,C),(A-C**3,B-C**2,C**5-C))
for t in range(5):
    point={B:t,C:t*t%5,D:pow(t,3,5)}
    det=s.hessian(f.subs(A,1),(B,C,D)).subs(point).det()
    assert int(det)%5==2
assert int(s.hessian(f.subs(D,1),(A,B,C)).subs({A:0,B:0,C:0}).det())%5==2
# The complementary locus a=d=0 has no projective singular points:
# the B and C derivatives are -B*C^2 and -B^2*C, and the remaining
# derivatives include 4 B^3 and 4 C^3, forcing B=C=0.
assert s.expand(s.diff(f,B).subs({A:0,D:0}))==4*B**3
assert s.expand(s.diff(f,C).subs({A:0,D:0}))==4*C**3
print('DETERMINANT_IDENTITY_OK')
print('CHART_a=1_GB=[b-d^3,c-d^2,d^5-d]')
print('CHART_d=1_GB=[a-c^3,b-c^2,c^5-c]')
print('SIX_ORDINARY_DOUBLE_POINTS_HESSIAN_DET=2_mod5')
print('NO_SINGULAR_POINTS_ON_a=d=0')
print('VERIFY_OK')
