#!/usr/bin/env python3
"""Reproducible checks for two-reach oxygen-deficit extrema; standard library only.

Analytic proofs, not these finite tests, establish all quantified results.
"""
import math
import random
from fractions import Fraction as Q
from math import factorial


def exp_bounds_pos(x, n=36):
    """Exact rational strict lower/upper bounds on exp(x), x>=0."""
    assert isinstance(x, Q) and x >= 0 and x < n + 2
    s = sum((x**j / factorial(j) for j in range(n+1)), Q(0))
    term = x**(n+1) / factorial(n+1)
    return s, s + term / (1-x/Q(n+2))


def exp_neg_bounds(x):
    lower, upper = exp_bounds_pos(x)
    return 1/upper, 1/lower


def ln3_bounds(n=45):
    lo = 2*sum((Q(1, 2)**(2*j+1)/Q(2*j+1) for j in range(n)), Q(0))
    tail = 2*Q(1,2)**(2*n+1)/Q(2*n+1)/(1-Q(1,4))
    return lo, lo+tail


def switch_expression_bounds(d):
    # Example rates a=1, b=3, c=1: x_2(d)=d+(1+exp(-2d))/2
    ell, ehi = exp_neg_bounds(2*d)
    return d+(1+ell)/2, d+(1+ehi)/2


def check_exact_bracket():
    l3lo, l3hi = ln3_bounds()
    for d, direction in [(Q(1), -1), (Q(6,5), 1),
                         (Q(1091575, 1000000), -1),
                         (Q(1091576, 1000000), 1)]:
        lo, hi = switch_expression_bounds(d)
        if direction == -1:
            assert hi < Q(3,2)*l3lo
        else:
            assert lo > Q(3,2)*l3hi
    assert l3hi < 2  # then ln(3)/2 < 1
    return 'Exact rational Taylor/atanh bounds certify 1.091575 < d_* < 1.091576'


def upstream(a, b, t):
    return math.exp(-a*t)*(-math.expm1(-(b-a)*t))/(b-a)


def zfun(a, b, d):
    return -math.expm1(-(b-a)*d)/(b-a)


def post(a, b, c, d, x):
    assert x >= d
    lag=x-d
    z=zfun(a,b,d)
    if abs(c-a)<1e-10:
        h=lag*math.exp(-a*lag)
    else:
        h=math.exp(-a*lag)*(-math.expm1(-(c-a)*lag))/(c-a)
    return math.exp(-a*d)*(z*math.exp(-c*lag)+h)


def post_slope(a,b,c,d,x):
    return math.exp(-a*x)-c*post(a,b,c,d,x)


def peak_lag(a,b,c,d):
    z=zfun(a,b,d)
    if abs(c-a)<1e-10:
        return 1/a-z
    return (math.log(c/a)+math.log1p(-(c-a)*z))/(c-a)


def run_random_checks():
    rng=random.Random(44082611)
    count=0
    double_count=0
    monotone_count=0
    for _ in range(20000):
        a=rng.uniform(.2,2.0)
        b=a+rng.uniform(.2,2.8)
        c=b*rng.uniform(.1,.96)
        x0=math.log(b/a)/(b-a)
        d=x0*rng.uniform(.15,4)
        z=zfun(a,b,d)
        u=upstream(a,b,d)
        assert math.isclose(u, math.exp(-a*d)*z, rel_tol=1e-12)
        assert math.isclose(post(a,b,c,d,d),u,rel_tol=1e-12)
        right=math.exp(-a*d)*(1-c*z)
        assert math.isclose(post_slope(a,b,c,d,d),right,rel_tol=1e-11,abs_tol=1e-14)
        t=peak_lag(a,b,c,d)
        # A positive lag is equivalent to an increasing postboundary slope.
        assert (t>0)==(right>0)
        if t>1e-8:
            xp=d+t
            assert math.isclose(post_slope(a,b,c,d,xp),0,abs_tol=5e-13)
            peak=post(a,b,c,d,xp)
            assert math.isclose(peak,math.exp(-a*xp)/c,rel_tol=5e-12)
            h=min(t/3, .03)
            assert post(a,b,c,d,xp-h)<peak and post(a,b,c,d,xp+h)<peak
        if d>x0 and t>1e-8:
            double_count+=1
            eps=min(.02, (d-x0)/4)
            assert upstream(a,b,x0-eps)<upstream(a,b,x0)
            assert upstream(a,b,x0+eps)<upstream(a,b,x0)
            assert right>0
        # Only compare positive lag stationary points.
        d1=x0*(1+rng.uniform(.002,.12))
        d2=d1+x0*rng.uniform(.002,.12)
        t1,t2=peak_lag(a,b,c,d1),peak_lag(a,b,c,d2)
        if t1>0 and t2>0:
            x1,x2=d1+t1,d2+t2
            assert x2>x1
            p1,p2=post(a,b,c,d1,x1),post(a,b,c,d2,x2)
            assert p1>p2
            # Lower downstream reaeration for longer gives larger deficit for fixed x.
            x=d2+max(t2, .1)
            assert post(a,b,c,d1,x)>post(a,b,c,d2,x)
            monotone_count+=1
        count+=1
    return count,double_count,monotone_count



def u_for_logconcave(a, p, b, t):
    """Quadrature of U_b(t) for f(t)=exp(-a*t-p*t*t), p>0."""
    n=400
    h=t/n
    def g(s):
        return math.exp(-b*(t-s)-a*s-p*s*s)
    return h/3*(g(0)+g(t)+4*sum(g(h*j) for j in range(1,n,2))
                +2*sum(g(h*j) for j in range(2,n,2)))


def check_logconcave_sources():
    rng=random.Random(442026)
    for _ in range(250):
        a=rng.uniform(.2,1.5)
        p=rng.uniform(.05,.9)
        b=rng.uniform(.7,3.1)
        old=float('inf')
        for j in range(1,16):
            t=.12*j
            f=math.exp(-a*t-p*t*t)
            R=f/u_for_logconcave(a,p,b,t)
            assert R<old-1e-8
            old=R
    return '3750 monotone ratio comparisons for nonexponential log-concave demand inputs'


def main():
    print(check_exact_bracket())
    print(check_logconcave_sources())
    n,dc,mc=run_random_checks()
    print('Random parameter triples checked:',n)
    print('Double-sag local-max cases checked:',dc)
    print('Strict second-location/height monotonicity pairs checked:',mc)
    a,b,c=1.,3.,1.
    x0=math.log(3)/2
    H=math.exp(-x0)/3
    for d in (1.,1.2):
        x2=d+peak_lag(a,b,c,d)
        P=post(a,b,c,d,x2)
        print('d = %.1f, upstream peak = %.12f, downstream peak = %.12f, second location = %.12f' % (d,H,P,x2))
        assert (P>H) if d==1. else (P<H)
    print('All finite supplemental checks passed.')

if __name__=='__main__':
    main()
