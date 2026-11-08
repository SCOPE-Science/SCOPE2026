#!/usr/bin/env python3
"""Exact and floating checks of quadratic-graph Walsh sampling, using only NumPy."""
import itertools
import numpy as np

def binary_matmul(A,B):return (A @ B) % 2

def polar(d, edges):
    A=np.zeros((d,d),dtype=np.int64)
    for i,j in edges:A[i,j]=A[j,i]=1
    return A

def check(d,edges,mask=0,constant=0,check_poly=True):
    n=1<<d; x=np.arange(n,dtype=np.int64)
    Q=np.array([(sum((int(y)>>i&1)*(int(y)>>j&1) for i,j in edges)+(int(y)&mask).bit_count()+constant)%2 for y in x])
    H=np.array([[1-2*((i&j).bit_count()%2) for j in range(n)] for i in range(n)],dtype=np.int64)
    K=H*(1-2*Q[:,None]*Q[None,:]); G=K@K.T; a=(n-1)//3; b=(n+2)//3
    assert a*3+1==n
    assert np.trace(G)==n*n
    # E=(G-nI)/n ; its nonzero eigenspaces have E^2=3/4.
    if check_poly:
        T=G-n*np.eye(n,dtype=np.int64)
        assert np.array_equal(4*(T@T@T),3*n*n*T)
    sv=np.linalg.svd(K.astype(float),compute_uv=False)
    exp=sorted([np.sqrt(n)*(np.sqrt(3)+1)/2]*a+[np.sqrt(n)]*b+[np.sqrt(n)*(np.sqrt(3)-1)/2]*a, reverse=True)
    assert np.max(np.abs(sv-exp))<1.e-8
    return {'d':d,'N':n,'edges':edges,'mask':mask,'constant':constant,'max_singular':float(sv[0]),'min_singular':float(sv[-1]),'a':a,'b':b}

if __name__=='__main__':
    total=0
    for d in (2,4,6):
        match=[(i,i+1) for i in range(0,d,2)]
        complete=list(itertools.combinations(range(d),2))
        for edges in (match,complete):
            for mask in (0,1,(1<<d)-1,((1<<d)-1)//3):
                for constant in (0,1):
                    print(check(d,edges,mask,constant));total+=1
    # Exhaustively examine all 2^(4 choose 2) alternating matrices P, retaining P^2=I.
    d=4
    pairs=list(itertools.combinations(range(d),2)); matched=0
    for subset in itertools.product((0,1),repeat=len(pairs)):
        edges=[p for p,b in zip(pairs,subset) if b]
        P=polar(d,edges)
        if np.array_equal(binary_matmul(P,P),np.eye(d,dtype=np.int64)):
            for mask in (0,1,3,15):
                for constant in (0,1):
                    check(d,edges,mask,constant)
                    total+=1
            matched+=1
    print('QUADRATIC_GRAPH_WALSH_EXACT_PASS', 'cases=',total,'involutive_four_dim_polar_matrices=',matched)
