#!/usr/bin/env python3
"""Standalone independent geometry and moment checks for rotational polygon intersections.

Run: python3 check_geometry.py
Uses only the Python standard library. All tolerances concern finite numerical checks.
"""
import math
from itertools import product

PI = math.pi

def clipping(poly, nx, ny, cap=1.0):
    result=[]
    for i,p in enumerate(poly):
        q=poly[(i+1)%len(poly)]
        h0=cap-nx*p[0]-ny*p[1]
        h1=cap-nx*q[0]-ny*q[1]
        inp=h0>=-1e-12
        inq=h1>=-1e-12
        if inp: result.append(p)
        if inp != inq:
            t=h0/(h0-h1)
            result.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
    return result

def polygon_by_clipping(n, gaps):
    # Deliberately independent of the tangent-sector area derivation.
    poly=[(-3.,-3.),(3.,-3.),(3.,3.),(-3.,3.)]
    angles=[0.0]
    for g in gaps[:-1]:angles.append(angles[-1]+g)
    for j in range(n):
        for a in angles:
            th=2*PI*j/n+a
            poly=clipping(poly,math.cos(th),math.sin(th))
    return poly

def polygon_moments(poly):
    c=mx=my=xx=xy=yy=0.0
    for i,(x,y) in enumerate(poly):
        u,v=poly[(i+1)%len(poly)]
        z=x*v-u*y
        c+=z
        mx+=(x+u)*z
        my+=(y+v)*z
        xx+=(x*x+x*u+u*u)*z
        yy+=(y*y+y*v+v*v)*z
        xy+=(2*x*y+x*v+u*y+2*u*v)*z
    a=c/2
    cx=mx/(6*a)
    cy=my/(6*a)
    exx=xx/(12*a)-cx*cx
    eyy=yy/(12*a)-cy*cy
    exy=xy/(24*a)-cx*cy
    return a, exx+eyy, (exx*eyy-exy**2)/a**2, (cx,cy)

def formula(n,gaps):
    u=[math.tan(g/2) for g in gaps]
    s=sum(u);t=sum(a*a*a for a in u)
    area=n*s
    polar=n*(s+t/3)/2
    isop=(3*s+t)**2/(144*n*n*s**4)
    return area, polar, isop

def specialized(n,theta):
    alpha=PI/n
    u=math.tan(theta/2)+math.tan(alpha-theta/2)
    return (1/math.tan(alpha)+u/3)**2/(16*n*n)

def run():
    checks=0
    for n in (3,4,5,7,9,16):
        alpha=2*PI/n
        for k in (2,3,4):
            for s in range(11):
                weights=[(j+1)*(1+((s*j+3*j+2*s)%7)/13) for j in range(k)]
                gaps=[alpha*w/sum(weights) for w in weights]
                poly=polygon_by_clipping(n,gaps)
                area,J_over_area,iso,center=polygon_moments(poly)
                Af,Jf,Lf=formula(n,gaps)
                assert abs(area-Af)<2e-9*(1+Af), (n,k,s,'area',area,Af)
                checks+=1
                assert abs(J_over_area-Jf/area)<2e-9*(1+J_over_area), (n,k,s,'inertia')
                checks+=1
                assert abs(iso-Lf)<2e-9*(1+Lf), (n,k,s,'isotropic')
                checks+=1
                assert math.hypot(*center)<1e-8, (n,k,s,'center')
                checks+=1
                assert abs(J_over_area**2/4/area**2-Lf)<2e-9
                checks+=1
        for s in range(11):
            theta=(PI/n)*s/10
            gaps=[theta,alpha-theta]
            L0=formula(n,gaps)[2]
            L1=specialized(n,theta)
            assert abs(L0-L1)<1e-12
            checks+=1
            if s>0:
                prev=specialized(n,(PI/n)*(s-1)/10)
                assert L1<prev
                checks+=1
        eps=.01
        ga=[alpha-2*eps,1.5*eps,.5*eps]
        gb=[alpha-2*eps,eps,eps]
        assert sorted(ga,reverse=True)[0]==sorted(gb,reverse=True)[0]
        assert formula(n,ga)[2]<formula(n,gb)[2]
        checks+=1
        # Test predicted universal cubic leading coefficient.
        T=math.tan(alpha/2); f0=(T*T+3)/(3*T)
        for eps in (.008,.005,.003):
            a=formula(n,[alpha-2*eps,1.5*eps,.5*eps])[2]
            b=formula(n,[alpha-2*eps,eps,eps])[2]
            coeff=(a-b)/eps**3
            pred=-f0/(192*n*n)
            assert abs(coeff/pred-1)<.30, (n,eps,coeff,pred)
            checks+=1
    print('PASS',checks,'independent numerical geometry and algebraic-profile checks')
if __name__=='__main__':run()
