#!/usr/bin/env python3
"""Reproducible numerical tests for the typical spherical-facet height crossover."""
import math
import numpy as np
from scipy.special import betainc, ndtr, ndtri, log_ndtr
from scipy.optimize import brentq
from scipy.integrate import simpson
from scipy.stats import norm

def mills(x): return math.exp(-x*x/2)/(math.sqrt(2*math.pi)*ndtr(x))
def saddle(rho):
    if rho == 0: return 0.
    return brentq(lambda x: x-rho*mills(x),0.,max(4.,rho+1))
def predicted(rho):
    u=saddle(rho); l=mills(u)
    return u,1/(1+rho*l*(u+l))
def sphere_cdf(h,d):
    h=np.asarray(h)
    return 0.5 + 0.5*np.sign(h)*betainc(.5,(d-1)/2,h*h)
def loglaw_y(y,d,m,u):
    x=u+y/math.sqrt(d)
    h=x/math.sqrt(d)
    if np.any(np.abs(h)>=1): raise ValueError('h exceeds support')
    F=sphere_cdf(h,d)
    return ((d*d-2*d-1)/2)*np.log1p(-h*h)+m*np.log(F)
def test(d,m):
    rho=m/d; u,v=predicted(rho)
    y=np.linspace(-11,11,22001)
    logp=loglaw_y(y,d,m,u)
    w=np.exp(logp-np.max(logp)); w/=simpson(w,x=y)
    mean=simpson(y*w,x=y); var=simpson((y-mean)**2*w,x=y)
    cdf=np.cumsum((w[:-1]+w[1:])*np.diff(y)/2)
    normcdf=norm.cdf(y[1:],scale=math.sqrt(v))
    kolm=np.max(np.abs(cdf-normcdf))
    assert abs(var-v)<.55, (d,m,var,v)
    assert kolm<.35,(d,m,kolm)
    print(f'd={d:4d} m={m:4d} rho={rho:5.3f} root={u: .5f} asympt-var={v:.5f} numeric-mean={mean:.5f} numeric-var={var:.5f} KS={kolm:.5f}')
    return (mean,var,kolm)

def check_curvature(d,m):
    from scipy.special import beta
    xs=np.linspace(-min(2*math.sqrt(d),d/2),min(2*math.sqrt(d),d/2),1001)
    def f(ys):
        h=ys/d
        return ((d*d-2*d-1)/2)*np.log1p(-h*h)+m*np.log(sphere_cdf(h,d))
    eps=.002
    second=(f(xs+eps)-2*f(xs)+f(xs-eps))/eps**2
    kappa=1-2/d-1/d**2
    assert np.max(second) <= -kappa+1e-5,(np.max(second),-kappa)

if __name__=='__main__':
    for d,m in [(30,1),(100,2),(200,16),(300,120),(400,400),(500,1000),(600,1800)]:
        test(d,m)
    for d,m in [(5,1),(5,10),(10,1),(10,10),(20,30),(100,200)]:
        check_curvature(d,m)
    print('FACET_HEIGHT_CROSSOVER_CHECKS_PASSED')

def monte_carlo_facet(d,m,reps=4000):
    """Independent construction of facets from random sphere points."""
    from scipy.integrate import quad
    rng=np.random.default_rng(17072017+d*101+m)
    hs=[]
    for _ in range(reps):
        x=rng.normal(size=(d+m,d))
        x/=np.linalg.norm(x,axis=1)[:,None]
        _,_,vt=np.linalg.svd(x[1:d]-x[0],full_matrices=True)
        u=vt[-1]
        z=(x[d:]-x[0])@u
        if np.all(z>0): hs.append(-float(x[0]@u))
        elif np.all(z<0): hs.append(float(x[0]@u))
    hs=np.array(hs)
    def f(h):return (1-h*h)**((d*d-2*d-1)/2)*float(sphere_cdf(np.asarray(h),d))**m
    den=quad(f,-1,1,epsabs=1e-10)[0]
    theory=quad(lambda h:h*f(h),-1,1,epsabs=1e-10)[0]/den
    empir=float(np.mean(hs)); se=float(np.std(hs)/np.sqrt(len(hs)))
    print(f'MC d={d} m={m}: facets={len(hs)}/{reps}; mean={empir:.6f}; exact={theory:.6f}; se={se:.6f}')
    assert len(hs)>200
    assert abs(empir-theory)<5*se+.015

if __name__=='__main__':
    for d,m in [(3,1),(3,4),(5,2),(6,3)]:
        monte_carlo_facet(d,m,2500)
    print('GEOMETRIC_FACET_CONSTRUCTION_PASSED')

def compare_gaussian_height(d,m):
    rho=m/d; u,_=predicted(rho)
    y=np.linspace(-10,10,16001); x=u+y/math.sqrt(d)
    lp_s=loglaw_y(y,d,m,u)
    lp_g=-d*x*x/2+m*log_ndtr(x)
    ps=np.exp(lp_s-np.max(lp_s)); ps/=simpson(ps,x=y)
    pg=np.exp(lp_g-np.max(lp_g)); pg/=simpson(pg,x=y)
    tv=.5*simpson(np.abs(ps-pg),x=y)
    print(f'Sphere vs Gaussian total variation: d={d} m={m} TV={tv:.6f}')
    assert tv<.25
    return tv

if __name__=='__main__':
    for d,m in [(100,3),(200,50),(300,300),(500,1000)]:
        compare_gaussian_height(d,m)
    mu=math.sqrt(2/math.pi)
    d=3000000; m=round(d**.75)
    shift=math.sqrt(d)*saddle(m/d)-mu*m/math.sqrt(d)
    assert abs(shift+mu**3)<.015
    print(f'First nonlinear-centering critical offset: observed={shift:.8f}, limit={-mu**3:.8f}')
    print('ALL_HEIGHT_UNIVERSALITY_CHECKS_PASSED')
