#!/usr/bin/env python3
"""Exact-rational reproduction for a two-step scalar positivity classification."""
from fractions import Fraction as F


def coefficients(k, z):
    D = 3 + 2*k - k*k
    d = D + 2*z
    alpha0 = (3*k-1)/(k-3)
    alpha1 = 4*(1-k)/(k-3)
    beta0, beta1, beta2 = 2*k*k/D, 4*k/D, F(2)/D
    B = -(alpha1 + z*beta1)/(1+z*beta2)
    C = (alpha0 + z*beta0)/(1+z*beta2)
    assert B == 4*(1-k*k-k*z)/d
    assert C == ((1-3*k)*(1+k)+2*k*k*z)/d
    q = 1/(1+z)
    assert (B*B-4*C)*d*d == 4*(1+k)**3*((1+k)-2*(1-k)*z)
    assert (q*q-B*q+C)*d*(1+z)**2 == z*z*(2*k*k*z+(1+k)**2)
    assert (2*q-B)*d*(1+z) == 2*(2*k*k*z+k*k+2*k*z*z+2*k*z+2*k+1)
    return B, C, q


def radius(k):
    return ((1+k)/(2*(1-k)) if k <= F(1,2) else (1-k*k)/k)


def first_negative(k, z, steps=500):
    B, C, q = coefficients(k,z)
    u,v = F(1),q
    for n in range(2,steps+1):
        u,v = v, B*v-C*u
        if v < 0:
            return n
    return None


def run():
    params = (F(0), F(1,8), F(1,4), F(2,5), F(1,2), F(3,5), F(3,4), F(9,10))
    configs = 0
    for k in params:
        R = radius(k)
        for scale in (F(1,3), F(4,5), F(1), F(6,5), F(3,2)):
            z = R*scale
            B,C,q = coefficients(k,z)
            if scale <= 1:
                u,v = F(1),q
                for _ in range(120):
                    u,v=v,B*v-C*u
                    assert v >= 0, (k,z)
            else:
                assert first_negative(k,z,500) is not None, (k,z)
            configs+=1
    assert radius(F(0)) == F(1,2)
    assert radius(F(1,2)) == F(3,2)
    assert radius(F(3,4)) == F(7,12)
    B,C,q=coefficients(F(1,2),F(3,2))
    assert (B,C,q)==(F(0),F(0),F(2,5))
    print('CHECK_OK: %d exact-rational parameter cases; source and characteristic identities verified' % configs)


if __name__=='__main__':
    run()
