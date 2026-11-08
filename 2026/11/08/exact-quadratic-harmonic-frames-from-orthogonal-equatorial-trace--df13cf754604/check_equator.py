"""Numerical independent matrix verification for quadratic equatorial restriction."""
from __future__ import annotations
from math import comb
import numpy as np
from scipy.linalg import eigh

TOL=5e-11
checks=0

def ck(ok, desc):
    global checks
    checks+=1
    if not ok: raise AssertionError(f'check {checks}: {desc}')

def basis(d):
    out=[]
    for i in range(d-1):
        M=np.zeros((d,d)); M[i,i]=1; M[d-1,d-1]=-1; out.append(M)
    for i in range(d):
        for j in range(i+1,d):
            M=np.zeros((d,d)); M[i,j]=1; M[j,i]=1; out.append(M)
    return out

def grams(d,k,weights=None):
    Bs=basis(d); r=len(Bs)
    weights=(np.ones(k)/k if weights is None else np.asarray(weights,dtype=float))
    G=np.empty((r,r)); H=np.empty((r,r))
    for p,A in enumerate(Bs):
        for q,B in enumerate(Bs):
            G[p,q]=2*np.sum(A*B)/(d*(d+2))
            val=0.
            for i,w in enumerate(weights):
                a=np.delete(np.delete(A,i,axis=0),i,axis=1)
                b=np.delete(np.delete(B,i,axis=0),i,axis=1)
                val+=w*(2*np.sum(a*b)+np.trace(a)*np.trace(b))/((d-1)*(d+1))
            H[p,q]=val
    return G,H

def spectrum(d,k):
    m=d-k; K=d*(d+2)/(2*k*(d*d-1))
    out=[]
    for s,num in ((2,comb(k,2)),(1,k*m),(0,comb(m,2))):
        out.extend([K*(2*k-2*s)]*num)
    if k>=2: out.extend([K*(2*k-1)]*(k-1))
    if m>=2: out.extend([K*2*k]*(m-1))
    if k and m: out.append(K*(2*k-m/d))
    return np.sort(out)

def direct_4th_moment_norm(d,A):
    tr=np.trace(A)
    return (2*np.sum(A*A)+tr*tr)/(d*(d+2))

for d in range(3,12):
    for k in range(1,d+1):
        G,H=grams(d,k)
        vals=eigh(H,G,eigvals_only=True)
        pred=spectrum(d,k)
        ck(len(vals)==len(pred),f'd={d}, k={k} multiplicity')
        ck(np.max(np.abs(vals-pred))<TOL,f'd={d}, k={k} spectrum')
        ck((vals[0]>1e-9)==(k>=3),f'd={d}, k={k} threshold')
        if k>=3:
            C=d*(d+2)/(d*d-1)
            ck(abs(vals[0]-C*(k-2)/k)<TOL,f'd={d}, k={k} lower frame bound')
            ratio=vals[-1]/vals[0]
            if d>=k+2: opt=k/(k-2)
            elif d==k+1: opt=(2*k-1/d)/(2*k-4)
            else: opt=(2*k-1)/(2*k-4)
            ck(abs(ratio-opt)<TOL,f'd={d}, k={k} sharp ratio')
            if d>=5 and k==3: ck(abs(ratio-3)<TOL,'three-equator dimensional uniformity')

rng=np.random.default_rng(1120)
for d,k in [(3,3),(4,3),(5,3),(6,4),(8,5)]:
    G,H0=grams(d,k)
    lower=eigh(H0,G,eigvals_only=True)[0]
    upper=eigh(H0,G,eigvals_only=True)[-1]
    for t in range(24):
        w=rng.dirichlet(np.ones(k))
        _,H=grams(d,k,w)
        vals=eigh(H,G,eigvals_only=True)
        ck(vals[0]<lower+TOL,f'weighted max-min d={d} k={k}')
        ck(vals[-1]/vals[0]+TOL>=upper/lower,f'weighted min condition d={d} k={k}')
        C=d*(d+2)/(d*d-1)
        ck(vals[0] <= C*(1-np.sort(w)[-2:].sum())+TOL, 'two-axis test')

for d in range(3,9):
    for t in range(4):
        M=rng.normal(size=(d,d));M=(M+M.T)/2;M-=np.eye(d)*(np.trace(M)/d)
        points=rng.normal(size=(120000,d));points/=np.linalg.norm(points,axis=1)[:,None]
        samples=np.einsum('ni,ij,nj->n',points,M,points)
        measured=np.mean(samples**2)
        target=direct_4th_moment_norm(d,M)
        ck(abs(measured-target)<.075*target,f'full-sphere fourth moment d={d}')

print('EQUATOR_QUADRATIC_CHECKS_PASS',checks)
