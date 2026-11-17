"""Finite diagnostic checks for the two-sample exponential kernel result.

Run: python3 check.py
Only the Python standard library is required. These are diagnostics, not proofs.
"""
import math
import random


def value(p, h, x):
    x=max(0.0,min(h,x))  # avoid floating roundoff at the grid endpoints
    return (math.sinh(x)/math.sinh(h))**p + (math.sinh(h-x)/math.sinh(h))**p


def critical(p):
    return 2*math.atanh(math.sqrt(1-p))


def logg(p, x):
    return math.log(math.cosh(x)) + (p-1)*math.log(math.sinh(x))


def optimizer(p, h):
    if h <= critical(p):
        return h/2
    a, b = 1e-14, h/2 - 1e-8
    for _ in range(85):
        m = (a+b)/2
        if logg(p,m) > logg(p,h-m):
            a=m
        else:
            b=m
    return (a+b)/2


def exact_factor(p, h):
    if h <= critical(p):
        return 2**(1-p)/math.cosh(h/2)**p
    return value(p, h, optimizer(p,h))


def inverse_coeff(h, t):
    q=math.exp(-h)
    ka=math.exp(-abs(t))
    kb=math.exp(-abs(t-h))
    return ((ka-q*kb)/(1-q*q), (kb-q*ka)/(1-q*q))


def check():
    count=0
    for p in [0.15,0.3,0.5,0.7,0.9]:
        hc=critical(p)
        for rat in [0.4,0.8,1.0,1.02,1.15,1.7,3.0,4.0]:
            h=hc*rat
            x=optimizer(p,h)
            v=exact_factor(p,h)
            assert 0<x<h/2+1e-12
            assert v>1
            if h>hc:
                assert abs(logg(p,x)-logg(p,h-x))<2e-8
            for k in range(351):
                xx=h*k/350
                assert value(p,h,xx)<=v+1e-9
                count+=1
            for k in range(30):
                t=-h+(3*h*k/29)
                c0,c1=inverse_coeff(h,t)
                if 0<=t<=h:
                    assert abs(c0-math.sinh(h-t)/math.sinh(h))<2e-11
                    assert abs(c1-math.sinh(t)/math.sinh(h))<2e-11
                assert abs(c0)**p+abs(c1)**p <= v+1e-9
                count+=1
            if p==0.5:
                if h<=hc:
                    explicit=math.sqrt(2/math.cosh(h/2))
                else:
                    explicit=math.sqrt(1/math.tanh(h/2))
                    xx=(h-math.acosh(math.cosh(h)-2))/2
                    assert abs(x-xx)<2e-9
                    count+=1
                assert abs(v-explicit)<3e-11
                count+=1
            for delta in [0.0001,0.001]:
                hs=hc+delta
                xs=optimizer(p,hs)
                asym=math.sqrt(3*math.sqrt(1-p)/(2-p))*math.sqrt(delta)
                assert abs((hs/2-xs)/asym-1)<0.005
                count+=1
    for p in [0.2,0.5,0.8]:
        hc=critical(p)
        prev=exact_factor(p,hc/2)
        for j in range(1,45):
            h=hc/2+0.10*j
            new=exact_factor(p,h)
            assert new<prev+1e-12
            prev=new
            count+=1
    rng=random.Random(745110)
    for _ in range(700):
        p=rng.uniform(.06,.94)
        h=rng.uniform(.10,5)
        x=optimizer(p,h)
        v=exact_factor(p,h)
        t=rng.uniform(-h,2*h)
        c0,c1=inverse_coeff(h,t)
        assert abs(c0)**p+abs(c1)**p <= v+1e-9
        count+=1
    print(f'LAPLACE_TWO_SAMPLE_OK {count} finite assertions')


if __name__=='__main__':
    check()
