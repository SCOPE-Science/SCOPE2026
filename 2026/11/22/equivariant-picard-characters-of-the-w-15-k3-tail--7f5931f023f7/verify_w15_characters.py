"""Finite exact checks for the W15 weighted bidouble K3 model.

Requires sympy. Geometry for general parameters and the Torelli step are proved
in the accompanying mathematical text, not by this finite program.
"""
from fractions import Fraction
import sympy as sp

weights = (1, 2, 3)
monomials = [(a,b,c) for a in range(7) for b in range(4) for c in range(3)
             if a+2*b+3*c == 6]
assert len(monomials) == 7
assert sorted(monomials) == sorted([(6,0,0),(4,1,0),(2,2,0),(0,3,0),
                                    (3,0,1),(1,1,1),(0,0,2)])
x, y = sp.symbols('x y')
f = x**3+y**2+1
g = 3*x**3+5*y**2+x*y+2
R = sp.factor(sp.resultant(f, g, y))
assert R == 4*x**6+x**5+12*x**3+x**2+9
assert sp.discriminant(R, x) == 1090482201
assert sp.gcd(R, sp.diff(R,x)) == 1
# At tau=0: f=alpha^3+beta^2, g=3alpha^3+5beta^2;
# their coefficient determinant is 5-3=2 !=0.
assert sp.det(sp.Matrix([[1,1],[3,5]])) == 2
intersection = Fraction(6*6, 1*2*3)
assert intersection == 6
genus = (2*0 + 6)//2 + 1  # Hurwitz: 2g-2 = 6
assert genus == 4
trace = {'e':22, 'a':-(2*genus), 'b':-(2*genus), 'ab':8-2}
assert trace == {'e':22,'a':-8,'b':-8,'ab':6}
chars = {(s,t):(trace['e']+s*trace['a']+t*trace['b']+s*t*trace['ab'])//4
         for s in (1,-1) for t in (1,-1)}
assert chars == {(1,1):3,(1,-1):4,(-1,1):4,(-1,-1):11}
assert sum(chars.values()) == 22
# Four A2 points, each with two exceptional components, form 2Q[G].
exceptional_character = {ch:2 for ch in chars}
assert sum(exceptional_character.values()) == 8
picard_lower = chars[(1,1)]+chars[(1,-1)]+chars[(-1,1)]+exceptional_character[(-1,-1)]
assert picard_lower == 13
# Parameter count: 2*(7-1) - (6-1) = 7.
parameter_dimension = 2*(len(monomials)-1)-(6-1)
assert parameter_dimension == 7
assert 20-parameter_dimension == picard_lower
polarization_square=Fraction(6*6*6*6,1*2*3*3*3)
assert polarization_square == 24
print('PASS: weighted monomials, transverse six-point witness, traces, characters, exceptional module, parameter count, H^2=24')
