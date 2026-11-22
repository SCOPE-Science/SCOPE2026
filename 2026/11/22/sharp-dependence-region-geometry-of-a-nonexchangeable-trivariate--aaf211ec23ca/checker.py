"""Exact identities for a three-dimensional polynomial copula.

Requires SymPy; the infinite-domain argument is in RESULT.md.
"""
import sympy as s
from fractions import Fraction

x,y,z,lam,alpha,beta=s.symbols('x y z lam alpha beta',real=True)
gamma=1-alpha-beta
C=x*y*z*(1+lam*(1-alpha*x-beta*y-gamma*x*y)*(1-z))
F=1-2*alpha*x-2*beta*y-4*gamma*x*y
assert s.simplify(s.diff(C,x,y,z)-(1+lam*(1-2*z)*F))==0
assert all(s.simplify(C.subs(subs)-ans)==0 for subs,ans in [({x:0},0),({y:0},0),({z:0},0),({x:1,y:1},z),({x:1,z:1},y),({y:1,z:1},x)])
assert [s.simplify(F.subs({x:X,y:Y})) for X,Y in [(0,0),(1,0),(0,1),(1,1)]] == [1,1-2*alpha,1-2*beta,2*(alpha+beta)-3]
rho=s.simplify(8*s.integrate(s.integrate(s.integrate(C,(x,0,1)),(y,0,1)),(z,0,1))-1)
med=s.simplify((8*C.subs({x:s.Rational(1,2),y:s.Rational(1,2),z:s.Rational(1,2)})-1)/3)
assert s.simplify(rho-lam*(5-2*alpha-2*beta)/27)==0
assert s.simplify(med-lam*(3-alpha-beta)/24)==0
u,v=s.symbols('u v',real=True)
assert s.simplify(rho.subs({alpha:(3+v/u)/4,beta:(3+v/u)/4,lam:u}) - (2*u-v)/27)==0
assert s.simplify(med.subs({alpha:(3+v/u)/4,beta:(3+v/u)/4,lam:u}) - (3*u-v)/48)==0
# Exact randomized rational tests are supportive of the algebraic proof, not a substitute for it.
import random
rng=random.Random(483103)
for k in range(160):
    a=Fraction(rng.randrange(-20,21),rng.randrange(1,13))
    b=Fraction(rng.randrange(-20,21),rng.randrange(1,13))
    f=lambda X,Y: 1-2*a*X-2*b*Y-4*(1-a-b)*X*Y
    cs=[f(X,Y) for X,Y in ((0,0),(1,0),(0,1),(1,1))]
    m=max(abs(c) for c in cs)
    l=Fraction(rng.choice((-1,1)),1)/m
    # All grid-point density signs follow from the corner bound.
    for X in [Fraction(j,7) for j in range(8)]:
        for Y in [Fraction(j,7) for j in range(8)]:
            for Z in [Fraction(0),Fraction(1,2),Fraction(1)]:
                assert 1+l*(1-2*Z)*f(X,Y)>=0
    # A slightly-too-large lambda in the most adverse sign violates a vertex.
    bad=Fraction(1001,1000)/m
    point=next(c for c in cs if abs(c)==m)
    assert 1-bad*(1 if point>0 else -1)*point<0
# Strict improvement at a shape from the source article.
a,b=Fraction(5),Fraction(2)
assert max(abs(1),abs(1-2*a),abs(1-2*b),abs(2*(a+b)-3)) == 11
# Sharp extrema and the missing seam, by exact linear reparameterization.
for U,V in [(Fraction(1),Fraction(-1)),(Fraction(1),Fraction(1)),(Fraction(-1),Fraction(-1)),(Fraction(-1),Fraction(1))]:
    R=(2*U-V)/27; M=(3*U-V)/48
    assert abs(R)<=Fraction(1,9) and abs(M)<=Fraction(1,12)
assert (2-Fraction(-1))/27 == Fraction(1,9)
assert (3-Fraction(-1))/48 == Fraction(1,12)
print('PASS: exact symbolic density, margins, corner identities, rank moments, feasible-coordinate construction; 160 rational probes and sharp boundary examples.')
