#!/usr/bin/env python3
"""Numerical checks for the local Crofton chord stability theorem."""
import math
import numpy as np

def q(alpha):
    return (1-alpha/math.tan(alpha))/2

def cross2(a,b):
    return a[...,0]*b[...,1]-a[...,1]*b[...,0]

def polygon(vertices):
    p=np.array(vertices,float)
    e=np.roll(p,-1,axis=0)-p
    lengths=np.linalg.norm(e,axis=1)
    if not (np.all(lengths>0) and np.all(cross2(e,np.roll(e,-1,axis=0))>0)):
        raise AssertionError('not CCW strictly convex')
    ext=[]
    for i in range(len(p)):
        v=e[i]/lengths[i]; w=e[(i+1)%len(p)]/lengths[(i+1)%len(p)]
        ext.append(math.atan2(cross2(v,w),np.dot(v,w)))
    return p,float(lengths.sum()),np.array(ext)

def sampled_chord_probability(vertices,threshold,ns=500000,seed=17):
    p,P,alpha=polygon(vertices)
    rng=np.random.default_rng(seed)
    # Rejection sample motion-invariant lines using orientation uniform, p uniform across bounding circle.
    R=np.max(np.linalg.norm(p,axis=1))*1.1
    phi=rng.uniform(0,math.pi,ns)
    offs=rng.uniform(-R,R,ns)
    norm=np.stack([np.cos(phi),np.sin(phi)],axis=1)
    tmins=np.full(ns,np.inf); tmaxs=np.full(ns,-np.inf)
    # intersection line p=dot(normal,x) with sides; distance coordinate v=(-sin phi, cos phi)
    d=np.array([-norm[:,1],norm[:,0]]).T
    for i in range(len(p)):
        a=p[i]; b=p[(i+1)%len(p)]; edge=b-a
        denom=norm@edge
        mask=np.abs(denom)>1.e-12
        t=np.zeros(ns)
        t[mask]=(offs[mask]-norm[mask]@a)/denom[mask]
        mask &= (t>=0)&(t<=1)
        coord=(a[0]+t*edge[0])*d[:,0]+(a[1]+t*edge[1])*d[:,1]
        tmins=np.where(mask,np.minimum(tmins,coord),tmins)
        tmaxs=np.where(mask,np.maximum(tmaxs,coord),tmaxs)
    valid=tmaxs>tmins+1e-12
    short=valid & ((tmaxs-tmins)<threshold)
    # unbiased normalization to lines hitting polygon
    return int(short.sum()),int(valid.sum()),short.sum()/valid.sum(),float((short.sum()/valid.sum())*(1-short.sum()/valid.sum())/valid.sum())**.5

def check():
    shapes={
      'square':[(1,1),(-1,1),(-1,-1),(1,-1)],
      'rectangle':[(2,1),(-2,1),(-2,-1),(2,-1)],
      'equilateral':[(1,0),(-.5,math.sqrt(3)/2),(-.5,-math.sqrt(3)/2)],
      'skew_quad':[(0,0),(4,0),(3,2),(.2,1.5)]}
    for name,v in shapes.items():
        p,P,alpha=polygon(v)
        m=len(v); h=sum(q(a) for a in alpha)
        baseline=m*q(2*math.pi/m)
        var=sum((a-2*math.pi/m)**2 for a in alpha)
        assert abs(sum(alpha)-2*math.pi)<1e-12
        assert h-baseline+1e-13 >= var/6
        t=.025*min(np.linalg.norm(np.roll(p,-1,axis=0)-p,axis=1))
        short,total,observed,se=sampled_chord_probability(v,t,400000,seed=19)
        predicted=t*h/P
        assert abs(observed-predicted)<6*se+0.0003,(name,observed,predicted,se)
        print('CHORD',name,'N',total,'P',round(P,9),'slope',round(h/P,9),'t',round(t,9),'pobs',round(observed,8),'ppred',round(predicted,8),'sd',round(se,8))
    for a in np.linspace(.0001,math.pi-.001,20000):
        qsecond=(math.sin(a)-a*math.cos(a))/math.sin(a)**3
        assert qsecond>=1/3-1e-8
    # local wedge Jacobian independently quadrature-integrate angular factor
    for theta in (.3,.7,math.pi/2,2.4):
        ps=np.linspace(theta-math.pi/2,math.pi/2,200001)
        integral=np.trapezoid(np.cos(ps)*np.cos(theta-ps)/math.sin(theta),ps)
        assert abs(integral-q(math.pi-theta))<1e-8
    for m in (20,40,80,160):
        alpha=np.array([2*math.pi/m+(-1)**i/m**2 for i in range(m)])
        dirs=np.r_[0,np.cumsum(alpha[:-1])]
        edges=np.stack([np.cos(dirs),np.sin(dirs)],axis=1)
        assert np.linalg.norm(edges.sum(axis=0))<1e-11
        verts=np.cumsum(np.vstack([np.zeros(2),edges]),axis=0)[:-1]
        polygon(verts)
        ratio=(sum(q(a) for a in alpha)-m*q(2*math.pi/m))/sum((alpha-2*math.pi/m)**2)
        assert .1666666 < ratio < .18,(m,ratio)
        print('SHARPNESS',m,format(ratio,'.12f'))
    print('CROFTON_STABILITY_OK shapes=4 curvature_tests=20000 wedge_integrals=4 sharpness_shapes=4')
if __name__=='__main__':check()
