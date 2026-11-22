"""Numerical diagnostics for centered-line intercepts of circular toroidal tubes.
Run: python check.py. These are diagnostics, not a substitute for the proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import betainc, erf

def exact(d, ratio, y):
    p = betainc(.5, (d-1)/2, ratio**2)
    q = math.sqrt(max(0., 1-y*y))
    psmall = betainc(.5, (d-1)/2, (ratio*q)**2)
    return p, 1-psmall/p

def moment2(d, ratio):
    k=(d-3)/2
    den=quad(lambda u:(1-ratio**2*u*u)**k,0,1,epsabs=1e-13)[0]
    num=quad(lambda u:(1-u*u)*(1-ratio**2*u*u)**k,0,1,epsabs=1e-13)[0]
    return num/den

count=0
rng=np.random.default_rng(7321)
for d in (3,4,6,9):
    for ratio in (.19,.45,.81):
        r=1.2; R=r/ratio
        z=rng.normal(size=(1500,d))
        z/=np.linalg.norm(z,axis=1)[:,None]
        mu=np.abs(z[:,-1]); s=np.sqrt(1-mu*mu)
        hit=mu<=ratio
        delta=r*r-R*R*mu[hit]**2
        plus=R*s[hit]+np.sqrt(delta)
        minus=R*s[hit]-np.sqrt(delta)
        assert np.all(minus>0)
        assert np.max(np.abs((plus-minus)*2-4*np.sqrt(delta)))<3e-13
        for row,a,b in zip(z[hit][:20],minus[:20],plus[:20]):
            for t in (a+(b-a)*.25, a+(b-a)*.8):
                point=t*row
                cross=np.linalg.norm(point[:-1]); height=point[-1]
                assert (cross-R)**2+height**2<=r*r+2e-13
            for t in (a*.8,b+(b-a)*.1):
                point=t*row
                assert (np.linalg.norm(point[:-1])-R)**2+point[-1]**2>=r*r-1e-12
            count+=4
        phit=betainc(.5,(d-1)/2,ratio**2)
        assert abs(np.mean(hit)-phit)<.04
        p,F=exact(d,ratio,.6)
        assert abs(p-phit)<1e-14
        if d==3:
            assert abs(phit-ratio)<1e-13
            assert abs(F-(1-math.sqrt(1-.6**2)))<1e-13
        count+=4
for d in (4,5,7,15):
    pts=[moment2(d,t) for t in (.001,.2,.4,.6,.8,.9999)]
    assert all(b>a for a,b in zip(pts,pts[1:]))
    assert abs(pts[0]-2/3)<1e-6
    assert abs(pts[-1]-(d-1)/d)<.001
    count+=8
for ratio in (.05,.25,.5,.97):
    for y in (.1,.3,.9):
        assert abs(exact(3,ratio,y)[1]-(1-math.sqrt(1-y*y)))<1e-13
        count+=1
for d in (300,1000):
    for kappa in (.6,1.3,2.2):
        t=kappa/math.sqrt(d)
        p,_=exact(d,t,.5)
        assert abs(p-erf(kappa/math.sqrt(2)))<.015
        for y in (.15,.4,.75):
            _,F=exact(d,t,y)
            g=1-erf(kappa*math.sqrt(1-y*y)/math.sqrt(2))/erf(kappa/math.sqrt(2))
            assert abs(F-g)<.016,(d,kappa,y,F,g)
            count+=1
assert abs(moment2(3,.8)-2/3)<1e-12
print('All tests passed. Assertion groups:',count)
print('conditional squared-length moments d=3 (any ratio):',moment2(3,.6))
print('d=5 conditional moments, ratios 0.2, 0.5, 0.8:',[moment2(5,t) for t in (.2,.5,.8)])
print('d=3 mean conditional total length for r=1.2:',math.pi*1.2)
