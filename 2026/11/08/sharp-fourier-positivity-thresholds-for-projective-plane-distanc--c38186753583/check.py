#!/usr/bin/env python3
"""Independent finite-field construction and spectral replay for projective-plane metric distances."""
from itertools import product
import numpy as np
from scipy.optimize import brentq
from collections import deque


def canonical(v,p):
    for x in v:
        if x%p:
            a=pow(int(x),-1,p)
            return tuple((int(y)*a)%p for y in v)
    raise ValueError('zero')


def run(p):
    P=sorted({canonical(v,p) for v in product(range(p),repeat=3) if any(v)})
    v=len(P)
    assert v==p*p+p+1
    B=np.fromiter((int(sum(a*b for a,b in zip(point,line))%p==0) for point in P for line in P),dtype=np.int64).reshape((v,v))
    assert np.array_equal(B@B.T,p*np.eye(v,dtype=np.int64)+np.ones((v,v),dtype=np.int64))
    assert np.all(B.sum(axis=0)==p+1)
    adj=np.block([[np.zeros((v,v),dtype=int),B],[B.T,np.zeros((v,v),dtype=int)]])
    dist=np.zeros((2*v,2*v),dtype=int)
    for x in range(2*v):
        row=[-1]*(2*v);row[x]=0;Q=deque([x])
        while Q:
            t=Q.popleft()
            for w in np.flatnonzero(adj[t]):
                if row[w]==-1:
                    row[w]=row[t]+1;Q.append(w)
        assert all(z>=0 for z in row)
        dist[x]=row
    beta=brentq(lambda a:3**a-1-2**a/(p**0.5),0.00000001,1)
    # Independent eigenspectrum check, starting with unnormalized shortest path distance.
    for a in [0.05,0.3,beta,beta+0.06,0.95]:
        D=dist.astype(float)**a
        eig=np.linalg.eigvalsh(D)
        pos=(v-1)*2**a+(p+1)+p*p*3**a
        sign=(v-1)*2**a-(p+1)-p*p*3**a
        minus=-2**a-(p**0.5)*(3**a-1)
        plus=-2**a+(p**0.5)*(3**a-1)
        expected=sorted([pos,sign]+[minus]*(v-1)+[plus]*(v-1))
        assert np.max(np.abs(eig-expected))<1e-9,(p,a,eig,expected)
        centered=np.eye(2*v)-np.ones((2*v,2*v))/(2*v)
        ceig=np.linalg.eigvalsh(centered@D@centered)
        # Numerically 0 one constant mode, and v-1 extra at the boundary.
        if a < beta-1e-8: assert np.count_nonzero(ceig > 1e-8)==0,(p,a,ceig)
        if a > beta+1e-8: assert np.count_nonzero(ceig > 1e-8)==v-1,(p,a,ceig)
        if abs(a-beta)<1e-8:
            assert np.count_nonzero(ceig<-1e-8)==v
            assert np.count_nonzero(abs(ceig)<1e-8)==v
    print('q=',p,'v=',v,'beta=',format(beta,'.15f'),'endpoint_embedding_dim=',v,'CHECK_OK')

if __name__=='__main__':
    for q in (2,3,5,7):run(q)
    print('ALL_PROJECTIVE_PLANE_NEGATIVE_TYPE_CHECKS_OK')
