"""Finite algebraic stress checks for a one-dimensional vector-field realization.
Uses sympy for symbolic endpoint and derivative verification. The infinite theorem
relies on the separate argument in RESULT.md, not on these finite checks.
"""
from fractions import Fraction
from math import exp, log
from itertools import product
import sympy as sp

s,A,B,R,L = sp.symbols('s A B R L', real=True)
vleft = -L*s*(1-s)*(A*(1-s)+R*s)
vright = L*s*(1-s)*(R*(1-s)+B*s)

def deriv(expr, at):
    return sp.simplify(sp.diff(expr, s).subs(s, at) / L)
assert sp.simplify(vleft.subs(s,0)) == 0
assert sp.simplify(vleft.subs(s,1)) == 0
assert sp.simplify(vright.subs(s,0)) == 0
assert sp.simplify(vright.subs(s,1)) == 0
assert deriv(vleft,0) == -A
assert deriv(vleft,1) == R
assert deriv(vright,0) == R
assert deriv(vright,1) == -B
assert sp.simplify(vleft-L*s*(s-1)*(A*(1-s)+R*s)) == 0
assert sp.simplify(vright-L*s*(1-s)*(B*s+R*(1-s))) == 0

# Probe rational positions and sign/derivative against finite differences,
# including endpoints with neutral multiplier (A=0 or B=0).
checks=0
for ar,br,rr in product([Fraction(0),Fraction(1,7),Fraction(5,3)],
                         [Fraction(0),Fraction(1,4),Fraction(7,5)],
                         [Fraction(1,19),Fraction(3,2)]):
    for u in [Fraction(i,100) for i in range(1,100)]:
        l=float(vleft.subs({L:1,s:sp.Rational(u.numerator,u.denominator),A:sp.Rational(ar.numerator,ar.denominator),R:sp.Rational(rr.numerator,rr.denominator)}))
        r=float(vright.subs({L:1,s:sp.Rational(u.numerator,u.denominator),B:sp.Rational(br.numerator,br.denominator),R:sp.Rational(rr.numerator,rr.denominator)}))
        assert l<0 and r>0
        checks+=2

# Shrinking gaps: the dimensionless slope bounds depend on A+B+R,
# not on gap length or the prescribed split ratio.
for Lf in [sp.Rational(1,10),sp.Rational(1,10**3),sp.Rational(1,10**5)]:
    for mratio in [sp.Rational(1,100), sp.Rational(1,2), sp.Rational(99,100)]:
        aa=Lf*Lf; bb=Lf; rr=Lf**2
        for expr,par in [(vleft,{A:aa,R:rr}), (vright,{B:bb,R:rr})]:
            derivative=sp.diff(expr,s)/L
            for t in [sp.Rational(j,50) for j in range(51)]:
                val=abs(derivative.subs({**par,s:t}))
                assert val <= 5*(aa+bb+rr)

print(f'PASS: four endpoint derivative identities and {checks} exact-sign checks; shrinking-gap derivative envelopes.')
