#!/usr/bin/env python3
"""Numerical consistency checks for rational-angle Feres circular caustic laws.

These finite tests are auxiliary to the analytic trigonometric proof. Standard library only.
"""
import math
from itertools import product


def states(n, t):
    a = math.pi / n
    if n % 2:
        m = (n - 1)//2
        return ([t + 2*k*a for k in range(m+1)]
                + [2*k*a-t for k in range(1,m+1)])
    m = n//2
    return ([t + 2*k*a for k in range(m)]
            + [2*k*a-t for k in range(1,m+1)])


def predicted_radius(n, t):
    a = math.pi/n
    if n%2: return math.sin(abs(t-a/2))
    if n%4==2: return math.sin(a-t)
    return math.sin(t)


def predicted_cdf(n, r):
    a = math.pi/n
    if n%2:
        width=math.sin(a/2)
        return min(1., max(0.,r/width))
    width=math.sin(a)
    if n%4==2: return min(1.,max(0.,r/width))
    return min(1.,max(0.,r/math.tan(a) + 1 -math.sqrt(1-r*r)))


def predicted_moments(n):
    a = math.pi/n
    if n%2:
        w = math.sin(a/2)
        return w/2, w*w/3
    if n%4==2:
        w=math.sin(a)
        return w/2,w*w/3
    return a/2, 2*(1-math.cos(a))/3


def simpson(f, lo, hi, N=6000):
    assert N%2 == 0
    h = (hi-lo)/N
    s=f(lo)+f(hi)
    for k in range(1,N):
        s+=(4 if k%2 else 2)*f(lo+k*h)
    return h*s/3


def run():
    checks=0
    for n in range(7,51):
        a=math.pi/n
        for i in range(1,301):
            t=a*i/301
            v=states(n,t)
            assert len(v)==n
            assert all(0<x<math.pi for x in v)
            assert len({round(x,11) for x in v})==n
            direct=min(abs(math.cos(x)) for x in v)
            assert abs(direct-predicted_radius(n,t))<3e-13
            S=sum(math.sin(x) for x in v)
            theoretical=(math.cos(t-a/2)/math.sin(a/2) if n%2
                         else 2*math.cos(t-a)/math.sin(a))
            assert abs(S-theoretical)<3e-12
            checks+=1
        pdf=lambda t: .5*sum(math.sin(x) for x in states(n,t))
        assert abs(simpson(pdf,0,a)-1)<1e-11
        m1=simpson(lambda t: pdf(t)*predicted_radius(n,t),0,a)
        m2=simpson(lambda t: pdf(t)*predicted_radius(n,t)**2,0,a)
        predicted=predicted_moments(n)
        # absolute-value corner at a/2 for odd n; Simpson handles even grid
        assert abs(m1-predicted[0])<2e-9, (n,m1,predicted)
        assert abs(m2-predicted[1])<2e-9, (n,m2,predicted)
        for j in range(1,20):
            upper=math.sin(a/2) if n%2 else math.sin(a)
            r=upper*j/20
            if n%2:
                t1=a/2-math.asin(r);t2=a/2+math.asin(r)
                c=simpson(pdf, t1,t2,1000)
            elif n%4==2:
                c=simpson(pdf,a-math.asin(r),a,1000)
            else:
                c=simpson(pdf,0,math.asin(r),1000)
            assert abs(c-predicted_cdf(n,r))<2e-10, (n,r,c,predicted_cdf(n,r))
            checks+=1
    print(f'PASS: {checks} direct orbit/radius/weight/CDF cases; 44 normalization and 88 moment integrals for n=7..50.')
    print('Limits: finite numerical checks only; all-n claims require the standalone proof.')

if __name__=='__main__':run()
