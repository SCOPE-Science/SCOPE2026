#!/usr/bin/env python3
"""Finite exact verification of the Hermite--Mehler sum-of-squares identity.
The universal theorem is proved analytically in RESULT.md; finite tests are not a substitute.
"""
from fractions import Fraction as F
from math import comb, factorial
import sympy as sp
x=sp.symbols('x')
g=sp.symbols('g')
checks=0

def binom_half(j):
    r=F(1)
    for t in range(j): r*=F(1,2)-t
    return r/F(factorial(j))

def a(k, gamma):
    return sum((binom_half(j)*(-gamma)**j for j in range(k+1)),F(0))

# Fully expanded polynomial identities, for five nontrivial rational parameters.
for G in [F(0),F(1,5),F(1,2),F(4,5),F(1)]:
  for m in range(0,13):
    L=sp.expand(sum(sp.Rational(G.numerator,G.denominator)**j *sp.hermite_prob(2*j,x)/(2**j*factorial(j)) for j in range(m+1)))
    R=sp.expand(sum(sp.Rational(a(m-j,G).numerator,a(m-j,G).denominator)*sp.Rational(G.numerator,G.denominator)**j*sp.hermite_prob(j,x/sp.sqrt(2))**2/factorial(j) for j in range(m+1)))
    assert sp.expand(L-R)==0,(G,m)
    checks+=1
    assert a(m,G)>0
    checks+=1
    for t in [F(-7,3),F(-1),F(0),F(1,4),F(2),F(19,4)]:
      v=sp.Rational(L.subs(x,sp.Rational(t.numerator,t.denominator)))
      assert v>0,(G,m,t,v)
      checks+=1
# Endpoint special cases and first gamma-outside failures.
assert a(1,F(1))==F(1,2)
assert a(2,F(1))==F(3,8)
assert a(3,F(1))==F(5,16)
checks+=3
assert 1+F(-1,2)*(100-1)/2<0
checks+=1
for G in [F(11,10), F(5,4),F(3,2),F(2)]:
  vals=[sum((-G)**j*F(comb(2*j,j),4**j) for j in range(m+1)) for m in range(1,251,2)]
  assert any(v<0 for v in vals),G
  checks+=1
print('PASS:',checks,'exact rational/symbolic assertions')
