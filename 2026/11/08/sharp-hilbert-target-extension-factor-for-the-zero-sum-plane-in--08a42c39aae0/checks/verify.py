#!/usr/bin/env python3
"""Finite numerical diagnostics for a three-point Hilbert extension inequality."""
import math
import random

EPS=1e-10

def dot(x,y):return sum(a*b for a,b in zip(x,y))
def sub(x,y):return tuple(a-b for a,b in zip(x,y))
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def mul(t,x):return tuple(t*a for a in x)
def norm(x):return math.sqrt(dot(x,x))

def center_of_triangle(A,B,C):
    pts=(A,B,C)
    edge=[(norm(sub(pts[i],pts[j])),i,j) for i,j in ((0,1),(0,2),(1,2))]
    diameter,i,j=max(edge)
    k=({0,1,2}-{i,j}).pop()
    v=sub(pts[k],pts[i]); w=sub(pts[k],pts[j])
    if dot(v,w)<=0 or diameter<=EPS:
        return mul(.5,add(pts[i],pts[j]))
    # Circumcenter in span(B-A,C-A).
    U=sub(B,A); V=sub(C,A)
    aa=dot(U,U); bb=dot(U,V); cc=dot(V,V)
    det=aa*cc-bb*bb
    if det<1e-20:
        return mul(.5,add(pts[i],pts[j]))
    s=(.5*aa*cc-.5*cc*bb)/det
    t=(.5*cc*aa-.5*aa*bb)/det
    return add(A,add(mul(s,U),mul(t,V)))

def run():
    random.seed(80911)
    cases=0
    for mode in (0,1,2):
        for _ in range(2000):
            if mode==0:
                u=(random.uniform(-3,3),random.uniform(-3,3))
                v=(random.uniform(-3,3),random.uniform(-3,3))
            elif mode==1:
                u=(1.,0.)
                v=(random.uniform(-1.,1.),random.uniform(-.001,.001))
            else:
                alpha=random.uniform(0,2*math.pi)
                u=(math.cos(alpha),math.sin(alpha))
                theta=random.uniform(-.01,.01)
                v=(math.cos(alpha+math.pi/3+theta),math.sin(alpha+math.pi/3+theta))
            A=(0.,0.); B=mul(2,u); C=mul(2,v)
            m=max(norm(u),norm(v),norm(sub(u,v)))
            D=2*m
            o=center_of_triangle(A,B,C)
            g=mul(1/3,add(add(A,B),C))
            R=max(norm(sub(o,p)) for p in (A,B,C))
            assert R<=D/math.sqrt(3)+1e-8
            assert norm(sub(o,g))<=D/6+1e-8
            upper=max(R,3*norm(sub(o,g)))
            assert upper <= 2*m/math.sqrt(3)+1e-8
            cases+=3
    # Equilateral exact: u and v are unit vectors at angle pi/3.
    u=(1.,0.);v=(.5,math.sqrt(3)/2)
    m=max(norm(u),norm(v),norm(sub(u,v)))
    A=(0.,0.);B=mul(2,u);C=mul(2,v)
    o=center_of_triangle(A,B,C)
    g=mul(1/3,add(add(A,B),C))
    assert norm(sub(o,g))<1e-10
    assert abs(max(norm(sub(o,p)) for p in (A,B,C))/m-2/math.sqrt(3))<1e-10
    cases+=2
    print('PASS',cases,'finite geometric diagnostics; infinite statement follows from proof')
if __name__=='__main__':run()
