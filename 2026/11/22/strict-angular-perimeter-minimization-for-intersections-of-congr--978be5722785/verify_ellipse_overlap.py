"""Numerical checks of exact ellipse-intersection perimeter law."""
import math
import numpy as np
from scipy.integrate import quad

def radial_speed(a,b,x):
    aa,bb=a*a,b*b
    t=math.sin(x)**2
    return math.sqrt(aa*bb*(bb*bb+(aa*aa-bb*bb)*t)/(bb+(aa-bb)*t)**3)

def exact_p(a,b,theta):
    return 4*quad(lambda x:radial_speed(a,b,x),theta/2,theta/2+math.pi/2,epsabs=1e-11)[0]

def direct_p(a,b,theta):
    # Arc length from full boundary, allocating pieces to smaller of two radial functions.
    # Break the polar-angle integral at every boundary-crossing ray.
    def one(x,rot):
        aa,bb=a*a,b*b
        y=x-rot
        return 1/math.sqrt((math.cos(y)**2)/aa+(math.sin(y)**2)/bb)
    def f(x):
        if one(x,0)<one(x,theta):return radial_speed(a,b,x)
        return radial_speed(a,b,x-theta)
    # ensure quadrature boundaries at crossing angles
    pts=sorted([0,theta/2,theta/2+math.pi/2,theta/2+math.pi,theta/2+3*math.pi/2,2*math.pi])
    return sum(quad(f,l,r,epsabs=1e-10)[0] for l,r in zip(pts[:-1],pts[1:]))

def qsharp(a,b):
    A,B=a*a,b*b
    return 4*a*b*(A-B)*(A*A-A*B+B*B)/((A+B)**2.5*math.sqrt(A*A+B*B))

def derivative(a,b,theta):
    return 2*(radial_speed(a,b,math.pi/2+theta/2)-radial_speed(a,b,theta/2))

def run():
    count=0
    for a,b in [(1.2,1),(2,1),(5,1),(100,1),(10,0.02)]:
        prev=math.inf
        for theta in np.linspace(0,math.pi/2,41):
            p=exact_p(a,b,theta)
            assert p<=prev+1e-9*max(1,a)
            prev=p
            assert abs(p-direct_p(a,b,theta))<1e-8*max(1,a)
            count+=2
            if 0<theta<math.pi/2:
                assert derivative(a,b,theta)<0
                count+=1
        for eta in [0.01,0.003,0.001]:
            diff=exact_p(a,b,math.pi/2-eta)-exact_p(a,b,math.pi/2)
            assert abs(diff/(eta*eta*qsharp(a,b))-1)<0.06
            count+=1
        assert abs(derivative(a,b,0)-2*(b-a))<1e-8*max(1,a)
        count+=1
        if a/b<=5:
            d=(exact_p(a,b,1e-5)-exact_p(a,b,0))/1e-5
            assert abs(d-2*(b-a))<0.001*max(1,a)
            count+=1
    assert abs(exact_p(1,1,0)-2*math.pi)<1e-10
    count+=1
    print('ELLIPSE_OVERLAP_CHECKS_OK',count)
if __name__=='__main__':run()
