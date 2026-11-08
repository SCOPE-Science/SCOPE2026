#!/usr/bin/env python3
"""Reproducible checks for central sections of centrally symmetric prisms."""
import math
import numpy as np

def hex_law(h):
    a=math.sqrt(1.0+h*h)
    q=lambda v: math.asin(v/a)
    p4=6/math.pi*(q(1.0)-q(math.sqrt(3)/2))
    p8=6/math.pi*(2*q(0.5)-q(math.sqrt(3)/2))
    return p4, 1-p4-p8, p8

def via_edge_signs(v, h, u):
    # All edges on two congruent bases and all vertical joins.
    p=u[:,:2]@v.T
    z=h*u[:,2,None]
    up=p+z; down=p-z
    return ((up*np.roll(up,-1,axis=1)<0).sum(axis=1)
            +(down*np.roll(down,-1,axis=1)<0).sum(axis=1)
            +(up*down<0).sum(axis=1))

def via_order_statistics(v, h, u):
    m=len(v)//2
    rho=np.linalg.norm(u[:,:2],axis=1)
    w=u[:,:2]/rho[:,None]
    r=np.abs(w @ v[:m].T)
    t=h*np.abs(u[:,2])/rho
    j=(r<t[:,None]).sum(axis=1)
    return np.where(j==m,2*m,4+2*j)

def via_integrated_probabilities(v,h, mesh=180000):
    m=len(v)//2
    angles=2*np.pi*(np.arange(mesh)+0.5)/mesh
    w=np.stack([np.cos(angles),np.sin(angles)],axis=-1)
    r=np.sort(abs(w@v[:m].T),axis=1)
    F=r/np.sqrt(h*h+r*r)
    probs=np.zeros(2*m+3)
    # j=0 -> four sides, ... j=m-1; j=m -> 2m sides.
    before=np.concatenate([np.zeros((mesh,1)),F[:,:-1]],axis=1)
    interval=F-before
    for j in range(m):
        probs[4+2*j]+=interval[:,j].mean()
    probs[2*m]+=(1-F[:,-1]).mean()
    return probs

def main():
    rng=np.random.default_rng(74031)
    N=350000
    normals=rng.normal(size=(N,3)); normals/=np.linalg.norm(normals,axis=1)[:,None]
    for n,v in [
         (6,np.stack([np.cos(np.arange(6)*np.pi/3),np.sin(np.arange(6)*np.pi/3)],axis=1)),
         (8,np.stack([np.cos(np.arange(8)*np.pi/4),np.sin(np.arange(8)*np.pi/4)],axis=1)),
         (6,np.array([[1.,0.],[.65,1.],[-.35,.9],[-1.,0.],[-.65,-1.],[.35,-.9]]))]:
        for h in [0.3,0.5,1.,math.sqrt(5)/2,3.]:
            actual=via_edge_signs(v,h,normals)
            predicted=via_order_statistics(v,h,normals)
            assert np.array_equal(actual,predicted),(n,h,int(np.count_nonzero(actual!=predicted)))
            check=via_integrated_probabilities(v,h,mesh=30000)
            for k in range(4,n+3,2):
                assert abs((actual==k).mean()-check[k])<0.004,(n,h,k,(actual==k).mean(),check[k])
            if n==6 and np.allclose(v[0],[1,0]) and abs(v[1,0]-0.5)<1e-7:
                formula=hex_law(h)
                assert max(abs(check[4]-formula[0]),abs(check[6]-formula[1]),abs(check[8]-formula[2]))<5e-7
                obs= (actual==4).mean(),(actual==6).mean(),(actual==8).mean()
                assert max(abs(obs[i]-formula[i]) for i in range(3))<0.004
                delta=math.pi*formula[0]/6
                inverted=(math.cos(delta)-math.sqrt(3)/2)/math.sin(delta)
                assert abs(inverted-h)<2e-12,(h,inverted)
    hopt=math.sqrt(5)/2
    assert hex_law(hopt)[2]>hex_law(hopt-0.1)[2]
    assert hex_law(hopt)[2]>hex_law(hopt+0.1)[2]
    assert abs(hex_law(hopt)[2]-6/math.pi*(2*math.asin(1/3)-math.asin(1/math.sqrt(3))))<1e-14
    print('PRISM_CENTRAL_SECTION_OK', 'normals_per_test', N, 'configurations',15, 'hex_p_unif',hex_law(0.5), 'oct_max', hex_law(hopt)[2])

if __name__=='__main__':
    main()
