"""Deterministic numerical checks for a finite-width Gaussian reset-clock law.
The analytic proof, not this finite test, establishes the universal assertions.
"""
import math
import random


def reward(t, contrast, omega=1.0):
    y = -math.expm1(-omega * t)
    return (contrast * contrast / 2) * y * y / (1 + contrast * y)


def derivative(t, contrast, omega=1.0):
    y = -math.expm1(-omega * t)
    return (contrast * contrast * omega / 2) * (1-y) * y * (2+contrast*y) / (1+contrast*y)**2


def second(t, contrast, omega=1.0):
    y = -math.expm1(-omega * t)
    cubic = 2 - 4*y - 3*contrast*y*y - contrast*contrast*y**3
    return (contrast * contrast * omega**2 / 2) * (1-y) * cubic / (1+contrast*y)**3


def bisect(f, a, b, repeats=100):
    fa, fb = f(a), f(b)
    assert fa * fb < 0, (a, b, fa, fb)
    for _ in range(repeats):
        m = (a+b)/2
        if m == a or m == b: return m
        fm = f(m)
        if fm * fa > 0:
            a, fa = m, fm
        else:
            b, fb = m, fm
    return (a+b)/2


def inflection(contrast, omega=1.0):
    c = contrast
    y = bisect(lambda z: 2 - 4*z - 3*c*z*z - c*c*z**3, 0.0, 1.0)
    return -math.log1p(-y)/omega


def tangency(contrast, delta, omega=1.0):
    ti = inflection(contrast, omega)
    if delta >= ti: return None
    def h(t):
        return (t-delta)*derivative(t,contrast,omega)-(reward(t,contrast,omega)-reward(delta,contrast,omega))
    hi=max(ti*4,delta+8/omega)
    while h(hi)>0:
        hi*=2
    return bisect(h,ti,hi)


def envelope(t, contrast, delta, omega=1.0):
    tangent=tangency(contrast,delta,omega)
    if tangent is None or t>=tangent:
        return reward(t,contrast,omega)
    return reward(delta,contrast,omega)+(t-delta)*(reward(tangent,contrast,omega)-reward(delta,contrast,omega))/(tangent-delta)


def check():
    count=0
    rng=random.Random(260528)
    for contrast in (0.1,1.0,10.0,100.0):
        for omega in (0.6,1.0,2.3):
            ti=inflection(contrast,omega)
            assert ti>0; count+=1
            for delta in (0.15*ti,0.5*ti,0.85*ti):
                tang=tangency(contrast,delta,omega)
                assert ti<tang<tangency(contrast,0.0,omega);count+=1
                slope=(reward(tang,contrast,omega)-reward(delta,contrast,omega))/(tang-delta)
                assert abs(slope-derivative(tang,contrast,omega))<1e-9*max(1,slope);count+=1
                for j in range(101):
                    x=delta+(tang*3-delta)*j/100
                    assert envelope(x,contrast,delta,omega)+1e-11*max(1,reward(x,contrast,omega))>=reward(x,contrast,omega)
                    count+=1
                for fraction in (0.25,0.5,0.8,1.3):
                    mean=delta+(tang-delta)*fraction
                    optimum=envelope(mean,contrast,delta,omega)
                    for _ in range(50):
                        lo=delta+rng.random()*(mean-delta)
                        hi=mean+rng.random()*(tang*4-mean)
                        w=(mean-lo)/(hi-lo)
                        value=(1-w)*reward(lo,contrast,omega)+w*reward(hi,contrast,omega)
                        assert value<=optimum+1e-10*max(1,optimum), (contrast,delta,mean,lo,hi,value,optimum)
                        count+=1
            for delta in (ti,1.5*ti):
                for j in range(21):
                    x=delta+(2*ti)*j/20
                    assert second(x+1e-9,contrast,omega)<1e-8
                    count+=1
    c,w,delta,mean=1.0,1.0,0.2,0.4
    tangent=tangency(c,delta,w)
    p=(mean-delta)/(tangent-delta)
    value=(1-p)*reward(delta,c,w)+p*reward(tangent,c,w)
    assert abs(tangent-0.6617551020847849)<2e-10
    assert abs(value/reward(mean,c,w)-1.0295092537459483)<2e-10
    print('PASS',count,'checks; c=1, omega=1, delta=0.2, mean=0.4: tangent=',round(tangent,12),'gain=',round(value/reward(mean,c,w)-1,12))

if __name__=='__main__':
    check()
