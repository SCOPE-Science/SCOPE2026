"""Reproduce finite-mask and finite-input checks for weighted squared-l1 proximal maps.

The global theorem and the radical envelope are analytic; these checks supplement them.
Uses only the Python standard library.
"""
from fractions import Fraction as F
from itertools import combinations
from random import Random
from math import sqrt


def fraction_jacobian(weights, scale, active):
    n = len(weights)
    W = sum((weights[i]**2 for i in active), F(0))
    return [[(F(int(i == j)) if i in active and j in active else F(0))
             - (scale * weights[i] * weights[j] / (1 + scale * W) if i in active and j in active else F(0))
             for j in range(n)] for i in range(n)]


def row_norms(jac):
    return [sum((abs(v) for v in row), F(0)) for row in jac]


def full_search(w, alpha):
    n=len(w)
    best=(F(0), None, None)
    for k in range(1,n+1):
        for t in combinations(range(n),k):
            J=fraction_jacobian(w,alpha,t)
            for i,v in enumerate(row_norms(J)):
                if v>best[0]:best=(v,t,i)
    return best


def prefix_search(w, alpha):
    n=len(w)
    best=F(1)
    for i in range(n):
        others=sorted(w[j] for j in range(n) if j!=i)
        sumw=F(0); sumsq=F(0)
        for k in range(n):
            if k:
                sumw+=others[k-1]
                sumsq+=others[k-1]**2
            r=F(1)+alpha*w[i]*(sumw-w[i])/(F(1)+alpha*(w[i]**2+sumsq))
            best=max(best,r)
    return best


def prox(w, alpha, x):
    # Exact threshold, independently of the Jacobian expression.
    if all(v==0 for v in x):return [F(0)]*len(x)
    entries=sorted([(abs(v)/wi,wi,abs(v),i) for i,(v,wi) in enumerate(zip(x,w))], reverse=True)
    threshold=None
    sw=F(0);sw2=F(0)
    for k,(_,wi,xi,_) in enumerate(entries,1):
        sw+=wi*xi;sw2+=wi*wi
        t=alpha*sw/(1+alpha*sw2)
        if k==len(entries) or entries[k][0]<=t:
            if entries[k-1][0]>=t:
                threshold=t;break
    if threshold is None:raise AssertionError('threshold not found')
    return [((abs(v)-threshold*wi) if abs(v)>threshold*wi else F(0))*(1 if v>=0 else -1)
            for v,wi in zip(x,w)]


def exact_witness(w, alpha, active, i):
    # Choose u active=1; other coordinates at strict inactive x=0.
    n=len(w)
    active=set(active)
    u=[F(1) if j in active else F(0) for j in range(n)]
    mass=sum((w[j] for j in active),F(0))
    x=[u[j]+alpha*w[j]*mass if j in active else F(0) for j in range(n)]
    J=fraction_jacobian(w,alpha,active)
    h=[F(1) if J[i][j]>=0 else F(-1) for j in range(n)]
    for j in range(n):
        if j not in active:h[j]=F(0)
    Jh=[sum((J[j][k]*h[k] for k in range(n)),F(0)) for j in range(n)]
    epsilon=F(1,10000)
    xp=[x[j]+epsilon*h[j] for j in range(n)]
    y=prox(w,alpha,x);yp=prox(w,alpha,xp)
    assert y==u, ('base solution',y,u)
    assert yp==[u[j]+epsilon*Jh[j] for j in range(n)], ('affine face',w,alpha,active)
    diff=max(abs(yp[j]-y[j]) for j in range(n))/epsilon
    assert diff>=row_norms(J)[i], ('finite exact ratio lower', diff,row_norms(J)[i])
    return diff


def run():
    rng=Random(21487)
    total=0
    for n in range(2,8):
      for rep in range(36):
        w=[F(rng.randint(1,25),rng.randint(1,11)) for _ in range(n)]
        alpha=F(rng.randint(1,17),rng.randint(1,9))
        best,active,i=full_search(w,alpha)
        assert best==prefix_search(w,alpha), (n,rep,best,prefix_search(w,alpha))
        ratio=exact_witness(w,alpha,active,i)
        assert ratio==best,(n,rep,ratio,best)
        total+=2
    # Check exact norm-one maximizers against the radical envelope,
    # and show equal weights only maximize when n=4.
    for n in range(2,10):
        exceptional=sqrt((1-1/sqrt(n))/2)
        repeated=sqrt((1-exceptional**2)/(n-1))
        weights=[exceptional]+[repeated]*(n-1)
        for alpha in [0.1,1.0,7.5]:
            # numerical exhaustive mask tests supplement the algebraic equality proof
            best=0.0
            for k in range(1,n+1):
                for indices in combinations(range(n),k):
                    W=sum(weights[j]**2 for j in indices)
                    for i in indices:
                        r=1+alpha*weights[i]*(sum(weights[j] for j in indices if j!=i)-weights[i])/(1+alpha*W)
                        best=max(best,r)
            env=1+alpha/(1+alpha)*(sqrt(n)-1)/2
            assert abs(best-env)<1e-12,(n,alpha,best,env)
            total+=1
        uniform=1+(n-2)/n/2  # alpha=1, normalized weights
        envelope=1+(sqrt(n)-1)/4
        assert (abs(uniform-envelope)<1e-12)==(n==4)
        total+=1
    print('PASS:',total,'finite exact-rational/analytic-envelope assertions')

if __name__=='__main__':run()
