"""Independent algebraic and Monte Carlo checks for random affine-exact quadrature.
This finite computation does not certify the asymptotic theorem, which has a proof.
"""
import math
import numpy as np
from fractions import Fraction as F
import random

RNG = np.random.default_rng(173921)

def min_norm_weights(x):
    z = x.mean(axis=-1, keepdims=True)
    v = x-z
    s = np.sum(v*v, axis=-1, keepdims=True)
    return np.ones_like(x)/x.shape[-1] + (0.5-z)*v/s

def constant(m):
    return (math.pi**((m-1)/2)/math.gamma((m+1)/2)) /(math.sqrt(m)*2**(m-1))

checks=0
rr=random.Random(173921)
for m in range(2,9):
    for rep in range(80):
        vals=rr.sample(range(1,996),m)
        xs=[F(z,997) for z in vals]
        mean=sum(xs)/m
        v=[xx-mean for xx in xs]
        ss=sum(xx*xx for xx in v)
        ws=[F(1,m)+(F(1,2)-mean)*vv/ss for vv in v]
        assert sum(ws)==1
        assert sum(ww*xx for ww,xx in zip(ws,xs))==F(1,2)
        assert all((ws[i]-F(1,m))*v[j]==(ws[j]-F(1,m))*v[i] for i in range(m) for j in range(m))
        assert sum(ww*ww for ww in ws)==F(1,m)+(F(1,2)-mean)**2/ss
        checks+=4
for m in range(2,9):
    xs=RNG.uniform(size=(256,m))
    w=min_norm_weights(xs)
    for x,ww in zip(xs,w):
        A=np.stack([np.ones(m),x])
        ref=np.linalg.lstsq(A, np.array([1.,.5]), rcond=None)[0]
        assert np.allclose(ww,ref,rtol=1e-8,atol=1e-9)
        checks+=1
        assert abs(ww.sum()-1)<1e-8, (m, x,ww,ww.sum())
        checks+=1
        assert abs(ww@x-.5)<1e-8
        checks+=1
        v=x-x.mean()
        assert abs(ww@ww-(1/m+(.5-x.mean())**2/(v@v)))<2e-9*max(1.0,ww@ww)
        checks+=1

N=3_000_000
bsize=100_000
for m in (2,3,4):
    t=16.0
    hits=0
    for _ in range(N//bsize):
        xs=RNG.random((bsize,m))
        z=xs.mean(axis=1)
        ss=np.sum((xs-z[:,None])**2,axis=1)
        norm_sq=1/m+(.5-z)**2/ss
        hits+=np.count_nonzero(norm_sq>t*t)
    estimate=hits/N*t**(m-1)
    theor=constant(m)
    # The limit is an asymptotic; errors include finite-t boundary effects and sampling error.
    assert abs(estimate/theor-1)<0.16,(m,estimate,theor,hits)
    checks+=1
    print(f'uniform m={m} threshold={t}: hits={hits}; scaled={estimate:.8f}; leading_constant={theor:.8f}')

# Model of independent unit-variance evaluation perturbations: exact conditional MSE=||w||_2^2.
for m in range(2,9):
    xs=RNG.random((64,m))
    w=min_norm_weights(xs)
    v=xs-xs.mean(axis=1,keepdims=True)
    theoretical=1/m+(0.5-xs.mean(axis=1))**2/np.sum(v*v,axis=1)
    assert np.allclose(np.sum(w*w,axis=1),theoretical,atol=1e-11)
    checks+=64

print('CHECKS_PASSED',checks)
