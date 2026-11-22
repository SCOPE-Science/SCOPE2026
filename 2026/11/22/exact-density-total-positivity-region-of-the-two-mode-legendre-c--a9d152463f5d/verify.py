"""Reproducible symbolic and rational checks for the two-mode Legendre TP2 classification.

The infinite-domain conclusions follow from the proof, not these finite tests.
Requires Python 3 and SymPy.
"""
from fractions import Fraction as F
import sympy as s

x, y, a, b, t = s.symbols('x y a b t', real=True)
c = 1 + a*x*y + b*(3*x*x-1)*(3*y*y-1)
D = s.expand(c*s.diff(c,x,y) - s.diff(c,x)*s.diff(c,y))
assert s.factor(D - (a*(1+b*(1+3*x*x)*(1+3*y*y))+36*b*x*y)) == 0
assert s.factor((1+4*b)*(1+16*b)-36*b) == (8*b-1)**2
assert s.factor((36*b)**2-24*b*(1-2*b)*(1+16*b)**2) == 24*b*(8*b-1)**3
assert s.factor(s.diff(t/(1+b*(1+3*t)**2),t)*(1+b*(1+3*t)**2)**2) == 1+b-9*b*t**2

# Exact rational checks of the analytic lower/upper envelope.
tests = 0
values = [-F(1,80), -F(1,100), F(0), F(1,64), F(1,32), F(1,16), F(1,8)]
for B in values:
    lower=36*abs(B)/(1+16*B)
    upper=1+4*B
    assert 0 <= lower <= upper
    for A in [lower,(lower+upper)/2,upper]:
        for i in range(-8,9):
            for j in range(-8,9):
                X,Y=F(i,8),F(j,8)
                C=1+A*X*Y+B*(3*X*X-1)*(3*Y*Y-1)
                Delta=A*(1+B*(1+3*X*X)*(1+3*Y*Y))+36*B*X*Y
                assert C>=0 and Delta>=0, (B,A,X,Y,C,Delta)
                tests+=2

# Constructive exclusions inside the valid-copula parameter region.
for B,A in [(F(1,16),F(0)),(F(-1,32),F(7,8)),(F(1,4),F(3,2))]:
    X,Y=F(1), -F(1) if B>0 else F(1)
    val=A*(1+16*B)+36*B*X*Y
    assert val<0
    tests+=1

root_min=(-s.Integer(7)+3*s.sqrt(5))/16
assert bool(root_min > -s.Rational(1,16))
assert bool(root_min < 0)
assert s.simplify(1+56*root_min+64*root_min**2)==0
assert s.simplify((1+4*root_min)*(1+16*root_min)-36*(-root_min))==0
# TP2 at (a,b)=(3/2,1/8) has Spearman rho=a/3=1/2.
assert s.simplify(s.Rational(3,2)-(1+4*s.Rational(1,8)))==0
print('VERIFICATION_OK', 'rational_checks', tests, 'b_min', s.N(root_min,25))
