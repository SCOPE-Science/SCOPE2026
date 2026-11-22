"""Finite diagnostics for a sharp weighted Bergman one-kernel approximation theorem.
No computation in this file is used in place of the global analytic proof.
"""
from math import sqrt, acos, cos, sin, pi, isclose
import numpy as np
from scipy.optimize import minimize_scalar, brentq

def direct(lam,a,r,theta):
    z=r*complex(cos(theta),sin(theta))
    return (1-r*r)**lam * abs(1+a*z-z*z)**2

def theorem(lam,a):
    if 1<lam<2:
        rc=sqrt((2-lam)/(2+lam))
        ac=2*sqrt(4-lam*lam)/lam
        if a<=ac:
            theta=acos(max(-1,min(1,a/ac)))
            v=(1+a*a/4)*(1-rc*rc)**lam*(1+rc*rc)**2
            return rc,theta,v,ac
    if a==0:
        return 0.0,0.0,1.0,0.0
    def h(r):return (lam+2)*r*(1-r*r)/(1-(lam+1)*r*r)
    rr=brentq(lambda r:h(r)-a,0,1/sqrt(lam+1)-1e-13,xtol=1e-14)
    return rr,0.0,direct(lam,a,rr,0.0),None

def angular_envelope(lam,a,r):
    if r==0:return 1.0
    t=r*r
    x=min(1., a*(1-t)/(4*r))
    return (1-t)**lam*((1+t)**2+a*a*t+2*a*r*(1-t)*x-4*t*x*x)

def run():
    count=0
    for lam in [1.001,1.05,1.2,1.5,1.8,1.99,2.,2.01,2.5,3.,7.]:
        ac=2*sqrt(4-lam*lam)/lam if lam<2 else 0
        for a in [0.,.001,.01,.1,.3,.5,1.,2.,4.,10.,100.,ac*.5,ac*.999,ac,ac*1.001,ac*1.5]:
            r,theta,v,_=theorem(lam,a)
            assert abs(v-direct(lam,a,r,theta))<5e-12*max(1,v)
            res=minimize_scalar(lambda x:-angular_envelope(lam,a,x),bounds=(0,1),method='bounded',options={'xatol':5e-13})
            assert v>=-res.fun-3e-8*max(1,v),(lam,a,v,-res.fun,r,theta,res.x)
            for t in np.linspace(0,1,121):
                assert angular_envelope(lam,a,t)<=v+3e-9*max(1,v)
                count+=1
            if a>0 and theta==0:
                assert r<1/sqrt(lam+1)+1e-12
            if a==0 and lam>=2:
                assert r==0
            count+=3
    # Critical and one-sided derivative checks
    for lam in [1.01,1.1,1.3,1.5,1.8,1.99]:
        ac=2*sqrt(4-lam**2)/lam
        rc=sqrt((2-lam)/(lam+2))
        assert abs(theorem(lam,ac)[0]-rc)<1e-12
        for delta in [1e-4,1e-5,1e-6]:
            below=theorem(lam,ac-delta)
            above=theorem(lam,ac+delta)
            assert abs(below[0]-rc)<1e-12
            assert abs(below[1]/sqrt(delta)-sqrt(2/ac))<1e-2
            assert abs((above[0]-rc)/delta-lam**3/(8*(lam+2)))<1e-4
            count+=4
    print('PASS',count,'finite assertions; theorem formulas checked numerically, not an infinite proof')
if __name__=='__main__':run()
