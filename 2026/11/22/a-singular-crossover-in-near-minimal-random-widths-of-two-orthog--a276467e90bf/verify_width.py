"""Finite deterministic diagnostics for a geometric width-endpoint theorem.

Requires numpy and scipy; nothing in this file certifies infinite asymptotics.
"""
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import quad

ROOT2=np.sqrt(2.)

def width(t,phi,v):
    q=np.sqrt(1-v*v)
    ux=q*np.cos(phi); uz=q*np.sin(phi)
    a=np.hypot(ux,v); b=np.hypot(uz,v)
    return a+b+np.maximum(np.abs(a-b),t*np.abs(v))

def via_support(t,u):
    x,y,z=u
    a=np.hypot(x,y);b=np.hypot(y,z)
    return max(a-t*y/2,b+t*y/2)+max(a+t*y/2,b-t*y/2)

def prob_exact_numeric(t,eps):
    threshold=ROOT2+eps
    vmax=brentq(lambda v: width(t,np.pi/4,v)-threshold,0,0.99)
    def angle(v):
        return brentq(lambda s:width(t,np.pi/4+s,v)-threshold,0,np.pi/4,xtol=1e-14)
    integ=quad(angle,0,vmax,epsabs=5e-13,epsrel=2e-9,limit=200)[0]
    return 4/np.pi*integ

def crossover(tau):
    ym=(np.sqrt(tau*tau+2*ROOT2)-tau)/ROOT2
    return (2*ROOT2/np.pi)*(ym-ym**3/(3*ROOT2))

def main():
    checks=0
    rng=np.random.default_rng(20261117)
    for t in [0.,.2,1.,2.,5.]:
        for _ in range(100):
            v=rng.normal(size=3);v/=np.linalg.norm(v)
            a=via_support(t,v)
            b=width(t,np.arctan2(v[2],v[0]),v[1])
            assert abs(a-b)<1e-12
            assert a>=ROOT2-1e-12
            checks+=2
    for t in [0,0.5,1,2,10]:
        for angle in [np.pi/4,3*np.pi/4,5*np.pi/4,7*np.pi/4]:
            assert abs(width(t,angle,0)-ROOT2)<1e-14
            checks+=1
    # Independent direct quadrature using exact spherical width, not the limiting formula.
    for t in [0.5,1,2]:
        targets=[]
        for eps in [0.04,0.02,0.01,0.005]:
            p=prob_exact_numeric(t,eps)
            targets.append(p/eps**2)
            checks+=1
        pred=2*ROOT2/(np.pi*t)
        assert abs(targets[-1]/pred-1)<0.055,(t,targets,pred)
        checks+=1
        print('fixed separation',t,'ratios',targets,'limit',pred)
    for tau in [0,0.5,2]:
        vals=[]
        for eps in [0.02,0.01,0.005,0.0025]:
            p=prob_exact_numeric(tau*np.sqrt(eps),eps)
            vals.append(p/eps**1.5)
            checks+=1
        pred=crossover(tau)
        assert abs(vals[-1]/pred-1)<0.03,(tau,vals,pred)
        checks+=1
        print('crossover',tau,'ratios',vals,'limit',pred)
    # Exact area of each limiting corner domain by independent Simpson quadrature.
    from scipy.integrate import simpson
    for tau in np.linspace(0,5,21):
        ymax=(np.sqrt(tau*tau+2*ROOT2)-tau)/ROOT2
        y=np.linspace(-ymax,ymax,5001)
        L=np.maximum(0,1-y*y/ROOT2)
        area=simpson(2*L/ROOT2, x=y)
        assert abs(area/np.pi-crossover(tau))<1e-10
        checks+=1
    print('WIDTH_DIAGNOSTICS_PASSED',checks)

if __name__=='__main__':main()
