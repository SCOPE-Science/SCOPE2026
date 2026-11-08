#!/usr/bin/env python3
"""Reproduce the exact two-state common-environment fourth-cumulant factorization.

Standard-library-only; arithmetic uses fractions rather than floating-point
or a symbolic factorization library. These checks supplement the proof.
"""
from fractions import Fraction as F
from itertools import product


def solve2(A,B,C,D,r,s):
    det=A*D-B*C
    assert det!=0
    return ((D*r-B*s)/det, (A*s-C*r)/det)


def cov_from_stationary_moments(a,b,c,d,p,q,D1,D2):
    pi0=q/(p+q); pi1=p/(p+q)
    t1=solve2(a+p,-q,-p,b+q,2*D1*pi0,2*D1*pi1)
    t2=solve2(c+p,-q,-p,d+q,2*D2*pi0,2*D2*pi1)
    z=solve2(a+c+p,-q,-p,b+d+q,
             2*D1*t2[0]+2*D2*t1[0],
             2*D1*t2[1]+2*D2*t1[1])
    return sum(z)-sum(t1)*sum(t2)


def factored_formula(a,b,c,d,p,q,D1,D2):
    N=(a*b+a*d+a*p+2*a*q+b*c+2*b*p+b*q+c*d+c*p+2*c*q+
       2*d*p+d*q+2*(p+q)**2)
    K1=a*b+a*q+b*p
    K2=c*d+c*q+d*p
    K12=(a+c)*(b+d)+(a+c)*q+(b+d)*p
    assert N>0 and K1>0 and K2>0 and K12>0
    return (4*D1*D2*p*q*(a-b)*(c-d)*N /
            ((p+q)**2*K1*K2*K12))


def run():
    n=0
    cases=[F(1), F(2), F(4), F(7)]
    rates=[(F(1),F(1)),(F(2),F(5)),(F(7),F(3))]
    for a,b,c,d in product(cases,repeat=4):
        for p,q in rates:
            for D1,D2 in [(F(1),F(1)),(F(3,2),F(4,3))]:
                direct=cov_from_stationary_moments(a,b,c,d,p,q,D1,D2)
                factor=factored_formula(a,b,c,d,p,q,D1,D2)
                assert direct==factor,(a,b,c,d,p,q,D1,D2,direct,factor)
                expected=(a-b)*(c-d)
                assert (direct>0)-(direct<0)==(expected>0)-(expected<0)
                n+=1
    a,b,c,d,p,q,D1,D2=map(F,[1,4,5,2,2,3,1,1])
    negative=factored_formula(a,b,c,d,p,q,D1,D2)
    assert negative<0
    print('PASS:',n,'exact independent rational moment/factorization checks')
    print('Counter-switching example:',negative,'=',float(negative))

if __name__=='__main__':
    run()
