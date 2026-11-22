#!/usr/bin/env python3
"""Reproduce exact Cassini-oval convexification checks; standard library only."""
from math import sqrt, pi, isclose


def simpson(func, a, b, n=6000):
    assert n % 2 == 0
    h = (b-a)/n
    s = func(a)+func(b)
    for j in range(1,n):
        s += (4 if j&1 else 2)*func(a+j*h)
    return h*s/3


def profile(d,t):
    x = sqrt(d)*t/2
    s = sqrt(4-d+d*t*t)
    yt = sqrt(4-d)/2
    y2 = -1-x*x+s
    y = sqrt(max(0.,y2))
    return x, y, yt, s


def scaled_area(d):
    # Stable exact integrand, including d -> 0.
    def integrand(t):
        x,y,yt,s=profile(d,t)
        return (1-t*t)**2/((2+s)**2*(yt+y))
    return simpson(integrand,0,1)/2


def area_defect(d):
    return d**2.5*scaled_area(d)


def perim_defect(d):
    xmax=sqrt(d)/2
    def integrand(t):
        x,y,yt,s=profile(d,t)
        if y==0: return 0. # Only d=3,t=0 is exceptional; avoid this endpoint.
        deriv=(-2*x+4*x/s)/(2*y)
        return (deriv*deriv)/(sqrt(1+deriv*deriv)+1)
    return 4*xmax*simpson(integrand,0,1)


def direct_defect(d):
    xt=sqrt(d)/2; b4=4-d; yt=sqrt(b4)/2
    def f(x):
        s=sqrt(b4+4*x*x)
        y=sqrt(-1-x*x+s)
        return (2-s)**2/(4*(yt+y))
    return 4*simpson(f,0,xt)


def test():
    dlist=[0.02,0.06,0.1,0.2,0.5,1.,1.8,2.5,2.9]
    constants=[scaled_area(d) for d in dlist]
    assert all(v>1/120 for v in constants)
    assert all(a<b for a,b in zip(constants, constants[1:])),constants
    sharp_upper=(3*sqrt(3)/2-2)/3**2.5
    assert all(v<sharp_upper for v in constants)
    for d in dlist:
        assert isclose(area_defect(d),direct_defect(d),rel_tol=2e-9)
    assert abs(scaled_area(1.e-6)-1/120)<1.e-8
    assert abs(scaled_area(3.0)-sharp_upper)<3.e-7
    for d in [0.001,0.005,0.01]:
        p=perim_defect(d)
        assert abs(p/d**3.5-1/3360)<2.e-6,(d,p/d**3.5)
    for d in [0.2,0.8,2.0]:
        x,y,yt,s=profile(d,0.6)
        assert abs((yt*yt-y*y)-((2-s)**2/4))<1.e-12
    print('CASSINI_CONVEX_HULL_STABILITY_CHECKS_OK',len(dlist),'area regimes')


if __name__=='__main__':test()
