#!/usr/bin/env python3
"""Self-contained supplemental arithmetic checks; not a substitute for the proof."""
from math import comb, isclose, sqrt, pi
from fractions import Fraction

# Finite Hardy monomial columns of A z^n = n(1-z)^3((1+z)/2)^(n-1).
partials=[]
running=Fraction(0)
for n in range(1,151):
    coefficients=[]
    for j in range(n+3):
        numerator=sum((-1)**k*comb(3,k)*comb(n-1,j-k)
                      for k in range(4) if 0<=j-k<=n-1)
        coefficients.append(Fraction(n*numerator,2**(n-1)))
    running+=sum((c*c for c in coefficients), Fraction(0))
    if n in (1,2,5,10,25,50,100,150):
        partials.append((n,float(running)))
    assert running<96
assert float(running)>84

# Independent weighted-Volterra kernel integration: after x=u+v,
# integral 2048*exp(-2u-4v)*(v-u)^2 dudv = 96.
# Evaluating factorial moments of the two exponential factors gives:
q = Fraction(2048)*(Fraction(2,2**3)*Fraction(1,4)-
                    2*Fraction(1,2**2)*Fraction(1,4**2)+
                    Fraction(1,2)*Fraction(2,4**3))
assert q==96, q

# Exact squared Hilbert-Schmidt norms in the trace-class factorization.
assert Fraction(1,4)*Fraction(1,3)==Fraction(1,12)
# The limiting constant is a scale times the inverse Liouville interval length.
limit=32*sqrt(2)/pi
assert 14.40<limit<14.41
print('PASS: monomial partial Hilbert-Schmidt energies',partials)
print('PASS: independent Volterra norm', q)
print('Predicted sharp n*s_n:', limit)
print('Note: asymptotic statement relies on the analytic proof, not finite tests.')
