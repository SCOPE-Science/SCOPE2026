#!/usr/bin/env python3
"""Reproducibility checks for the asymmetric triangular bipyramid invisibility law.
Only standard library is required; sampling and geometry are independent of the
spherical-Gauss-Bonnet calculation in the accompanying proof.
"""
import math
import random

pi=math.pi

def exact(a,b):
    alpha, beta=1/(2*a),1/(2*b)
    if alpha >= 2*beta:
        c=(beta*beta-0.5)/(1+beta*beta)
        return 1-3/(2*pi)*math.acos(c), 'triangle-B'
    if beta >= 2*alpha:
        c=(alpha*alpha-0.5)/(1+alpha*alpha)
        return 1-3/(2*pi)*math.acos(c), 'triangle--B'
    c=(.5+alpha*beta)/math.sqrt((1+alpha*alpha)*(1+beta*beta))
    return 1-3/pi*math.acos(c),'hexagon'

def cross(p,q,r):
    return (q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0])

def in_triangle(p,A,B,C):
    s0,s1,s2=cross(A,B,p),cross(B,C,p),cross(C,A,p)
    return (s0>0 and s1>0 and s2>0) or (s0<0 and s1<0 and s2<0)

def independent_sim(a,b,N,seed):
    rng=random.Random(seed)
    vv=[(math.cos(k*2*pi/3),math.sin(k*2*pi/3),0.) for k in range(3)] + [(0.,0.,a),(0.,0.,-b)]
    total=0
    for _ in range(N):
        z=2*rng.random()-1
        t=2*pi*rng.random()
        rho=math.sqrt(1-z*z)
        dx,dy,dz=rho*math.cos(t),rho*math.sin(t),z
        # Plane frame; choosing e1 horizontal makes it possible to project without 3D hull routines.
        if rho>1e-12:
            e1=(-dy/rho,dx/rho,0.)
            e2=(-dz*dx/rho,-dz*dy/rho,rho)
        else:
            e1=(1.,0.,0.)
            e2=(0.,1.,0.)
        projected=[(sum(p[i]*e1[i] for i in range(3)),sum(p[i]*e2[i] for i in range(3))) for p in vv]
        if in_triangle(projected[3],*projected[:3]) and in_triangle(projected[4],*projected[:3]):
            total+=1
    return total/N

def angular_quadrature(a,b,steps=120000):
    # Direct radial integration of the spherical area density over the feasible slope polygon.
    alpha,beta=1/(2*a),1/(2*b)
    value=0.0
    for k in range(steps):
        theta=2*pi*(k+0.5)/steps
        dx,dy=math.cos(theta),math.sin(theta)
        rho=float('inf')
        for j in range(3):
            n=(math.cos((2*j+1)*pi/3),math.sin((2*j+1)*pi/3))
            dot=n[0]*dx+n[1]*dy
            if dot>0:rho=min(rho,beta/dot)
            elif dot<0:rho=min(rho,alpha/(-dot))
        value+=1-1/math.sqrt(1+rho*rho)
    return value/steps

if __name__=='__main__':
    cases=[(.25,.25),(.5,.9),(.5,1),(.5,1.5),(.2,1.8),(1.4,.3),(2.5,2.5)]
    N=180000
    for k,(a,b) in enumerate(cases):
        p,kind=exact(a,b)
        q=independent_sim(a,b,N,11933+k)
        se=math.sqrt(max(1e-8,p*(1-p))/N)
        z=abs(q-p)/se
        print(f'{a:.4g} {b:.4g} {kind:12s} exact={p:.10f} sampled={q:.10f} z={z:.3f}')
        if z>4.5:raise AssertionError((a,b,z))
    for a,b in [(.5,.9),(.5,1),(.2,1.8),(1.4,.3),(2.5,2.5)]:
        analytic=exact(a,b)[0]
        quadrature=angular_quadrature(a,b)
        print('quadrature',a,b,analytic,quadrature)
        assert abs(analytic-quadrature)<2e-8
    # deterministic positivity and fixed-total balancing check across all phase domains
    for total in (.5,1.,2.,3.,7.,15.):
        opt=exact(total/2,total/2)[0]
        for k in range(1,500):
            a=total*k/1000; b=total-a
            if not (exact(a,b)[0] < opt):raise AssertionError(('unique optimum',total,k))
    print('ASYMMETRIC_BIPYRAMID_BOTH_APICES_HIDDEN_OK', N*len(cases))
