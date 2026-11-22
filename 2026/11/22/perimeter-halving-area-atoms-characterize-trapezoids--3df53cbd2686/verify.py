"""Reproduce exact plateaux and local curvature of perimeter-halving cut areas.

Only Python standard library is needed. The analytic proof covers all convex
polygons and trapezoids; finite tests below are independent cross-checks.
"""
from fractions import Fraction as F
from math import hypot
import random


def cross(p, q):
    return p[0]*q[1]-p[1]*q[0]


def shoelace(vertices):
    return abs(sum(cross(p,q) for p,q in zip(vertices,vertices[1:]+vertices[:1])))/2


def polygon_cut_area(poly, s):
    """CCW area between boundary arclength s and s+P/2, with closing chord."""
    n=len(poly)
    lengths=[hypot(*(poly[(i+1)%n][j]-poly[i][j] for j in range(2))) for i in range(n)]
    starts=[0.0]
    for length in lengths: starts.append(starts[-1]+length)
    perimeter=starts[-1]
    s=s%perimeter
    e=(s+perimeter/2)%perimeter
    def locate(v):
        for i in range(n):
            if v < starts[i+1]-1e-12:
                f=(v-starts[i])/lengths[i]
                return (i, (poly[i][0]+f*(poly[(i+1)%n][0]-poly[i][0]),poly[i][1]+f*(poly[(i+1)%n][1]-poly[i][1])))
        return n-1,poly[0]
    i,p=locate(s)
    j,q=locate(e)
    mid=[]
    k=(i+1)%n
    while k!=((j+1)%n):
        distance=(starts[k]-s)%perimeter
        if 1e-10<distance<perimeter/2-1e-10:
            mid.append(poly[k])
        k=(k+1)%n
    return shoelace([p]+mid+[q]),i,j,lengths


def exact_trapezoid(b,a,c,d,h,C,x):
    assert c*c == (a-b)*(a-b)+h*h and d==h
    p=(x,F(0)); B=(b,F(0)); T=(a,h); q=(C-x,h)
    area=shoelace([p,B,T,q]); total=h*(a+b)/2
    expected=h*(a+b-C)/2
    assert area==expected
    return min(area,total-area)/total


def main():
    count=0
    for b,a,h,c,d in [(F(7),F(4),F(4),F(5),F(4)),
                        (F(10),F(5),F(12),F(13),F(12)),
                        (F(7),F(7),F(4),F(4),F(4))]:
        P=a+b+c+d; C=(a+b+c-d)/2
        lo=max(F(0),C-a); hi=min(b,C)
        assert hi-lo==min(a,b);count+=1
        atom=F(1,2)-abs(c-d)/(2*(a+b))
        for i in range(101):
            x=lo+(hi-lo)*F(i,100)
            got=exact_trapezoid(b,a,c,d,h,C,x)
            assert got==atom
            count+=1
        assert 2*(hi-lo)/P == 2*min(a,b)/P
        count+=1

    rng=random.Random(2831)
    # Independent general-boundary shoelace evaluation and second derivative.
    # Check 4- and 5-vertex examples with no parallel paired sides.
    polygons=[[(0.,0.),(7.,0.),(4.,4.),(0.,4.)],
              [(0.,0.),(5.,0.),(6.,3.),(2.,5.),(-1.,2.)],
              [(0.,0.),(4.,0.),(6.,2.),(5.,5.),(1.,6.),(-1.,3.)],
              [(0.,0.),(4.,0.),(5.,2.),(3.,5.),(-1.,4.)]]
    for poly in polygons:
        for _ in range(160):
            length=sum(hypot(poly[(j+1)%len(poly)][0]-poly[j][0],
                             poly[(j+1)%len(poly)][1]-poly[j][1])
                       for j in range(len(poly)))
            s=rng.uniform(0,length/2)
            dt=1e-3
            area,ei,ej,L=polygon_cut_area(poly,s)
            am,em,enm,_=polygon_cut_area(poly,s-dt)
            ap,ep,enp,_=polygon_cut_area(poly,s+dt)
            if ei!=em or ei!=ep or ej!=enm or ej!=enp: continue
            u=((poly[(ei+1)%len(poly)][0]-poly[ei][0])/L[ei],
               (poly[(ei+1)%len(poly)][1]-poly[ei][1])/L[ei])
            v=((poly[(ej+1)%len(poly)][0]-poly[ej][0])/L[ej],
               (poly[(ej+1)%len(poly)][1]-poly[ej][1])/L[ej])
            curvature=(ap-2*area+am)/dt**2
            assert abs(curvature+cross(u,v)) < 4e-5, (curvature, cross(u,v))
            count+=1
    print('VERIFY_OK',count,'exact_and_geometric_assertions')

if __name__=='__main__':main()
