#!/usr/bin/env python3
"""Standalone reproducibility diagnostics for surface-boundary visibility of concentric shells.
Only the Python standard library is required. Tests do not replace the general proof.
"""
from fractions import Fraction
from math import acos, comb, cos, exp, gamma, isclose, lgamma, pi, sin, sqrt, erf
from random import Random


def q(d, s):
    """Exact spherical angular cap probability, numerically integrated by smooth-angle Simpson."""
    assert d >= 2 and -1 <= s <= 1
    angle = acos(s)
    c = exp(lgamma(d / 2) - lgamma((d - 1) / 2)) / sqrt(pi)
    n = 4096
    h = angle / n
    summation = 0.0
    for j in range(n + 1):
        theta = j * h
        summation += (1 if j in (0, n) else (4 if j % 2 else 2)) * sin(theta) ** (d - 2)
    return c * h * summation / 3


def visible_probability(d, t):
    u = t ** (d - 1)
    return (q(d, 2 * t * t - 1) + 2 * u * q(d, t)) / (1 + u)**2


def q_odd_exact(d, s):
    """Independent exact polynomial integration when ambient d is odd."""
    assert d >= 3 and d % 2 == 1
    s = Fraction(s)
    m = (d - 3) // 2
    def anti(z):
        return sum((Fraction((-1)**k * comb(m, k), 2*k + 1) * z**(2*k+1)
                    for k in range(m+1)), Fraction(0))
    return (anti(Fraction(1)) - anti(s)) / (anti(Fraction(1)) - anti(Fraction(-1)))


def v_odd_exact(d, t):
    t = Fraction(t)
    u = t**(d-1)
    return (q_odd_exact(d, 2*t*t-1)+2*u*q_odd_exact(d,t))/(1+u)**2


def direct_mc(d, t, count, rng):
    inner_weight=t**(d-1)/(1+t**(d-1))
    matches=0
    for _ in range(count):
        vecs=[]
        for _ in range(2):
            v=[rng.gauss(0,1) for _ in range(d)]
            norm=sqrt(sum(z*z for z in v))
            rad=t if rng.random()<inner_weight else 1.0
            vecs.append([rad*z/norm for z in v])
        x,y=vecs
        diff=[y_i-x_i for x_i,y_i in zip(x,y)]
        norm2=sum(z*z for z in diff)
        alpha=max(0.,min(1.,-sum(a*b for a,b in zip(x,diff))/norm2))
        mindist2=sum((a+alpha*b)**2 for a,b in zip(x,diff))
        if mindist2 >= t*t - 1e-12:
            matches+=1
    return matches/count


def thin_c(d):
    cd=exp(lgamma(d/2)-lgamma((d-1)/2))/sqrt(pi)
    return cd*2**((d-1)/2)*(2**(d-1)+2)/(4*(d-1))


def ld_approx(d,t):
    s=abs(2*t*t-1)
    return (1-s*s)**((d-1)/2)/(s*sqrt(2*pi*d))


def check():
    exact=0
    for d in (3,5,7,9):
        for t in [Fraction(1,6),Fraction(2,5),Fraction(3,5),Fraction(4,5)]:
            v=v_odd_exact(d,t)
            assert 0<v<1
            assert abs(float(v)-visible_probability(d,float(t)))<3e-11
            exact+=1
    for t in [Fraction(1,5),Fraction(2,5),Fraction(4,5)]:
        assert v_odd_exact(3,t)==(1-t**3)/(1+t*t)**2
        exact+=1
    for d in (2,3,4,5,9,20):
        values=[visible_probability(d,j/20) for j in range(1,20)]
        assert all(v1>v2 for v1,v2 in zip(values,values[1:]))
        for t in (.2,.3,.6,.83):
            v2=visible_probability(d,sqrt(1-t*t))
            assert visible_probability(d,t)+v2 < 1-1e-12
        exact+=1
    for t in (.25,.5,.8):
        assert abs(visible_probability(2,t)-2*acos(t)/(pi*(1+t)))<1e-12
        exact+=1
    for d in (2,3,4,5,8):
        ratio=visible_probability(d,1-1e-5)/(thin_c(d)*1e-5**((d-1)/2))
        assert abs(ratio-1)<.0005,(d,ratio)
    for d in (80,160):
        for t in (.55,.8):
            r=(1-visible_probability(d,t)) if t < 1/sqrt(2) else visible_probability(d,t)
            assert .72 < r/ld_approx(d,t) < 1.09,(d,t,r/ld_approx(d,t))
        for lam in (-2,-1,0,1,2):
            t=sqrt((1+lam/sqrt(d))/2)
            target=.5*(1-erf(lam/sqrt(2)))
            assert abs(visible_probability(d,t)-target)<.035,(d,lam,visible_probability(d,t),target)
    rng=Random(17290341)
    cases=[(2,.3),(2,.7),(3,.4),(3,.75),(4,.45),(4,.78),(6,.55),(6,.85)]
    errs=[]
    for d,t in cases:
        empirical=direct_mc(d,t,24000,rng)
        expected=visible_probability(d,t)
        errs.append(abs(empirical-expected))
        assert abs(empirical-expected)<.025,(d,t,empirical,expected)
    print('VERIFY_OK exact_rational_and_monotonic_checks=%d independent_segment_mc_cases=%d max_mc_deviation=%.5f thin_shell_and_large_dimension_checks=passed' % (exact,len(cases),max(errs)))

if __name__=='__main__':
    check()
