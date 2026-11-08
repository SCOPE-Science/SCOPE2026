#!/usr/bin/env python3
"""Supplementary numerical checks of support functions and angular-grid asymptotics.
Requires numpy and scipy. Numerical samples cannot replace the universal proof.
"""
import math
import numpy as np
from scipy.optimize import minimize_scalar

def vertices(p,n):
    theta=2*math.pi*np.arange(n)/n
    c=np.cos(theta);s=np.sin(theta)
    r=(abs(c)**p+abs(s)**p)**(-1/p)
    return np.stack([r*c,r*s],axis=1)

def dist_support(p,n):
    pts=vertices(p,n)
    edges=np.roll(pts,-1,axis=0)-pts
    normal=np.stack([edges[:,1],-edges[:,0]],axis=1)
    phi=np.unwrap(np.arctan2(normal[:,1],normal[:,0]))
    assert np.all(np.diff(phi)>0)
    phi=np.r_[phi,phi[0]+2*math.pi]
    q=p/(p-1)
    best=0
    for k in range(n):
        lo=phi[k-1] if k else phi[-2]-2*math.pi
        hi=phi[k]
        assert hi>lo
        def deficit(t):
            c=math.cos(t);s=math.sin(t)
            h=(abs(c)**q+abs(s)**q)**(1/q)
            return h-c*pts[k,0]-s*pts[k,1]
        opt=minimize_scalar(lambda x:-deficit(x),bounds=(lo,hi),method='bounded',options={'xatol':1e-12})
        best=max(best,-opt.fun,deficit(lo),deficit(hi))
    return best

def constant(p,divisible):
    return (p-1)*p**(-1-p/(p-1)) if divisible else 1/(p*2**p)

def gap(p,u,t):
    return (1-t)*abs(u)**p+t*abs(u+1)**p-abs(u+t)**p

def main():
    checked=0
    for p in (1.2,1.5,1.8,1.95):
        mid=2**(-p)
        assert abs(gap(p,-.5,.5)-mid)<1e-12
        s=p**(-1/(p-1))
        integer=(p-1)*p**(-p/(p-1))
        assert abs(gap(p,0,s)-integer)<1e-12
        assert mid>integer
        for u in np.linspace(-4,4,81):
            for t in np.linspace(0,1,61):
                assert gap(p,float(u),float(t))<=mid+1e-10
                checked+=1
        for residue in (0,1,2,3):
            ratios=[]
            for k in (16,32,64):
                n=4*k+residue
                d=dist_support(p,n)
                reference=constant(p,residue==0)*(2*math.pi/n)**p
                ratios.append(d/reference)
                checked+=1
            print('p=',p,'n_mod_4=',residue,'n=',[4*k+residue for k in (16,32,64)],'ratios=',[round(x,7) for x in ratios])
            assert all(.5<r<1.01 for r in ratios)
            assert abs(ratios[-1]-1)<abs(ratios[0]-1)+1e-5
    print('SUPERELLIPSE_SUPPORT_CHECK_OK',checked)
if __name__=='__main__':
    main()
