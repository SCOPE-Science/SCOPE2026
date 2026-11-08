#!/usr/bin/env python3
"""Exact algebra and deterministic numerical checks for curvature-frame risk."""
from fractions import Fraction
import math
import sympy as S
import numpy as np

n, tr, norm2 = S.symbols('n tr norm2', real=True)
assert S.simplify((n*(n+2)/2)**2 - 2*(n*(n+2)/2)*(n/2)+n*(n/2)**2 - n**3*(n+3)/4)==0
Eq2 = (tr**2+2*norm2)/(n*(n+2))
Eqq = S.factor(((tr**2/n)-Eq2)/(n-1))
assert S.simplify(Eqq - ((n+1)*tr**2-2*norm2)/(n*(n-1)*(n+2))) == 0
cross = -n**2*(n+4)/4*Eqq - norm2
claimed = ((-n*n+2*n+4)*norm2/(2*(n-1)*(n+2))
          - n*(n+1)*(n+4)*tr**2/(4*(n-1)*(n+2)))
assert S.simplify(cross-claimed)==0
single = S.factor(n**3*(n+3)/4 * Eq2 - norm2)
assert S.simplify(single - (n*n*(n+3)*(tr**2+2*norm2)/(4*(n+2))-norm2))==0
for dim in range(2,100):
    cS = S.factor(claimed.subs({n:dim,tr:0,norm2:1}))
    if dim in (2,3): assert cS > 0
    else: assert cS < 0
for dim, threshold in [(2,S.Rational(2,9)),(3,S.Rational(1,42))]:
    a=S.simplify(claimed.subs({n:dim,tr:S.symbols('q'),norm2:1}))
    q=S.symbols('q')
    assert S.simplify(a.subs(q*q,threshold))==0
    assert S.factor(a.subs(q,0))>0
assert S.simplify(1 + claimed.subs({n:2,tr:0,norm2:1})/single.subs({n:2,tr:0,norm2:1})-S.Rational(4,3))==0
for k, ratio in [(2,S.Rational(89,88)),(3,S.Rational(45,44))]:
    assert S.simplify(1+(k-1)*claimed.subs({n:3,tr:0,norm2:1})/single.subs({n:3,tr:0,norm2:1})-ratio)==0

# Independent deterministic quadrature on S^1 for n=2, k=2.
N=32768
angles=2*math.pi*(np.arange(N)+0.31)/N
u=np.stack([np.cos(angles),np.sin(angles)],axis=1)
v=np.stack([-u[:,1],u[:,0]],axis=1)
for A in [np.diag([1.,-1.]),np.eye(2),np.diag([2.,-1.]),np.diag([2.,3.])]:
    def M(w):
        q=np.einsum('ni,ij,nj->n',w,A,w)
        return (q[:,None,None]*(4*w[:,:,None]*w[:,None,:]-np.eye(2)[None,:,:]))
    mu=M(u); mv=M(v)
    assert np.allclose(mu.mean(axis=0),A,atol=1e-11)
    ortherr=((mu+mv)/2-A)**2
    orth=float(ortherr.sum(axis=(1,2)).mean())
    iid=float(((mu-A)**2).sum(axis=(1,2)).mean()/2)
    s=float(np.sum(A*A)); t=float(np.trace(A))
    c=float(claimed.subs({n:2,tr:t,norm2:s}))
    assert abs((orth-iid)-c/2)<1e-10,(orth,iid,c)
    print('n=2, k=2, diagA=', np.diag(A).tolist(),'iid=',round(iid,12),'orth=',round(orth,12),'difference=',round(orth-iid,12))

# A distinct Monte Carlo sanity check in dimensions 3 and 4 (not a proof).
rng=np.random.default_rng(1729)
for dim in (3,4):
    A=np.diag([1.,-1.]+[0.]*(dim-2))
    k=dim
    sumrisk=0.0
    nsamp=30000
    for _ in range(nsamp):
        G=rng.standard_normal((dim,dim))
        Q,R=np.linalg.qr(G)
        Q=Q*np.sign(np.diag(R))[None,:]
        q=np.einsum('ik,ij,jk->k',Q,A,Q)
        O=(dim/(2*k))*((dim+2)*(Q*q[None,:])@Q.T - np.sum(q)*np.eye(dim))
        sumrisk+=float(np.sum((O-A)**2))
    empirical=sumrisk/nsamp
    spec={n:dim,tr:0,norm2:2}
    exact=float((single+(k-1)*claimed).subs(spec)/k)
    assert abs(empirical-exact)<0.075,(dim,empirical,exact)
    print('n=',dim,'k=',k,'orth-risk-MC=',round(empirical,6),'orth-risk-exact=',round(exact,6))
print('PASS: exact identities, thresholds, extremal ratios, planar quadrature, and dimensional sanity checks')
