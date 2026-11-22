#!/usr/bin/env python3
"""Reproduce diagnostic checks for a two-readout-mode exposure model.

Only finite numerical assertions are implemented here. The mathematical
classification for all positive parameters is established by the proof.
"""
import math
import random


def stationarity(t, a, h):
    return a/(t*(t+a)) + h/(t*(t+h))


def optimum(a, h, hazard):
    assert min(a, h, hazard) > 0
    lo, hi = 0.0, 2/hazard
    for _ in range(115):
        mid = (lo + hi)/2
        if stationarity(mid, a, h) > hazard:
            lo = mid
        else:
            hi = mid
    t=(lo+hi)/2
    log_value = -hazard*t + 2*math.log(t)-math.log(t+a)-math.log(t+h)
    return t, log_value


def mode_log_ratio(a1,h1,a2,h2,hazard):
    t1,y1=optimum(a1,h1,hazard)
    t2,y2=optimum(a2,h2,hazard)
    return y1-y2,t1,t2


def switch(a1,h1,a2,h2):
    s1,p1=a1+h1,a1*h1
    s2,p2=a2+h2,a2*h2
    assert s1<s2 and p1>p2
    # Find the unique positive sign change in optimized log-efficiency.
    lo=1.e-12/(s1+s2)
    # Mathematical small-hazard asymptotic guarantees positivity, but
    # float precision can underflow; increase when required.
    for _ in range(50):
        if mode_log_ratio(a1,h1,a2,h2,lo)[0]>1.e-12:
            break
        lo*=3
    else:
        raise AssertionError('no resolvable small-hazard comparison')
    hi=lo
    for _ in range(120):
        hi*=2
        if mode_log_ratio(a1,h1,a2,h2,hi)[0]<-1.e-12:
            break
    else:
        raise AssertionError('no high-hazard comparison')
    for _ in range(105):
        mid=(lo+hi)/2
        if mode_log_ratio(a1,h1,a2,h2,mid)[0]>0: lo=mid
        else:hi=mid
    return (lo+hi)/2


def run():
    checks=0
    a1,h1,a2,h2=4.,4.,.1,20.
    cross=switch(a1,h1,a2,h2)
    r,example_t1,example_t2=mode_log_ratio(a1,h1,a2,h2,cross)
    assert abs(cross-1.0988848516722565)<1.e-12; checks+=1
    assert abs(r)<2.e-13;checks+=1
    assert example_t1>example_t2 and abs(example_t1-1.3585871488221106)<1.e-8 and abs(example_t2-0.9548200165256728)<1.e-8;checks+=1
    for hazard in [cross*.1, cross*.5, cross*.99, cross*1.01, cross*2, cross*10]:
        d,_,_=mode_log_ratio(a1,h1,a2,h2,hazard)
        assert (d>0)==(hazard<cross);checks+=1
    rng=random.Random(20261117)
    for _ in range(3000):
        a=10**rng.uniform(-2,2)
        h=10**rng.uniform(-2,2)
        haz=10**rng.uniform(-3,2)
        t,y=optimum(a,h,haz)
        assert 0<t<2/haz;checks+=1
        assert abs(stationarity(t,a,h)/haz-1)<5.e-13;checks+=1
        for fac in [.3,.7,1.3,3.]:
            t2=t*fac
            val=-haz*t2+2*math.log(t2)-math.log(t2+a)-math.log(t2+h)
            assert y>val; checks+=1
        # Exact single-mode mean-hit-time comparator.
        assert ((t>1/haz)==(haz*haz*a*h>1));checks+=1
        # The mode is invariant under swapping overhead and readnoise scales.
        t_swap,y_swap=optimum(h,a,haz)
        assert abs(t-t_swap)/t<1.e-13 and abs(y-y_swap)<1.e-13;checks+=1
    # Pairwise mode dominance and monotone switching diagnostics.
    for _ in range(1100):
        a1=10**rng.uniform(-1,1)
        h1=10**rng.uniform(-1,1)
        a2=10**rng.uniform(-1,1)
        h2=10**rng.uniform(-1,1)
        s1,p1=a1+h1,a1*h1
        s2,p2=a2+h2,a2*h2
        for haz in [.002,.02,.2,2.,20.]:
            d,_,_=mode_log_ratio(a1,h1,a2,h2,haz)
            if s1<s2 and p1<p2:
                assert d>0;checks+=1
            elif s1>s2 and p1>p2:
                assert d<0;checks+=1
        # Quadratic for equality of stationarity functions.
        if (s1-s2)*(p1-p2)<0:
            A=s1-s2; B=2*(p1-p2); C=s2*p1-s1*p2
            disc=B*B-4*A*C
            assert disc>0;checks+=1
            roots=((-B+math.sqrt(disc))/(2*A),(-B-math.sqrt(disc))/(2*A))
            assert sum(r>0 for r in roots)==1;checks+=1
            pos=max(roots)
            lhs=stationarity(pos,a1,h1)-stationarity(pos,a2,h2)
            assert abs(lhs)<2.e-11;checks+=1
    print('PASS: %d finite assertions' % checks)
    print('illustrative two-mode hazard switch: %.15g' % cross)
    print('optimal durations at switch: %.13g and %.13g' % (example_t1,example_t2))

if __name__=='__main__':run()
