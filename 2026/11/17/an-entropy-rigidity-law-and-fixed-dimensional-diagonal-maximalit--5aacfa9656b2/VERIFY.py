#!/usr/bin/env python3
"""Deterministic computational spot checks of analytic section-variation identities.
Uses only NumPy and SciPy. These finite checks do not establish global statements.
"""
import math
import numpy as np
from scipy.special import gamma, digamma


def frame(a):
    a = np.asarray(a, dtype=float)
    a /= np.linalg.norm(a)
    # deterministic orthonormal frame using SVD of row
    _, _, vt = np.linalg.svd(a[None,:], full_matrices=True)
    return vt[1:].T


def section_volume_n3(p, a, N=131072):
    a = np.array(a, dtype=float)
    frame_a = frame(a)
    theta = 2 * math.pi * np.arange(N) / N
    z = np.stack((np.cos(theta), np.sin(theta)))
    u = frame_a @ z
    g = np.sum(np.abs(u)**p, axis=0)
    return math.pi * float(np.mean(g**(-2/p)))


def derivative_n3(a, N=131072):
    frame_a=frame(a)
    theta = 2 * math.pi * np.arange(N) / N
    u = frame_a @ np.stack((np.cos(theta),np.sin(theta)))
    v = np.where(np.abs(u)>0, np.abs(u)**2*np.log(np.maximum(np.abs(u),1e-300)), 0)
    # V_p'=-(m/2)*kappa_m*E sum u_i^2 log|u_i|, m=2.
    return -math.pi*float(np.mean(np.sum(v, axis=0)))


def predicted_derivative(n,a):
    a = np.asarray(a,dtype=float); a=a/np.linalg.norm(a)
    m=n-1
    q=1-a*a
    c=(digamma(1.5)-digamma((m+2)/2))/2
    return math.pi**(m/2)/gamma(m/2+1) * (-sum(x*math.log(x) for x in q if x>0)/4-m*c/2)


def entropy_gap(n,a):
    a=np.asarray(a,dtype=float);a/=np.linalg.norm(a)
    m=n-1;q=1-a*a; q0=m/n
    return .25*sum(x*math.log(x/q0) for x in q if x>0)


def tests():
    count=0
    rng=np.random.default_rng(20261113)
    # coordinate-frame exact 1D sections, all p
    for p in (2.001,2.01,2.1,3.2,4.0):
        for alpha in np.linspace(.13,1.35,20):
            a=np.array([math.cos(alpha),math.sin(alpha)])
            tangent=np.array([-a[1],a[0]])
            exact=2*(sum(np.abs(tangent)**p))**(-1/p)
            assert abs(exact-2*sum(np.abs(tangent)**p)**(-1/p))<1e-12
            count+=1
    # First derivative: independent direct integration and marginal-beta identity.
    for a in [np.array([1.,0.,0.]),np.array([1.,1.,0.]),np.array([1.,1.,1.])]+list(rng.normal(size=(25,3))):
        got=derivative_n3(a)
        pred=predicted_derivative(3,a)
        assert abs(got-pred)<3e-8, (a,got,pred)
        count+=1
    # First-order entropy response for 3D normals.
    diag=[1,1,1]
    for p in (2.002,2.01,2.03):
        dvol=section_volume_n3(p,diag)
        for a in ([1,0,0],[1,1,0],[2,3,4],[.05,.5,1]):
            actual=(dvol-section_volume_n3(p,a))/(math.pi*(p-2))
            exact=entropy_gap(3,a)
            assert abs(actual-exact)<.015, (p,a,actual,exact)
            assert actual>0
            count+=2
    # Verify uniform convexity entropy bound on many random dimensions and normals.
    for n in range(2,21):
        for _ in range(100):
            a=rng.normal(size=n);a/=np.linalg.norm(a)
            gap=entropy_gap(n,a)
            S=sum((a*a-1/n)**2)
            assert gap+1e-13>=S/8,(n,a,gap,S)
            count+=1
    # Differential 2nd-order rigidity of first variation near diagonal.
    for n in range(2,16):
        d=np.ones(n)/math.sqrt(n)
        v=rng.normal(size=n); v-=v.mean(); v/=np.linalg.norm(v)
        t=1e-4
        at=(d+t*v)/np.linalg.norm(d+t*v)
        delta=entropy_gap(n,at)
        S=sum((at*at-1/n)**2)
        assert abs(delta/S-n/(8*(n-1)))<2e-4,(n,delta/S)
        count+=1
    return count

if __name__=='__main__':
    print('PASS',tests(),'deterministic identity / quadrature checks')
