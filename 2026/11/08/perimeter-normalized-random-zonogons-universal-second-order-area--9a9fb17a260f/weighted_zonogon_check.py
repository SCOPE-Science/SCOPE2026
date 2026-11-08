"""Numerical consistency tests for perimeter-normalized random zonogons.

All infinite-dimensional claims are proved analytically in RESULT.md; these
finite computations check geometry, normalization, moments and transform limits.
Requires numpy/scipy; run: python weighted_zonogon_check.py
"""
import math
import numpy as np
from scipy.spatial import ConvexHull

rng=np.random.default_rng(1729)

def geom(theta, w):
    theta=np.asarray(theta); w=np.asarray(w)
    return sum(w[i]*w[j]*abs(math.sin(theta[j]-theta[i]))
               for i in range(len(w)) for j in range(i+1,len(w)))

def hull(theta,w):
    v=np.column_stack((w*np.cos(theta),w*np.sin(theta)))
    vv=np.array([v[[i for i in range(len(w)) if (k>>i)&1]].sum(axis=0)
                 for k in range(1<<len(w))])
    h=ConvexHull(vv)
    return h.volume,h.area

def fft_def(theta,w,m=12000):
    ks=np.arange(1,m+1)
    z=(np.exp(2j*ks[:,None]*np.asarray(theta)[None,:])*np.asarray(w)[None,:]).sum(axis=1)
    return 2*len(w)/math.pi*np.sum(np.abs(z)**2/(4*ks**2-1))

def transform(s,rho=1,c=None,cut=15000):
    k=np.arange(1,cut+1,dtype=float)
    t=(2*s/math.pi)/(4*k*k-1)
    if c is None:
        return math.exp(-np.log1p(rho*t).sum())
    return math.exp((-np.log1p(t)-c*c*t/(1+t)).sum())

for n in (3,5,7):
    for _ in range(8):
        theta=rng.uniform(0,math.pi,n)
        lens=rng.uniform(.2,2.3,n);w=lens/lens.sum()
        a=geom(theta,w)
        ah,p=hull(theta,w)
        assert abs(a-ah)<2e-12 and abs(p-2)<2e-12
        deficit=n*(1/math.pi-a)
        approx=fft_def(theta,w)
        assert deficit>=-1e-12 and abs(deficit-approx)<.004, (deficit,approx)

def samples(n,how,N=15000,chunk=1500,c=1.):
    out=[]
    for off in range(0,N,chunk):
        b=min(chunk,N-off)
        angles=rng.uniform(0,math.pi,(b,n))
        if how=='equal': L=np.ones((b,n))
        elif how=='binary': L=rng.choice([1.,3.],size=(b,n))
        elif how=='spike':
            L=np.ones((b,n))*(1-c/math.sqrt(n))/(n-1)
            L[:,0]=c/math.sqrt(n)
        idx=np.argsort(angles,axis=1)
        th=np.take_along_axis(angles,idx,axis=1)
        w=np.take_along_axis(L/np.sum(L,axis=1)[:,None],idx,axis=1)
        wc=w*np.cos(th); ws=w*np.sin(th)
        area=np.sum(ws*(np.cumsum(wc,axis=1)-wc)-wc*(np.cumsum(ws,axis=1)-ws),axis=1)
        out.append(n*(1/math.pi-area))
    return np.concatenate(out)

for how, rho in [('equal',1.),('binary',1.25),('spike',2.)]:
    n=240
    arr=samples(n,how)
    print(how,'n',n,'observed mean',arr.mean(),'target',rho/math.pi,'observed var',arr.var())
    finite_rho=(n*((1/math.sqrt(n))**2+(n-1)*((1-1/math.sqrt(n))/(n-1))**2)) if how=='spike' else rho
    assert abs(arr.mean()-finite_rho/math.pi)<.032
    for s in (.5,1.5):
        empirical=np.exp(-s*arr).mean()
        theory=transform(s,rho) if how!='spike' else transform(s,c=1.)
        print('laplace',how,s,empirical,theory)
        assert abs(empirical-theory)<.03

s=1.5
assert abs(transform(s,2.)-transform(s,c=1.))>.002
print('ALL_WEIGHTED_ZONOGON_GEOMETRY_AND_TRANSFORM_CHECKS_PASSED')
