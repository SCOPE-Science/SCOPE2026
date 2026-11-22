#!/usr/bin/env python3
"""Reproduce the exact sinusoidal thermal-window amplitude theorem checks.

Requires only Python 3 standard library. These numerical checks supplement, but
cannot replace, the analytic proof of strict monotonicity and uniqueness.
"""
import math

PI = math.pi
CHECKS = 0

def verify(ok, message='check failed'):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(message)

def response(T, low=0.0, high=1.0):
    return (T-low)*(high-T) if low < T < high else 0.0

def daily_mean(delta, width, amplitude, n=8000):
    # delta = low - fixed daily mean; low is translated to zero.
    h = PI/n
    acc = response(-delta+amplitude,0,width)+response(-delta-amplitude,0,width)
    for j in range(1,n):
        acc += (4 if j % 2 else 2)*response(-delta+amplitude*math.cos(j*h), 0, width)
    return acc*h/(3*PI)

def closed_partial(delta, width, amplitude):
    x = delta/amplitude
    verify(0 <= x <= 1)
    j0 = math.acos(x)
    j1 = math.sqrt(max(0.0, 1-x*x))
    j2 = (j0+x*j1)/2
    return (-amplitude*amplitude*j2+amplitude*(width+2*delta)*j1-delta*(width+delta)*j0)/PI

def derivative_partial(delta, width, amplitude):
    x = delta/amplitude
    verify(0 <= x <= 1)
    return ((width+delta)*math.sqrt(max(0.,1-x*x))-amplitude*math.acos(x))/PI

def dimensionless_optimum(delta, width):
    if delta == 0.0:
        return 2*width/PI
    k = 1+width/delta
    low, high = 0.0, PI/2
    for _ in range(100):
        t = (low+high)/2
        ratio = t/(math.sin(t)*math.cos(t)) if t else 1.0
        if ratio < k:
            low = t
        else:
            high = t
    t = (low+high)/2
    return delta/math.cos(t)

for width in (0.5, 1.0, 4.0):
    for ratio in (0.0, .01, .04, .1, .25, .5, 1.0, 2.0, 5.0, 20.0):
        delta = width*ratio
        opt = dimensionless_optimum(delta,width)
        verify(opt>delta)
        verify(opt<delta+width)
        frac = (opt-delta)/width
        if delta>0:
            verify(2/PI < frac < .75)
        else:
            verify(abs(frac-2/PI)<1.e-12)
        derivative = derivative_partial(delta,width,opt)
        verify(abs(derivative)<3e-11*width)
        # Verify global winner analytically on each regime, numerically from integral.
        value = daily_mean(delta,width,opt)
        verify(value>0)
        for f in (.001, .01, .1, .25, .5, .75, .95, .999, 1.001, 1.01, 1.05, 1.25, 2.0, 5.0, 10.0):
            a = opt*f
            v = daily_mean(delta,width,a)
            verify(value>v-3e-7*width*width, f'global failure delta={delta},width={width},f={f}: {value} {v}')
        for f in (0.05, 0.2, 0.5, 0.8, 1.0):
            a=delta + f*(opt-delta)
            if a>delta:
                verify(abs(closed_partial(delta,width,a)-daily_mean(delta,width,a))<5e-7*width*width, f'closed mismatch delta={delta}, width={width}, a={a}, closed={closed_partial(delta,width,a)}, quad={daily_mean(delta,width,a)}')
                verify(derivative_partial(delta,width,a)>-1e-11*width)
        for f in (1.001,1.03,1.25,1.5):
            a = opt + f*(delta+width-opt)
            # f>1: beyond hot threshold. The mean is strictly decreasing.
            verify(daily_mean(delta,width,a+width*.1)<daily_mean(delta,width,a)+1e-7*width*width)
        if delta>0:
            for f in (0.10,0.40,0.70):
                a=delta + f*(opt-delta)
                verify(derivative_partial(delta,width,a)>0)
            for f in (.10,.5,.90):
                a=opt+f*(delta+width-opt)
                verify(derivative_partial(delta,width,a)<0)

# Check limiting universal fractions and selected independent values.
for delta in (0.000001, .1, .5, 1.,2., 10., 100., 10000.):
    opt=dimensionless_optimum(delta,1)
    frac=opt-delta
    verify(frac>2/PI and frac<.75)
verify(abs(dimensionless_optimum(1,1)-1.7137545630796778)<1e-12)
verify(abs(dimensionless_optimum(.5,1)-1.195854263189691)<1e-12)
verify(abs(dimensionless_optimum(10,1)-10.744680670652649)<1e-11)
print(f'PASS: {CHECKS} numerical and independent-integral assertions')
