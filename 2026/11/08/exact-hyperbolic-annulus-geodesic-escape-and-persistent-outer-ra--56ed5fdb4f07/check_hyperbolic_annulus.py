#!/usr/bin/env python3
"""Independent numerical diagnostics for area-uniform hyperbolic-annulus geodesic escape.
Scientific diagnostic only; the analytic proof is in RESULT.md.
"""
import math
import random


def closed(a, b):
    assert 0 < a < b
    c, C = math.cosh(a), math.cosh(b)
    psi = math.acos(math.tanh(a) / math.tanh(b))
    J = C * psi - math.atan(math.sqrt(C*C - c*c) / math.sinh(a))
    return 1 - 2*J/(math.pi * (C-c))


def quad(a, b, n=16000):
    assert n % 2 == 0
    h = (b-a) / n
    t = math.tanh(a)
    def fn(r):
        return math.sinh(r)*math.acos(min(1.0, t/math.tanh(r)))
    z = fn(a)+fn(b)
    for k in range(1,n):
        z += (4 if k % 2 else 2)*fn(a+k*h)
    return 1-2*h*z/(3*math.pi*(math.cosh(b)-math.cosh(a)))


def single_check(a,b,count,seed):
    rng = random.Random(seed)
    ch_a, ch_b = math.cosh(a), math.cosh(b)
    hits = 0
    for _ in range(count):
        r = math.acosh(rng.uniform(ch_a,ch_b))
        s = math.acosh(rng.uniform(ch_a,ch_b))
        angle = rng.random()*math.pi
        R, S = math.sinh(r), math.sinh(s)
        C, D = math.cosh(r), math.cosh(s)
        # Hyperboloid metric: cosh(d) = cosh(r)cosh(s)-sinh(r)sinh(s)cos(angle).
        cd = C*D-R*S*math.cos(angle)
        shd = math.sqrt(max(0.0,cd*cd-1))
        # Foot lies on the segment iff radial distance decreases initially
        # and increases finally. Otherwise minimum is an endpoint.
        foot_in_segment = (D < C*cd) and (C < D*cd)
        if foot_in_segment:
            # Lorentzian plane-normal formula, independent of Klein tangents.
            minrad = math.asinh(abs(R*S*math.sin(angle))/shd)
        else:
            minrad = min(r,s)
        hits += minrad < a
    value = hits/count
    expected = closed(a,b)
    tolerance = 6*math.sqrt(max(1e-8,expected*(1-expected))/count) + 0.002
    assert abs(value-expected)<tolerance,(a,b,value,expected,tolerance)
    return value


def main():
    cases = [(0.2,0.8),(0.5,1.5),(1,2),(0.3,7),(2,2.0003)]
    for i,(a,b) in enumerate(cases):
        f=closed(a,b)
        q=quad(a,b)
        assert 0<f<1,(a,b,f)
        assert abs(f-q)<3e-6,(a,b,f,q)
        mc=single_check(a,b,36000, 981237+i)
        print('case',a,b,'exact',f,'quadrature',q,'hyperboloid_Monte_Carlo',mc)
    a=1.0
    assert closed(a,a+0.001)>closed(a,a+0.1)>closed(a,2)>closed(a,5)>closed(a,14)
    limit=2/math.pi*math.asin(math.tanh(a))
    assert abs(closed(a,14)-limit)<1e-5
    eps=1e-4
    asym=4/(3*math.pi)*math.sqrt(2*eps/(math.sinh(a)*math.cosh(a)))
    assert abs((1-closed(a,a+eps))/asym-1)<0.002
    a,b=.6,2.5
    eu=1-2/math.pi*(b*b*math.acos(a/b)-a*math.sqrt(b*b-a*a))/(b*b-a*a)
    k=.002
    assert abs(closed(k*a,k*b)-eu)<2e-5
    print('HYPERBOLIC_ANNULUS_EXACT_AND_INDEPENDENT_SEGMENT_TESTS_OK')


if __name__=='__main__':
    main()
