"""Independent numerical checks for formulas on planar shadows of circular double cones.
No numerical test is used as a proof of continuum or extremal classifications.
"""
import math
import numpy as np
from scipy.optimize import brentq, minimize_scalar
from scipy.integrate import quad
from scipy.spatial import ConvexHull

PI = math.pi

def brightness(k,z):
    if not (k > 0 and 0 <= z <= 1): raise ValueError
    z0=k/math.sqrt(1+k*k)
    if z>=z0:
        return PI*z
    S=math.sqrt(max(0,k*k-(1+k*k)*z*z))
    return 2*(S+z*math.atan2(z,S))

def H(t):
    return (1+t*t)*math.atan(t)/t if t else 1.

def stationary(k):
    if k<=1: return 0.
    hi=max(k*k,1.)
    while H(hi)<=k*k:hi*=2
    t=brentq(lambda t:H(t)-k*k, 1e-14,hi,xtol=1e-14)
    z=k*t/math.sqrt(1+(1+k*k)*t*t)
    return z

def hull_area(k,z,n=4096):
    s=math.sqrt(max(0,1-z*z))
    t=np.arange(n)*2*PI/n
    pts=np.vstack((np.column_stack([z*np.cos(t),np.sin(t)]),np.array([[-k*s,0],[k*s,0]])))
    return ConvexHull(pts).volume

def asecond(k,z):
    S=math.sqrt(k*k-(1+k*k)*z*z)
    t=z/S
    tprime=k*k/S**3
    return 2*tprime*((1+t*t)-(k*k)*(1-t*t))/(1+t*t)**2

def test():
    n=0
    rng=np.random.default_rng(727207)
    # Independent polygon hull projection of the whole generating circle and both apices.
    for k in [0.18,0.5,0.999,1.,1.001,1.1,1.4,PI/2,1.9,2.5,5.,12.]:
      for z in np.concatenate([rng.uniform(0.002,0.998,16),[0.,1.,k/math.sqrt(1+k*k)]]):
        a=brightness(k,float(z))
        b=hull_area(k,float(z),2048)
        assert abs(a-b)<1.e-4,(k,z,a,b)
        n+=1
    # Cauchy mean-area identity for every aspect.
    for k in np.geomspace(.07,15,40):
        area=quad(lambda z:brightness(float(k),z),0,1,epsabs=2e-11,points=[k/math.sqrt(1+k*k)])[0]
        expected=PI*math.hypot(1,k)/2
        assert abs(area-expected)<3.e-8,(k,area,expected)
        n+=1
    # Global min and max compared to independent Brent bounded search across both domains.
    for k in np.geomspace(.08,15,71):
        zc=stationary(float(k))
        grid=np.linspace(0,1,2001)
        a=np.array([brightness(float(k),float(z)) for z in grid])
        candidate_min=brightness(float(k),zc)
        candidate_max=max(PI,2*k)
        assert candidate_min<=a.min()+1e-8
        assert candidate_max>=a.max()-1e-8
        if k>1:
           assert 0<zc<k/math.sqrt(1+k*k)
           assert asecond(float(k),zc)>0
        n+=1
    # Derivative and Taylor data: exact numerical finite differences away from seams.
    for k in [.25,.9,1.,1.05,1.4,2.,3.]:
      for z in np.linspace(.01,0.9*k/math.sqrt(1+k*k),12):
        S=math.sqrt(k*k-(k*k+1)*z*z)
        t=z/S
        deriv=2*(math.atan(t)-k*k*t/(1+t*t))
        fd=(brightness(k,z+1e-6)-brightness(k,z-1e-6))/2e-6
        assert abs(deriv-fd)<1e-7,(k,z,fd,deriv)
        n+=1
    # Fourfold rare tail at k=1; minimum location bifurcation; positive second derivative.
    for e in [1e-4,3e-5,1e-5]:
        zroot=brentq(lambda z:brightness(1,z)-(2+e),0,.6)
        assert abs(zroot/((3*e)**.25)-1)<0.03
        n+=1
    for d in [1e-3,1e-4,1e-5]:
        zc=stationary(1+d)
        assert abs(zc/math.sqrt(3*d)-1)<.02
        delta=brightness(1+d,0)-brightness(1+d,zc)
        assert abs(delta/(3*d*d)-1)<.03
        n+=2
    print('PASS',n,'independent hull / Cauchy / extrema / derivative / singularity checks')
    for k in [.5,1,1.1,1.4,PI/2,2.0,3.0]:
        zc=stationary(k)
        print('k=',round(k,7),'zmin=',round(zc,9),'min=',round(brightness(k,zc),10),'max=',round(max(PI,2*k),10))

if __name__=='__main__':test()
