#!/usr/bin/env python3
"""Numerical cross-checks for the ellipse endpoint-chord density. Python standard library only."""
import math
import random
from fractions import Fraction

PI = math.pi

def K_of_m(m):
    """Complete elliptic K with parameter m by arithmetic-geometric mean."""
    assert 0 <= m < 1
    x, y = 1.0, math.sqrt(1.0-m)
    while abs(x-y) > 3e-16*x:
        x, y = (x+y)/2, math.sqrt(x*y)
    return PI/(2*x)

def pdf_ellipse(l, a, b):
    """Length density for two independent uniform eccentric anomalies; a>b>0."""
    d = a*a-b*b
    x = l/2
    if x < 0 or x > a: return 0.0
    if x < b:
        return 2*K_of_m(d/(a*a-x*x))/(PI*PI*math.sqrt(a*a-x*x))
    if x > b:
        return 2*K_of_m((a*a-x*x)/d)/(PI*PI*math.sqrt(d))
    return float('inf')

def integrate_moment(p, a, b, n=6000, zmax=25):
    assert n%2 == 0
    def piece(z, first):
        q=math.exp(-z)
        if first:
            x=b*(1-q);dx=b*q
        else:
            x=b+(a-b)*q;dx=(a-b)*q
        return ((2*x)**p)*pdf_ellipse(2*x,a,b)*2*dx
    def simp(first):
        h=zmax/n
        s=piece(0,first)+piece(zmax,first)
        for j in range(1,n):
            s+=(4 if j%2 else 2)*piece(j*h,first)
        return s*h/3
    return simp(True)+simp(False)

def check():
    r=random.Random(193746)
    for a,b in [(3.0,2.0),(2.0,0.5),(1.01,1.0)]:
        target2=a*a+b*b
        target4=Fraction(9,4)*(a**4+b**4)+Fraction(3,2)*a*a*b*b
        for p,target in [(0,1),(2,target2),(4,target4)]:
            got=integrate_moment(p,a,b)
            assert abs(got-target)<3e-7*max(1,abs(target)), (a,b,p,got,target)
        delta=a*a-b*b
        reconstructed_gap=math.sqrt(4*target4/3-2*target2**2)
        assert abs(reconstructed_gap-delta)<1e-9
        assert abs(math.sqrt((target2+reconstructed_gap)/2)-a)<1e-9
        assert abs(math.sqrt((target2-reconstructed_gap)/2)-b)<1e-9
        # Check both sides of the interior logarithmic singularity, including constant term.
        if delta>.1:
            h=1e-7
            for sg in [-1,1]:
                ll=2*b+sg*h
                leading=(1/(PI*PI*math.sqrt(delta)))*math.log(16*delta/(b*h))
                assert abs(pdf_ellipse(ll,a,b)-leading)<2e-6, (a,b,sg)
        for j in range(1200):
            t=2*PI*r.random();u=2*PI*r.random()
            direct=math.hypot(a*(math.cos(t)-math.cos(u)), b*(math.sin(t)-math.sin(u)))
            factored=2*abs(math.sin((t-u)/2))*math.hypot(a*math.sin((t+u)/2),b*math.cos((t+u)/2))
            assert abs(direct-factored)<2e-13
    # Independent Monte Carlo moment cross-check (no numerical integration inside this test).
    a,b,N=3.0,2.0,220000
    sums=[0.,0.]
    for _ in range(N):
        t=2*PI*r.random(); u=2*PI*r.random()
        d=math.hypot(a*(math.cos(t)-math.cos(u)), b*(math.sin(t)-math.sin(u)))
        sums[0]+=d*d;sums[1]+=d**4
    assert abs(sums[0]/N-13.0)<.11
    assert abs(sums[1]/N-272.25)<3.0
    print('ELLIPSE_END_POINT_CHORD_DENSITY_CHECKS_OK')

if __name__=='__main__': check()
