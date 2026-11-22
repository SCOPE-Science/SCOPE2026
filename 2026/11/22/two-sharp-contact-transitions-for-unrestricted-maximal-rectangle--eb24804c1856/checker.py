#!/usr/bin/env python3
"""Independent numerical diagnostics for the circular-segment rectangle theorem.
Run: python3 checker.py. This is a finite check, not an infinite-domain proof.
"""
import math
import random

SQRT2 = math.sqrt(2.0)
H1 = -1.0 / SQRT2
H2 = -1.0 / math.sqrt(3.0)

def critical_top(h):
    return (h + math.sqrt(h*h+8.0))/4.0

def optimal(h):
    assert -1.0 < h < 1.0
    if h <= H1:
        b = 1.0/math.sqrt(2.0)
        a = b
        z = 0.0
    elif h <= H2:
        b = -h
        a = math.sqrt(1.0-h*h)
        z = 0.0
    else:
        top = critical_top(h)
        a = math.sqrt(1.0-top*top)
        b = (top-h)/2.0
        z = (top+h)/2.0
    return a,b,z,4.0*a*b

def area_bound_t(h,t):
    if t < max(0.0,h) or t > 1.0: return 0.0
    return 2.0*math.sqrt(max(0.0,1.0-t*t))*min(2.0*t, t-h)

def vertices(a,b,theta,cx,cy):
    u=(a*math.cos(theta),a*math.sin(theta))
    v=(-b*math.sin(theta),b*math.cos(theta))
    return [(cx+e*u[0]+f*v[0],cy+e*u[1]+f*v[1]) for e in (-1,1) for f in (-1,1)]

def feasible(h,points,tol=1e-12):
    return min(y for x,y in points)>=h-tol and max(x*x+y*y for x,y in points)<=1.0+tol

def main():
    checks=0
    criticals=(H1,H2,0.0)
    for h in [-0.999,-0.95,-0.8,H1,-.70,-.67,-.6,H2,-.57,-.51,-.3,0.0,.2,.5,.8,.95,.999]:
        a,b,z,ma=optimal(h)
        assert feasible(h,vertices(a,b,0.0,0.0,z),1e-12);checks+=1
        # Exhaustive checks on stated *finite grid* of top-height parameters.
        for i in range(3001):
            t=max(0,h)+(1-max(0,h))*i/3000
            assert area_bound_t(h,t)<=ma+1e-10,(h,t,ma,area_bound_t(h,t))
            checks+=1
    # Check arbitrary rotated and translated boxes against analytic optimum.
    rng=random.Random(1140506)
    for j in range(120000):
        h=rng.uniform(-.999,.999)
        a=rng.uniform(.01,.9)
        b=rng.uniform(.01,.9)
        theta=rng.uniform(0,math.pi/2)
        cx=rng.uniform(-.5,.5)
        cy=rng.uniform(-.5,.75)
        pts=vertices(a,b,theta,cx,cy)
        if feasible(h,pts):
            assert 4*a*b<=optimal(h)[3]+1e-11
            checks+=1
    # Contact and smoothness formula checks by independent finite-difference quotients.
    def f(h):return optimal(h)[3]
    assert abs(f(H1)-2.0)<1e-13;checks+=1
    assert abs(f(H2)-4.0*SQRT2/3.0)<1e-13;checks+=1
    assert abs(f(0.0)-1.0)<1e-13;checks+=1
    target_second = [(H1,0.0,-16.0),(H2,-7.0*SQRT2,SQRT2/5.0)]
    for h,left_target,right_target in target_second:
        for e in [1e-3,3e-4,1e-4]:
            d2left=(f(h)-2.0*f(h-e)+f(h-2.0*e))/(e*e)
            d2right=(f(h+2.0*e)-2.0*f(h+e)+f(h))/(e*e)
            assert abs(d2left-left_target)<0.15,(h,e,d2left,left_target)
            assert abs(d2right-right_target)<0.15,(h,e,d2right,right_target)
            checks+=2
    # Thin cap area utilization tends to 1/sqrt(3).
    for delta in [1e-3,1e-4,1e-5]:
        h=1-delta
        cap=math.acos(h)-h*math.sqrt(1-h*h)
        ratio=f(h)/cap
        assert abs(ratio-1.0/math.sqrt(3.0))<5e-4,(delta,ratio)
        assert abs(f(h)/delta**1.5-4.0*math.sqrt(6.0)/9.0)<5e-3
        checks+=2
    print('PASS',checks,'finite diagnostic assertions')

if __name__=='__main__':main()
