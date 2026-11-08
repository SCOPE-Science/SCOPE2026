#!/usr/bin/env python3
"""Independent finite checks for an explicit Frobenius inball in hollow symmetric Monge simplices.

Requires numpy and scipy. The paper's proof, not these finite checks, establishes all dimensions.
"""
import math
import numpy as np
from scipy.optimize import linprog


def simplex_data(n):
    if n < 3:
        raise ValueError('n must be >=3')
    pairs = [(a, m-a) for m in range(2, n+1) for a in range(1, m)]
    count = len(pairs)
    V = np.empty((count, count), dtype=float)
    for k, (a, b) in enumerate(pairs):
        for z, (i, j) in enumerate(pairs):
            V[z, k] = (1.0 / (2*a*b)) if i<=a and j<=b else 0.0
    return pairs, V


def theorem(n):
    N = n*(n-1)//2
    alpha = math.sqrt(3-1/N)
    beta = math.sqrt(1-1/N)
    D = 2*math.comb(n, 4) + alpha*math.comb(n, 3) + beta*math.comb(n+1, 3)
    r = 1/(math.sqrt(2)*D)
    return r, alpha, beta, D


def norm_expected(n, a, b):
    N = n*(n-1)//2
    layer = a+b
    if layer <= n-2:
        t, s = 4, 0
    elif layer == n-1:
        t, s = 3, -1
    else:
        t, s = 1, 1
    return math.sqrt(2)*a*b*math.sqrt(t-s*s/N)


def run():
    for n in range(3, 11):
        pairs, V = simplex_data(n)
        N=len(pairs)
        # Independent matrix inverse, rather than the claimed four-point inverse.
        inverse=np.linalg.inv(V)
        assert np.linalg.norm(V@inverse-np.eye(N),ord=np.inf) < 2e-10
        # In the independent upper-triangular coordinates the metric is 2*Euclidean,
        # and the affine normalization restricts vectors to the sum-zero hyperplane.
        gradients=(inverse-inverse.mean(axis=1,keepdims=True))/math.sqrt(2)
        norms=np.linalg.norm(gradients,axis=1)
        predicted=np.array([norm_expected(n,a,b) for (a,b) in pairs])
        assert np.max(np.abs(norms-predicted))<5e-9
        r,alpha,beta,D=theorem(n)
        assert abs(r -1/sum(norms)) < 1e-11
        lam=r*predicted
        y=V@lam
        assert abs(2*sum(y)-1)<1e-10
        assert np.min(y)>=0
        assert np.max(np.abs(inverse@y-lam))<2e-10
        # Independent simplex LP in the original coordinates. Constraints are
        # facet-distance inequalities using gradients computed from V^{-1}.
        A=np.column_stack((-inverse,norms))
        res=linprog(np.r_[np.zeros(N),-1.0],A_ub=A,b_ub=np.zeros(N),
                    A_eq=np.array([[*([2.0]*N),0.0]]),b_eq=[1.0],
                    bounds=[(None,None)]*N+[(0,None)], method='highs')
        assert res.success, res.message
        assert abs(res.x[-1]-r) < 2e-10
        # Toeplitz assertion checked directly against the vertex combination.
        for idx,(i,b) in enumerate(pairs):
            d=n+1-i-b
            q=(d-1)*max(d-2,0)+alpha*(d-1)+beta*d
            expected=q/(2*D)
            assert abs(y[idx]-expected)<2e-10
            assert expected>0
        # Strict superadditivity of the distance profile: every ordered
        # triangle inequality is reversed at the predicted center.
        q=lambda d: (d-1)*max(d-2,0)+alpha*(d-1)+beta*d
        for p in range(1,n):
            for k in range(1,n-p):
                assert q(p+k)>q(p)+q(k)
        print('n=%d dimensions=%d radius=%.13g inverse/LP/Toeplitz/anti-metric PASS'
              % (n,N-1,r))
    for n in (20,40,80,160,320,640):
        r,alpha,beta,D=theorem(n)
        err=max(abs(n*n*((d-1)*max(d-2,0)+alpha*(d-1)+beta*d)/(2*D)
                    -6*(d/n)**2) for d in range(1,n))
        print('n=%d radius-normalization=%.12f max-profile-error=%.7g'
              % (n,n**4*r,err))
    print('HOLLOW_SYMMETRIC_MONGE_INBALL_CHECKS_PASSED')

if __name__=='__main__':
    run()
