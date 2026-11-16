#!/usr/bin/env python3
"""Supplementary finite tests for a three-atom Fourier-zero theorem.

Run with python3 checks/tri_atomic_zeros.py. Requires only the Python standard library.
Numerics never substitute for the general proof.
"""
import cmath
import math
import random
from itertools import product

PI = math.pi
TWO_PI = 2 * PI


def phases(w):
    a, b, c = w
    angle = math.acos(max(-1.0, min(1.0, (c*c-a*a-b*b)/(2*a*b))))
    z = -(a+b*cmath.exp(1j*angle))/c
    assert abs(abs(z)-1) < 2e-12
    return [0., angle, cmath.phase(z)]


def constant(w):
    angles = []
    for i in range(3):
        j, k = (i+1)%3, (i+2)%3
        co = (w[j]**2+w[k]**2-w[i]**2)/(2*w[j]*w[k])
        angles.append(math.acos(max(-1., min(1., co))))
    return .5 + min(angles)/TWO_PI


def diameter(p):
    return max(math.dist(p[i],p[j]) for i in range(3) for j in range(i+1,3))


def roots2(w, p, N=7):
    # Explicit inverse of the two-by-two row-coordinate matrix.
    a = (p[1][0]-p[0][0],p[1][1]-p[0][1])
    b = (p[2][0]-p[0][0],p[2][1]-p[0][1])
    det = a[0]*b[1]-a[1]*b[0]
    assert abs(det) > 1e-6
    t = phases(w)
    v = [-t[1]/TWO_PI,-t[2]/TWO_PI]
    out=[]
    for s in (1,-1):
        for n,m in product(range(-N,N+1),repeat=2):
            u1,u2 = n+s*v[0],m+s*v[1]
            x=(b[1]*u1-a[1]*u2)/det
            y=(-b[0]*u1+a[0]*u2)/det
            out.append((math.hypot(x,y),(x,y)))
    return min(out)


def fourier(w,p,x):
    return sum(w[j]*cmath.exp(-2j*PI*(p[j][0]*x[0]+p[j][1]*x[1])) for j in range(3))


def extremal_sites(w,h=0.04):
    th = phases(w)
    # Projected phases in cycles, with sign chosen to match the Fourier convention.
    vals = [(-x/TWO_PI)%1 for x in th]
    indexed=sorted((v,j) for j,v in enumerate(vals))
    gaps=[(indexed[(i+1)%3][0] + (1 if i==2 else 0) - indexed[i][0]) for i in range(3)]
    cut=max(range(3),key=lambda i:gaps[i]); start=indexed[(cut+1)%3][0]
    lifts=[(v-start)%1 for v in vals]
    c=constant(w)
    assert abs(max(lifts)-c)<2e-12, (w,lifts,c)
    mid=sorted(range(3),key=lambda j:lifts[j])[1]
    pts=[(lifts[j]/c, h if j==mid else 0.) for j in range(3)]
    assert abs(diameter(pts)-1)<2e-12
    return pts,c


def check():
    rng=random.Random(20261112)
    assertions=0
    for weights in ((1.,1.,1.),(1.,1.,1.5),(.8,1.1,1.25),(1.,1.98,2.0)):
        p, c=extremal_sites(weights)
        assert abs(fourier(weights,p,(c,0)))<1e-11
        assert abs(roots2(weights,p,N=5)[0]-c)<1e-10
        assertions+=2
    for m in range(1,16):
        h=m*.04
        p=((0.,0.),(1.,0.),(.5,h))
        assert diameter(p)==1.
        assert abs(fourier((1.,1.,1.),p,(2/3,0)))<1e-11
        assertions+=2
    for _ in range(500):
        for attempt in range(100):
            weights=[rng.uniform(.25,2) for j in range(3)]
            if 2*max(weights)<sum(weights):break
        p=[(rng.uniform(-1.,1.),rng.uniform(-1.,1.)) for j in range(3)]
        det=(p[1][0]-p[0][0])*(p[2][1]-p[0][1])-(p[1][1]-p[0][1])*(p[2][0]-p[0][0])
        if abs(det)<1e-5:continue
        near,x=roots2(weights,p,N=7)
        assert near*diameter(p)+1e-9>=constant(weights)
        assert abs(fourier(weights,p,x))<2e-10
        assertions+=2
    for w in ((3.,1.,1.),(4.,1.,2.)):
        p=((-1.,.5),(1.,0.),(.4,.8))
        for x in ((0.,0.),(.3,.7),(1.4,-.2),(200.,3.)):
            assert abs(fourier(w,p,x))>max(w)-sum(w)+max(w)-1e-10
            assertions+=1
    print('CHECK_OK finite_assertions=', assertions, 'analytic_proof_required=YES')


if __name__=='__main__':
    check()
