"""Direct numerical checks for the product-measure slender-triangle law.
Numerical experiments corroborate, but cannot prove, the limit theorem.
"""
from __future__ import annotations
import math
import numpy as np
import mpmath as mp

def bernoulli_exact(eps):
    # Y is iid +-1, so only the middle-X vertex at the opposite height
    # from BOTH endpoints can yield an acute triangle (probability 1/4).
    # Then the exact condition on horizontal successive gaps S,T is S*T<4*eps**2.
    mp.mp.dps=65
    d=4*mp.mpf(str(eps))**2
    if d>=mp.mpf('0.25'): return 0.25
    a=(1-mp.sqrt(1-4*d))/2
    b=1-a
    low=lambda x: (x-x*x+x*x*x/3)/2
    middle=lambda x: d*(mp.log(x)-x)+d*d/(2*x)
    return float(mp.mpf(6)/4*((low(a)-low(0))+(middle(b)-middle(a))+(low(mp.mpf(1))-low(b))))

def sample(n, eps, density='uniform', vertical='bernoulli', seed=1):
    rng=np.random.default_rng(seed)
    x=rng.random((n,3)) if density=='uniform' else np.sqrt(rng.random((n,3)))
    if vertical=='bernoulli':
        y=2*rng.integers(0,2,size=(n,3))-1
    elif vertical=='uniform':
        y=(2*rng.random((n,3))-1)*math.sqrt(3)
    elif vertical=='triangular':
        y=(rng.random((n,3))+rng.random((n,3))-1)*math.sqrt(6)
    else: raise ValueError(vertical)
    ix=np.argsort(x,axis=1)
    x=np.take_along_axis(x,ix,axis=1)
    y=np.take_along_axis(y,ix,axis=1)
    s=x[:,1]-x[:,0]; t=x[:,2]-x[:,1]
    a=y[:,1]-y[:,0]; b=y[:,2]-y[:,1]
    e=eps**2
    yes=(s*(s+t)+e*a*(a+b)>0)&(-s*t-e*a*b>0)&(t*(s+t)+e*b*(a+b)>0)
    p=float(np.mean(yes)); se=float(np.sqrt(max(p*(1-p),1/n)/n))
    return p,se

def check():
    # Polynomial exact-integration identity for the vertical shape weight:
    # average over all permutations of (a,b,c) of A*min(A,B)
    # when the middle-X ordinate is an extreme equals (1/6) sum pairwise squared differences.
    import itertools
    for a,b,c in [(-3,1,5),(-1,-1,7),(0,0,0),(-4,-2,-1)]:
        weights=[]
        for y1,y2,y3 in itertools.permutations([a,b,c]):
            A=abs(y2-y1); B=abs(y2-y3)
            ext=(y2-y1)*(y2-y3)>0
            weights.append((A*min(A,B)) if ext else 0)
        lhs=sum(weights)/6
        rhs=((a-b)**2+(a-c)**2+(b-c)**2)/6
        assert abs(lhs-rhs)<1e-10,(lhs,rhs)
    # Bernoulli model: exact finite-width integral converges to coefficient 12.
    targets=[]
    for eps in [1e-3,1e-5,1e-8,1e-12]:
        p=bernoulli_exact(eps)
        ratio=p/(eps*eps*math.log(1/eps))
        targets.append((eps,p,ratio))
    assert abs(targets[-1][2]-12)<0.6,targets
    print('BERNOULLI_EXACT',targets)
    for density,vert,c in [('uniform','bernoulli',12),('uniform','uniform',12),('uniform','triangular',12),('triangular','bernoulli',24)]:
        p,se=sample(800000,0.02,density,vert,seed=13)
        pred=bernoulli_exact(0.02) if density=='uniform' and vert=='bernoulli' else None
        if pred is not None: assert abs(p-pred)<5*se, (p,pred,se)
        assert p>0 and p <0.1,(density,vert,p)
        print('MONTECARLO',density,vert,'estimate',round(p,7),'se',round(se,7),'leading_asymptotic',round(c*0.02**2*math.log(1/0.02),7))
    print('PRODUCT_ACUTENESS_CHECKS_OK')
if __name__=='__main__': check()
