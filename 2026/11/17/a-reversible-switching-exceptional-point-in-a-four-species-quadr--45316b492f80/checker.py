"""Independent exact algebra and reproducible finite checks for the two-season population map.

Requires Python 3 and SymPy (tested with SymPy 1.13 or newer).
Finite samples corroborate; the proof in RESULT.md establishes the universal statements.
"""
from fractions import Fraction
from itertools import product
import sympy as sp

A, X = sp.symbols('A X', real=True)
P12 = sp.Matrix([[A, 1-A, 0], [1-A, A, 0], [0, 0, 1]])
P23 = sp.Matrix([[1, 0, 0], [0, A, 1-A], [0, 1-A, A]])
M = sp.expand(P23*P12)
poly = (X-1)*(X**2-(A*A+2*A-1)*X+(2*A-1)**2)
assert sp.factor(M.charpoly().as_expr()-poly.subs(X, sp.Symbol('lambda'))) == 0
assert sp.factor((A*A+2*A-1)**2-4*(2*A-1)**2) == (A-1)**2*(A*A+6*A-3)
assert M*sp.ones(3,1) == sp.ones(3,1)
assert (sp.ones(1,3)*M) == sp.ones(1,3)

ac = 2*sp.sqrt(3)-3
lam = 7-4*sp.sqrt(3)
Mc = M.subs(A, ac)
u = sp.ones(3,1)/3
Q = Mc-lam*sp.eye(3)
H1 = sp.Matrix([1,-1,0]); H2 = sp.Matrix([0,1,-1])
assert (Q*Q*H1).applyfunc(sp.simplify) == sp.zeros(3,1)
assert (Q*Q*H2).applyfunc(sp.simplify) == sp.zeros(3,1)
z = sp.Matrix([1,0,0])-u
assert sp.simplify((Q*z)[0]) == -8 + 14*sp.sqrt(3)/3
assert sp.simplify((Q*z)[0]) != 0
for n in range(1,9):
    direct = sp.simplify(Mc**n*z)
    jordan = sp.simplify(lam**n*z+n*lam**(n-1)*Q*z)
    assert (direct-jordan).applyfunc(sp.simplify) == sp.zeros(3,1)

# Rational four-species trajectories, with odd and even alternating seasons.
def step(state, alpha, swap):
    s = state[3]
    per = list(state[:3])
    mixed = [alpha*per[j]+(1-alpha)*per[swap[j]] for j in range(3)]
    return tuple([2*s*v for v in mixed]+[s*s+(1-s)**2])

trials=0
for den in (5, 7, 11):
    for v1,v2,v3,alpha_num in product(range(1,den), repeat=4):
        if v1+v2+v3>=den:
            continue
        s0=Fraction(v3,den)
        p0=(Fraction(v1,den), Fraction(v2,den), Fraction(den-v1-v2,den))
        x0=tuple([(1-s0)*v for v in p0]+[s0])
        alpha=Fraction(alpha_num,den)
        x1=step(x0,alpha,(1,0,2))
        x2=step(x1,alpha,(0,2,1))
        assert sum(x1)==1 and sum(x2)==1
        p2=sp.Matrix([sp.Rational(x2[i].numerator,x2[i].denominator)/sp.Rational((1-x2[3]).numerator,(1-x2[3]).denominator) for i in range(3)])
        vec=sp.Matrix([sp.Rational(y.numerator,y.denominator) for y in p0]); alpha_sp=sp.Rational(alpha.numerator,alpha.denominator)
        assert p2 == M.subs(A,alpha_sp)*vec
        s2=sp.Rational(x2[3].numerator,x2[3].denominator)
        b=sp.Rational((2*s0-1).numerator,(2*s0-1).denominator)
        assert s2==(1+b**4)/2
        trials+=1
        if trials>=220:break
    if trials>=220:break
assert trials>=100
assert (sp.Rational(1,4)**2+6*sp.Rational(1,4)-3)<0
assert (sp.Rational(3,4)**2+6*sp.Rational(3,4)-3)>0
assert 0<float(ac)<0.5 and 0<float(lam)<1
print(f'ALTERNATING_JAMILOV_EXCEPTIONAL_POINT_OK symbolic_Jordan_powers=8 rational_trajectories={trials}')
