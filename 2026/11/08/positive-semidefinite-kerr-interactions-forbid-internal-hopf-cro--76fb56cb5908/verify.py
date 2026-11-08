#!/usr/bin/env python3
"""Standalone arithmetic and spectral checks for the stated Kerr dimer theorem.
Only Python's standard library is required; finite checks do not prove the theorem.
"""
from fractions import Fraction as F
from cmath import sqrt as csqrt
from math import sqrt, isclose


def sample(a,b,chi,I):
    assert a>0 and b>a and chi>0 and I>0
    eps=(b-a)/(2*b)
    ie=I*(1-eps); io=I*(1+eps)
    de=a*ie+b*io+chi
    do=b*ie+a*io-chi
    t=4*chi*a*(ie-io)
    d=16*chi*chi*ie*io*(b*b-a*a)
    kc2=2*b*chi*I*(3*b+5*a)/a
    om2=2*a*chi*I*(b-a)/b
    assert ie>0 and io>0 and t<0 and d>0
    assert a*ie+b*io==de-chi
    assert b*ie+a*io==do+chi
    assert t==-2*om2
    assert t*t-2*kc2*t-4*d==0
    assert (4*d-t*t)/(-2*t)==kc2
    assert om2>0 and kc2>0
    # Check the imaginary-root and companion-pair factorization coefficientwise.
    # (z²+w²)[(z+k)²+w²] = z^4 +2k z³ +(k²+2w²)z²+2kw²z +w²(k²+w²).
    assert kc2-t==kc2+2*om2
    assert -t==2*om2
    assert d==om2*(kc2+om2)
    # At fixed susceptiblity chi, changing k changes G=sqrt(chi²+k²/4).
    # The four spectral roots are obtained from two roots of z(z+k)=mu.
    for fraction in [F(3,5),F(9,10),F(1),F(11,10),F(7,5)]:
        k=sqrt(float(kc2))*float(fraction)
        tf=float(t); df=float(d)
        mu1=(tf+csqrt(tf*tf-4*df))/2
        mu2=(tf-csqrt(tf*tf-4*df))/2
        roots=[]
        for mu in [mu1,mu2]:
            roots.append((-k+csqrt(k*k+4*mu))/2)
            roots.append((-k-csqrt(k*k+4*mu))/2)
        largest=max(z.real for z in roots)
        if fraction<F(1):assert largest>1e-10, (a,b,largest)
        elif fraction>F(1):assert largest< -1e-10, (a,b,largest)
        else:
            assert abs(largest)<1e-9 and abs(sorted((abs(z.imag) for z in roots))[-1]-sqrt(float(om2)))<1e-9
        G=sqrt(float(chi)**2+k*k/4)
        assert isclose(G*G-k*k/4,float(chi*chi),rel_tol=1e-10,abs_tol=1e-10)
    slope=-2*float(om2)/(float(kc2)+4*float(om2))
    assert -0.5<slope<0
    return (eps,kc2,om2)


def run():
    cases=0
    for q in [F(101,100),F(11,10),F(5,4),F(3,2),F(2),F(3),F(10)]:
        for a in [F(1,3),F(1),F(2),F(5,2)]:
            for chi in [F(1,2),F(1),F(7,3)]:
                eps,kc2,om2=sample(a,a*q,chi,F(5,3))
                assert eps==(q-1)/(2*q)
                cases+=1
    eps,kc2,om2=sample(F(1),F(3,2),F(1),F(1))
    assert eps==F(1,6) and kc2==F(57,2) and om2==F(2,3)
    print('PASS:',cases,'exact-rational dimer parameter checks; Hopf spectral comparisons on both sides, and exact witness')
    print('Scope: tests are finite; arbitrary-size finite-matrix statements are analytical.')


if __name__=='__main__':run()
