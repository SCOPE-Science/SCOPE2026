"""Exact-algebra and finite rational test suite for centered
three-point cube geometry. Requires Python 3 and SymPy.
Proof of all-dimensional bounds is given in RESULT.md, not by finite tests.
"""
import random
from fractions import Fraction
from math import factorial
import sympy as S

a,b,c=S.symbols('a b c', real=True)
assert S.simplify(S.expand((a*a+b*b+(a-b)**2)-(a+b)).subs(b,a)-2*a*(a-1))==0
assert S.simplify(S.expand(a*a+b*b+(a-b)**2-a-b).subs(b,a/2)) == S.Rational(3,2)*a*(a-1)
assert S.simplify(S.expand((2-a*a-b*b-c*c)-((1-a)**2+(1-b)**2+c*c)) - 2*(a+b-a*a-b*b-c*c)) == 0
assert S.simplify(S.expand((2-a*a-b*b-c*c)+2*c*c - ((1-a*a)+(1-b*b)+c*c)))==0

sqrt2,sqrt3=S.sqrt(2),S.sqrt(3)
B3=S.Matrix([[1,-1,0],[0,1,-1],[-1,0,1]])
B4=S.Matrix([[1,-1,0],[-1,0,1],[1-sqrt2,1,sqrt2-2],[1-sqrt2,sqrt2-2,1]])
B2=S.Matrix([[-1,sqrt3-1,2-sqrt3],[2-sqrt3,sqrt3-1,-1]])

def verify_block(A, expected):
    assert A*S.ones(3,1) == S.zeros(A.rows,1)
    rows = [S.simplify((A[:,i].T*A[:,i])[0]) for i in range(3)]
    assert all(S.simplify(r-expected/3)==0 for r in rows)
    edges=[S.simplify(sum((A[j,i]-A[j,k])**2 for j in range(A.rows))) for i,k in [(0,1),(0,2),(1,2)]]
    assert all(S.simplify(v-expected)==0 for v in edges)
    for coord in A:
        assert -1 <= float(coord) <= 1

verify_block(B3,S.Integer(6))
verify_block(B4,24-12*sqrt2)
verify_block(B2,24-12*sqrt3)
assert S.simplify((S.Integer(8)-(24-12*sqrt2))-(12*sqrt2-16))==0
assert S.simplify((S.Integer(4)-(24-12*sqrt3))-(12*sqrt3-20))==0

for m in range(1,11):
    d=3*m
    M=B3
    for _ in range(m-1): M=M.col_join(B3)
    verify_block(M,S.Integer(2*d))
    count=2**d*factorial(d)//(6*factorial(m)**3)
    assert count >=8
    if m==1: assert count==8
    if m==2: assert count==960
    C=B4
    for _ in range(m-1): C=C.col_join(B3)
    verify_block(C,S.Integer(2*(3*m+1))-(12*sqrt2-16))
for m in range(0,11):
    C=B2
    for _ in range(m): C=C.col_join(B3)
    verify_block(C,S.Integer(2*(3*m+2))-(12*sqrt3-20))

# The modular comparison constants used in the proof are exactly rooted
# in the minimum L1 distance to an integer triple of fixed total.
delta=S.symbols('delta',nonnegative=True)
assert S.solve(S.Eq(2*delta,(4+delta)/3),delta)==[S.Rational(4,5)]
assert S.solve(S.Eq(2*delta,(4-delta)/3),delta)==[S.Rational(4,7)]
assert S.solve(S.Eq(2*delta,2+delta/3),delta)==[S.Rational(6,5)]

R=random.Random(20261121)
for _ in range(30000):
    a0=Fraction(R.randrange(1,1001),1000)
    b0=a0*Fraction(R.randrange(500,1001),1000)
    c0=a0-b0
    assert b0>=c0>=0 and a0<=1
    ds=2-a0*a0-b0*b0-c0*c0
    err=(1-a0)**2+(1-b0)**2+c0*c0
    l1=(1-a0*a0)+(1-b0*b0)+c0*c0
    assert ds>=err>=0
    assert l1<=2*ds
print('PASS: all exact identities, 34 exact-dimensional block constructions, and 60,000 rational near-vertex inequalities')
