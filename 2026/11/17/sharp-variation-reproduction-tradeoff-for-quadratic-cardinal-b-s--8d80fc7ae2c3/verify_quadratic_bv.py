#!/usr/bin/env python3
"""Exact rational verification of the centered quadratic-spline BV calculation."""
from fractions import Fraction as F
from random import Random


def t(x):
    return max(F(0), F(1)-abs(x))


def b2(x):
    r=abs(x)
    if r<=F(1,2): return F(3,4)-r*r
    if r<=F(3,2): return (F(3,2)-r)**2/2
    return F(0)


def b2prime(x):
    r=abs(x)
    if r<=F(1,2): return -2*x
    if r<=F(3,2): return (F(3,2)-r)*(-1 if x>0 else 1)
    return F(0)


def g(x, a):
    return -a*t(x+F(3,2))+(1+2*a)*t(x+F(1,2))-a*t(x-F(1,2))


def abs_linear_integral(u,v,length):
    if u*v>=0:
        return length*(abs(u)+abs(v))/2
    return length*(u*u+v*v)/(2*(abs(u)+abs(v)))


def exact_var(d,a):
    points=sorted({F(j)+h for j in d for h in (F(-5,2),F(-3,2),F(-1,2),F(1,2),F(3,2))})
    def f(x):return sum(c*g(x-F(j),a) for j,c in d.items())
    return sum((abs_linear_integral(f(u),f(v),v-u) for u,v in zip(points,points[1:])), F(0))


def constant(a):
    return 1+2*a+2*a*a/(1+3*a)


def main():
    rng=Random(20261114)
    for x in [F(i,12) for i in range(-35,36)]:
        assert b2prime(x)==t(x+F(1,2))-t(x-F(1,2))
        assert sum(b2(x-j) for j in range(-10,11))==1
        assert sum(j*b2(x-j) for j in range(-10,11))==x
        assert sum(j*j*b2(x-j) for j in range(-10,11))==x*x+F(1,4)
    print('CARDINAL_SPLINE_DERIVATIVE_AND_MOMENTS_PASS',71)
    for a in [F(0),F(1,32),F(1,8),F(1,4),F(1,2),F(1)]:
        k=constant(a)
        assert exact_var({0:F(1)},a)==k
        neg=a+a*a/(1+3*a)
        assert k==1+2*neg
    assert constant(F(1,8))==F(14,11)
    assert constant(F(0))==1
    print('EXACT_STEP_FORMULAS_AND_QUADRATIC_REPRODUCTION_PASS',F(14,11))
    for a in [F(0),F(1,8),F(1,4),F(1)]:
        for _ in range(240):
            d={j:F(rng.randrange(-6,7), rng.randrange(1,7)) for j in range(-5,6)}
            v=exact_var(d,a)
            assert v<=constant(a)*sum(map(abs,d.values()))
    print('EXACT_MULTI_JUMP_BV_BOUND_PASS',960)
    for a in [F(0),F(1,32),F(1,8),F(1,4),F(1,2),F(1)]:
        # Equality is attained by a step at any integer site.
        for j in (-10,0,7):
            assert exact_var({j:F(1)},a)==constant(a)
    print('TRANSLATION_INVARIANT_SHARPNESS_PASS',18)
    print('ALL_QUADRATIC_QUASI_INTERPOLANT_TESTS_PASS')
if __name__=='__main__':main()
