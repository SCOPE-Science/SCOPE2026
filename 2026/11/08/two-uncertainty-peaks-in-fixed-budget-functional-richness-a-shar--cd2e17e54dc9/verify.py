"""Exact diagnostics for the profile (1,m,m), Python 3 standard library."""
from fractions import Fraction
from math import comb


def variance(m, k):
    mass = first = second = 0
    for singleton in range(2):
        for left in range(m + 1):
            right = k - singleton - left
            if 0 <= right <= m:
                count = comb(m, left) * comb(m, right)
                f = singleton + (left != 0) + (right != 0)
                mass += count
                first += count * f
                second += count * f * f
    assert mass == comb(2*m+1,k)
    return Fraction(mass*second-first**2, mass**2)


for m in range(6, 101):
    early = variance(m, 3) - variance(m, 4)
    later = variance(m, m) - variance(m, m-1)
    early_numerator = 5*m**4-42*m**3+123*m**2-94*m+24
    assert early == Fraction(early_numerator, 4*(2*m-1)**2*(2*m+1)**2)
    B = comb(2*m+1,m)
    Q = 4*m**6+28*m**5+61*m**4+58*m**3+25*m**2+4*m
    assert later == Fraction(2*B**2-(10*m**3+15*m**2+5*m)*B+Q, B**2*(2*m+1)**2)
    assert early > 0 and later > 0
print('PASS: 95 exact checks of both identities and signs (m=6..100)')
