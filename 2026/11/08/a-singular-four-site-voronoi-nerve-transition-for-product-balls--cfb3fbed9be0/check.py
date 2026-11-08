#!/usr/bin/env python3
"""Numerical sanity checks for a four-site product-norm Voronoi nerve theorem.
The proof is analytic; these finite checks do not certify all parameters.
Run with Python 3 standard library only: python check.py
"""
import math
import random

RNG = random.Random(20261103)
TWO_PI = 2 * math.pi

def sites(R, h):
    return [(R*math.cos(k*TWO_PI/3), R*math.sin(k*TWO_PI/3), 0.0)
            for k in range(3)] + [(0.0,0.0,h)]

def distance_p(x, y, p):
    planar=math.hypot(x[0]-y[0], x[1]-y[1]); z=abs(x[2]-y[2])
    return (planar**p + z**p)**(1/p)

def quadruple_height(R,h,p):
    assert p>1 and h>0
    if h==R: return 0.
    if h>R:
        lo,hi=0.,h
        for _ in range(180):
            mid=(lo+hi)/2
            left=math.hypot(R,mid) if p==2 else (R**p+mid**p)**(1/p)
            if left>h-mid:hi=mid
            else:lo=mid
        return (lo+hi)/2
    # root for negative w: (R^p+t^p)^(1/p)=t+h
    def g(t):
        if t==0:return R-h
        return t*math.expm1(math.log1p((R/t)**p)/p)-h
    lo,hi=0.,max(1.,R)
    while g(hi)>0:hi*=2
    for _ in range(180):
        mid=(lo+hi)/2
        if g(mid)>0:lo=mid
        else:hi=mid
    return -(lo+hi)/2

def close(a,b,tol=2e-9):
    assert abs(a-b)<tol*(1+abs(a)+abs(b)), (a,b)

n1=n2=0
for _ in range(4500):
    R=.1+2*RNG.random(); h=R*(.1+.9*RNG.random())
    s=sites(R,h)
    a=(h*h-R*R)/(R+2*h)
    y=(a,0.,-0.2-RNG.random())
    ds=[distance_p(z,y,1) for z in s]
    close(ds[1],ds[2]);close(ds[1],ds[3])
    assert ds[0]>ds[1]+1e-10
    # Triple 123 cannot belong to all closest cells: at horizontal center, the fourth is closer.
    for w in [-100.,-2.,0.,2.,100.]:
        dtri=R+abs(w);d4=abs(h-w)
        assert d4<dtri
    n1+=1
for _ in range(4000):
    R=.3+RNG.random(); q=.70+1.5*RNG.random(); h=R*q
    p=1.04+4*RNG.random()
    w=quadruple_height(R,h,p)
    ds=[distance_p(z,(0.,0.,w),p) for z in sites(R,h)]
    assert max(ds)-min(ds)<2e-8*(1+R+abs(w)+h), (R,h,p,w,ds)
    if h<R:assert w<0
    if h>R:assert 0<w<h
    n2+=1
R=11/20; h=1/2
assert h<R and math.sqrt(3)*R<1<R+h
delta=min(1-math.sqrt(3)*R,R+h-1)
assert delta>0
for p in (1.03,1.02,1.015,1.01):
    w=quadruple_height(R,h,p)
    t=-w
    approx=R/math.e*(R/h)**(1/(p-1))
    print('p=',p,'height=',repr(w),'asymptotic_ratio=',repr(t/approx))
    assert t>0
print('FOUR_SITE_BICONE_VERIFIER_OK', n1+n2+4, 'random_1=',n1, 'random_p=',n2,
      'lower_defect_bound=',(2*math.pi/3)*delta**3)
