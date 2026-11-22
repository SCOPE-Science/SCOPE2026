"""Reproduce exact three-cohort first-rain optimum and test the event model.

Requires only the Python 3 standard library. Numerical tests supplement the
closed-form argument in RESULT.md; they do not certify a continuum theorem.
"""
import math
import random
from fractions import Fraction

P1 = (8 - math.sqrt(10.0)) / 9
P2 = (3 + math.sqrt(9 + 48 * P1 * (1-P1)**2)) / 8


def probability(p, u, v):
    if u == 0:
        return p/2
    return (p/2*(1+u+v) - p*p/3*(u*u+v*v+v*v/u)
            + p**3/4*v**3/u)


def z(y):
    return (8*y-6)/(y*(9*y-8))


def g(p, y):
    q = z(y)
    return 3*p+3*y-4*p*p*q-4*y*y*q-2*y*y+3*y**3*q


def optimum(p):
    if not (0 < p <= 1):
        raise ValueError('p must be in (0,1]')
    if p <= P1:
        return 1., 1.
    if p <= P2:
        return 1., P1/p
    lo, hi = P1, .75
    for _ in range(72):
        m = (lo+hi)/2
        if g(p,m) < 0:
            lo = m
        else:
            hi = m
    y = (lo+hi)/2
    u = z(y)
    return u, u*y/p


def simpson(f, a, b, n=8000):
    if b <= a:
        return 0.
    h = (b-a)/n
    return h/3*(f(a)+f(b)+4*sum(f(a+i*h) for i in range(1,n,2))
                +2*sum(f(a+i*h) for i in range(2,n,2)))


def event_integral(p, u, v):
    t2, t3 = -math.log(u), -math.log(v)
    def f(r, dates):
        failure = 1.
        for t in dates:
            failure *= 1-p*math.exp(-(r-t))
        return math.exp(-r)*(1-failure)
    return (simpson(lambda r:f(r,[0.]),0.,t2)
            +simpson(lambda r:f(r,[0.,t2]),t2,t3)
            +simpson(lambda r:f(r,[0.,t2,t3]),t3,t3+35.))


def exact_identity():
    # Equality between the monotone G-expression and its quartic numerator.
    for p in (Fraction(1,4),Fraction(2,3),Fraction(1,1)):
        for y in (Fraction(3,5),Fraction(2,3),Fraction(7,10)):
            zz = (8*y-6)/(y*(9*y-8))
            lhs = 3*p+3*y-4*p*p*zz-4*y*y*zz-2*y*y+3*y*y*y*zz
            num = 6*y**4-7*y**3+27*p*y*y-(32*p*p+24*p)*y+24*p*p
            assert lhs == num/(y*(9*y-8))
    return 9


def main():
    tests = exact_identity()
    assert 0 < P1 < .75 < P2 < 1
    for p in (.01,.1,.4,P1, .6, .8,P2,.9,1.):
        u,v = optimum(p)
        assert 0 < v <= u <= 1 + 1e-12, (p,u,v)
        assert 0 < probability(p,u,v) < 1
        if p > P2:
            y = p*v/u
            assert P1 < y < .75
            assert abs(g(p,y)) < 1e-10, (p,y,g(p,y))
        tests += 4
    rng = random.Random(20260302)
    for _ in range(18000):
        p = rng.uniform(.0001,1.)
        u,v = optimum(p)
        probe_u = rng.uniform(.0001,1.)
        probe_v = probe_u * rng.random()
        assert probability(p,u,v) + 2e-13 >= probability(p,probe_u,probe_v), (p,probe_u,probe_v)
    tests += 18000
    for _ in range(65):
        p = rng.uniform(.05,1.)
        u = rng.uniform(.2,1.)
        v = u*rng.uniform(.1,1.)
        analytic = probability(p,u,v)
        integrated = event_integral(p,u,v)
        assert abs(analytic-integrated) < 8e-11, (p,u,v,analytic,integrated)
    tests += 65
    for p in (P1-1e-8,P1,P1+1e-8,P2-1e-8,P2,P2+1e-8,1):
        u,v=optimum(p)
        for du in (-1e-5,0,1e-5):
            uu=min(1.,max(.00001,u+du))
            vv=min(uu,v)
            assert probability(p,u,v)+1e-10>=probability(p,uu,vv)
            tests += 1
    print(f'PASS: {tests} checks of rational identities, event integrals, regime boundaries and feasible calendars')
    print(f'p1={P1:.12f}; p2={P2:.12f}')
    u,v=optimum(1.)
    print('p=1 optimal dates:',0., -math.log(u),-math.log(v))
    print('p=1 establishment:',probability(1.,u,v))


if __name__=='__main__':
    main()
