#!/usr/bin/env python3
"""Numerical diagnostic for a rare-small-area marked limit in side-sampled triangles.

Requires NumPy and mpmath. This is a finite diagnostic, not a proof of an asymptotic theorem.
"""
import math
import numpy as np
import mpmath as mp

def area(x,y,z):
    return x*y*z+(1-x)*(1-y)*(1-z)

def cdf_prior(t):
    t=mp.mpf(str(t))
    if t<=0: return mp.mpf('0')
    if t>=1: return mp.mpf('1')
    if t<mp.mpf('0.25'):
        return t-(3*t-mp.mpf('0.5'))*mp.log(t)+(1-4*t)**mp.mpf('1.5')*mp.atanh(mp.sqrt(1-4*t))
    raise ValueError('This diagnostic only uses t<1/4.')

def main():
    mp.mp.dps=110
    rng=np.random.default_rng(210912)
    # Full-cube, unconditioned check against a published exact CDF.
    xyz=rng.random((900000,3))
    q=area(xyz[:,0],xyz[:,1],xyz[:,2])
    assert abs(np.mean(q)-.25)<.001
    for t in (.05,.1,.2):
        empirical=float(np.mean(q<t)); exact=float(cdf_prior(t))
        assert abs(empirical-exact)<.0025,(t,empirical,exact)
    print('CUBE_GEOMETRY_OK', '900000 samples', 'mean',round(float(q.mean()),7))
    for t in (mp.mpf('1e-4'),mp.mpf('1e-8'),mp.mpf('1e-15')):
        actual=cdf_prior(t)
        asym=3*t*t*mp.log(1/t)+mp.mpf('4.5')*t*t
        assert abs(actual/asym-1)<mp.mpf('.002')
    print('PRIOR_CDF_ASYMPTOTIC_OK', 'three scales')
    # Change of variables at one of the six small-area corners:
    # p=xy=t*a, x=p**u, y=p**(1-u), w=t*b.
    # dxdydw = t^2*[-log(t*a)] da db du.
    # Integrate on a,b in (0,2), u in (0,1) using importance sampling.
    n=1100000
    u=rng.random(n)
    a=2*rng.random(n)
    b=2*rng.random(n)
    for t in (1e-7,1e-18,1e-70):
        p=t*a
        x=np.exp(u*np.log(p)); y=np.exp((1-u)*np.log(p)); w=t*b
        sscaled=a+b*(1-x-y)
        indicator=(sscaled<1)&(x<.20)&(y<.20)&(w<.20)
        wt=(1-np.log(a)/math.log(1/t))*indicator
        coef=4*float(np.mean(wt))
        assert .20<coef<.53,(t,coef)
        mu=float(np.sum(wt*u)/np.sum(wt))
        ma=float(np.sum(wt*a)/np.sum(wt))
        mb=float(np.sum(wt*b)/np.sum(wt))
        print('CORNER_IMPORTANCE',f't={t:.0e}',f'coefficient={coef:.5f}',f'E[log_split]={mu:.5f}',f'E[product_fraction]={ma:.5f}',f'E[linear_fraction]={mb:.5f}')
        if t<1e-50:
            assert abs(coef-.5)<.045
            assert abs(mu-.5)<.02
            assert abs(ma-1/3)<.03 and abs(mb-1/3)<.03
    print('MARKED_SMALL_AREA_SIX_CORNERS_DIAGNOSTIC_OK')
if __name__=='__main__':main()
