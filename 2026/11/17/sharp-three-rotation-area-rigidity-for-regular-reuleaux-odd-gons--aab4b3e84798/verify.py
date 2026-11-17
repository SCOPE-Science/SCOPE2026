#!/usr/bin/env python3
"""Independent numerical checks for the three-rotation Reuleaux theorem.

Uses only Python standard-library functions. Finite checks are not substitutes
for the analytical all-parameter proof.
"""
from math import pi, cos, sin, sqrt, fsum
from itertools import product

CHECKS = 0

def check(condition, detail):
    global CHECKS
    if not condition:
        raise AssertionError(detail)
    CHECKS += 1

def F(n, t):
    t = abs((t + pi) % (2*pi) - pi)
    c = pi/(2*n)
    return -pi*pi/8 + pi*t/4 + (pi*n/(4*cos(c)))*sin((pi/2-t)/n)

def deficit(n, phases, w=1.0):
    m = len(phases)
    return (2*w*w/(pi*m*m))*fsum(F(n, a-b) for a in phases for b in phases)

def disc_gap_formula(n, w=1):
    c = pi/(2*n)
    return w*w*(-pi/36 + n*(sin(c)-2*sin(c/3))/(6*cos(c)))

def exact_area(n, phases, w=1):
    return pi*w*w/4-deficit(n, phases, w)

def polygon_area(points):
    return abs(fsum(p[0]*q[1]-p[1]*q[0]
                    for p,q in zip(points, points[1:]+points[:1])))/2

def independent_boundary_area(n, rotations, M=320, w=1):
    """Integrate radius of curvature, then Minkowski-average support points.
    Every normal segment between adjacent grid nodes has exactly radius 0 or w.
    Rotations are integer multiples of 2*pi/(3*n).
    """
    L = 6*n*M
    h = 2*pi/L
    points = [(0.,0.)]
    x=y=0.
    for k in range(L):
        a, b = k*h, (k+1)*h
        if cos(n*(a+b)/2)>0:
            x += w*(cos(b)-cos(a))
            y += w*(sin(b)-sin(a))
        points.append((x,y))
    check(abs(x)<2e-9 and abs(y)<2e-9,(n,'curvature loop closure',x,y))
    result=[]
    shifts=[int(round(rot*L/(2*pi)))%L for rot in rotations]
    for k in range(L):
        X=Y=0.0
        for rot,s in zip(rotations,shifts):
            px,py=points[(k-s)%L]
            X += cos(rot)*px-sin(rot)*py
            Y += sin(rot)*px+cos(rot)*py
        result.append((X/len(rotations),Y/len(rotations)))
    return polygon_area(result)

def run():
    for n in [3,5,7,9,13,21]:
        c=pi/(2*n)
        # Check the Fourier identity at multiple non-special angles.
        for q in range(31):
            t=pi*q/30
            series=fsum(cos(j*t)/(j*j*(n*n*j*j-1)) for j in range(1,20000,2))
            check(abs(series-F(n,t))<2e-11,(n,t,'Fourier',series,F(n,t)))
        zero=deficit(n, [0,0,0])
        expected_zero=n/2*sin(c)/cos(c)-pi/4
        check(abs(zero-expected_zero)<1e-11,(n,'full deficit'))
        for q in range(61):
            x=2*pi*q/60
            check(F(n,x)<=F(n,0)+1e-12,(n,x,'kernel maximum'))
        rotations=[0,2*pi/(3*n),4*pi/(3*n)]
        phases=[n*x for x in rotations]
        D=deficit(n,phases)
        check(abs(D-disc_gap_formula(n))<1e-11,(n,'equal phases'))
        check(0<D<zero,(n,'positive disk gap'))
        # Exhaustively compare a two-dimensional 41x41 phase grid.
        equi=deficit(n,[0,2*pi/3,4*pi/3])
        for a,b in product(range(41),repeat=2):
            cand=deficit(n,[0,2*pi*a/40,2*pi*b/40])
            check(cand>=equi-3e-11,(n,a,b,'grid optimum'))
        # Independently integrate planar support points, not Fourier moments.
        for rots in [rotations,[0,0,0], [0,2*pi/(3*n),2*pi/(3*n)]]:
            ph=[n*r for r in rots]
            numeric=independent_boundary_area(n,rots)
            predicted=exact_area(n,ph)
            check(abs(numeric-predicted)<6e-5,(n,'boundary area',numeric,predicted))
    print('PASS',CHECKS,'finite checks; analytical proof required for all parameters')

if __name__=='__main__':
    run()
