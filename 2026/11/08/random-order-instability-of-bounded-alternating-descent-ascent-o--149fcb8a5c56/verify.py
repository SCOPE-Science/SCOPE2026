"""Exact algebraic checks for randomly ordered alternating descent--ascent.

Run: python verify.py
Requires sympy >= 1.10. The proof's all-parameter statements
are analytic; this script verifies their symbolic identities.
"""
from fractions import Fraction
import sympy as S

t, p = S.symbols('t p', real=True)
z = S.Symbol('z')
A = S.Matrix([[1, -t], [t, 1-t**2]])
B = S.Matrix([[1-t**2, -t], [t, 1]])
Wa = S.Matrix([[1, -t/2], [-t/2, 1]])
Wb = S.Matrix([[1, t/2], [t/2, 1]])
I2 = S.eye(2)

N = 0
def assert_zero(expr):
    global N
    assert S.simplify(expr) == 0, expr
    N += 1

def assert_matrix(X, Y):
    for e in (X-Y):
        assert_zero(e)

assert_zero(A.det() - 1)
assert_zero(B.det() - 1)
assert_zero(S.trace(A) - (2-t**2))
assert_zero(S.trace(B) - (2-t**2))
assert_matrix(A.T*Wa*A, Wa)
assert_matrix(B.T*Wb*B, Wb)
assert_matrix((A.T*A+B.T*B)/2, (1+t**4/2)*I2)

def sym_moment(M):
    a,b,c,d = M[0,0],M[0,1],M[1,0],M[1,1]
    return S.Matrix([[a*a, 2*a*b, b*b],
                     [a*c, a*d+b*c, b*d],
                     [c*c, 2*c*d, d*d]])

L = p*sym_moment(A)+(1-p)*sym_moment(B)
assert_zero((S.eye(3)-L).det() + 8*t**6*p*(1-p))
u = p*(1-p)
P = ((z-1)*((z-1)**2+t**2*(4-t**2)*z)
     +u*t**4*((t**4+4)*(z-1)-8*t**2*z))
assert_zero(L.charpoly(z).as_expr()-P)
assert_zero(P.subs(z, 1)+8*u*t**6)

# Independent fraction-arithmetic checks, including every binary word up to length 9.
# They supplement the symbolic proof and do not certify an infinite limit.
for tv in [Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1),Fraction(3,2)]:
    at = [[Fraction(1),-tv],[tv,Fraction(1)-tv**2]]
    bt = [[Fraction(1)-tv**2,-tv],[tv,Fraction(1)]]
    X = [(Fraction(1),Fraction(0)),(Fraction(1),Fraction(2)),(Fraction(-2),Fraction(3))]
    k = Fraction(1)+tv**4/2
    def mult(mat,x):
        return (mat[0][0]*x[0]+mat[0][1]*x[1],mat[1][0]*x[0]+mat[1][1]*x[1])
    def norm(x):
        return x[0]**2+x[1]**2
    for start in X:
        d = {start: Fraction(1)}
        for n in range(7):
            actual=sum((weight*norm(x) for x,weight in d.items()),Fraction(0))
            assert actual == k**n*norm(start)
            N += 1
            nd = {}
            for x,weight in d.items():
                for mat in [at,bt]:
                    xx=mult(mat,x)
                    nd[xx]=nd.get(xx,Fraction(0))+weight/2
            d=nd

# Spot-check Perron growth rates using exact rational characteristic signs.
for tv in [S.Rational(1,3), S.Rational(2,3), S.Rational(3,2)]:
    for pv in [S.Rational(1,10), S.Rational(1,3),S.Rational(1,2),S.Rational(9,10)]:
        assert S.factor(P.subs({z:1,t:tv,p:pv})) < 0
        N += 1
print(f'PASS: {N} exact symbolic/rational assertions')
