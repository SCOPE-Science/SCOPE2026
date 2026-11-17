"""Reproducible geometry and optimization diagnostics; standard-library only.

The numerical checks are finite diagnostics and are not substitutes for the
geometric proof of the covering threshold.
"""
import math
import random

ROOT3=math.sqrt(3)

def threshold(b):
    assert b>=0
    if b<=0.5:
        return math.sqrt(1-b+b*b)
    if b<1:
        return (ROOT3-math.sqrt(4*b*b-1))/2
    return 0.0

def price(w,b):
    return threshold(b)**2+2*w*b*b

def stationary(w):
    c=1+2*w
    a=1/(2*c)
    b=0.5*math.sqrt(1+3/c**2)
    va=1-1/(4*c)
    vb=(c+2-3/c)/4
    return (a,va),(b,vb)

def nearest_b(p, radius=4):
    x,y=p
    return min(math.hypot(x-(m+n/2),y-n*ROOT3/2)
               for m in range(-radius,radius+1)
               for n in range(-radius,radius+1)
               if (m-n)%3!=0)

def hex_point(rng):
    t=rng.random()*2*math.pi
    sector=t%(math.pi/3)
    maxr=(ROOT3/2)/math.cos(sector-math.pi/6)
    r=maxr*math.sqrt(rng.random())
    return (r*math.cos(t),r*math.sin(t))

def run():
    rng=random.Random(20261110)
    vertices=[(math.cos(i*math.pi/3),math.sin(i*math.pi/3)) for i in range(6)]
    for k in range(40000):
        p=hex_point(rng)
        d6=min(math.dist(p,v) for v in vertices)
        dall=nearest_b(p)
        assert abs(d6-dall)<1e-12, (k,p,d6,dall)
    for b in [0.,.04,.1,.25,.49,.5,.52,.6,.75,.9,.99,1.]:
        r=threshold(b)
        # For any point more than r from the origin, one B disk must cover it.
        for k in range(6000):
            p=hex_point(rng)
            radial=math.hypot(*p)
            covered = radial<=r+1e-12 or nearest_b(p)<=b+1e-12
            assert covered,(b,r,p,radial)
        if 0<b<1:
            if b<=.5:
                # On a side of the hexagon at distance b from one endpoint.
                q=(1-b/2,b*ROOT3/2)
            else:
                # Inner disk-intersection point on the 30-degree bisector.
                q=(r*ROOT3/2,r/2)
            assert abs(math.hypot(*q)-r)<1e-10
            assert abs(nearest_b(q)-b)<1e-10,(b,q,nearest_b(q))
    for w in [0.01,0.2,0.5,0.8,ROOT3/2,1.,2.,10.]:
        (a,fa),(b,fb)=stationary(w)
        assert abs(price(w,a)-fa)<1e-11
        assert abs(price(w,b)-fb)<1e-11
        actual=min(fa,fb)
        # Independent grid minimization of the original covering cost.
        brute=min(price(w,j/10000) for j in range(10001))
        assert 0<=brute-actual<1e-6, (w,actual,brute)
        assert (fa<fb)==(w>ROOT3/2) if abs(w-ROOT3/2)>1e-9 else abs(fa-fb)<1e-11
    # The equal-weight answer is the previously known geometric benchmark.
    (a,fa),_ = stationary(1.)
    assert abs(a-1/6)<1e-14 and abs(threshold(a)-math.sqrt(31)/6)<1e-14
    assert abs(fa-11/12)<1e-14
    print('TWO_RADIUS_TRIANGULAR_WEIGHTED_COVERING_OK')

if __name__=='__main__':
    run()
