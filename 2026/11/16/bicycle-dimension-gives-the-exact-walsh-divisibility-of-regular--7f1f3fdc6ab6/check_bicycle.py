#!/usr/bin/env python3
"""Exact finite checks of bicycle-dimension bounds for signed regular-matroid basis sums."""
from itertools import combinations
from math import gcd
import random


def gf2rank(rows,cols):
    b=[]
    for row in rows:
        x=0
        for j,a in enumerate(row):
            if a%2:x|=1<<j
        b.append(x)
    p=0
    for j in range(cols):
        q=next((i for i in range(p,len(b)) if b[i]&(1<<j)),None)
        if q is None:continue
        b[p],b[q]=b[q],b[p]
        for i in range(len(b)):
            if i!=p and b[i]&(1<<j):b[i]^=b[p]
        p+=1
    return p


def det_bareiss(mat):
    A=[list(x) for x in mat]
    n=len(A)
    if n==0:return 1
    sg=1; prev=1
    for k in range(n-1):
        if A[k][k]==0:
            q=next((i for i in range(k+1,n) if A[i][k]),None)
            if q is None:return 0
            A[q],A[k]=A[k],A[q];sg=-sg
        piv=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                val=A[i][j]*piv-A[i][k]*A[k][j]
                assert val%prev==0
                A[i][j]=val//prev
        for i in range(k+1,n):A[i][k]=0
        prev=piv
    return sg*A[n-1][n-1]


def fwht(a):
    a=a[:];h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j]=x+y;a[j+h]=x-y
        h*=2
    return a


def matmul_aat(B):
    return [[sum(x*y for x,y in zip(u,v)) for v in B] for u in B]


def graph_matrices(n,edges):
    B=[[0]*len(edges) for _ in range(n-1)]
    for j,(u,v) in enumerate(edges):
        if u<n-1:B[u][j]=1
        if v<n-1:B[v][j]=-1
    return B


def all_basis_vectors(B):
    r=len(B);m=len(B[0]) if r else 0
    out=[]
    for C in combinations(range(m),r):
        if abs(det_bareiss([[row[j] for j in C] for row in B]))==1:
            out.append(sum(1<<j for j in C))
    return out


def verify(B):
    r=len(B);m=len(B[0])
    assert gf2rank(B,m)==r
    S=matmul_aat(B)
    k=r-gf2rank(S,r)
    f=[0]*(1<<m)
    bases=all_basis_vectors(B)
    for b in bases:f[b]=1
    W=fwht(f)
    g=0
    for w in W:g=gcd(g,abs(w))
    assert g==(1<<k),(k,g)
    return k,g,len(bases),sum(w==0 for w in W),min(abs(w) for w in W if w)


def exact_signed_det(B,bits):
    r=len(B);m=len(B[0]);L=[[0]*r for _ in range(r)]
    for j in range(m):
        w= -1 if (bits>>j)&1 else 1
        for u in range(r):
            if B[u][j]:
                for v in range(r):
                    if B[v][j]:L[u][v]+=w*B[u][j]*B[v][j]
    return det_bareiss(L)


def main():
    checked=0
    for n in range(2,6):
        all_edges=list(combinations(range(n),2));tot=1<<len(all_edges)
        for x in range(tot):
            edges=[e for j,e in enumerate(all_edges) if x>>j&1]
            if len(edges)<n-1:continue
            B=graph_matrices(n,edges)
            if gf2rank(B,len(edges))!=n-1:continue
            verify(B);checked+=1
    print('EXHAUSTIVE_CONNECTED_SIMPLE_GRAPHS_PASS count=',checked)
    for d in range(1,4):
        n=1<<d
        edges=[(v,v^(1<<j)) for v in range(n) for j in range(d) if v<v^(1<<j)]
        B=graph_matrices(n,edges)
        k,g,bases,zeros,gap=verify(B)
        assert k==(1<<(d-1))-1
        print(f'HYPERCUBE_Q{d}_PASS edges={len(edges)} k={k} gcd={g} bases={bases} zeros={zeros} gap={gap}')
    d=4;n=1<<d
    edges=[(v,v^(1<<j)) for v in range(n) for j in range(d) if v<v^(1<<j)]
    B=graph_matrices(n,edges)
    k=n-1-gf2rank(matmul_aat(B),n-1)
    assert k==7
    rng=random.Random(61234)
    for trial in range(200):
        bits=rng.getrandbits(len(edges))
        val=exact_signed_det(B,bits)
        if val and val%(1<<(k+1))==(1<<k):
            print(f'HYPERCUBE_Q4_SHARP_PASS k={k} witness=0x{bits:08x} determinant={val} trials={trial+1}')
            break
    else:raise AssertionError('could not find Q4 witness')
    # Cographic K4 from fundamental cut/cycle dual representation
    E=list(combinations(range(4),2))
    A=graph_matrices(4,E)
    # First choose tree edges (01,02,03), yielding first three unit columns.
    assert E[:3]==[(0,1),(0,2),(0,3)]
    # The deleted vertex is 3, so the first three columns are not the identity.
    # Construct a unimodular pivot basis from any spanning tree of the 6 columns.
    idx=next(t for t in combinations(range(6),3)
             if abs(det_bareiss([[row[j] for j in t] for row in A]))==1)
    rest=[j for j in range(6) if j not in idx]
    def inv3(M):
        D=det_bareiss(M);assert abs(D)==1
        cof=[[(-1)**(i+j)*det_bareiss([row[:j]+row[j+1:] for h,row in enumerate(M) if h!=i]) for j in range(3)] for i in range(3)]
        return [[cof[j][i]//D for j in range(3)] for i in range(3)]
    AA=[[row[j] for j in idx] for row in A];AAi=inv3(AA)
    X=[[sum(AAi[i][t]*A[t][j] for t in range(3)) for j in rest] for i in range(3)]
    dual=[[-X[t][i] for t in range(3)]+[int(i==j) for j in range(3)] for i in range(3)]
    assert verify(dual)[1]>=1
    print('COGRAPHIC_K4_DUAL_PASS',verify(dual))
    print('REGULAR_MATROID_BICYCLE_WALSH_CHECK_PASS')
if __name__=='__main__':main()
