#!/usr/bin/env python3
"""Numerical checks for the diameter-disk covering theorem; Python standard library only.

The analytical argument in RESULT.md, not these finite checks, proves the theorem.
"""
import math
import random

PI=math.pi

def polygon(n):
    return [(math.cos(2*PI*j/n), math.sin(2*PI*j/n)) for j in range(n)]

def area(p):
    return abs(sum(x*y1-y*x1 for (x,y),(x1,y1) in zip(p,p[1:]+p[:1])))/2

def clip(poly,nx,ny,c):
    if not poly:
        return []
    out=[]
    a=poly[-1]
    fa=nx*a[0]+ny*a[1]-c
    for b in poly:
        fb=nx*b[0]+ny*b[1]-c
        if fa <= 0 and fb <= 0:
            out.append(b)
        elif fa <= 0 < fb:
            t=fa/(fa-fb)
            out.append((a[0]+t*(b[0]-a[0]),a[1]+t*(b[1]-a[1])))
        elif fa > 0 >= fb:
            t=fa/(fa-fb)
            out.append((a[0]+t*(b[0]-a[0]),a[1]+t*(b[1]-a[1])))
            out.append(b)
        a,fa=b,fb
    return out

def intersection_area(n,sides=8192):
    # Independent polygonal approximation to a circular disk followed by
    # intersection with *every* supporting half-plane of the regular n-gon.
    disk=[(0.5+0.5*math.cos(2*PI*k/sides),0.5*math.sin(2*PI*k/sides)) for k in range(sides)]
    c=math.cos(PI/n)
    for j in range(n):
        a=(2*j+1)*PI/n
        disk=clip(disk,math.cos(a),math.sin(a),c)
    return area(disk)

def theorem_area(n):
    b=PI/n
    return PI/4-b/2+math.sin(2*b)/4

def theorem_mean(n):
    b=PI/n
    return (PI/2-b)/math.sin(2*b)+0.5

def vdc(i,base):
    num=0.0
    f=1.0/base
    while i:
        i,k=divmod(i,base)
        num+=k*f
        f/=base
    return num

def run():
    polygon_tests=[]
    for n in [3,4,5,6,7,9,12,17,24,31]:
        a=intersection_area(n)
        expected=theorem_area(n)
        err=abs(a-expected)
        assert err<1.4e-6,(n,a,expected,err)
        polygon_tests.append(err)
        expected_mean=theorem_mean(n)
        assert abs(n*a/area(polygon(n))-expected_mean)<2e-5
        assert expected_mean>n/4
    exact_point_checks=0
    for n in [3,4,5,6,7,8,13,25,51]:
        vertices=polygon(n)
        for k in range(1600):
            r=0.0001+0.9998*vdc(k+1,2)
            theta=2*PI*vdc(k+1,3)
            x=r*math.cos(theta); y=r*math.sin(theta)
            count=sum(1 for vx,vy in vertices if x*x+y*y <= x*vx+y*vy+1e-14)
            target=n*math.acos(r)/PI
            assert abs(count-target)<1.0000000001,(n,r,theta,count,target)
            exact_point_checks+=1
        # Exact geometrical witness on a polygon side midpoint.
        c=math.cos(PI/n)
        theta=PI/n
        x=c*math.cos(theta); y=c*math.sin(theta)
        count=sum(1 for vx,vy in vertices if x*x+y*y <= x*vx+y*vy+1e-12)
        assert count==2 and abs(n*math.acos(c)/PI-1)<1e-13
    # Independent area-uniform point Monte Carlo in a partition into n triangles.
    rng=random.Random(6406506)
    sample_results=[]
    for n in [3,4,5,6,10,21,31]:
        vertices=polygon(n)
        N=80000
        summ=0
        for _ in range(N):
            j=rng.randrange(n)
            r=math.sqrt(rng.random())
            t=rng.random()
            a,b=vertices[j],vertices[(j+1)%n]
            x=r*((1-t)*a[0]+t*b[0]);y=r*((1-t)*a[1]+t*b[1])
            rr=x*x+y*y
            summ+=sum(1 for vx,vy in vertices if rr<=x*vx+y*vy)
        empirical=summ/N
        truth=theorem_mean(n)
        assert abs(empirical-truth)<0.065,(n,empirical,truth)
        sample_results.append((n,round(empirical,5),round(truth,5)))
    for n in [3,4,5,6,9,12,31,100,1000,10000]:
        delta=1-n*math.sin(2*PI/n)/(2*PI)
        assert delta>=0
        bound=PI/n+delta
        assert bound>=0
    print('PASS: exact theorem area versus independent disk-polygon clipping:',len(polygon_tests),'instances; max area error',max(polygon_tests))
    print('PASS: deterministic pointwise angular count checks:',exact_point_checks,'plus sharp side-midpoint witnesses')
    print('PASS: independent uniform-polygon Monte Carlo:',sample_results)
    print('PASS: quantitative distribution bounds checked for 10 polygon sizes')
    print('NOTE: finite tests support, but do not replace, the analytic proof')

if __name__=='__main__':run()
