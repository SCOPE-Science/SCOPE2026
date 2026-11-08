#!/usr/bin/env python3
"""Independent numerical checks for spherical small-circle acute triangles."""
import math
import numpy as np
from scipy.integrate import quad

def exact_p(lam):
    if lam<=1/3: return 0.0
    if lam>=1: return 0.25
    K=(1+lam)/(1-lam)
    q0=2*math.asin(math.sqrt((3-K)/4)) if K<3 else 0.
    q1=2*math.asin(1/K)
    D=lambda x:(math.pi-3*x)/2
    base=(math.pi/2)*(math.pi/3-q0) - .75*((math.pi/3)**2-q0*q0)
    integ=quad(lambda x: math.acos(min(1,max(-1,K*math.sin(x/2)))),q0,q1,epsabs=3e-13)[0]
    return 3/math.pi**2*(base-integ)

def check(n=300_000):
    rng=np.random.default_rng(271828)
    ph=np.sort(rng.uniform(0,2*math.pi,size=(n,3)),axis=1)
    gaps=np.column_stack((ph[:,1]-ph[:,0],ph[:,2]-ph[:,1],2*math.pi-ph[:,2]+ph[:,0]))
    for lam in [.25,1/3,0.34,.36,.4,.5,.6,.8,.95]:
        # direct projected tangent cos signs, without using derived half-angle test
        c=math.sqrt(lam)
        s=math.sqrt(1-lam)
        xyz=np.stack([s*np.cos(ph),s*np.sin(ph),np.full_like(ph,c)],axis=-1)
        acute=np.ones(n,dtype=bool)
        for j in range(3):
            x=xyz[:,j,:]; y=xyz[:,(j+1)%3,:]; z=xyz[:,(j+2)%3,:]
            xy=np.einsum('ij,ij->i',x,y);xz=np.einsum('ij,ij->i',x,z);yz=np.einsum('ij,ij->i',y,z)
            acute &= (yz-xy*xz)>1e-13
        p=exact_p(lam)
        obs=acute.mean()
        bound=6*math.sqrt(max(p*(1-p),1e-8)/n)
        assert abs(obs-p)<bound+0.001,(lam,p,obs)
        print(f'lambda={lam:.5f} exact={p:.9f} sampled={obs:.9f} error={obs-p:+.6f}')
    for d in [0.002,.003,.005,.01,.02]:
        p=exact_p(1/3+d)
        print('onset',d,p/d**2,'limit',243/(16*math.pi**2))
    assert abs(exact_p(0.99999)-.25)<0.002
    print('LATITUDE_ACUTE_CHECK_OK')
if __name__=='__main__':check()
