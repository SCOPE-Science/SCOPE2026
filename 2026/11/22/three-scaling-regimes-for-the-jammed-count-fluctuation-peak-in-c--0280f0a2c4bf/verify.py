"""Reproduce beta-kernel finite-shell calculations and singular-peak checks.

Requires Python 3, numpy, scipy. Deterministic checks are numerical, not proofs.
"""
from math import exp, log, sqrt
import numpy as np
from scipy.optimize import brentq
from scipy.special import betainc


def H(a, b, e):
    return betainc(a, b, e) + betainc(b, a, e)


def params(p, left, right):
    assert 0 < p < 1 and left in ('+', '-') and right in ('+', '-')
    ma = p if left == '+' else 1-p
    mb = p if right == '+' else 1-p
    return ma, mb


def prob(e, t, ma, mb):
    assert 0 < e < .5 and 0 < t <= 1
    q, h, k = ma*mb, ma*(1-mb)+(1-ma)*mb, (1-ma)*(1-mb)
    return q*H(2-t, 2-t, e) + h*H(t, 2-t, e) + k*H(t, t, e)


def brute_prob(e, t, p, left, right):
    output = 0.0
    for a in '+-':
        for b in '+-':
            a_shape = 2-t if a == left else t
            b_shape = 2-t if b == right else t
            output += (p if a=='+' else 1-p)*(p if b=='+' else 1-p)*H(a_shape,b_shape,e)
    return output


def root(t, ma, mb):
    # Solving in the logarithm of the normalized gap avoids underflow
    # for the exponentially small case. This bracket suffices for tests.
    f = lambda s: prob(exp(-s), t, ma, mb) - .5
    s = brentq(f, log(2)+1e-12, 500, xtol=1e-12)
    e = exp(-s)
    return e/(1-e)


def run():
    checks=0
    for p in (.23,.5,.73,.9):
        for a in '+-':
            for b in '+-':
                ma,mb=params(p,a,b)
                for t in (.02,.1,.5,1.):
                    for e in (.0005,.01,.11,.3,.49):
                        assert abs(prob(e,t,ma,mb)-brute_prob(e,t,p,a,b)) < 3e-15
                        checks+=1
                    values=[prob(e,t,ma,mb) for e in (.00001,.01,.05,.15,.3,.49)]
                    assert all(x<y for x,y in zip(values,values[1:]))
                    d=root(t,ma,mb); E=d/(1+d)
                    assert abs(prob(E,t,ma,mb)-.5)<1e-11
                    assert abs(prob(E,t,ma,mb)*(1-prob(E,t,ma,mb))-.25)<1e-12
                    checks+=3

    # Exponential, critical, and fixed-spacing regimes for ++ boundaries.
    for p in (.5,1/sqrt(2),.9):
        ma,mb=params(p,'+','+')
        w=1-ma*mb
        for t in (.05,.02,.01,.005):
            d=root(t,ma,mb)
            if w>.500000001:
                scaled=t*log(1/d)
                assert abs(scaled-log(2*w))<.04
            elif w<.499999999:
                e=d/(1+d)
                g=6*e*e-4*e**3
                assert abs(g-(.5-w)/(1-w))<.02
            else:
                ratio=d/sqrt(t*log(1/t)/12)
                assert abs(ratio-1)<.12
            checks+=1

    rng=np.random.default_rng(260828289)
    for p,t,left,right in ((.6,.2,'+','+'),(.25,.7,'+','-'),(.85,.1,'-','-')):
        e=.2; ma,mb=params(p,left,right)
        size=100000
        a=(rng.random(size)<p)
        b=(rng.random(size)<p)
        left_plus=(left=='+'); right_plus=(right=='+')
        ashape=np.where(a==left_plus,2-t,t)
        bshape=np.where(b==right_plus,2-t,t)
        y=rng.beta(ashape,bshape)
        observed=np.mean((y<e)|(y>1-e))
        expected=prob(e,t,ma,mb)
        assert abs(observed-expected)<.012,(observed,expected)
        checks+=1
    print('PASS: numerical/analytic consistency checks', checks)


if __name__ == '__main__':
    run()
