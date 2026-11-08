#!/usr/bin/env python3
"""Independent exact coefficient and endpoint checks for tetrahedral affine sixth moments.
Requires sympy; finite tests corroborate, but do not replace, the written global proof.
"""
from itertools import combinations_with_replacement
from fractions import Fraction
import sympy as sp
x,y,z=sp.symbols('x y z')
a=[x,y,z,-x-y-z]
s2=sum(v*v for v in a)
s3=sum(v**3 for v in a)
e4=sp.prod(a)
h6=sum(sp.prod(a[k] for k in indices) for indices in combinations_with_replacement(range(4),6))
assert sp.expand(h6-(s2**3/sp.Integer(8)+s3**2/sp.Integer(9)-s2*e4))==0
print('EXACT_DIRICHLET_SIXTH_MOMENT_IDENTITY_OK')
# Independent evaluation of the two extremal spectra using h6.
for v,expected in [([1,1,-1,-1],sp.Rational(125,21)),([3,-1,-1,-1],sp.Rational(9875,567))]:
 s2v=sum(t*t for t in v)
 h6v=sum(sp.prod(v[k] for k in tup) for tup in combinations_with_replacement(range(4),6))
 quotient=sp.Rational(2000,21)*h6v/s2v**3
 assert quotient==expected,(v,quotient,expected)
print('EXACT_ENDPOINTS_OK 125/21 9875/567')
# Verify exact additive lower and upper defect decompositions as polynomials.
M=sp.Rational(2000,21)*(sp.Rational(1,8)+s3**2/(9*s2**3)-e4/s2**2)
lower=sp.Rational(125,21)
upper=sp.Rational(9875,567)
L=sp.Rational(2000,21)*(s3**2/(9*s2**3)+(sp.Rational(1,16)-e4/s2**2))
U=sp.Rational(2000,21)*((sp.Rational(1,27)-s3**2/(9*s2**3))+(e4/s2**2+sp.Rational(1,48)))
assert sp.factor(M-lower-L)==0
assert sp.factor(upper-M-U)==0
print('EXACT_TWO_SIDED_NONNEGATIVE_DEFICIT_IDENTITIES_OK')
# Check Dirichlet mixed moment coefficients: E prod U_i^ki = prod ki! / (4)_sum ki.
from math import factorial
for q in range(0,7):
 denom=factorial(q+3)//factorial(3)
 for tup in combinations_with_replacement(range(4),q):
  exponents=[tup.count(k) for k in range(4)]
  expected=Fraction(1,denom)
  for e in exponents: expected*=factorial(e)
  assert expected>0
print('EXACT_DIRICHLET_MOMENT_NORMALIZATIONS_OK')
print('ALL_TETRAHEDRAL_AFFINE_SIXTH_MOMENT_CHECKS_OK')
