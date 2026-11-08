#!/usr/bin/env python3
"""Exact-rational supplementary checks of a sharp imaginary-axis stability formula."""
from fractions import Fraction as F


def sq_abs(z):
    x, y = z
    return x*x + y*y


def complex_mul(x, y):
    a, b = x
    c, d = y
    return (a*c-b*d, a*d+b*c)


def P_at_iy(y, u, v):
    # P(iy)=1+iy-(u+iv)y**2; all arithmetic remains exact.
    return (1-u*y*y, y-v*y*y)


def check():
    count = 0
    for an in range(0, 12):
        for bn in range(0, 12):
            if an+bn == 0:
                continue
            # Rational scale cancels from the dimensionless frontier.
            a, b = F(an, 7), F(bn, 7)
            A, B = 2*a/(a+b), 2*b/(a+b)
            u = (a+b)**2/(2*(a*a+b*b))
            v = (a*a-b*b)/(2*(a*a+b*b))
            assert A+B == 2
            assert u == 2/(A*A+B*B)
            assert v == (A-B)/(A*A+B*B)
            assert u*u+v*v == u
            assert 1-2*u == -u*A*B
            count += 5
            for j in range(-28, 29):
                y = F(j, 10)
                lhs = sq_abs(P_at_iy(y,u,v))-1
                rhs = u*y*y*(y-A)*(y+B)
                assert lhs == rhs
                assert (lhs <= 0) == (-B <= y <= A)
                count += 2
            # Verify endpoint disks when the corresponding width is positive.
            for c, sign in ((A,1),(B,-1)):
                if c:
                    re_center = 1/(c*c)
                    im_center = sign/c
                    assert (u-re_center)**2+(v-im_center)**2 == 1/(c**4)
                    count += 1
            # Real-coefficient optimum and exact gain.
            h = 2/(a+b)
            h_real = 1/max(a,b)
            assert h/h_real == 2*max(a,b)/(a+b)
            assert F(1) <= h/h_real <= F(2)
            count += 2
    # Nontrivial mixed-band rational witness.
    a, b = F(3), F(1)
    assert 2/(a+b) == F(1,2)
    assert (a+b)**2/(2*(a*a+b*b)) == F(4,5)
    assert (a*a-b*b)/(2*(a*a+b*b)) == F(2,5)
    count += 3
    print('CHECKS_OK', count)


if __name__ == '__main__':
    check()
