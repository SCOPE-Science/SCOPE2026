#!/usr/bin/env python3
"""Deterministic checks for the two-timelag, joint-dryness frequency theorem.

No stochastic sampling; these tests supplement, rather than replace, the analysis.
"""
import math
from fractions import Fraction

COUNT=0

def check(test, message):
    global COUNT
    COUNT += 1
    if not test:
        raise AssertionError(message)

def geom(x, r):
    return 1/(math.hypot(1,x)*math.hypot(1,x/r))

def cutoff(c):
    return math.sqrt(1/c**2-1)

def angles(x,r,c):
    h1=math.acos(min(1,c*math.hypot(1,x)))
    h2=math.acos(min(1,c*math.hypot(1,x/r)))
    d=math.atan(x)-math.atan(x/r)
    return h1,h2,d

def exposure(x,r,c):
    if x>=cutoff(c):return 0.
    h1,h2,d=angles(x,r,c)
    return min(2*h1,h1+h2-d)/(2*math.pi)

def bound_B(x,r):
    return (r-1)*(x*x-r)/((1+x*x)*(r*r+x*x))

def bound_S(x,r,c):
    a=math.hypot(1,x);b=math.hypot(1,x/r)
    return c*x/(a*math.sqrt(1-c*c*a*a))+c*x/(r*r*b*math.sqrt(1-c*c*b*b))

def critical_at_frequency(x,r):
    assert x>math.sqrt(r)
    hi=geom(x,r)
    lo=0.
    check(bound_S(x,r,hi)>bound_B(x,r), 'root interval')
    for _ in range(80):
        mid=(hi+lo)/2
        if bound_S(x,r,mid)>bound_B(x,r):hi=mid
        else:lo=mid
    return (lo+hi)/2

def optimum(r):
    # Single bounded maximizing search is illustrative; existence is analytic.
    # Sample a wide compact range to bracket a global *candidate*.
    values=[]
    for i in range(1800):
        x=math.sqrt(r)*math.exp(.0005+12*i/1799)
        values.append((critical_at_frequency(x,r),x))
    _,x=max(values)
    return max(values)[0], x

def count_fraction_direct(x,r,c,n=30000):
    # Uniform midpoints in phase; the slow/fast responses are exact harmonic states.
    total=0
    a=1/math.hypot(1,x);b=1/math.hypot(1,x/r)
    d1=math.atan(x);d2=math.atan(x/r)
    for k in range(n):
        phase=2*math.pi*(k+.5)/n
        if a*math.cos(phase-d1)<-c and b*math.cos(phase-d2)<-c:
            total+=1
    return total/n

def main():
    for r in (1.1,1.2,1.5,2,3,5,10):
        cstar,xmax=optimum(r)
        check(0<cstar<math.sqrt(r)/(r+1),'strict threshold bound')
        check(xmax>math.sqrt(r),'location bound')
        check(critical_at_frequency(xmax,r)>0,'positive root')
        for x in (0,.01,.1,.3,.7,1,math.sqrt(r),2*math.sqrt(r),5*math.sqrt(r)):
            for c in (.005,.02,.05,.1,.2,.4,.8):
                if x>=cutoff(c):continue
                h1,h2,d=angles(x,r,c)
                check(h2+1e-12>=h1,'halfwidth ordering')
                check(exposure(x,r,c)>=0,'fraction nonnegative')
                if x>0:
                    check((d > h2-h1)==(c<geom(x,r)),'branch boundary')
        for c in (.005,.02,.05,.2):
            for x in (0.2,math.sqrt(r),2*math.sqrt(r),4*math.sqrt(r)):
                if x>=cutoff(c):continue
                theo=exposure(x,r,c)
                direct=count_fraction_direct(x,r,c,6000)
                check(abs(theo-direct)<1.7/6000,'phase enumeration versus closed form')
        # Samples bracketing the transition, with generous margins.
        high=min(.995, cstar*1.2)
        ws=[cutoff(high)*(i+.5)/300 for i in range(300)]
        ys=[exposure(w,r,high) for w in ws]
        check(all(ys[i+1]<=ys[i]+1e-12 for i in range(len(ys)-1)), 'above-threshold monotonicity')
        low=.5*cstar
        ws=[cutoff(low)*(i+.5)/500 for i in range(500)]
        ys=[exposure(w,r,low) for w in ws]
        check(any(ys[i+1]>ys[i]+1e-6 for i in range(len(ys)-1)), 'below-threshold recovery')
    # Explicit rational witness: rho=2, x=2, c=1/50.
    c=Fraction(1,50);r=Fraction(2);x=Fraction(2)
    B=(r-1)*(x*x-r)/((1+x*x)*(r*r+x*x))
    check(B == Fraction(1,20),'exact positive phase recovery')
    check(float(c) < geom(2.,2.), 'partial overlap for rational witness')
    check(bound_S(2.,2.,.02)<float(B), 'strict positive derivative witness')
    # Small relaxation contrast coefficient.
    z=(5+math.sqrt(33))/4
    K=(z-1)/(2*math.sqrt(z)*(1+z)**1.5)
    check(.07268<K<.07269,'analytic asymptotic coefficient')
    for r in (1.01,1.005):
        c,x=optimum(r)
        check(abs(c/(r-1)-K)<.001,'small contrast asymptotic diagnostic')
    print(f'PASS: {COUNT} deterministic checks')
    print('rho=2 candidate threshold and frequency:',optimum(2.))
    print('small-contrast coefficient:',K)

if __name__=='__main__':main()
