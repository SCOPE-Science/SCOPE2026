#!/usr/bin/env python3
"""Numerical consistency tests for planar flat-torus distance reconstruction.

Uses Python's standard library only.  These finite checks are not the
analytic proof of injectivity or the square-root threshold theorem.
"""
import math
from itertools import product

TAU=2.0*math.pi

def dot(a,b):
    return a[0]*b[0]+a[1]*b[1]

def cross(a,b):
    return a[0]*b[1]-a[1]*b[0]

def clip(poly,v):
    h=dot(v,v)/2.0; out=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        a=dot(p,v)-h; b=dot(q,v)-h
        if a<=1.e-10: out.append(p)
        if (a<-1.e-10 and b>1.e-10) or (a>1.e-10 and b<-1.e-10):
            t=a/(a-b)
            out.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
    return out

def polygon(b1,b2):
    R=10.0*max(math.hypot(*b1),math.hypot(*b2))
    p=[(-R,-R),(R,-R),(R,R),(-R,R)]
    for i,j in product(range(-4,5),repeat=2):
        if i==0 and j==0: continue
        v=(i*b1[0]+j*b2[0],i*b1[1]+j*b2[1])
        p=clip(p,v)
    p=[q for k,q in enumerate(p) if math.dist(q,p[k-1])>1.e-8]
    a=sum(cross(u,v) for u,v in zip(p,p[1:]+p[:1]))/2
    facets=[]
    for u,v in zip(p,p[1:]+p[:1]):
        d=(v[0]-u[0],v[1]-u[1]); norm=math.hypot(*d)
        if norm<1e-8: continue
        normal=(d[1]/norm,-d[0]/norm)
        facets.append((dot(normal,u),math.atan2(normal[1],normal[0])%TAU,norm))
    return p,a,facets

def outside_angle(r,facets):
    intervals=[]
    for h,theta,_ in facets:
        if r<=h: continue
        alpha=math.acos(min(1.0,max(-1.0,h/r)))
        lo=(theta-alpha)%TAU; hi=(theta+alpha)%TAU
        if lo<=hi:intervals.append((lo,hi))
        else:intervals.extend(((0.0,hi),(lo,TAU)))
    intervals.sort()
    total=0.0; high=0.0
    for lo,hi in intervals:
        if hi>high:
            total+=hi-max(lo,high)
            high=hi
    return total

def threshold_groups(facets):
    out=[]
    for h,_,_ in sorted(facets):
        if out and abs(h-out[-1][0])<=1e-8:
            out[-1][1]+=1
        else:out.append([h,1])
    return out

def cdf_from_angles(r,area,facets,steps=5000):
    # Independent polar radial integral using the half-plane description.
    accum=0.0
    for j in range(steps):
        theta=TAU*(j+0.5)/steps
        e=(math.cos(theta),math.sin(theta)); rho=math.inf
        for h,alpha,_ in facets:
            proj=math.cos(theta-alpha)
            if proj>1e-15:rho=min(rho,h/proj)
        accum+=min(r,rho)**2
    return TAU*accum/(2*steps*area)

def cdf_from_circular_arcs(r,area,facets,steps=5000):
    # Independent radial integral via union of excluded circle arcs.
    ss=0.0
    for j in range(steps):
        t=r*(j+0.5)/steps
        ss+=t*(TAU-outside_angle(t,facets))
    return r*ss/(steps*area)

def check(b1,b2):
    poly,area,facets=polygon(b1,b2)
    true_area=abs(cross(b1,b2))
    assert abs(area-true_area)<1e-8,(area,true_area)
    groups=threshold_groups(facets)
    assert len(facets) in (4,6) and sum(m for _,m in groups)==len(facets)
    assert all(m%2==0 for _,m in groups)
    assert all(h>0 and length>0 for h,_,length in facets)
    for h,m in groups:
        # The square-root coefficient is obtained solely from circle-arc data.
        expected=2*m*math.sqrt(2/h)
        small=[]
        for eps in (1e-6,1e-8,1e-10):
            measured=(outside_angle(h+eps,facets)-outside_angle(h,facets))/math.sqrt(eps)
            small.append(measured)
        assert abs(small[-1]-expected)<0.04, (b1,b2,h,m,small,expected)
    # Decode the lattice shape from recovered lengths, including degeneracies.
    hs=[h for h,_,_ in facets]
    if len(facets)==4:
        a,b=(2*groups[0][0],2*groups[-1][0]) if len(groups)==2 else (2*groups[0][0],2*groups[0][0])
        assert abs(a*b-area)<1e-6,(a,b,area)
    else:
        ls=sorted([2*h for h,_,_ in facets])[::2]
        assert len(ls)==3,(ls,facets)
        u,v,w=ls
        uv=(w*w-u*u-v*v)/2
        decoded_area=math.sqrt(u*u*v*v-uv*uv)
        assert abs(decoded_area-area)<1e-6,(decoded_area,area)
    # Two independent integration coordinates for the same torus CDF.
    radius=max(math.hypot(*v) for v in poly)
    for f in (0.15,0.4,0.65,0.85,1.0,1.15):
        r=f*radius
        a=cdf_from_angles(r,area,facets)
        b=cdf_from_circular_arcs(r,area,facets)
        assert abs(a-b)<0.0025,(f,a,b)
        assert -3e-5<=a<=1+3e-5,(b1,b2,f,a)
    return len(facets),[(round(h,8),m) for h,m in groups]

def main():
    configs=[
        ((1.,0.),(0.,2.)),
        ((1.,0.),(0.,1.)),
        ((1.,0.),(.5,math.sqrt(3)/2)),
        ((1.,0.),(.4,1.2)),
        ((2.,0.),(.1,3.)),
        ((1.,0.),(.03,1.7)),
        ((1.4,0.),(.45,1.25)),
        ((1.0,0.),(.8,.75)),
    ]
    for b1,b2 in configs:
        facets,groups=check(b1,b2)
        print(f'PASS lattice {b1!r},{b2!r}: {facets} facets, threshold/multiplicity {groups}')
    print(f'PASS {len(configs)} lattice configurations, {len(configs)*6} independent-CDF comparisons, {sum(len(threshold_groups(polygon(*cfg)[2])) for cfg in configs)*3} threshold limits, and reconstruction/area checks.')

if __name__=='__main__': main()
