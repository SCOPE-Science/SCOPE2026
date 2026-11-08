#!/usr/bin/env python3
"""Exact rational checks for the two-band spherical Poisson norm formula.

Uses only the Python standard library. These finite checks supplement the
analytical proof; they are not a proof of an all-dimensional assertion.
"""
from fractions import Fraction as F
from math import sqrt


def moment(d,k):
    if k == 0:
        return F(1)
    z = F(1)
    for j in range(1,k+1):
        z *= F(2*j-1,d+2*j-2)
    return z


def coeffs(d):
    d=F(d)
    a=3*d/(d+2)
    b=3*(10*d-8)/(d+4)
    c=3*(d+2)*(5*d*d-13*d+12)/((d-1)*(d+4)*(d+6))
    return a,b,c


def direct_zonal_moments(d):
    # X=omega_1, Z=X^2-1/d, omega uniform on sphere.
    dd=F(d)
    v1=moment(d,1)
    v2=moment(d,2)-2*moment(d,1)/dd+F(1)/(dd*dd)
    x4=moment(d,2)
    x2z2=moment(d,3)-2*moment(d,2)/dd+moment(d,1)/(dd*dd)
    z4=sum(F((-1)**(4-k)*__import__('math').comb(4,k),dd**(4-k))*moment(d,k) for k in range(5))
    return v1,v2,x4,x2z2,z4


def maxval(d,r):
    a,b,c=coeffs(d)
    if not r:
        return F(0),F(1)
    r0=2*a/b
    if r<=r0:
        return a*r*r,F(1)
    s=(b*r-2*c*r*r)/(2*(b*r-a-c*r*r))
    assert 0<s<1
    m=r*r*(a*s*s+b*r*s*(1-s)+c*r*r*(1-s)**2)
    closed=(b*b-4*a*c)*r**4/(4*(b*r-a-c*r*r))
    assert m==closed
    return m,s


def verify():
    trials=0
    for d in list(range(2,21)) + [25,40,80,120]:
        a,b,c=coeffs(d)
        V1,V2,X4,X2Z2,Z4=direct_zonal_moments(d)
        assert a==X4/V1**2
        assert b==6*X2Z2/(V1*V2)
        assert c==Z4/V2**2
        assert c>=a and b>2*c
        assert 0<2*a/b<=F(1,2)
        for r in [F(1,20),F(1,5),F(1,3),F(1,2),F(3,4),F(1)]:
            m,s=maxval(d,r)
            alpha2=s/V1
            beta2=(1-s)/V2
            direct=(r*r*alpha2**2*X4+6*r**3*alpha2*beta2*X2Z2+r**4*beta2**2*Z4)
            assert direct==m,(d,r,direct,m)
            trials+=1
    for d in range(2,80):
        for r in (F(1,5),F(1,2),F(1)):
            assert maxval(d+1,r)[0]>maxval(d,r)[0]
    # Rational threshold brackets for contractive radius squared.
    for d,lo,hi in [(2,F(75266,100000),F(75267,100000)),
                    (3,F(66029,100000),F(66030,100000)),
                    (4,F(61261,100000),F(61262,100000))]:
        assert maxval(d,lo)[0]<1<maxval(d,hi)[0]
    a,b,c=F(3),F(30),F(15)
    def gauss(r):
        r0=2*a/b
        if r<=r0:return a*r*r
        return (b*b-4*a*c)*r**4/(4*(b*r-a-c*r*r))
    assert gauss(F(45164,100000))<1<gauss(F(45165,100000))
    print('EXACT_SPHERICAL_ZONAL_EIGHTH_MOMENTS_OK',trials,'CASES')
    print('DIMENSION_MONOTONE_AND_SHARP_THRESHOLD_BRACKETS_OK')
    print('ALL_TWO_BAND_SPHERICAL_POISSON_CHECKS_PASSED')

if __name__=='__main__':
    verify()
