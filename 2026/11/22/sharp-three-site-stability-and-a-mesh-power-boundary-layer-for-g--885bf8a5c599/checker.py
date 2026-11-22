#!/usr/bin/env python3
"""Numerical corroboration of a three-site generalized rational interpolation theorem.
All global and asymptotic assertions require the separate analytic proof.
Uses only Python's standard library.
"""
import math
import random
from fractions import Fraction


def blend_weight(x, gamma):
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    logratio = gamma * (math.log(x) - math.log1p(-x))
    if logratio > 40.0:
        return 1.0 / (1.0 + math.exp(-logratio))
    if logratio < -40.0:
        return math.exp(logratio) / (1.0 + math.exp(logratio))
    return 1.0 / (1.0 + math.exp(-logratio))


def cardinal(x, a, gamma):
    w = blend_weight(x, gamma)
    return ((1-w)*(1-x/a),
            (1-w)*x/a + w*(1-(x-a)/(1-a)),
            w*(x-a)/(1-a))


def objective(x, a, gamma):
    return (a-x)/(1-a) * blend_weight(x, gamma)


def scalar_max(a, gamma):
    # Stationarity has one root by strict monotonicity of its ratio.
    lo, hi = 0.0, a
    for _ in range(120):
        x=(lo+hi)/2
        w=blend_weight(x,gamma)
        k=gamma*(a-x)*(1-w)/(x*(1-x))
        if k>1:
            lo=x
        else:
            hi=x
    return objective((lo+hi)/2,a,gamma)


def minimum_bound(a,gamma):
    return 1+2*max(scalar_max(a,gamma),scalar_max(1-a,gamma))


def t_root(gamma):
    lo,hi=0.0,1.0
    for _ in range(200):
        t=(lo+hi)/2
        q=gamma*(1-t*t)-2*t*(1+t**gamma)
        if q>0: lo=t
        else: hi=t
    return (lo+hi)/2


def delta(gamma):
    t=t_root(gamma)
    return (1-t)/(1+t)*t**gamma/(1+t**gamma)


def lambert_w_positive(z):
    w=math.log1p(z)
    for _ in range(60):
        f=w*math.exp(w)-z
        df=(1+w)*math.exp(w)
        new=w-f/df
        if abs(new-w)<1e-14:
            return new
        w=new
    raise AssertionError('Lambert iteration')


def exact_blend(a,x,gamma,ys):
    # Direct signed blending formula with exact rational arithmetic.
    x0,x1,x2=Fraction(0),a,Fraction(1)
    assert x not in (x0,x1,x2)
    p0=ys[0]+(ys[1]-ys[0])*(x-x0)/(x1-x0)
    p1=ys[1]+(ys[2]-ys[1])*(x-x1)/(x2-x1)
    lam0=Fraction(1,1)/((x-x0)*(x-x1))**gamma
    lam1=Fraction((-1)**gamma,1)/((x-x1)*(x-x2))**gamma
    return (lam0*p0+lam1*p1)/(lam0+lam1)


def main():
    rng=random.Random(20231107)
    count=0
    for gamma in (1,2,3,4,7,13):
        for a in (Fraction(1,7),Fraction(2,5),Fraction(1,2),Fraction(5,6)):
            for x in (Fraction(1,11),Fraction(3,8),Fraction(7,9)):
                if x==a: continue
                ys=(Fraction(1,6),Fraction(1,3),Fraction(7,8))
                w=x**gamma/(x**gamma+(1-x)**gamma)
                p0=ys[0]+(ys[1]-ys[0])*x/a
                p1=ys[1]+(ys[2]-ys[1])*(x-a)/(1-a)
                assert exact_blend(a,x,gamma,ys)==(1-w)*p0+w*p1
                count+=1
    assert t_root(1)>0 and abs(t_root(1)-1/3)<1e-13
    assert abs(delta(1)-1/8)<1e-14
    assert abs(delta(2)-0.0674422488681)<1e-10
    count+=3

    for _ in range(360):
        gamma=rng.randrange(1,30)
        a=rng.uniform(.05,.95)
        x=rng.random()
        c=cardinal(x,a,gamma)
        lebesgue=sum(abs(t) for t in c)
        assert abs(sum(c)-1)<3e-12
        if x<a:
            assert c[0]>=-1e-13 and c[1]>=-1e-13 and c[2]<=1e-13
            assert abs(lebesgue-(1-2*c[2]))<2e-12
        else:
            assert c[0]<=1e-13 and c[1]>=-1e-13 and c[2]>=-1e-13
            assert abs(lebesgue-(1-2*c[0]))<2e-12
        count+=1

    for gamma in (1,2,3,4,8,16,32):
        centered=minimum_bound(.5,gamma)
        assert abs(centered-(1+2*delta(gamma)))<5e-10
        for a in (.1,.2,.35,.49,.51,.7,.9):
            assert minimum_bound(a,gamma)>centered+1e-11
            count+=1
    for a in (.2,.35,.65,.8):
        estimate=minimum_bound(a,1200)
        limit=1/min(a,1-a)-1
        assert 0<limit-estimate<.035
        count+=1

    for beta in (-1.,-.5,0.,.25,.5,1.,2.):
        gamma=1400
        a=.5+beta/gamma
        scaled=gamma*(minimum_bound(a,gamma)-1)
        limit=lambert_w_positive(math.exp(4*abs(beta)-1))
        assert abs(scaled-limit)<.024
        count+=1

    assert abs(1500*(minimum_bound(.5,1500)-1)-lambert_w_positive(math.exp(-1)))<5e-5
    count+=1
    print('PASS: %d exact rational and numerical corroboration cases' % count)
    print('gamma=1 centered minimum Lebesgue constant: %.12f' % (1+2*delta(1)))
    print('gamma=2 centered minimum Lebesgue constant: %.12f' % (1+2*delta(2)))
    print('sharp scaled limit W(exp(-1)): %.12f' % lambert_w_positive(math.exp(-1)))

if __name__=='__main__':
    main()
