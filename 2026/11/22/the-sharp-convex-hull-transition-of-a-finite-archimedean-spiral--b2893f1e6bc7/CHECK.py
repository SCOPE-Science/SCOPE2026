#!/usr/bin/env python3
"""Separate finite numerical tests for the convex hull of the finite Archimedean spiral.
Requires numpy and scipy. The analytical proof is in RESULT.md; tests do not prove all real-parameter claims.
"""
import math
import numpy as np
from scipy.optimize import brentq
from scipy.spatial import ConvexHull

PI=math.pi

def F(t,T):
    ph=T-t
    return T*(math.sin(ph)-t*math.cos(ph))+t*t

def primitive(t):
    return (t*math.hypot(1,t)+math.asinh(t))/2

def geom(T):
    if not (T>0): raise ValueError('T>0 required')
    if T<=PI:
        u=0.0
        return u,T**3/6,primitive(T)+T
    lo=max(0.,T-2*PI)
    # At exactly T=2pi the spurious endpoint t=0 is a zero. Move slightly inside.
    if abs(T-2*PI)<1e-10:lo=1e-7
    elif lo==0.:lo=0.
    u=brentq(lambda t:F(t,T),lo,T-.1,xtol=3e-13)
    phi=T-u
    assert PI<phi<2*PI
    area=(T**3-u**3)/6+T*u*math.sin(u-T)/2
    perimeter=primitive(T)-primitive(u)+math.sqrt((T-u)**2+2*T*u*(1-math.cos(phi)))
    return u,area,perimeter

def check():
    # All six pairwise edges of a sampled curve are not sufficient: compare the
    # actual planar convex hull formed from 30001 support samples instead.
    for T in [0.8,2.0,PI,PI+.1,4.0,5.0,2*PI,8.0,11.0,20.0,30.0]:
        u,A,P=geom(T)
        ts=np.linspace(0,T,30001)
        pts=np.column_stack((ts*np.cos(ts),ts*np.sin(ts)))
        hull=ConvexHull(pts)
        polygon=pts[hull.vertices]
        numerical_A=hull.volume
        numerical_P=np.linalg.norm(polygon-np.roll(polygon,-1,axis=0),axis=1).sum()
        assert abs(A-numerical_A)<max(4e-5,2.5e-7*A),(T,'area',A,numerical_A)
        assert abs(P-numerical_P)<max(5e-5,2.5e-7*P),(T,'perimeter',P,numerical_P)
        if T>PI+1e-8:
            assert abs(F(u,T))<1e-7*max(1,T*T)
            tangent=np.array([math.cos(u)-u*math.sin(u),math.sin(u)+u*math.cos(u)])
            difference=np.array([T*math.cos(T)-u*math.cos(u),T*math.sin(T)-u*math.sin(u)])
            assert abs(np.linalg.det(np.stack((tangent,difference))))<1e-8*max(1,T*T)
            assert np.dot(tangent,difference)<0
        else:
            assert u==0
    for d in [.02,.005,.001]:
        T=PI+d
        u,A,P=geom(T)
        assert abs(u/d-.5)<.025
        assert abs((A-T**3/6)/d**2-PI/8)<.004
        assert abs((P-primitive(T)-T)/d**3+1/12)<.002
    for T in [1000.,10000.]:
        u,A,P=geom(T)
        eps=2*PI-(T-u)
        assert abs(eps*math.sqrt(T)-2*math.sqrt(PI))<.01
        assert abs((A-PI*T*T+2*PI**2*T)/math.sqrt(T)-4*PI**1.5/3)<1.4
        assert abs((P-2*PI*T+2*PI**2)*math.sqrt(T)-8*PI**1.5/3)<.13
    print('ARCHIMEDEAN_SPIRAL_HULL_CHECKS_OK')

if __name__=='__main__':
    check()
