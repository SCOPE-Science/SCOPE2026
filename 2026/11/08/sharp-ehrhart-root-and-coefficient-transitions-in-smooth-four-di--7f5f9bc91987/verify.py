#!/usr/bin/env python3
"""Exact self-contained checks for the four-dimensional smooth Cayley family.

Run: python3 verify.py
Uses only the Python standard library. Finite checks of polynomial identities
are exhaustive because rigorous degree bounds are established in RESULT.md.
"""
from fractions import Fraction as F
from math import comb


def count_lattice(c, m):
    assert c >= 0 and m >= 0
    return sum(comb(m + c*j + 2, 2)*((c+1)*m-c*j+1)
               for j in range(m+1))


def predicted_ehrhart(c, t):
    a = c*c+6*c+6
    b = -c*c+6*c+12
    return F((t+1)*((c+2)*t+4)*(a*t*t+b*t+6),24)


def predicted_hstar(c):
    return [1, (c+1)*(c+7), F((c+1)*(c*c+11*c+8),2),
            F(c*(c+1)*(c+1),2), 0]


def ehrhart_coefficients(c):
    return [F(1), F(-(2*c*c-15*c-42),12),
            F(-(c+6)*(c*c-10*c-18),24),
            F(8*c*c+33*c+30,12),
            F((c+2)*(c*c+6*c+6),24)]


def hdisc(c):
    h = predicted_hstar(c)
    d,b,a = F(h[0]),F(h[1]),F(h[2])
    w = F(h[3])
    return b*b*a*a-4*w*b*b*b-4*a*a*a*d-27*w*w*d*d+18*w*a*b*d


def hdisc_expected(c):
    q = (c**7+27*c**6+298*c**5+1714*c**4+5258*c**3+
         8416*c*c+6696*c+2112)
    return F((c+1)**3*q,4)


def test():
    count=0
    # The original lattice-slice sum and the proposed factorization are
    # polynomials of bidegree <= (3,4) in (c,t). This complete 4x5 grid
    # is an exact, non-asymptotic polynomial-identity certificate.
    for c in range(4):
        for t in range(5):
            assert count_lattice(c,t)==predicted_ehrhart(c,t)
            count+=1
    # For each c, h*_j is the finite difference of lattice counts.
    # Both it and predicted h*_j have degree <=3 in c, hence four
    # c-values suffice to certify equality for every nonnegative c.
    for c in range(4):
        h=predicted_hstar(c)
        for j in range(5):
            actual=sum((-1)**(j-k)*comb(5,j-k)*count_lattice(c,k)
                       for k in range(j+1))
            assert actual==h[j]
            count+=1
    # The degree-10 discriminant identity is certified by 11 points.
    for c in range(11):
        assert hdisc(c)==hdisc_expected(c)
        count+=1
    # Confirm the derived coefficient phase diagram and root discriminant.
    for c in range(101):
        ec=ehrhart_coefficients(c)
        assert ec[0]==1
        assert all(x>0 for x in ec[3:5])
        assert (ec[1]<0)==(c>=10)
        assert (ec[2]<0)==(c>=12)
        assert (c*c*(c*c-12*c-12)>0)==(c>=13)
        assert hdisc(c)>0
        count+=6
    # Explicit values at the boundaries.
    assert ehrhart_coefficients(12)==[1,F(-11,2),F(-9,2),F(263,2),F(259,2)]
    count+=1
    print('VERIFY_OK',count)


if __name__=='__main__':
    test()
