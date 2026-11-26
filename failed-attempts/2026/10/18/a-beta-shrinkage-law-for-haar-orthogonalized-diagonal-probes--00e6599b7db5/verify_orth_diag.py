#!/usr/bin/env python3
"""Reproduce finite checks for Haar-orthogonalized self-normalized diagonal probing.

The infinite-dimensional quantifiers in the theorem are established analytically;
these numerical checks are independent consistency tests only.
"""
import math
import numpy as np


def exact_factor(n, k, power):
    if k == 1:
        return 1.0
    a = (n-k)/2.0
    b = (k-1)/2.0
    return math.exp(math.lgamma(a+power/2)+math.lgamma(a+b)
                    - math.lgamma(a)-math.lgamma(a+b+power/2))


def random_projector(rng, n, k):
    g = rng.standard_normal((n,k))
    q, _ = np.linalg.qr(g,mode="reduced")
    return q@q.T, g


def do_checks(seed=184211):
    rng=np.random.default_rng(seed)
    count=0
    # Projection geometry and the estimator formula on genuine matrices.
    for n in (3,5,8):
        for k in range(1,n+1):
            for _ in range(36):
                P,G=random_projector(rng,n,k)
                assert np.allclose(P@P,P,rtol=0,atol=1e-12)
                assert np.allclose(np.diag(P@P),np.diag(P),rtol=0,atol=1e-12)
                for i in range(n):
                    assert abs(sum(P[i,j]**2 for j in range(n) if j!=i)
                               -(P[i,i]-P[i,i]**2)) < 2e-12
                    A=rng.standard_normal((n,n))
                    h=A[i,:].copy();h[i]=0
                    err=(A@P)[i,i]/P[i,i]-A[i,i]
                    assert abs(err-h@P[:,i]/P[i,i])<5e-11
                    if k==1:
                        gi=G[i,0]
                        iid=((A@G)[i,0]*gi)/(gi*gi)
                        assert abs(err-(iid-A[i,i]))<5e-11
                    if k==n:
                        assert abs(err)<5e-11
                    count+=4
    # Gamma/beta product moment identities; these are not empirical tests.
    for n in range(3,24):
        for k in range(1,n):
            for power in (0.5,1.0,2.0,3.5):
                if k==1:
                    assert exact_factor(n,k,power)==1.0
                if power==2.0:
                    assert abs(exact_factor(n,k,2.0) - (n-k)/(n-1))<5e-13
                count+=1
    # Distribution checks: actual QR estimator vs independently sampled
    # beta x Student mixture. Quantile tolerances include sampling noise.
    for n,k in ((3,1),(5,2),(7,4),(9,7)):
        trials=11000
        h=np.arange(1,n,dtype=float)
        h/=np.linalg.norm(h)
        obs=np.empty(trials)
        for j in range(trials):
            P,_=random_projector(rng,n,k)
            obs[j]=h@P[1:,0]/P[0,0]
        beta=(np.ones(trials) if k==1 else
              rng.beta((n-k)/2,(k-1)/2,size=trials))
        law=np.sqrt(beta)*rng.normal(size=trials)/np.sqrt(
            rng.chisquare(k,size=trials))
        for quantile in (0.25,0.5,0.75,0.9):
            x=np.quantile(np.abs(obs),quantile)
            y=np.quantile(np.abs(law),quantile)
            assert abs(x-y)<0.16*max(y,0.15),(n,k,quantile,x,y)
            count+=1
        if k>3:
            target=(n-k)/((n-1)*(k-2))
            mse=np.mean(obs*obs)
            assert abs(mse/target-1)<0.2,(n,k,mse,target)
            count+=1
    print(f"PASS: {count} finite algebraic, geometry and distribution checks")
    print("All universal and infinite-tail assertions require the written proof.")


if __name__=="__main__":
    do_checks()
