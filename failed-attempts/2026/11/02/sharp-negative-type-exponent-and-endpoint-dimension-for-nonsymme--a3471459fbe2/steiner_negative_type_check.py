"""Finite diagnostics for negative type of incidence metrics of Steiner 2-designs.
Run: python steiner_negative_type_check.py. Requires NumPy >= 1.24.
The checker constructs incidence structures and graph distances independently.
"""
from itertools import combinations,product
from collections import deque
from math import log
import numpy as np


def affine(q):
    pts=list(product(range(q),repeat=2))
    blocks=[]
    for slope in range(q):
        for intercept in range(q):
            blocks.append({i for i,(x,y) in enumerate(pts) if y==(slope*x+intercept)%q})
    for x0 in range(q):
        blocks.append({i for i,(x,y) in enumerate(pts) if x==x0})
    return len(pts),q,blocks


def binary_steiner(m):
    pts=list(range(1,2**m))
    index={x:i for i,x in enumerate(pts)}
    seen=set()
    for a,b in combinations(pts,2):
        c=a^b
        seen.add(tuple(sorted((index[a],index[b],index[c]))))
    return len(pts),3,[set(triple) for triple in sorted(seen)]


def verify_design(v,k,blocks):
    b=len(blocks)
    N=np.zeros((v,b),dtype=np.int64)
    for j,B in enumerate(blocks):
        assert len(B)==k
        for i in B:N[i,j]=1
    r=(v-1)//(k-1)
    assert r*(k-1)==v-1 and b*k==v*r and b>v
    assert np.array_equal(N@N.T,(r-1)*np.eye(v,dtype=np.int64)+np.ones((v,v),dtype=np.int64))
    return N,r


def graph_distances(N):
    v,b=N.shape
    n=v+b
    adj=np.zeros((n,n),dtype=np.int64)
    adj[:v,v:]=N;adj[v:,:v]=N.T
    d=np.full((n,n),1000,dtype=np.int64)
    for source in range(n):
        d[source,source]=0
        fringe=deque([source])
        while fringe:
            x=fringe.popleft()
            for y in np.flatnonzero(adj[x]):
                if d[source,y]==1000:
                    d[source,y]=d[source,x]+1
                    fringe.append(y)
    assert int(np.max(d))==4
    # Exact combinatorial distance classes.
    test=np.zeros((n,n),dtype=np.int64)
    test[:v,:v]=2*(np.ones((v,v),dtype=np.int64)-np.eye(v,dtype=np.int64))
    test[:v,v:]=3-2*N; test[v:,:v]=3-2*N.T
    overlap=N.T@N
    test[v:,v:]=2*(overlap-np.diag(np.diag(overlap)))+4*(1-(overlap>0).astype(np.int64))
    np.fill_diagonal(test,0)
    assert np.array_equal(test,d)
    return d


def main():
    checked=0
    for label,(v,k,blocks) in [('affine3',affine(3)),('affine5',affine(5)),
                                ('binarySTS15',binary_steiner(4)),('binarySTS31',binary_steiner(5))]:
        N,r=verify_design(v,k,blocks)
        d=graph_distances(N)
        b=len(blocks);s=log(k/(k-1),2)
        center=np.eye(v+b)-np.ones((v+b,v+b))/(v+b)
        for p in [0.1*s,s,1.01*s]:
            dp=d.astype(float)**p
            np.fill_diagonal(dp,0)
            gram=-0.5*(center@dp@center)
            eigen=np.linalg.eigvalsh(gram)
            if p <s-1e-12:
                assert eigen[1]>1e-8,(label,p,eigen[:4]);rank=v+b-1
            elif abs(p-s)<1e-12:
                assert eigen[0]>-5e-9,(label,eigen[:4])
                rank=int(np.sum(eigen>1e-8))
                assert rank==2*v-1,(label,rank,2*v-1)
                assert np.sum(abs(eigen)<1e-8)==1+b-v
            else:assert eigen[0]<-1e-8,(label,p,eigen[:4])
            checked+=1
        print(label,'v',v,'k',k,'b',b,'critical_p',round(s,12),
              'endpoint_dim',2*v-1,'nullity',b-v)
    print('STEINER_NEGATIVE_TYPE_CHECK_OK', 'designs=4','powered_distance_cases='+str(checked))

if __name__=='__main__':main()
