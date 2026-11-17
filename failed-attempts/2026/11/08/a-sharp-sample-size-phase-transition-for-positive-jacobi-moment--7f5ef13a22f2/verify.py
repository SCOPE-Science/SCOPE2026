"""Reproducible arithmetic/numerical checks of the quadratic quadrature theorem.

Uses Python standard library only. No finite test establishes the asymptotic assertions.
"""
from fractions import Fraction
from itertools import combinations
from math import log, pi, sqrt
from random import Random


def allowed(nodes, tau):
    neg = [-x for x in nodes if x < 0]
    pos = [x for x in nodes if x > 0]
    return bool(neg and pos) and min(neg)*min(pos) <= tau <= max(neg)*max(pos)


def triple_supported(nodes, tau):
    for a, b, c in combinations(nodes, 3):
        weights = ((tau+b*c)/((a-b)*(a-c)),
                   (tau+a*c)/((b-a)*(b-c)),
                   (tau+a*b)/((c-a)*(c-b)))
        if all(w >= 0 for w in weights):
            assert sum(weights) == 1
            assert a*weights[0] + b*weights[1] + c*weights[2] == 0
            assert a*a*weights[0] + b*b*weights[1] + c*c*weights[2] == tau
            return True
    return False


def simpson(f, lo, hi, n=12000):
    assert n % 2 == 0
    h = (hi-lo)/n
    acc = f(lo) + f(hi)
    for i in range(1,n):
        acc += (4 if i % 2 else 2)*f(lo + h*i)
    return h*acc/3


def events(m, t, n=12000):
    spread = 2.0**(1-m)
    aa = simpson(lambda u:(1+u)**(m-1)-u**(m-1),0,t,n)
    bb = simpson(lambda u:(u+t/u)**(m-1)-u**(m-1),t,1,n)
    spread += m*(aa+bb)/2.0**m
    center = m/2.0**m*simpson(lambda u:(2-u-t/u)**(m-1)-(1-u)**(m-1),t,1,n)
    return spread,center


def probability(m,t,n=12000):
    return (m/2.0**m)*simpson(
        lambda u:(1+u)**(m-1)+(1-u)**(m-1)
                  -(u+t/u)**(m-1)-(2-u-t/u)**(m-1), t,1,n)


def check():
    rng=Random(260926)
    count=0
    for m in range(3,9):
        for tau in (Fraction(1,3),Fraction(1,9),Fraction(4,5)):
            for _ in range(120):
                xs=rng.sample([Fraction(k,103) for k in range(-102,103) if k],m)
                assert allowed(xs,tau)==triple_supported(xs,tau)
                count+=1
    for m in range(2,13):
        for t in (0.05,0.1715728752538099,1/3,0.8):
            p=probability(m,t)
            a,b=events(m,t)
            assert abs(p+a+b-1)<3e-10,(m,t,p,a,b)
            assert -1e-10<=p<=1+1e-10,(m,t,p)
            count+=1
    for t in (0.05,0.11,0.1715728752538099,1/3,0.8):
        exact=1.5*t*(log(1/t)-1+t)
        assert abs(probability(3,t)-exact)<1e-11
        assert abs(probability(4,t)-2*exact)<1e-11
        count+=2
    t=1/3
    assert abs(probability(3,t)-(log(3)/2-1/3))<1e-11
    assert abs(probability(4,t)-(log(3)-2/3))<1e-11
    count+=2
    for t in (0.05,0.1715728752538099,1/3):
        r=sqrt(t);m=120
        a,b=events(m,t,30000)
        ap=2/(1-t)*((1+t)/2)**m
        bp=sqrt(pi*r/(2*(1-r)))*sqrt(m)*(1-r)**m
        assert abs(a/ap-1)<0.06,(t,'spread',a/ap)
        assert abs(b/bp-1)<0.06,(t,'center',b/bp)
        count+=2
    print('PASS:',count,'exact-rational consistency cases and numerical identities/checks')
    for t in (1/3,3-2*sqrt(2),1/9):
        a,b=events(60,t,30000)
        print('tau',t,'P60 failure decomposition:',a,b,'P3:',1.5*t*(log(1/t)-1+t))

if __name__=='__main__':
    check()
