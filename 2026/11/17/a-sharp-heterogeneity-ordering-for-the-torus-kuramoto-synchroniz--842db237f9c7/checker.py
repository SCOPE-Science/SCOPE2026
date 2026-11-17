"""Numerical diagnostics for the sharp dispersion-majorization threshold theorem.
These computations are supportive checks and not the proof.
"""
import math
import numpy as np
from scipy.optimize import brentq

def onset(d):
    d=np.asarray(d,dtype=float)
    assert np.all(d>0) and len(d)>=3
    fn=lambda t:sum(d/(t+d))-1.
    hi=max(float(sum(d)),1.)*2.
    t=brentq(fn,1.e-14,hi,xtol=1e-13)
    K=t*np.prod(1+d/t)
    x=t/(t+d)
    assert abs(sum(1-x)-1)<1e-10
    assert abs(K*t**(len(d)-1)-np.prod(t+d))<1e-6*max(1.,np.prod(t+d))
    J=-np.diag(d+t)+np.outer(np.sqrt(d),np.sqrt(d))
    lam=np.linalg.eigvalsh(J)
    assert abs(lam[-1])<1e-7*max(1,t)
    return K,t,x

def test():
    rng=np.random.default_rng(20261114)
    trials=0
    for D in range(3,17):
        for _ in range(100):
            d=np.exp(rng.uniform(-4,4,size=D))
            K,_,_=onset(d)
            S=sum(d)
            upper=S*(D/(D-1))**(D-1)
            assert S<K+1e-10
            assert K<upper+1e-9*upper
            # Mean-preserving equalizing transfer raises onset.
            i,j=sorted(rng.choice(D,size=2,replace=False))
            if d[i]>d[j]: i,j=j,i
            eta=rng.uniform(0,.5)*(d[j]-d[i])
            e=d.copy();e[i]+=eta;e[j]-=eta
            Ke,_,_=onset(e)
            assert Ke+1e-9*Ke>=K
            assert float(np.prod(onset(e)[2]))+1e-10 >= float(np.prod(onset(d)[2]))
            trials+=1
    for D in [3,4,8,12]:
        m=2.4
        v=np.arange(D)-np.mean(np.arange(D))
        v=v/max(abs(v))
        K0=onset([m]*D)[0]
        epss=[.04,.02,.01,.005]
        errors=[]
        for eps in epss:
            vec=m*(1+eps*v)
            K=onset(vec)[0]
            approximation=K0*(1-eps*eps*np.dot(v,v)/(2*D*D))
            errors.append(abs(K-approximation)/K0)
        assert errors[-1]<2.e-8
        assert errors[-1]<errors[0]
        X0=((D-1)/D)**D
        amplitude_errors=[]
        for eps in epss:
            vec=m*(1+eps*v)
            X=np.prod(onset(vec)[2])
            approximation=X0*(1-eps*eps*np.dot(v,v)/(2*D*D))
            amplitude_errors.append(abs(X-approximation)/X0)
        assert amplitude_errors[-1]<1e-7
        assert amplitude_errors[-1]<amplitude_errors[0]
    print('PASS:',trials,'majorization/bounds/stationary/Jacobian checks; four curvature families')

if __name__=='__main__':test()
