"""Reproducible direct line-segment/box tests for a rectangle's boundary-chord interception law.
Uses only Python's standard library. The proof is analytic; these checks are diagnostics.
"""
from math import log, sqrt
from random import Random

def conditional_opposite(t):
    return 1.0-(1.0-t)**2/(1.0+t)

def conditional_adjacent(t):
    return ((1.0+t)**2-(1.0-t)**2*(1.0+2.0*log((1.0+t)/(1.0-t))))/4.0

def exact(a,b,t):
    w=2.0*a*b/(a+b)**2
    return (1.0-w)*conditional_opposite(t)/2.0+w*conditional_adjacent(t)

def hit(p,q,a,b,t):
    """Independent parametric segment clipping against [-ta,ta] x [-tb,tb]."""
    lo,hi=0.0,1.0
    for x,dx,R in ((p[0],q[0]-p[0],t*a),(p[1],q[1]-p[1],t*b)):
        if abs(dx)<1e-14:
            if abs(x)>R:
                return False
        else:
            u,v=(-R-x)/dx,(R-x)/dx
            if u>v: u,v=v,u
            lo=max(lo,u);hi=min(hi,v)
    return lo<=hi

def point_on_edge(rng,a,b):
    s=rng.random()*(4*a+4*b)
    if s<2*a: return -a+s,b
    if s<2*a+2*b: return a,b-(s-2*a)
    if s<4*a+2*b: return a-(s-2*a-2*b),-b
    return -a,-b+(s-4*a-2*b)

def main():
    rng=Random(98421)
    total=0
    for a,b in ((1.,1.),(1.,2.),(1.,6.)):
        for t in (.05,.25,.56,.80,.97):
            n=110000
            count=0
            for _ in range(n):
                p,q=point_on_edge(rng,a,b),point_on_edge(rng,a,b)
                count+=hit(p,q,a,b,t)
            empirical=count/n; prediction=exact(a,b,t)
            bound=5.5*sqrt(prediction*(1-prediction)/n)+0.0005
            assert abs(empirical-prediction)<bound,(a,b,t,empirical,prediction,bound)
            total+=n
    def N(z): return 1-2*z-z*z+2*z**3+4*z*z*log(z)
    lo,hi=.1,.5
    for _ in range(100):
        md=(lo+hi)/2
        if N(md)>0:lo=md
        else:hi=md
    z=(lo+hi)/2; critical=(1-z)/(1+z)
    assert .5604879233 < critical < .5604879234
    for a,b in ((1,1),(1,2),(1,100)):
        assert abs(exact(a,b,critical)-exact(1,1,critical))<1e-13
    assert exact(1,1,.2)<exact(1,8,.2)
    assert exact(1,1,.8)>exact(1,8,.8)
    print('RECTANGLE_BOUNDARY_CHORD_INTERCEPTION_OK',total,critical)

if __name__=='__main__':main()
