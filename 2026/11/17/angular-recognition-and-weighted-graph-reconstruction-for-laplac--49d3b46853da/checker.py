"""Numerical stress tests for the Laplacian-simplex angular inverse theorem.
Use: python checker.py. Finite tests corroborate, not certify, all-dimensional theorem.
"""
import itertools
import math
import numpy as np


def pinv_psd(A, threshold=1.e-7):
    lam,U=np.linalg.eigh((A+A.T)/2)
    lam2=np.array([1/t if t>threshold else 0 for t in lam])
    return (U*lam2)@U.T

def sqrt_psd(A, threshold=1.e-7):
    lam,U=np.linalg.eigh((A+A.T)/2)
    return (U*np.sqrt(np.where(lam>threshold,lam,0)))@U.T

def recovered(C):
    lam,U=np.linalg.eigh((C+C.T)/2)
    assert lam[1]>1.e-9,lam
    a=U[:,0]
    if np.mean(a)<0:a=-a
    assert min(a)>1.e-9
    # normalization forces sum(a_i)=n, an arbitrary scale for weight recovery
    a=a*len(a)/sum(a)
    K=(a[:,None]*C)*a[None,:]
    return sqrt_psd(pinv_psd(K))

def graph_lap(n, edges, weights):
    L=np.zeros((n,n))
    for (i,j),w in zip(edges,weights):
        L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
    return L

def graph_connected(n, edges):
    adj=[[] for _ in range(n)]
    for i,j in edges: adj[i].append(j);adj[j].append(i)
    seen={0}; stack=[0]
    while stack:
        v=stack.pop()
        for w in adj[v]:
            if w not in seen:seen.add(w);stack.append(w)
    return len(seen)==n

def facet_normal_cos(L):
    Q=pinv_psd(L)
    H=Q@Q
    d=np.sqrt(np.diag(H))
    return H/d[:,None]/d[None,:]

count=0; weighted=0
for n in range(3,6):
    all_edges=list(itertools.combinations(range(n),2))
    for mask in range(1,2**len(all_edges)):
        edges=[e for k,e in enumerate(all_edges) if (mask>>k)&1]
        if not graph_connected(n,edges):continue
        L=graph_lap(n,edges,[1.]*len(edges))
        C=facet_normal_cos(L)
        R=recovered(C)
        s=(R*L).sum()/(L*L).sum()
        assert np.max(abs(R-s*L)) <1.e-6,(n,edges,R-s*L)
        assert np.max(abs(facet_normal_cos(R)-C))<1.e-6
        nonzero=[-R[i,j] for i,j in edges]
        assert max(nonzero)-min(nonzero)<1.e-6
        for i,j in all_edges:
            if (i,j) not in edges: assert abs(R[i,j])<1.e-6
        count+=1
        # Weighted distinct rational values and global rescale
        ws=[float(1+((k+2*n)%5))/3 for k in range(len(edges))]
        LW=graph_lap(n,edges,ws)
        CW=facet_normal_cos(LW)
        RW=recovered(CW)
        sw=(RW*LW).sum()/(LW*LW).sum()
        assert np.max(abs(RW-sw*LW)) <1.e-6
        assert np.max(abs(facet_normal_cos(RW)-CW))<1.e-6
        assert np.max(abs(facet_normal_cos(LW*7)-CW))<1.e-6
        weighted+=1
print(f'GRAPH_LAPLACIAN_ANGULAR_INVERSE_PASS connected_simple={count} rational_weighted={weighted}')
assert count==770 and weighted==770
# Independent matrix-angle test from a simplex not in the graph Laplacian class
M=np.array([[3.,1.,-4.],[1.,3.,-4.],[-4.,-4.,8.]])
assert np.max(abs(M@np.ones(3)))<1.e-9
C=facet_normal_cos(M) # M is PSD centered but has positive offdiagonal: not a graph Laplacian
assert recovered(C)[0,1]>1.e-6
print('NON_GRAPH_POSITIVE_OFFDIAGONAL_REJECT_PASS')
print('CHECKER_PASS')
