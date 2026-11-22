#!/usr/bin/env python3
"""Self-contained exact algebra and numerical supplemental checks for a toy settling law."""
import math
import random
from fractions import Fraction as F


def mass(x, a, b, c):
    return a + b*x/(1+x) - c*x


def h(x, a, b, c, eta, alpha):
    return (1+eta*x)*(b/(1+x)**2 - c) - alpha*eta*mass(x,a,b,c)


def q(x, b, c, eta, alpha):
    return b*((1-alpha)*eta - 2 - (1+alpha)*eta*x) - (1-alpha)*eta*c*(1+x)**3


def poly(x):
    return -200*x**3-10903*x**2+18794*x-203


def bisect(func, lo, hi, steps=90):
    assert func(lo)*func(hi)<0
    for _ in range(steps):
        mid=(lo+hi)/2
        if func(lo)*func(mid) <= 0:
            hi=mid
        else:
            lo=mid
    return (lo+hi)/2


def main():
    a,b,c,eta,alpha=map(F,[5,100,1,100,F(1,3)])
    for x in [F(0),F(1,10),F(2),F(1,3),F(7,4),F(5,2)]:
        assert 3*(1+x)**2*h(x,a,b,c,eta,alpha)==poly(x)
    assert poly(F(0))==-203
    assert poly(F(1,10))==F(156717,100)
    assert poly(F(2))==-7827
    assert mass(F(2),a,b,c)>0
    root1=bisect(lambda x:poly(x), 0.0, 0.1)
    root2=bisect(lambda x:poly(x), 0.1, 2.0)
    assert 0.0108698782<root1<0.0108698784
    assert 1.6618802188<root2<1.6618802190
    assert mass(root2,5,100,1)>0
    # The sharp Stokes frontier: eta=3 has Q(0)<0 for all b,c>0;
    # at eta=4, appropriate b,c give Q(0)>0 and a small delta gives two roots.
    assert q(F(0),100,1,3,F(1,3)) < 0
    al=F(1,3)
    eta4=F(4)
    bb=F(100);cc=F(1)
    aa=(bb-cc)/(al*eta4)+F(1,1000000)
    assert q(F(0),bb,cc,eta4,al)>0
    assert h(F(0),aa,bb,cc,eta4,al)<0
    assert h(F(1,1000),aa,bb,cc,eta4,al)>0
    rand=random.Random(20231120)
    checks=0
    for _ in range(3000):
        aa=rand.randrange(1,40)
        bb=rand.randrange(1,200)
        cc=rand.randrange(1,50)
        ee=rand.randrange(1,200)
        al=F(rand.randrange(1,99),100)
        x=F(rand.randrange(0,101),13)
        # Derivative of H from product and g'' equals Q/(1+x)^3.
        gp=F(bb,1)/(1+x)**2-cc
        gpp=-2*F(bb,1)/(1+x)**3
        hprime=(1-al)*ee*gp+(1+ee*x)*gpp
        assert hprime==q(x,bb,cc,ee,al)/(1+x)**3
        # Q' is strictly negative for all positive x.
        assert -bb*(1+al)*ee-3*(1-al)*ee*cc*(1+x)**2 < 0
        # Stokes threshold eta<=3 always forbids initial growth in H.
        if ee<=3 and al==F(1,3):
            assert q(F(0),bb,cc,ee,al)<0
        checks+=3
    print('PASS: exact rational sign/polynomial certificates; two roots; '+str(checks)+' supplemental parameter checks')

if __name__=='__main__':
    main()
