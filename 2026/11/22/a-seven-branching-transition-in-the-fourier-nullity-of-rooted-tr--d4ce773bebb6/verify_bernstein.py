#!/usr/bin/env python3
"""Exact positive-Bernstein certificate for the d=2,...,6 inequalities.
Requires sympy. Every rational conversion is exact.
"""
from fractions import Fraction
from math import comb
import sympy as sp
z,t=sp.symbols('z t')
reference={
 2: Fraction(7,8),
 3: Fraction(169,256),
 4: Fraction(14911,32768),
 5: Fraction(79069927,289406976),
 6: Fraction(43122177312287,435713694760960)
}
for d in range(2,7):
    poly=sp.Poly(sp.cancel((2*z-(1-(1-z)**d)**d)/z),z)
    q=sp.Poly(sp.expand(poly.as_expr().subs(z,t/2)),t)
    N=d*d-1
    assert q.degree()==N
    coeff=[Fraction(int(q.nth(k).p),int(q.nth(k).q)) for k in range(N+1)]
    bern=[sum((coeff[k]*Fraction(comb(i,k),comb(N,k)) for k in range(i+1)),Fraction()) for i in range(N+1)]
    mn=min(bern)
    assert mn == reference[d] and mn>0,(d,mn)
    assert sum(bern[i]*Fraction(comb(N,i))*Fraction(1,2)**N for i in range(N+1))==Fraction(poly.eval(sp.Rational(1,4)))
    print('PASS d=%d degree=%d minimum Bernstein coefficient=%s'%(d,N,mn))

# Exact certificate g_d(2/5)>2/5 for all d>=7:
assert 7*Fraction(3,5)**7 < Fraction(1,5)
# Since (d+1) (3/5)^(d+1) < d(3/5)^d for d>=7.
assert Fraction(3,5)*Fraction(8,7)<1
print('PASS uniform branching lower-bound witness at z=2/5 for d>=7')
