"""Reproducible finite checks for rank-one random-plane Ritz-gap identities.

The analytic proofs, not these finite tests, establish the distributional
identity and the asymptotic large-deviation statement.
"""
import math
import numpy as np
from scipy.special import gammaln, digamma, polygamma


def test_direct_ritz():
    rng=np.random.default_rng(261042071)
    total=0
    for d in (3, 4, 7, 20):
        for _ in range(80):
            u=rng.normal(size=d); u/=np.linalg.norm(u)
            v=rng.normal(size=d); v/=np.linalg.norm(v)
            x=rng.normal(size=d); x-=v*np.dot(v,x); x/=np.linalg.norm(x)
            # Baseline-plus-rank-one positive definite Gram matrix.
            A=.4*np.eye(d)+1.7*np.outer(u,u)
            T=np.array([[v@A@v,v@A@x],[x@A@v,x@A@x]])
            eig,vec=np.linalg.eigh(T)
            w=vec[0,-1]*v+vec[1,-1]*x
            eps0=(.4+1.7)-v@A@v
            eps1=(.4+1.7)-w@A@w
            p=(u-v*np.dot(u,v)); p/=np.linalg.norm(p)
            factor=1.0-(p@x)**2
            assert abs(eps1/eps0-factor) < 5e-12,(d,eps1/eps0,factor)
            total+=1
    return total


def test_beta_moments():
    rng=np.random.default_rng(20261102)
    sample_size=85000
    tests=0
    for d in (3,4,9,25):
        a=(d-2)/2
        values=rng.beta(a,.5,size=sample_size)
        for s in (.25,1.,2.):
            exact=math.exp(gammaln(a+s)+gammaln(a+.5)-gammaln(a)-gammaln(a+.5+s))
            observed=float(np.mean(values**s))
            assert abs(observed-exact)<.012,(d,s,observed,exact)
            tests+=1
    # The source's exact mean factor and dimension-three log rate.
    assert abs(math.exp(gammaln(.5+1)+gammaln(1)-gammaln(.5)-gammaln(2))-.5)<1e-13
    assert abs(digamma(.5)-digamma(1)+2*math.log(2))<1e-13
    assert polygamma(1,.5)-polygamma(1,1)>0
    return tests


def test_scaled_mgf():
    # Log M_d(-theta*d), not the full sum, tends to -log(1-2theta)/2.
    for theta in (-.4,.1,.3):
        values=[]
        for d in (100, 400, 1600):
            a=(d-2)/2
            s=-theta*d
            assert a+s>0
            log_m=(gammaln(a+s)+gammaln(a+.5)-gammaln(a)-gammaln(a+.5+s))
            values.append(log_m)
        expected=-.5*math.log(1-2*theta)
        assert abs(values[-1]-expected)<.015,(theta,values[-1],expected)
    for c in (.5,1,2):
        for s in (.25*c,c,2*c):
            theta=(1-c/s)/2
            rate=(s-c-c*math.log(s/c))/2
            value=theta*s + c*.5*math.log(1-2*theta)
            assert abs(rate-value)<1e-12
    return 3+9


if __name__=='__main__':
    direct=test_direct_ritz()
    moments=test_beta_moments()
    ld=test_scaled_mgf()
    print(f'VERIFY_OK direct_ritz={direct} beta_moments={moments} scaled_mgf_and_rate={ld}')
