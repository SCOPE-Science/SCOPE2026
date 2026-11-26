#!/usr/bin/env python3
"""Independent numerical consistency checks for explicit Poisson Gabor bounds.

Scientific calculations only; numerical spot checks do not prove universal theorems.
"""
import math
import cmath


def approx(a, b, rtol=2e-8, atol=2e-8):
    if abs(a - b) > atol + rtol * max(abs(a), abs(b)):
        raise AssertionError((a, b, abs(a-b)))


def closed(w, q):
    t = math.pi * w
    coth = lambda a: 1.0 / math.tanh(a)
    csch = lambda a: 1.0 / math.sinh(a)
    sech2 = lambda a: 1.0 / math.cosh(a) ** 2
    a = (math.pi / w)**2 * (math.tanh(t)*csch(2*t/q) - 0.5*q*sech2(t))
    b = (math.pi / w)**2 * (coth(t)*coth(2*t/q) + 0.5*q*csch(t)**2)
    return a,b


def zak_rational(w, x, s):
    r = math.exp(-2 * math.pi * w)
    u = cmath.exp(2j * math.pi * x)
    a = r**s-r**(2-s)
    b = r**(1-s)-r**(1+s)
    den = 1+r*r-2*r*math.cos(2*math.pi*x)
    return math.pi/w * cmath.exp(2j*math.pi*s*x) * (a+b/u) / den


def zak_direct(w, x, s, K=5000):
    return sum(cmath.exp(-2j*math.pi*k*s) / ((x+k)**2 + w*w)
               for k in range(-K, K+1))


def multiplier(w, q, x, omega, func):
    return sum(abs(func(w,x,omega+j/q))**2 for j in range(q))


def geometric_extrema(w,q):
    r=math.exp(-2*math.pi*w)
    k=(1-r*r)/(1-r**(2/q))
    hm=2*k*r**(1/q)
    h0=k*(1+r**(2/q))
    return ((math.pi/w)**2*(hm-2*q*r)/(1+r)**2,
            (math.pi/w)**2*(h0+2*q*r)/(1-r)**2)


def test():
    cases=((0.13,2),(0.41,3),(0.86,5),(1.3,2),(2.1,4))
    for w,q in cases:
        a,b=closed(w,q)
        ag,bg=geometric_extrema(w,q)
        assert 0<a<b
        approx(a,ag,rtol=1e-9)
        approx(b,bg,rtol=1e-9)
        approx(a,multiplier(w,q,0.5,0.5/q,zak_rational),rtol=1e-9)
        approx(b,multiplier(w,q,0.,0.,zak_rational),rtol=1e-9)
        # Strict global bounds at interior nonextremal fibers.
        for x in (0.0,0.17,0.31,0.5):
            for n in range(9):
                s=n/(9*q)
                y=multiplier(w,q,x,s,zak_rational)
                assert a-1e-9<=y<=b+1e-9
        # Direct Zak-series check with no dependence on the rational formula.
        for x,s in ((0.21,0.17),(0.,0.27),(0.5,0.5/q)):
            if s > 1: continue
            approx(zak_direct(w,x,s),zak_rational(w,x,s),rtol=2e-6,atol=2e-6)
    for q in (2,3,5):
        tiny=0.002
        a,b=closed(tiny,q)
        target=math.pi**4*(q-1/q)/3
        assert abs(a/target-1)<0.0003
        assert abs(b*tiny**4/q-1)<0.0003
        w=8.
        a,b=closed(w,q)
        assert abs(a/(2*math.pi**2/w**2*math.exp(-2*math.pi*w/q))-1)<0.03
        assert abs(b/(math.pi**2/w**2)-1)<0.03
    print('CHECK_OK: independent direct Zak sums, rational fiber bounds and asymptotics')

if __name__=='__main__':
    test()
