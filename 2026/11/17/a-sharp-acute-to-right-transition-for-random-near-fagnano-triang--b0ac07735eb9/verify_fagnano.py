#!/usr/bin/env python3
"""Reproducible numerical diagnostics for near-minimal side-sampled triangle perimeters.

Requires numpy and scipy. Computations are diagnostics, not an infinite proof.
"""
import math
import numpy as np
from scipy.stats import qmc
from scipy.special import ndtri


def triangle_data(vertices):
    vertices=np.array(vertices,float)
    pairs=((1,2),(2,0),(0,1))
    lengths=np.array([np.linalg.norm(vertices[k]-vertices[j]) for j,k in pairs])
    u=np.array([(vertices[k]-vertices[j])/lengths[i] for i,(j,k) in enumerate(pairs)])
    feet=np.array([vertices[j]+np.dot(vertices[i]-vertices[j],u[i])*u[i] for i,(j,k) in enumerate(pairs)])
    offsets=np.array([np.dot(feet[i]-vertices[j],u[i]) for i,(j,k) in enumerate(pairs)])
    angles=np.arccos(np.clip((np.roll(lengths,1)**2+np.roll(lengths,-1)**2-lengths**2)/(2*np.roll(lengths,1)*np.roll(lengths,-1)),-1,1))
    p0=sum(np.linalg.norm(feet[i]-feet[j]) for i,j in ((0,1),(1,2),(2,0)))
    return lengths,u,feet,offsets,angles,p0


def perimeter(points):
    return (np.linalg.norm(points[...,0,:]-points[...,1,:],axis=-1)
            +np.linalg.norm(points[...,1,:]-points[...,2,:],axis=-1)
            +np.linalg.norm(points[...,2,:]-points[...,0,:],axis=-1))


def hessian_from_geometry(vertices):
    lengths,u,feet,offs,angles,p0=triangle_data(vertices)
    H=np.zeros((3,3))
    for i,j in ((0,1),(1,2),(2,0)):
        e=feet[i]-feet[j]; edge=np.linalg.norm(e); e=e/edge
        proj=np.eye(2)-np.outer(e,e)
        H[i,i]+=u[i]@proj@u[i]/edge
        H[j,j]+=u[j]@proj@u[j]/edge
        cross=-u[i]@proj@u[j]/edge
        H[i,j]+=cross; H[j,i]+=cross
    return H


def sample_for_acute(vertices, t, N=2**18):
    lengths,u,feet,offsets,angles,p0=triangle_data(vertices)
    H=hessian_from_geometry(vertices)
    eig,V=np.linalg.eigh(H)
    Hmi=(V/np.sqrt(eig))@V.T
    W=qmc.Sobol(4,scramble=True,seed=20261109).random_base2(int(math.log2(N)))
    dirs=ndtri(np.clip(W[:,:3],1e-14,1-1e-14))
    dirs/=np.linalg.norm(dirs,axis=1)[:,None]
    radius=1.35*W[:,3]**(1/3)
    z=dirs*radius[:,None]
    shifts=np.sqrt(2*t)*z@Hmi.T
    pts=feet[None,:,:]+shifts[:,:,None]*u[None,:,:]
    inside=np.all((offsets[None,:]+shifts>=0)&(offsets[None,:]+shifts<=lengths[None,:]),axis=1)
    mask=inside & (perimeter(pts)<p0+t)
    pred=4*math.pi*2**1.5/(3*np.prod(lengths)*math.sqrt(np.linalg.det(H)))
    est=pred*(1.35**3)*mask.mean()
    return est,pred


def sample_for_right(t, N=2**19):
    # Right angle at origin, unit legs along coordinate axes.
    a=math.sqrt(2);h=1/math.sqrt(2)
    kappa=h/a
    W=qmc.Sobol(3,scramble=True,seed=20261110).random_base2(int(math.log2(N)))
    U=2.8*(W[:,0]-.5)
    R=1.7*W[:,1]
    Q=3.4*(W[:,2]-.5)
    small=np.maximum(R,1.e-100)
    u=math.sqrt(h*t)*U
    r=math.sqrt(h*t)*R/kappa
    phi=math.pi/4+np.sqrt(2*t/np.maximum(r,1e-100))*Q
    x=r*np.cos(phi);y=r*np.sin(phi)
    X=np.column_stack((.5-u/math.sqrt(2), .5+u/math.sqrt(2)))
    d1=np.hypot(X[:,0],X[:,1]-y)
    d2=np.hypot(X[:,0]-x,X[:,1])
    f=d1+d2+r
    mask=(np.abs(u)<=a/2)&(phi>=0)&(phi<=math.pi/2)&(x>=0)&(x<=1)&(y>=0)&(y<=1)&(f<2*h+t)
    boxvolume=2.8*1.7*3.4
    integral=boxvolume*np.mean(np.sqrt(R)*mask)
    pre=math.sqrt(2)*h**1.25*kappa**(-1.5)/a  # side product = sqrt(2)*1*1
    est=pre*integral
    pred=8*math.pi*math.sqrt(2)/(21*math.sqrt(a)*h**1.25)
    return est,pred,integral


def run():
    cases=[('equilateral',[(0,0),(1,0),(.5,math.sqrt(3)/2)]),
           ('scalene acute',[(0,0),(4,0),(1,3)])]
    for name,v in cases:
        lengths,_,_,_,ang,p0=triangle_data(v)
        assert max(ang)<math.pi/2
        H=hessian_from_geometry(v)
        explicit=4*np.prod(np.sin(ang)**2)/(np.prod(lengths)*np.prod(np.cos(ang)))
        assert np.all(np.linalg.eigvalsh(H)>0)
        assert abs(np.linalg.det(H)-explicit)<1e-9*explicit
        print(name,'det(H)',round(explicit,10),'p0',round(p0,10))
        for t in (0.01,0.002,0.0004):
            est,pred=sample_for_acute(v,t)
            print('  t',t,'empirical_coefficient',round(est,7),'predicted',round(pred,7))
            assert abs(est/pred-1)<0.15
    for t in (0.004,0.001,0.0002):
        est,pred,integral=sample_for_right(t)
        print('right t',t,'empirical_coefficient',round(est,7),'predicted',round(pred,7), 'limit_integral',round(8*math.pi/21,7))
        assert abs(est/pred-1)<0.20
    print('FAGNANO_ACUTE_RIGHT_SMALL_EXCESS_DIAGNOSTIC_OK')

if __name__=='__main__':
    run()
