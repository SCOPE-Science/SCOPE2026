#!/usr/bin/env python3
"""Recompute projected areas directly and test universal right-prism moment identities.

Only Python standard library. These finite tests are diagnostics, not infinite proofs.
"""
import math
import random

PI=math.pi
ROOT3=math.sqrt(3.0)


def dot(v,w):return sum(a*b for a,b in zip(v,w))
def cross(v,w):return (v[1]*w[2]-v[2]*w[1],v[2]*w[0]-v[0]*w[2],v[0]*w[1]-v[1]*w[0])
def polygon_area(poly):return abs(sum(poly[i][0]*poly[(i+1)%len(poly)][1]-poly[(i+1)%len(poly)][0]*poly[i][1] for i in range(len(poly))))/2

def prism_vertices(base,height):
    return [(x,y,z*height/2) for x,y in base for z in [-1,1]]

def shadow_area(vertices,u):
    p=(1.,0.,0.) if abs(u[0])<.8 else (0.,1.,0.)
    e=cross(u,p)
    e=tuple(x/math.sqrt(dot(e,e)) for x in e)
    f=cross(u,e)
    points=sorted(set((dot(v,e),dot(v,f)) for v in vertices))
    def det(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lower=[]
    for v in points:
        while len(lower)>1 and det(lower[-2],lower[-1],v)<=0:lower.pop()
        lower.append(v)
    upper=[]
    for v in reversed(points):
        while len(upper)>1 and det(upper[-2],upper[-1],v)<=0:upper.pop()
        upper.append(v)
    return polygon_area(lower[:-1]+upper[:-1])

def width(base,theta):
    c,s=math.cos(theta),math.sin(theta)
    coords=[x*c+y*s for x,y in base]
    return max(coords)-min(coords)

def moments(base,height,grid=65536):
    area=polygon_area(base)
    vals=[width(base,2*PI*j/grid) for j in range(grid)]
    beta=sum(vals)/grid
    eta=sum(v*v for v in vals)/grid
    mean=area/2+PI*beta*height/4
    var=(area*area/12+area*height*beta*(2/3-PI/4)
         +height*height*(2*eta/3-PI*PI*beta*beta/16))
    h_opt=area*beta*(PI-2)/(4*eta-PI*beta*beta)
    return (mean,var,beta,eta,h_opt)

def draw_normal(rng):
    z=rng.uniform(-1.,1.)
    phi=rng.uniform(0.,2*PI)
    r=math.sqrt(1-z*z)
    return (r*math.cos(phi),r*math.sin(phi),z),phi


def test():
    rng=random.Random(20261101)
    triangle=[(math.cos(2*PI*j/3),math.sin(2*PI*j/3)) for j in range(3)]
    square=[(-1,-1),(1,-1),(1,1),(-1,1)]
    pentagon=[(math.cos(2*PI*j/5),math.sin(2*PI*j/5)) for j in range(5)]
    skew=[(-1.,-.7),(1.3,-.5),(1.7,.7),(.3,1.2),(-.8,.7)]
    for base in (triangle,square,pentagon,skew):
        area=polygon_area(base)
        for height in (.35,1.1,2.75):
            v=prism_vertices(base,height)
            mu,vari,beta,eta,opt=moments(base,height)
            assert eta>=beta*beta-1e-10
            assert opt>0
            x=[]
            for j in range(4800):
                u,phi=draw_normal(rng)
                direct=shadow_area(v,u)
                analytic=area*abs(u[2])+height*math.sqrt(1-u[2]*u[2])*width(base,phi+PI/2)
                assert abs(direct-analytic)<1e-10,(direct,analytic)
                x.append(direct)
            observed=sum(x)/len(x)
            observedvar=sum((t-observed)**2 for t in x)/len(x)
            assert abs(observed-mu)<.09,(base,height,observed,mu)
            assert abs(observedvar-vari)<.11,(base,height,observedvar,vari)
            def cv2(h):
                m,v,b,e,o=moments(base,h,grid=8192)
                return v/m**2
            assert all(cv2(h)>=cv2(opt)-1e-12 for h in (.0001,.01,opt*.7,opt*1.3,opt*2.,100.))
    area=3*ROOT3/4
    beta=3*ROOT3/PI
    eta=1.5+9*ROOT3/(4*PI)
    h_star=area*beta*(PI-2)/(4*eta-PI*beta*beta)
    assert abs(h_star-1.035995798238795)<1e-11
    assert abs(h_star-moments(triangle,1.)[4])<1e-7
    h_worst=ROOT3/2
    assert h_star>h_worst
    x=(ROOT3*h_star/2)/area
    assert abs(math.sqrt(1+4*x*x)-1.7053053393420001)<1e-12
    assert abs(math.sqrt(7/3)-1.5275252316519468)<1e-12
    smax=(PI-2)/(4-PI)
    for base in (triangle,square,pentagon,skew):
        _,_,b,e,h=moments(base,1.)
        assert h*b/polygon_area(base)<=smax+1e-10
    print('ALL_CONVEX_POLYGON_PRISM_SHADOW_CHECKS_PASSED')
    print('TRIANGLE_TWO_DISTINCT_OPTIMAL_HEIGHTS_PASSED')
    print('triangle_coefficient_of_variation_height=',h_star)
    print('triangle_worst_view_ratio_height=',h_worst)

if __name__=='__main__':test()
