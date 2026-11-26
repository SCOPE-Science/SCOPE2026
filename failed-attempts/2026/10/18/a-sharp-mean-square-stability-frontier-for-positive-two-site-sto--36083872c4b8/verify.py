"""Reproduce covariance spectra and the sharp two-site Lie--Trotter stability threshold."""
import numpy as np
from math import exp, cosh, sinh, log, sqrt

def frontier(a,b,h):
    q=exp(2*a*h); c=cosh(2*b*h)
    return log((q-c)/(c-1/q))/h

def radius(a,b,noise,h):
    v=exp(noise*h); c=cosh(2*b*h)
    return exp(-2*a*h)*((v+1)*c+sqrt((v+1)**2*c*c-4*v))/2

def covariance_matrix(a,b,noise,h):
    C=cosh(b*h); S=sinh(b*h)
    H=exp(-a*h)*np.array([[C,S],[S,C]])
    V=exp(noise*h)
    basis=[np.array([[1.,0.],[0,0]]),np.array([[0.,1.],[1.,0.]]),np.array([[0.,0.],[0,1.]])]
    M=np.zeros((3,3))
    for j,B in enumerate(basis):
        T=H*(0) # distinct matrix
        T=H @ (B*np.array([[V,1.],[1.,V]])) @ H.T
        M[:,j]=[T[0,0],T[0,1],T[1,1]]
    return M

checks=0
for a,b in [(2.,1.),(1.,.5),(1.7,.24),(3.,2.4)]:
    for h in [.03,.1,.5,1.,2.]:
        cutoff=frontier(a,b,h)
        assert cutoff>0; checks+=1
        assert abs(radius(a,b,cutoff,h)-1)<3e-12; checks+=1
        for sigma2 in [0.,.8*cutoff,1.2*cutoff]:
            R=radius(a,b,sigma2,h)
            M=covariance_matrix(a,b,sigma2,h)
            ev=np.linalg.eigvals(M)
            assert abs(max(abs(ev))-R)<3e-12; checks+=1
            assert (R<1)==(sigma2<cutoff); checks+=1
        # check explicit update from independent lognormal exponential weights via exact moments
        v=exp(.7*h); H=exp(-a*h)*np.array([[cosh(b*h),sinh(b*h)],[sinh(b*h),cosh(b*h)]])
        X=np.array([[2.,-.3],[-.3,1.]])
        K=H @ (X*np.array([[v,1],[1,v]])) @ H.T
        Md=covariance_matrix(a,b,.7,h) @ np.array([X[0,0],X[0,1],X[1,1]])
        assert np.max(abs(Md-np.array([K[0,0],K[0,1],K[1,1]])))<1e-12;checks+=1
for a,b in [(1.,.5),(2.,1.)]:
    assert abs(frontier(a,b,1e-5)-2*(a-b*b/a))<2e-4;checks+=1
    assert abs(frontier(a,b,40./a)-2*(a-b))<.06*a;checks+=1
assert radius(2,1,2.5,.1)<1<radius(2,1,2.5,5);checks+=1
print(f'PASS {checks} deterministic matrix and frontier checks')
