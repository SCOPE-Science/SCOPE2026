#!/usr/bin/env python3
"""Standalone reproducible checks for section-area cusp of a prolate spheroid.
Only NumPy and SciPy are required. All random trials use a fixed seed.
"""
import math
import numpy as np
from scipy.integrate import quad

rng = np.random.default_rng(20261107)

def H(r):
    k = math.sqrt(r*r-1)
    return 0.5*(r+math.asinh(k)/k)

def surv(x, r):
    h=lambda s: math.sqrt(1+(r*r-1)*s*s)
    return quad(lambda s: h(s)*math.sqrt(max(0.0,1-x*h(s)/r)),0,
                1 if x<=1 else math.sqrt(((r/x)**2-1)/(r*r-1)),
                epsabs=1e-11,epsrel=1e-11)[0]/H(r)

def pdf(x,r):
    k=math.sqrt(r*r-1)
    end=min(r,r/x)
    if end<=1: return math.pi/(2*math.sqrt(2)*r*H(r)*k)
    # h=1+(end-1)sin^2(theta) kills both integrable endpoints.
    delta=end-1
    def fn(z):
        h=1+delta*math.sin(z)**2
        dh=2*delta*math.sin(z)*math.cos(z)
        if z==0 or z==math.pi/2: return 0
        return dh*h**3/(math.sqrt(h*h-1)*math.sqrt(1-x*h/r))
    return quad(fn,0,math.pi/2,epsabs=1e-10,epsrel=1e-10,limit=200)[0]/(2*r*H(r)*k)

def sample_x(r,n):
    # Rejection from isotropic plane orientation: conditional hitting weights normal by width.
    raw=[]
    while sum(len(a) for a in raw)<n:
        m=max(5000,n//3)
        z=rng.random(m)
        keep=rng.random(m)<np.sqrt(1+(r*r-1)*z*z)/r
        raw.append(z[keep])
    z=np.concatenate(raw)[:n]
    v=rng.uniform(-1,1,n)
    h=np.sqrt(1+(r*r-1)*z*z)
    # Independent direct matrix-sectional calculation for random normal azimuth.
    phi=rng.uniform(0,2*np.pi,n)
    normal=np.array([np.sqrt(1-z*z)*np.cos(phi),np.sqrt(1-z*z)*np.sin(phi),z]).T
    e1=np.array([-np.sin(phi),np.cos(phi),np.zeros(n)]).T
    e2=np.cross(normal,e1)
    D=np.array([1.,1.,1./(r*r)])
    a=np.sum(e1*e1*D,axis=1)
    b=np.sum(e2*e2*D,axis=1)
    c=np.sum(e1*e2*D,axis=1)
    # restricted inverse metric; slice reduced radius squared 1-v^2
    x=(1-v*v)/np.sqrt(a*b-c*c)
    assert np.max(np.abs(x-r*(1-v*v)/h))<2e-10
    return x

def check():
    for r in (1.3,2.0,4.0):
        n=130000
        x=sample_x(r,n)
        assert abs(x.mean()-2*r/(3*H(r)))<0.028, (r,x.mean())
        for q in (0.25,0.6,1.,(1+r)/2,0.9*r):
            emp=np.mean(x>q)
            target=surv(q,r)
            assert abs(emp-target)<0.013,(r,q,emp,target)
        assert 0<=x.min()<x.max()<r
        # density derived by independent finite difference of exact survival
        for q in (0.4,0.8,(1+r)/2):
            delta=1e-5
            fd=(surv(q-delta,r)-surv(q+delta,r))/(2*delta)
            assert abs(fd-pdf(q,r))<1e-5,(r,q,fd,pdf(q,r))
        cusp=r**3/(H(r)*(r*r-1))
        f1=pdf(1,r)
        errs=[]
        for e in (0.005,0.00125,0.0003125):
            observed=(f1-pdf(1-e,r))/math.sqrt(e)
            errs.append(abs(observed-cusp))
        assert errs[2]<errs[1]<errs[0],(r,errs)
        assert errs[2]/cusp<0.07,(r,cusp,errs)
        # Right continuity and finite one-sided slope.
        assert abs(pdf(1+0.0001,r)-f1)<0.05
        print('r=',r,'mean=',round(x.mean(),7),'target=',round(2*r/(3*H(r)),7),
              'cusp_coefficient=',round(cusp,8),'cusp_errors=',[round(v,5) for v in errs])
    print('PROLATE_CROFTON_SECTION_AREA_CUSP_OK')

if __name__=='__main__':check()
