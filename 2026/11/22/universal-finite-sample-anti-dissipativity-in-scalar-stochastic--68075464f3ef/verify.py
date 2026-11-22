#!/usr/bin/env python3
"""Reproduce exact finite arithmetic checks for the circle SDMD-R instability theorem."""
from fractions import Fraction as F
from itertools import product


def ratio(c):
    return -c / (2 + c)


def empirical(cs, ridge=F(0)):
    numerator = sum((2+c)*(-c) for c in cs)
    denominator = sum((2+c)**2 for c in cs) + len(cs)*ridge
    return numerator/denominator


def q(h, z):
    return 1+h*z+h*h*z*z/2


def run():
    checks=0
    G=F(4)+F(1,2)
    H=-F(1,2)
    assert G==F(9,2) and H/G == -F(1,9)
    checks+=2
    for h in [F(1,100),F(1),F(9),F(17),F(18),F(19)]:
        v=q(h,-F(1,9))
        assert (v<1)==(h<F(18)) and v>0
        checks+=1
    assert ratio(-F(1,2))==F(1,3)
    checks+=1
    B=[-F(1),-F(7,8),-F(3,4),-F(5,8),-F(1,2)]
    for m in range(1,6):
        for cs in product(B,repeat=m):
            z=empirical(cs)
            assert z>=F(1,3)
            for h in [F(1,8),F(1),F(3)]:
                assert q(h,z)>=q(h,F(1,3))>1
                checks+=1
            checks+=1
    # Positivity persists under a nonnegative scalar ridge, with a uniform event floor.
    for m in range(1,5):
        for cs in product(B,repeat=m):
            for gamma in [F(0),F(1,4),F(2)]:
                z=empirical(cs,gamma)
                assert z>=F(3)/(F(9)+4*gamma)
                checks+=1
    print(f'PASS: {checks} exact-rational assertions; finite-grid checks are not an infinite proof.')


if __name__=='__main__':
    run()
