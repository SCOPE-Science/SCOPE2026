#!/usr/bin/env python3
"""Exact finite checks and asymptotic sanity tests of Mallows boundary fixed-point law."""
from fractions import Fraction
from itertools import permutations
from math import exp, log

def qint(m,q):
    return sum((q**i for i in range(m)),Fraction(0))

def inv(p):
    return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

def check(n,q):
    Z=Fraction(0); e1=e2=en=e12=e1n=Fraction(0)
    for p in permutations(range(1,n+1)):
        w=q**inv(p); Z+=w
        f1=p[0]==1; f2=p[1]==2; fn=p[-1]==n
        e1+=w*f1;e2+=w*f2;en+=w*fn;e12+=w*f1*f2;e1n+=w*f1*fn
    e1/=Z;e2/=Z;en/=Z;e12/=Z;e1n/=Z
    z=qint(n,q);h=qint(n-1,q)
    assert Z==__import__('math').prod(qint(k,q) for k in range(1,n+1))
    assert e1==1/z and en==1/z
    assert e2==(1+sum(q**i for i in range(3,n+1)))/(z*h)
    assert e12==e1n==1/(z*h)
    assert e12-e1*e2==(q+q*q-q**n)/(z*z*h)
    assert e1n-e1*en==q**(n-1)/(z*z*h)
    return 6
count=0
for n in range(3,8):
    for q in (Fraction(1,5),Fraction(1,2),Fraction(3,4),Fraction(1),Fraction(6,5),Fraction(2),Fraction(5)):
        count+=check(n,q)
for n in (3,4,5,10,100,1000):
    lo=1.;hi=2.
    for _ in range(80):
        mid=(lo+hi)/2
        if (n-1)*log(mid)>log(1+mid):hi=mid
        else:lo=mid
    root=(lo+hi)/2
    if n==3: assert abs(root-(1+5**.5)/2)<1.e-12
    assert abs(n*log(root)-log(2))<max(1,12/n)  # coarse independent asymptotic check
for beta in (-2,0,0.5,log(2),1.5):
    n=10000
    q=exp(beta/n)
    L= -__import__('math').expm1(beta)/(-beta) if beta else 1
    qa= (q+q*q-exp(beta)) / ( ((exp(beta)-1)/(q-1) if beta else n)**2 * (sum(q**k for k in range(n-1))))
    predicted=(2-exp(beta))/L**3
    assert abs(n**3*qa-predicted)<0.02
print('VERIFY_OK',count,'exact identities; phase roots and weak-bias limits checked')
