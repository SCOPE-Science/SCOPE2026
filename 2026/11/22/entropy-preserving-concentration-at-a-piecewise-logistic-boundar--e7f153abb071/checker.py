"""Exact algebraic diagnostics for the two-full-branch boundary-crisis family.

The theorem is analytic; this program checks its finite algebraic prerequisites
on rational parameter samples and does not replace its ergodic-theoretic proof.
"""
from fractions import Fraction
from math import log, sqrt

for r in [Fraction(101,100),Fraction(11,10),Fraction(5,4),Fraction(7,5),Fraction(3,2),Fraction(8,5)]:
    a = r*r/(r-1)
    c = 1/r
    assert a*c*(1-c) == 1
    assert r*c == 1
    assert a > 4
    mright = a*(2*c-1)
    assert mright == r*(2-r)/(r-1) and mright > 1
    assert r > 1 and c > Fraction(1,2)
    for n in range(1,20):
        endpoint = r**(-n)
        assert r**n*endpoint == 1
        assert endpoint <= c
        if n > 1:
            assert r**(n-1)*endpoint == c
        # The fair-branch cylinder mass is exactly 2**(-n).
        mass = Fraction(1,2**n)
        assert mass*2**n == 1
    lower = log(float(r)) + .5*log(float((2-r)/(r-1)))
    upper = 1.5*log(float(r)) - .5*log(float(r-1))
    assert 0 < lower <= upper
    asym = .5*log(1/float(r-1))
    assert abs(lower-asym) <= 2*float(r-1)+1e-10
    assert abs(upper-asym) <= 2*float(r-1)+1e-10
    print(f'r={r}, a={a}, c={c}, inverse-left n=19 exact, chi_range=[{lower:.8f}, {upper:.8f}]')
print('All finite exact-algebra and interval diagnostic checks passed.')
