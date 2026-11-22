#!/usr/bin/env python3
"""Numerical diagnostics for a random planar ellipsoid-shadow aspect-ratio law.
Requires Python 3, NumPy, and SciPy. Diagnostics complement, not replace, the proof.
"""
import math
import warnings
import numpy as np
from scipy.integrate import quad, IntegrationWarning

PI = math.pi

def density(A,B,C,r):
    if not 1 < r < A/C: return 0.
    lo, hi = max(C,B/r), min(B,A/r)
    if hi <= lo: return 0.
    def f(t):
        s = math.sin(t); y = lo + (hi-lo)*s*s
        if y <= lo or y >= hi: return 0.
        x = r*y
        v=(A-x)*(A-y)*(x-B)*(B-y)*(x-C)*(y-C)
        if v <= 0: return 0.
        return (r-1)*y*y*(hi-lo)*math.sin(2*t)/(2*PI*math.sqrt(v))
    with warnings.catch_warnings():
        warnings.simplefilter('ignore',IntegrationWarning)
        return sum(quad(f, a,b,epsabs=5e-9,epsrel=5e-9,limit=350)[0]
                   for a,b in [(0,PI/4),(PI/4,PI/2)])

def coefficients(A,B,C):
    kA = C**1.5/(2*PI*math.sqrt(B*(A-B)*(A-C)))
    kC = B**1.5/(2*PI*math.sqrt(A*(A-C)*(B-C)))
    lower = B**2/(4*(A-B)*(B-C))
    upper = C**1.5/(2*math.sqrt(A*(A-B)*(B-C)))
    return kA,kC,lower,upper

def projected_eigenvalues(A,B,C,n):
    ref=np.array((1.,0.,0.))
    if abs(n[0])>.85:ref=np.array((0.,1.,0.))
    t=np.cross(n,ref);t=t/np.linalg.norm(t)
    v=np.cross(n,t)
    U=np.column_stack((t,v))
    return np.linalg.eigvalsh(U.T@np.diag((A,B,C))@U)[::-1]

def reconstruct(p,q,k):
    if abs(p-q)<1e-10:
        return (1.,1./p,1./p**2)
    k_one=1/(2*PI*q*math.sqrt((p-1)*(p*q-1)))
    k_two=p/(2*PI*math.sqrt(q*(p-1)*(p*q-1)))
    if abs(k-k_one)<abs(k-k_two):return (1.,1/p,1/(p*q))
    return (1.,1/q,1/(p*q))

def test():
    count=0
    rng=np.random.default_rng(3852965)
    for A,B,C in [(9.,4.,1.),(9.,2.25,1.),(9.,3.,1.),(4.7,3.1,.8)]:
        for i in range(120):
            n=rng.normal(size=3);n=n/np.linalg.norm(n)
            x,y=projected_eigenvalues(A,B,C,n)
            weights=((A-x)*(A-y)/((A-B)*(A-C)),
                     (x-B)*(B-y)/((A-B)*(B-C)),
                     (x-C)*(y-C)/((A-C)*(B-C)))
            assert np.max(np.abs(np.array(weights)-n*n))<2e-12
            assert C-1e-12<=y<=B+1e-12 and B-1e-12<=x<=A+1e-12
            count+=2
        vals=sorted((A/B,B/C));p,q=vals
        kA,kC,lower,upper=coefficients(A,B,C)
        if p<q-1e-7:
            kh=kA if B/C==q else kC
            recovered=reconstruct(p,q,kh)
            assert np.allclose(np.array(recovered),np.array([1,B/A,C/A]),rtol=1e-12)
            count+=1
            for centre,coef in [(B/C,kA),(A/B,kC)]:
                f1=(density(A,B,C,centre+1e-3)+density(A,B,C,centre-1e-3))/2
                f2=(density(A,B,C,centre+1e-5)+density(A,B,C,centre-1e-5))/2
                approx=(f2-f1)/math.log(100)
                assert abs(approx/coef-1)<0.006,(A,B,C,centre,approx,coef)
                count+=1
        else:
            assert abs(p-q)<1e-10
            assert np.allclose(reconstruct(p,q,kA+kC),(1,B/A,C/A))
            count+=1
            f1=(density(A,B,C,p+1e-3)+density(A,B,C,p-1e-3))/2
            f2=(density(A,B,C,p+1e-5)+density(A,B,C,p-1e-5))/2
            approx=(f2-f1)/math.log(100)
            assert abs(approx/(kA+kC)-1)<0.01,(approx,kA+kC)
            count+=1
        for delta in [1e-3,2e-4]:
            fnear=density(A,B,C,1+delta)
            assert abs(fnear/(2*lower*delta)-1)<0.02,(A,B,C,'lower',delta,fnear,2*lower*delta)
            ffar=density(A,B,C,A/C-delta)
            assert abs(ffar/upper-1)<0.04,(A,B,C,'upper',delta,ffar,upper)
            count+=2
    A,B,C=9.,4.,1.
    total=sum(quad(lambda rr:density(A,B,C,rr),a,b,epsabs=3e-7,epsrel=3e-7,limit=300)[0] for a,b in [(1,A/B),(A/B,B/C),(B/C,A/C)])
    assert abs(total-1)<2e-5,total
    count+=1
    p,q=2.25,4.
    k1=1/(2*PI*q*math.sqrt((p-1)*(p*q-1)))
    k2=p/(2*PI*math.sqrt(q*(p-1)*(p*q-1)))
    assert k2/k1==p*math.sqrt(q)
    assert not np.allclose(reconstruct(p,q,k1),reconstruct(p,q,k2))
    count+=2
    print(f"PASS {count} numeric/algebraic assertions; example normalization={total:.12f}; distinct high-peak log amplitudes={k1:.12f},{k2:.12f}")

if __name__=='__main__':test()
