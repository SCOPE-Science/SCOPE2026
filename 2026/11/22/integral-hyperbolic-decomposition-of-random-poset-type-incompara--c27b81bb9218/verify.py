#!/usr/bin/env python3
"""Exact integer checks for the discrete-interval meet matrix. Python 3 stdlib only."""

def intervals(n):
    return [(a,b) for a in range(n+1) for b in range(a,n+1)]

def intersect(x,y):
    return int(not (x[1]<y[0] or y[1]<x[0]))

def matrix(n):
    t=intervals(n)
    return [[intersect(x,y) for y in t] for x in t]

def transformation(n):
    t=intervals(n)
    pos={interval:i for i,interval in enumerate(t)}
    N=len(t)
    def col(dic):
        c=[0]*N
        for v,k in dic.items():c[pos[v]]+=k
        return c
    f=(0,n)
    cols=[col({f:1})]
    for j in range(n):
        lj=(0,j)
        if j<n-1:
            # u_j-u_{j+1} = e_(0,j) - e_(0,j+1)
            columns={lj:1,(0,j+1):-1}
        else:
            columns={lj:1,f:-1}
        cols.append(col(columns))
        cols.append(col({(j+1,n):1,f:-1}))
    for i,j in t:
        if 1<=i<=j<=n-1:
            cols.append(col({(i,j):1,(0,j):-1,(i,n):-1,f:1}))
    assert len(cols)==N
    return cols

def multiply_form(M, cols):
    N=len(M)
    MC=[[sum(M[i][k]*v[k] for k in range(N)) for i in range(N)] for v in cols]
    return [[sum(c[i]*d[i] for i in range(N)) for d in MC] for c in cols]

def determinant_bareiss(A):
    A=[r[:] for r in A]
    n=len(A)
    if not n:return 1
    sign=1;den=1
    for k in range(n-1):
        if A[k][k]==0:
            t=next((t for t in range(k+1,n) if A[t][k]),None)
            if t is None:return 0
            A[k],A[t]=A[t],A[k];sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numer=A[i][j]*pivot-A[i][k]*A[k][j]
                assert numer%den==0
                A[i][j]=numer//den
            A[i][k]=0
        den=pivot
    return sign*A[-1][-1]

def test(n):
    M=matrix(n)
    cols=transformation(n)
    N=len(M)
    D=multiply_form(M,cols)
    expected=[[0]*N for _ in range(N)]
    expected[0][0]=1
    for j in range(n):
        expected[1+2*j][2+2*j]=-1
        expected[2+2*j][1+2*j]=-1
    assert D==expected,(n,D,expected)
    assert determinant_bareiss([list(r) for r in zip(*cols)]) in (-1,1)
    # Derive the row relation independently on the raw input matrix.
    t=intervals(n)
    for i,j in t:
        if 1<=i<=j<=n-1:
            for w in t:
                assert intersect((i,j),w)==(intersect((0,j),w)+intersect((i,n),w)-intersect((0,n),w))
    return N,2*n+1,n*(n-1)//2

def test_feasibility(n):
    # Check pairwise incomparability iff interval cuts overlap, by constructing
    # the full finite relation with x,y incomparable and verifying transitivity.
    ts=intervals(n);count=0
    for a,b in ts:
        for c,d in ts:
            size=n+2;x=n;y=n+1
            edges=set((i,j) for i in range(n) for j in range(i+1,n))
            for z,lo,up in [(x,a,b),(y,c,d)]:
                edges.update((i,z) for i in range(lo))
                edges.update((z,i) for i in range(up,n))
            transitive=all(not((u,v) in edges and (v,w) in edges) or (u,w) in edges
                           for u in range(size) for v in range(size) for w in range(size))
            assert transitive==bool(intersect((a,b),(c,d)))
            count+=1
    return count

if __name__=='__main__':
    for n in range(0,10):
        N,r,z=test(n)
        print('n=%d types=%d rank=%d zeros=%d integral_congruence=OK'%(n,N,r,z))
    for n in range(0,6):
        print('n=%d poset_pair_check=%d OK'%(n,test_feasibility(n)))
    print('ALL_CHECKS_PASS')
