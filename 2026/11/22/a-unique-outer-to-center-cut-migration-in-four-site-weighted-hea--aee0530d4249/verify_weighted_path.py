"""Numerical corroboration for symmetric four-node graph heat approximation."""
import math
import random
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq

def spec(r,u):
    d=math.hypot(1.0,r); em=math.exp(-(1+r-d)*u); ep=math.exp(-(1+r+d)*u)
    co=2-(1+math.exp(-2*u))/2-((1+r/d)*em+(1-r/d)*ep)/2
    cm=2-((1+1/d)*em+(1-1/d)*ep)
    return co,cm

def mat(r,u):
    L=np.diag([1,1+r,1+r,1.0])-np.diag([1,r,1],1)-np.diag([1,r,1],-1)
    return expm(-u*L)

def root(r):
    assert 0<r<1
    # log-time bracket valid for ordinary ratios
    return brentq(lambda u: spec(r,u)[1]-spec(r,u)[0],1e-8,50/r,xtol=1e-12)

def run():
    rng=random.Random(2908)
    cases=0
    for _ in range(200):
        r=math.exp(rng.uniform(math.log(.05),math.log(7)))
        u=rng.uniform(.01,3.0)/max(1,r)
        H=mat(r,u)
        c1,c2=spec(r,u)
        assert np.min(H)>-1e-12
        assert abs(c1-2*(1-H[0,0]))<5e-12
        assert abs(c2-2*sum(H[i,j] for i in range(2) for j in range(2,4)))<5e-12
        assert abs(2*(H[0,2]+H[1,2]-H[0,1])-(c2-c1))<5e-12
        for _ in range(20):
            x=np.array([rng.uniform(-2,2) for i in range(4)])
            v=np.sum(abs(np.diff(x)))
            e=np.sum(abs(x-H@x))
            assert e<=max(c1,c2)*v+1e-10
            cases+=1
    for r in [.1,.2,.5,.8,.95,.99]:
        u=root(r)
        assert spec(r,u*(1-1e-5))[0]>spec(r,u*(1-1e-5))[1]
        assert spec(r,u*(1+1e-5))[0]<spec(r,u*(1+1e-5))[1]
    for r in [1,1.1,2,5]:
        for u in [.001,.01,.1,1.,5.]:
            assert spec(r,u)[1]>spec(r,u)[0]
    for r in [.005,.002]:
        assert abs(root(r)*r-math.log(3))<.025
    for r in [.99,.999,.9999]:
        t=root(r)
        assert abs(t/math.sqrt(6*(1-r)/r)-1)<.15
    print('MATRIX_EXPONENTIAL_AND_LEAKAGE_PASS: 200')
    print('REAL_SIGNAL_BV_ERROR_BOUNDS_PASS:',cases)
    print('PHASE_TRANSITION_ASYMPTOTICS_PASS')
    for r in [.25,.5,.8]:
        print('r',r,'crossing u',root(r))

if __name__=='__main__':run()
