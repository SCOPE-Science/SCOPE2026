#!/usr/bin/env python3
"""Numerical diagnostics for fixed-mean rate-summation envelopes.
Analytical conclusions require the proof, not finite tests.
"""
import math
import random


def val(t, a, b, B, c):
    return math.exp(a*t) - B*math.exp(b*t) + c


def deriv(t, a, b, B):
    return a*math.exp(a*t) - B*b*math.exp(b*t)


def second(t, a, b, B):
    return a*a*math.exp(a*t) - B*b*b*math.exp(b*t)


def tangency(a, b, B, lo):
    theta=math.log(a*a/(B*b*b))/(b-a)
    top=math.log(a/(B*b))/(b-a)
    assert lo < theta < top
    def h(t):
        return (t-lo)*deriv(t,a,b,B) - (val(t,a,b,B,0)-val(lo,a,b,B,0))
    x,y=theta,top
    for _ in range(100):
        mid=(x+y)/2
        if h(mid)>0: x=mid
        else: y=mid
    return (x+y)/2,theta,top


def envelope(t,a,b,B,c,lo,hi):
    theta=math.log(a*a/(B*b*b))/(b-a)
    if lo>=theta:
        return val(t,a,b,B,c), ('constant',t)
    cut,_,_=tangency(a,b,B,lo)
    cap=min(hi,cut)
    if t>=cap and hi>cut:
        return val(t,a,b,B,c),('constant',t)
    if t==lo: return val(lo,a,b,B,c),('constant',lo)
    if t==hi: return val(hi,a,b,B,c),('constant',hi)
    mix=(t-lo)/(cap-lo)
    return (1-mix)*val(lo,a,b,B,c)+mix*val(cap,a,b,B,c), ('two-point',lo,cap,mix)


def run():
    rng=random.Random(202611170453)
    tests=0
    for k in range(160):
        a=rng.uniform(.055,.14)
        b=a+rng.uniform(.055,.18)
        theta=rng.uniform(4,22)
        B=(a/b)**2*math.exp(-(b-a)*theta)
        peak=theta+math.log(b/a)/(b-a)
        lo=theta-rng.uniform(.2,8)
        hi=theta+rng.uniform(-.15,1.9)*(peak-theta)
        if hi<=lo: hi=theta+.1
        c=max(0, 1-min(val(lo,a,b,B,0),val(hi,a,b,B,0)))
        cut,_,_=tangency(a,b,B,lo)
        tests+=1;assert theta<cut<peak
        tests+=1;assert abs((cut-lo)*deriv(cut,a,b,B)-(val(cut,a,b,B,c)-val(lo,a,b,B,c)))<2e-7*max(1,abs(val(cut,a,b,B,c)))
        # Test the predicted piecewise upper concave envelope.
        for j in range(33):
            t=lo+(hi-lo)*j/32
            upper,_=envelope(t,a,b,B,c,lo,hi)
            f=val(t,a,b,B,c)
            tests+=1;assert upper+1e-7*max(1,abs(f)) >=f,(k,t,upper,f)
        for z in range(14):
            mean=lo+(hi-lo)*rng.random()
            best,_=envelope(mean,a,b,B,c,lo,hi)
            for j in range(35):
                left=lo+(mean-lo)*rng.random()
                right=mean+(hi-mean)*rng.random()
                w=(mean-left)/(right-left)
                v=(1-w)*val(left,a,b,B,c)+w*val(right,a,b,B,c)
                tests+=1;assert best+1e-7*max(1,abs(best))>=v,(k,mean,best,v)
        # Single-contact temperature independent of upper bound and offset.
        tests+=1;assert abs(second(theta,a,b,B))<2e-10*max(1,abs(val(theta,a,b,B,0)))
    # One physical positive-rate example in convenient temperature units.
    a,b=.1,.2
    B=(a/b)**2*math.exp(-(b-a)*20)
    lo,hi=15,31
    cut,theta,peak=tangency(a,b,B,lo)
    tests+=1;assert abs(theta-20)<1e-12 and 21.94<cut<21.95 and 26.93<peak<26.94
    for i in range(1001):
        t=lo+(hi-lo)*i/1000
        tests+=1;assert val(t,a,b,B,0)>0
    # Universal one-half onset as cold endpoint tends to inflection.
    for eps in [.1,.02,.004,.0008]:
        contact,_,_=tangency(a,b,B,theta-eps)
        tests+=1;assert abs((contact-theta)/eps-0.5)<.003
    # Cold-limit approaches physical peak, and is strictly monotone in cold floor.
    prev=theta
    for lo2 in [theta-0.2,theta-1,theta-4,theta-10,theta-30,theta-1000]:
        contact,_,_=tangency(a,b,B,lo2)
        tests+=1;assert contact>prev
        prev=contact
    tests+=1;assert abs(peak-prev)<.06
    # The unique rate-gain maximizer and sharp cubic onset are checked.
    theta=20.0
    curvature=-a*a*(b-a)*math.exp(a*theta)
    for eps in [0.1,0.075,0.05,0.04,0.025]:
        lo2=theta-eps
        hot,_,_=tangency(a,b,B,lo2)
        slope=deriv(hot,a,b,B)
        left,right=lo2,theta
        for _ in range(90):
            middle=(left+right)/2
            if deriv(middle,a,b,B)<slope: left=middle
            else: right=middle
        cold=(left+right)/2
        tests+=1;assert lo2<cold<theta<hot
        tests+=1;assert abs((cold-theta)/eps + .5)<.002
        line=val(lo2,a,b,B,0)+slope*(cold-lo2)
        delta=line-val(cold,a,b,B,0)
        target=-curvature*eps**3/12
        tests+=1;assert target>0 and abs(delta/target-1)<.02,(eps,delta,target)
    return tests,cut,peak


if __name__=='__main__':
    n,t,p=run()
    print('PASS',n,'diagnostic assertions; contact',repr(t),'peak',repr(p))
