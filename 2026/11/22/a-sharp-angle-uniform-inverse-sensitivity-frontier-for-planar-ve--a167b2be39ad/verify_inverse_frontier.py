#!/usr/bin/env python3
"""Exact rational consistency checks for the planar inverse-sensitivity frontier.

This tests matrix identities and finite rational parameter samples. The proof of
uniformity over all parameters and angles is in RESULT.md, not in this script.
"""
from fractions import Fraction as Q
from random import Random
from math import sqrt


def det2(a,b,c,d):
    return a*d-b*c


def check(a,t,g,u):
    # (cos theta,sin theta) is an exact rational unit vector.
    c=(1-u*u)/(1+u*u)
    s=2*u/(1+u*u)
    v11=a+(t-a)*c*c
    v22=a+(t-a)*s*s
    off=(t-a)*c*s
    j11=1+v11
    j12=g*off
    j21=off
    j22=1+g*v22
    # J.T J - I, with exact rational matrix multiplication.
    d11=j11*j11+j21*j21-1
    d12=j11*j12+j21*j22
    d22=j12*j12+j22*j22-1
    det=det2(d11,d12,d12,d22)
    d=a*t
    w=off*off
    expected=d*g*(4+2*v11+g*(2*v22+d))-(1-g)**2*w
    assert det==expected, (a,t,g,u,det,expected)
    assert d11+d22>0
    return det


def test():
    r=Random(319141)
    count=0
    for i in range(1729):
        a=Q(r.randrange(1,100),r.randrange(1,40))
        t=Q(r.randrange(1,100),r.randrange(1,40))
        if a<t: a,t=t,a
        g=Q(r.randrange(1,100),100)
        u=Q(r.randrange(-35,36),r.randrange(1,30))
        val=check(a,t,g,u)
        d=a*t;S=a+t;D=a-t
        F=d*g*(4+S*(1+g))-(1-g)**2*D*D/4
        if F>=0: assert val>=0
        if D>0:
            z0=2*d*g/(D*(1-g))
            K=(1-g)**2*D*D/4
            atz0=d*g*(4+S*(1+g)+g*d-D*(1-g)*z0)-K*(1-z0*z0)
            assert atz0==F
            if F<0: assert 0<z0<1
        count+=1
    # Realizable, strictly monotone counterexample: A=[[5/2,-3/2],[-3/2,5/2]].
    a,t,g=Q(4),Q(1),Q(1,50)
    v11=v22=Q(5,2);off=-Q(3,2)
    J=(Q(7,2),-Q(3,100),-Q(3,2),Q(21,20))
    j11,j12,j21,j22=J
    e11=j11*j11+j21*j21-1
    e12=j11*j12+j21*j22
    e22=j12*j12+j22*j22-1
    assert det2(e11,e12,e12,e22)==-Q(2853,2000)
    symoff=(j12+j21)/2
    assert det2(j11,symoff,symoff,j22)==Q(123591,40000)
    assert j11>0
    # Exact achievability of local susceptibilities: M(s)=16s/(1+3s), at s=1.
    assert Q(16,1)/(1+Q(3,1))==a
    assert Q(16,1)/(1+Q(3,1))**2==t
    count+=5
    print('VERIFY_OK',count)

if __name__=='__main__': test()
