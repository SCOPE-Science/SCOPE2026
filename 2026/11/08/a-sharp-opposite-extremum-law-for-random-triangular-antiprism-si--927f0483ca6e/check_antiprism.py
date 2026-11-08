#!/usr/bin/env python3
"""Seeded direct geometric checks for the exact antiprism projection law."""
import math
import random

PI = math.pi

def vertices(h):
    vs = [(math.cos(2*PI*i/3),math.sin(2*PI*i/3),h) for i in range(3)]
    return vs + [(-x,-y,-z) for (x,y,z) in vs]

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def norm(a):return math.sqrt(dot(a,a))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def unit(a):return tuple(x/norm(a) for x in a)

def projection_hull_size(pts,normal):
    axis=(1.0,0.0,0.0) if abs(normal[0])<0.9 else (0.0,1.0,0.0)
    e1=unit(cross(normal,axis));e2=cross(normal,e1)
    q=sorted((dot(p,e1),dot(p,e2)) for p in pts)
    def cv(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    low=[]
    for p in q:
        while len(low)>1 and cv(low[-2],low[-1],p)<=1e-12:low.pop()
        low.append(p)
    up=[]
    for p in reversed(q):
        while len(up)>1 and cv(up[-2],up[-1],p)<=1e-12:up.pop()
        up.append(p)
    return len(low)+len(up)-2

def pair_solid_angles(h):
    v=vertices(h)[:3]
    def plus(a,b):return tuple(x+y for x,y in zip(a,b))
    def neg(a):return tuple(-x for x in a)
    def sol(r):
        a,b,c=r
        det=abs(dot(a,cross(b,c)))
        den=norm(a)*norm(b)*norm(c)+dot(a,b)*norm(c)+dot(b,c)*norm(a)+dot(c,a)*norm(b)
        return 2*math.atan2(det,den)
    oplus=sol([plus(v[0],v[1]),plus(v[0],v[2]),plus(v[1],v[2])])
    omin=sol([plus(v[0],v[1]),plus(v[0],neg(v[2])),plus(v[1],neg(v[2]))])
    return (oplus+3*omin)/(2*PI)

def formula(h):
    return 1+(3/PI)*math.atan(4*h)-(6/PI)*math.atan(2*math.sqrt(3)*h/math.sqrt(1+4*h*h))

def derivative(h):
    s=math.sqrt(1+4*h*h)
    return (12/PI)*(s-math.sqrt(3))/(s*(1+16*h*h))

def random_spherical_unit(rng):
    z=2*rng.random()-1;t=2*PI*rng.random();r=math.sqrt(1-z*z)
    return (r*math.cos(t),r*math.sin(t),z)

if __name__=='__main__':
    rng=random.Random(20261101)
    test_heights=[0.16,0.4,1/math.sqrt(2),1.4,3.0]
    for h in test_heights:
        pred=formula(h);cone=pair_solid_angles(h)
        assert abs(pred-cone)<3e-13,(h,pred,cone)
        eps=1e-6
        dnum=(formula(h+eps)-formula(h-eps))/(2*eps)
        assert abs(dnum-derivative(h))<2e-9,(h,dnum,derivative(h))
        points=vertices(h)
        c=0
        num=18000
        for _ in range(num):
            u=random_spherical_unit(rng)
            if projection_hull_size(points,u)==6:c+=1
        p=c/num
        tolerance=5.5*math.sqrt(pred*(1-pred)/num)+.003
        assert abs(p-pred)<tolerance,(h,p,pred,tolerance)
        print('h={:.8f} exact={:.10f} cone={:.10f} direct_projection={:.10f} tolerance={:.6f}'.format(h,pred,cone,p,tolerance))
    crit=1/math.sqrt(2)
    assert abs(derivative(crit))<1e-14
    assert all(derivative(x)<0 for x in (0.03,.25,.65))
    assert all(derivative(x)>0 for x in (.75,1,4,100))
    assert abs(formula(crit)-4/PI*math.atan(math.sqrt(2)/5))<3e-15
    assert abs(formula(1e-8)-1)<1e-6
    assert abs(formula(1e8)-.5)<1e-6
    print('TRIANGULAR_ANTIPRISM_SIX_SHADOW_CHECKS_PASSED')
