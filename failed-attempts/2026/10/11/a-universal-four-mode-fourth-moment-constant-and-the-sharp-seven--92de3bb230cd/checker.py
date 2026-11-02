#!/usr/bin/env python3
"""Independent numerical checks of four-mode fourth-moment identities and bounds.
No external packages required; the accompanying algebraic proof covers all groups.
"""
import cmath
import math
import random


def root():
    def p(t):
        return 3*t*t*t+3*t*t-3*t-1
    a,b=1/3,1.0
    for _ in range(90):
        m=(a+b)/2
        if p(m)>0:
            b=m
        else:
            a=m
    return (a+b)/2


def sharp(t):
    return (3*t**4+12*t*t+4*t+3)/(2*(1+t*t)**2)


def corr(c,s):
    return sum(c[j+s]*c[j].conjugate() for j in range(4-s))


def moment_coeff(c):
    return sum(abs(z)**2 for z in c)**2+2*sum(abs(corr(c,s))**2 for s in (1,2,3))


def moment_finite(c,n):
    return sum(abs(sum(c[j]*cmath.exp(2j*math.pi*j*k/n) for j in range(4)))**4
               for k in range(n))/n


def normalized(c,m):
    return m / sum(abs(z)**2 for z in c)**2


def run():
    t=root()
    K=sharp(t)
    assert .7925172139<t<.7925172141
    assert 2.8088401654<K<2.8088401656
    assert abs(3*t**3+3*t*t-3*t-1)<2e-14
    for n,expected in ((4,4),(5,13/4),(6,23/8)):
        assert abs(normalized([1]*4,moment_finite([1]*4,n))-expected)<1e-12
        assert expected>K
    rr=random.Random(104093)
    tests=0
    for n in (7,8,9,11,16,32,47):
        for _ in range(500):
            c=[complex(rr.uniform(-1,1),rr.uniform(-1,1)) for _ in range(4)]
            m=moment_finite(c,n)
            assert abs(m-moment_coeff(c))<3e-10
            assert normalized(c,m)<K+2e-10
            tests+=1
        for _ in range(80):
            lam=complex(rr.uniform(-2,2),rr.uniform(-2,2))
            theta=rr.uniform(-math.pi,math.pi)
            c=[lam * ([t,1,1,t][j])*cmath.exp(1j*theta*j) for j in range(4)]
            assert abs(normalized(c,moment_finite(c,n))-K)<3e-10
            tests+=1
    # Analytic identity at the normalized extremizer.
    a,b=t,1.
    lhs=moment_coeff([a,b,b,a])
    rhs=2*(3*a**4+12*a*a*b*b+4*a*b**3+3*b**4)
    assert abs(lhs-rhs)<1e-12
    print('PASS',tests,'randomized finite-group cases + special orders; root=',repr(t),'sharp=',repr(K))


if __name__=='__main__':
    run()
