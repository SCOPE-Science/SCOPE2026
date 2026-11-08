#!/usr/bin/env python3
"""Numerical consistency tests for the Wigner caustic of two-mode constant-width ovals."""
import math

def boundary(lam):
    s = math.acos(1.25*math.sqrt(1-lam*lam))
    return 5*s/3 - math.atan((5/3)*math.tan(s))

def q(t,lam,phi):
    return math.cos(3*t)+lam*math.cos(5*t+phi)

def dq(t,lam,phi):
    return -3*math.sin(3*t)-5*lam*math.sin(5*t+phi)

def count(lam,phi,N=12000):
    # q(theta+pi)=-q(theta); grid phase offset avoids exact roots.
    vals=[q(math.pi*(j+0.1234567)/N,lam,phi) for j in range(N+1)]
    # sign changes on [theta0,theta0+pi) also last interval endpoint matches antiperiodicity
    return sum(vals[j]*vals[j+1]<0 for j in range(N))

def predicted(lam,phi):
    if lam<.6: return 3
    if lam>1: return 5
    r=boundary(lam)
    d=min(abs((phi-2*math.pi*k/3+math.pi)%(2*math.pi)-math.pi) for k in range(3))
    return 5 if d<r else 3

def main():
    cases=0
    for lam in (.0,.1,.45,.59,.601,.63,.7,.83,.97,.999,1.001,1.1,2.,8.):
        for j in range(97):
            phi=2*math.pi*(j+.362)/97
            want=predicted(lam,phi)
            got=count(lam,phi,N=6000)
            assert got==want,(lam,phi,want,got)
            cases+=1
    for lam in (.61,.7,.85,.99):
        r=boundary(lam)
        assert 0<r<math.pi/3
        for center in [0,2*math.pi/3,4*math.pi/3]:
            for eps in (.003,-.003):
                phi=center+r+eps
                assert count(lam,phi)==predicted(lam,phi)
                cases+=1
        s=math.acos(1.25*math.sqrt(1-lam*lam))
        t=math.pi/2+s/3
        phi=-r
        assert abs(q(t,lam,phi))<1e-11,('tangency q',lam,q(t,lam,phi))
        assert abs(dq(t,lam,phi))<1e-11,('tangency dq',lam,dq(t,lam,phi))
        cases+=1
    # Exactly the two codimension-one threshold degeneracies
    assert abs(q(math.pi/2,3/5,0))<1e-12
    assert abs(dq(math.pi/2,3/5,0))<1e-12
    assert abs(q(0,1,math.pi))<1e-12
    assert abs(dq(0,1,math.pi))<1e-12
    # Sharp spectral threshold lambda=3b/a;  fifth-area fraction= lambda^2/(3+lambda^2)
    assert abs((.6**2)/(3+.6**2)-3/28)<1e-14
    assert abs((1**2)/(3+1**2)-.25)<1e-14
    print('TWO_MODE_WIGNER_CAUSTIC_PHASE_DIAGRAM_OK',cases)

if __name__=='__main__': main()
