#!/usr/bin/env python3
"""Numerical and symbolic consistency checks for the radial-grid classification.

Finite computation illustrates the exact formulas; it does not prove the
classification for every side count or every real parameter.
"""
import math


def test_one(n, length, t):
    theta = 2 * math.pi / n
    kappa = math.cos(theta)
    b = length / math.sqrt(t*t+1-2*kappa*t)
    a = t*b
    xy = [(a if i % 2 == 0 else b)*math.cos(i*theta) for i in range(n)]
    yy = [(a if i % 2 == 0 else b)*math.sin(i*theta) for i in range(n)]
    assert all(abs(math.hypot(xy[(i+1)%n]-xy[i], yy[(i+1)%n]-yy[i])-length)<1e-9*max(1,length) for i in range(n))
    cross = lambda i: ((xy[i]-xy[(i-1)%n])*(yy[(i+1)%n]-yy[i])-
                       (yy[i]-yy[(i-1)%n])*(xy[(i+1)%n]-xy[i]))
    assert all(cross(i) > 1e-9 for i in range(n))
    area = sum(xy[i]*yy[(i+1)%n]-yy[i]*xy[(i+1)%n] for i in range(n))/2
    expected = n*a*b*math.sin(theta)/2
    assert abs(area-expected)<1e-8*max(1,area)
    upper = n*length**2*math.cos(math.pi/n)/(4*math.sin(math.pi/n))
    lower = n*length**2*math.cos(theta)/(2*math.sin(theta))
    assert lower < area + 1e-9
    assert area < upper+1e-9*max(1,upper)
    return 4*n+4


def main():
    total=0
    for n in range(4, 102, 2):
        kappa=math.cos(2*math.pi/n)
        for ell in (0.37, 1.0, 3.1):
            low=max(0,kappa)
            high=(1/kappa if kappa>1e-10 else 25.)
            for f in (0.015,0.075,0.25,0.49,0.5,0.51,0.75,0.91,0.985):
                t=low+(high-low)*f
                total+=test_one(n,ell,t)
    for n in range(3, 102, 2):
        radius=1/(2*math.sin(math.pi/n))
        theta=2*math.pi/n
        for i in range(n):
            j=(i+1)%n
            d=math.hypot(radius*(math.cos(j*theta)-math.cos(i*theta)),
                         radius*(math.sin(j*theta)-math.sin(i*theta)))
            assert abs(d-1)<1e-10
            total+=1
    try:
        import sympy as s
    except ImportError:
        pass
    else:
        t,k=s.symbols('t k',real=True)
        f=t/(t**2+1-2*k*t)
        assert s.factor(s.diff(f,t)-(1-t**2)/(t**2+1-2*k*t)**2)==0
        assert s.factor(f.subs(t,k)-k/(1-k**2))==0
        total+=2
    print(f"PASS: {total} edge/turn/area/formula consistency checks across side counts 3..100")

if __name__=='__main__':
    main()
