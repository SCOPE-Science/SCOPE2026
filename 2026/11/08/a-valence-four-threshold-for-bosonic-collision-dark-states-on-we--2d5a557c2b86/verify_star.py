#!/usr/bin/env python3
"""Exact finite checks for a two-boson collision-loss model on weighted stars.
Uses integer two-body evolution in symmetric coordinate amplitudes, which
is independent of the incidence-matrix derivation used for the theorem.
No numerical tolerance or finite truncation in the Krylov calculation.
"""
from itertools import combinations
import sympy as S

def symmetric_walk_on_star(weights):
    n=len(weights)+1
    A=S.zeros(n)
    for k,w in enumerate(weights,1):
        A[0,k]=A[k,0]=S.Integer(w)
    pairs=[(a,b) for a in range(n) for b in range(a,n)]
    where={pair:k for k,pair in enumerate(pairs)}
    H=S.zeros(len(pairs))
    for col,(a,b) in enumerate(pairs):
        X=S.zeros(n)
        X[a,b]=X[b,a]=1
        Y=A*X+X*A
        for row,(i,j) in enumerate(pairs):
            H[row,col]=Y[i,j]
    C=S.zeros(n,len(pairs))
    for i in range(n): C[i,where[(i,i)]]=1
    return H,C

def dark_by_observability(weights):
    H,C=symmetric_walk_on_star(weights)
    # The single-particle star has spectrum {0, +/-sqrt(W)}.
    # Two-particle Kronecker sums have at most five eigenvalues;
    # powers 0..4 give the entire exact unobservable subspace.
    M=C
    P=C
    for k in range(1,5):
        P=P*H
        M=M.col_join(P)
    return H.cols-M.rank()

def incidence_projector(weights):
    q=len(weights)
    edges=list(combinations(range(q),2))
    B=S.zeros(q,len(edges))
    for a,(i,j) in enumerate(edges):
        B[i,a]=weights[j]
        B[j,a]=weights[i]
    G=B*B.T
    assert G.det()!=0 if q>=3 else True
    if q>=3:
        P=S.eye(len(edges))-B.T*G.inv()*B
        assert B*P==S.zeros(q,len(edges))
        assert P*P==P
        assert P==P.T
        assert P.trace()==S.Rational(q*(q-3),2)
        return B,G,P
    return B,G,None

samples={
    2:[[1,2]],
    3:[[1,1,1],[1,2,3]],
    4:[[1]*4,[1,2,3,4],[2,4,3,7]],
    5:[[1]*5,[1,2,3,4,5]],
    6:[[1]*6,[1,2,1,3,5,2]],
    7:[[1]*7,[1,2,3,2,1,4,5]],
    8:[[1]*8],
}
for q,cases in samples.items():
    for ws in cases:
        d=dark_by_observability(ws)
        expect=max(0,q*(q-3)//2)
        assert d==expect, (q,ws,d,expect)
        B,G,P=incidence_projector(ws)
        if P is not None:
            assert P.rank()==d
            if len(set(ws))==1:
                for a in range(P.rows):
                    assert P[a,a]==S.Rational(q-3,q-1)
        print('EXACT_OK',q,','.join(map(str,ws)),'dark',d,flush=True)
print('STAR_EXACT_ALL_OK')
