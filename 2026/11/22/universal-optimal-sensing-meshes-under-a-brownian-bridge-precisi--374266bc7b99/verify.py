"""Exact algebra and independent finite checks for optimal precision-budget Brownian-bridge quadrature."""
from fractions import Fraction as F
from random import Random
from math import sqrt


def covariance(x,y):
    return min(x,y)-x*y


def direct_mse(t,w,p):
    n=len(t)
    z=F(1,12)
    for i in range(n):
        z-=w[i]*t[i]*(1-t[i])
        z+=w[i]*w[i]/p[i]
        for j in range(n):
            z+=w[i]*w[j]*covariance(t[i],t[j])
    return z


def positions(w):
    W=sum(w,F(0))
    return [(1-W)/2+sum(w[:i],F(0))+w[i]/2 for i in range(len(w))]


def optimal_scalar(n,P):
    a=1-1/n**2
    b=2+8/P
    # Cancellation-free smaller root.
    return 2/(b+sqrt(b*b-4*a))


def numerical_risk(n,P):
    W=optimal_scalar(n,P)
    return ((1-W)**3+W**3/n**2)/12 +W*W/P


def numerical_direct(t,w,p):
    n=len(t)
    r=1/12
    for i in range(n):
        r-=w[i]*t[i]*(1-t[i])
        r+=w[i]**2/p[i]
        for j in range(n):
            r+=w[i]*w[j]*covariance(t[i],t[j])
    return r


def test():
    checks=0
    # All identities checked exactly over independent rational examples.
    for n in (1,2,3,4,5,7):
        for k in (1,2,3,4,5,7,11):
            w=[F(((i+2)*k)%13+1, 15*(n+1)*13) for i in range(n)]
            W=sum(w)
            assert 0<W<1
            x=positions(w)
            assert all(0<x[i]<1 for i in range(n)) and x==sorted(x)
            # No-noise cost is computed independently via covariance sums.
            R=direct_mse(x,w,[F(1)]*n)-sum(wi*wi for wi in w)
            certificate=((1-W)**3+sum(wi**3 for wi in w))/12
            assert R==certificate,(n,k,R,certificate)
            checks+=1
    # Recompute closed form using the covariance matrix inverse, unrelated to dual quadratic weights.
    import numpy as np
    rng=Random(20261117)
    for n in (1,2,3,4,5,8):
        for P in (0.05,0.5,2,10,30,1000):
            W=optimal_scalar(n,P); w=W/n
            t=[(1-W)/2+(i+.5)*w for i in range(n)]
            p=[P/n]*n
            mat=np.array([[covariance(t[i],t[j]) for j in range(n)] for i in range(n)])+np.eye(n)*(n/P)
            m=np.array([u*(1-u)/2 for u in t])
            wt=np.linalg.solve(mat,m)
            assert np.allclose(wt,w,rtol=2e-10,atol=2e-10),(n,P,w,wt)
            rr=1/12-m@wt
            assert abs(rr-numerical_risk(n,P))<2e-11,(n,P,rr,numerical_risk(n,P))
            checks+=1
    # Broader random competitor tests, supplementary only, not a proof of globality.
    for n in (1,2,3,4,5,8):
        for P in (0.03,0.5,3,50,1000):
            opt=numerical_risk(n,P)
            for _ in range(150):
                t=sorted(rng.random() for _ in range(n))
                q=[rng.random()+.001 for i in range(n)]; p=[P*qi/sum(q) for qi in q]
                import numpy as np
                K=np.array([[covariance(t[i],t[j]) for j in range(n)] for i in range(n)]) + np.diag([1/pi for pi in p])
                m=np.array([u*(1-u)/2 for u in t]); r=1/12-m@np.linalg.solve(K,m)
                assert r+1e-11>=opt, (n,P,r,opt)
                checks+=1
    # Exact n=2, P=10 certificate.
    n=2; P=F(10); W=F(2,5); w=[F(1,5)]*2;x=[F(2,5),F(3,5)];p=[F(5)]*2
    assert x==positions(w)
    assert direct_mse(x,w,p)==F(1,12)-F(6,125)
    w3=[F(1,6)]*3; t3=[F(1,3),F(1,2),F(2,3)]; p3=[F(6)]*3
    assert positions(w3)==t3
    assert direct_mse(t3,w3,p3)==F(11,432)
    print('PASS:',checks,'exact-identity/matrix-identity/random competitors, plus two rational examples')

if __name__=='__main__':
    test()
