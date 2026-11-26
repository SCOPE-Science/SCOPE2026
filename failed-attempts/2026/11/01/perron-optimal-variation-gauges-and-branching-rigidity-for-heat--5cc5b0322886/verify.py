#!/usr/bin/env python3
"""Independent numerical/exact checks of weighted tree heat variation identities.
Requires Python 3, NumPy, SciPy. Run: python verify.py
"""
from fractions import Fraction
from itertools import product
import random
import numpy as np
from scipy.linalg import expm,eigh

rng=random.Random(20261025)

def trial(edges,c,w):
    n=len(edges)+1; m=len(edges)
    B=np.zeros((m,n))
    for j,(a,b) in enumerate(edges):B[j,a]=1;B[j,b]=-1
    A=np.zeros((m,m))
    for j in range(m):
        for k in range(j):
            if len(set(edges[j])&set(edges[k])):
                A[j,k]=A[k,j]=1
    C=np.diag(c); W=np.diag(w)
    Q=-(B@B.T)@C
    H=(A-2*np.eye(m))@C
    assert np.max(np.abs(np.abs(Q-np.diag(np.diag(Q)))-(H-np.diag(np.diag(H)))))<1e-13
    mu=max(c[j]*((A@w)[j]/w[j]-2) for j in range(m))
    for j in range(m):
        x=np.zeros(m); x[j]=1
        eps=1e-7
        derivative=(np.sum(w*np.abs(expm(eps*Q)@x))-np.sum(w*np.abs(x)))/(eps*w[j])
        exact=c[j]*((A@w)[j]/w[j]-2)
        assert abs(derivative-exact)<2e-4,(edges,c,w,derivative,exact)
    for t in [0.002,0.03,0.3]:
        P=expm(t*Q)
        norm=max(np.sum(w*np.abs(P[:,j]))/w[j] for j in range(m))
        assert norm<=np.exp(mu*t)+2e-12,(norm,mu,t)
    S=np.diag(np.sqrt(c))@(A-2*np.eye(m))@np.diag(np.sqrt(c))
    e,V=eigh(S)
    rho=float(e[-1]); p=V[:,-1];p*=np.sign(p[0])
    assert np.min(p)>-1e-9
    wopt=np.diag(np.sqrt(c))@p
    assert min(wopt)>0
    muopt=max(c[j]*((A@wopt)[j]/wopt[j]-2) for j in range(m))
    assert abs(muopt-rho)<1e-10,(muopt,rho)
    # Rayleigh numerical: random positive choices cannot improve PF optimum
    for k in range(12):
        ww=np.array([rng.uniform(.3,2.) for _ in range(m)])
        mui=max(c[j]*((A@ww)[j]/ww[j]-2) for j in range(m))
        assert mui>=rho-1e-9
    return rho

def generate_tree(n):
    return [(i,rng.randrange(i)) for i in range(1,n)]

count=0; path=0; claw=0; non=0
for n in range(2,16):
    for rep in range(135):
        E=generate_tree(n)
        cs=np.array([rng.choice([.25,.5,.75,1,1.5,2,3,4]) for _ in E]);
        ws=np.array([rng.choice([.25,.5,.75,1,1.5,2,3,4]) for _ in E])
        rate=trial(E,cs,ws)
        deg=[0]*n
        for u,v in E:deg[u]+=1;deg[v]+=1
        is_path=max(deg)<=2
        is_claw=n==4 and max(deg)==3
        assert (rate < -1e-9)==is_path,(E,rate)
        assert (abs(rate)<1e-9)==is_claw,(E,rate)
        assert (rate>1e-9)==(not is_path and not is_claw),(E,rate)
        if is_path: path+=1
        elif is_claw: claw+=1
        else: non+=1
        count+=1
# Exact rational generator derivative, no floating-point dependency
exact=0
for n in range(2,12):
    for rep in range(80):
        E=generate_tree(n); m=n-1
        c=[Fraction(rng.randrange(1,8),rng.randrange(1,7)) for _ in E]
        w=[Fraction(rng.randrange(1,8),rng.randrange(1,7)) for _ in E]
        for j in range(m):
            actual= -2*c[j]*w[j]+sum(c[j]*w[k] for k in range(m) if k!=j and len(set(E[j])&set(E[k])))
            pred=w[j]*c[j]*(sum(w[k] for k in range(m) if k!=j and len(set(E[j])&set(E[k])))/w[j]-2)
            assert actual==pred
            exact+=1
# Analytic path spectral relation checked independently on nonconstant conductances
for n in range(2,24):
    E=[(i,i+1) for i in range(n-1)]
    c=np.array([rng.uniform(.25,3.) for _ in E]); w=np.ones(n-1)
    M=np.zeros((n,n))
    for (u,v),a in zip(E,c):M[u,u]+=a;M[v,v]+=a;M[u,v]-=a;M[v,u]-=a
    vals=eigh(M,eigvals_only=True)
    B=np.zeros((n-1,n))
    for i in range(n-1):B[i,i]=1;B[i,i+1]=-1
    A=np.zeros((n-1,n-1))
    for i in range(n-2):A[i,i+1]=A[i+1,i]=1
    S=np.diag(np.sqrt(c))@(A-2*np.eye(n-1))@np.diag(np.sqrt(c))
    rate=eigh(S,eigvals_only=True)[-1]
    assert abs(-rate-vals[1])<1e-10
print(f'PASS: {count} weighted-tree Perron/log-norm cases ({path} path, {claw} claw, {non} other); {exact} rational column-derivative checks; 23 weighted-path spectral-gap cross-checks.')
