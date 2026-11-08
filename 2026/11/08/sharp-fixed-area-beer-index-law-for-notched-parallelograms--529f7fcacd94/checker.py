#!/usr/bin/env python3
"""Checks for exact Beer visibility of right-angled L-polygons.
Reproducible standard-library verification, with both direct segment testing
and conditional four-uniform simulations. No external dependencies.
"""
import math, random
RNG=random.Random(360912)

def blocked(s,t):
    q=(1-s)*(1-t); z=s*t/q
    if z<=1: k=z-z*z*(2-math.log(z))/4
    else: k=(2+math.log(z))/4
    return 2*q*q*k/(1-q)**2

def segment_crosses_removed(p0,p1,s,t):
    # Independent parameter-interval computation: find positive-length
    # intersection of the segment with the open northeast rectangle.
    low,high=0.0,1.0
    for a,b,threshold in ((p0[0],p1[0],s),(p0[1],p1[1],t)):
        if a==b:
            if a<=threshold:return False
            continue
        root=(threshold-a)/(b-a)
        if b>a:low=max(low,root)
        else:high=min(high,root)
    return low<high

def direct(s,t,n):
    # Independently use segment/rectangle parameter clipping; no products.
    def point():
        while True:
            x,y=RNG.random(),RNG.random()
            if x<s or y<t:return x,y
    bad=0
    for _ in range(n):
        bad+=segment_crosses_removed(point(),point(),s,t)
    return bad/n

def conditional(s,t,n):
    bad=0
    for _ in range(n):
        x=(1-s)*RNG.random(); v=(1-t)*RNG.random()
        u=s*RNG.random(); y=t*RNG.random()
        bad+= x*v > u*y
    return bad/n

def stability_constant(q):
    w=(1-q**0.5)**2/q
    derivative= 1-w*(3-2*math.log(w))/4 if w<=1 else 1/(4*w)
    return 2*q/(1-q)**2*derivative

def test():
    for s,t in [(0.2,0.1),(0.3,0.9),(0.5,0.5),(0.9,0.9),(0.7,0.4),(0.12,0.73)]:
        n=100000
        q=(1-s)*(1-t)
        theory=blocked(s,t)
        obs=direct(s,t,n)
        p=conditional(s,t,n)
        expect=theory/(2*(1-s)*t*s*(1-t)/(1-q)**2)
        assert abs(obs-theory)<0.012,(s,t,obs,theory)
        assert abs(p-expect)<0.012,(s,t,p,expect)
        print(s,t,'theory',round(theory,6),'direct',round(obs,6),'cond',round(p,6),'cond-theory',round(expect,6))
    for q in (0.01,0.08,0.24,0.25,0.26,0.55,0.9):
        a=q**0.5; peak=blocked(1-a,1-a)
        for j in range(1,100):
            x=q+(1-q)*j/100
            y=q/x
            val=blocked(1-x,1-y)
            assert val<peak+1e-12,(q,x,val,peak)
            gap=(x**0.5-y**0.5)**2
            assert peak-val>=stability_constant(q)*gap-1e-12,(q,x,peak-val,gap)
    print('L_NOTCH_BEER_INDEX_AND_FIXED_AREA_OPTIMIZER_OK')
if __name__=='__main__':test()
