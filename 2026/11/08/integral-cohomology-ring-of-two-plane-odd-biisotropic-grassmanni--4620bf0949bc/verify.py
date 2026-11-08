"""Exact Schur/Pieri lattice checks for two-form biisotropic Grassmannians.
No external packages; a finite consistency check, not a proof for all n.
"""
from math import comb


def schur(a,b):
    assert a >= b >= 0
    return {(a-i,b+i):1 for i in range(a-b+1)}


def multiply(A,B):
    out={}
    for (i,j),v in A.items():
        for (r,s),w in B.items():
            out[(i+r,j+s)]=out.get((i+r,j+s),0)+v*w
    return out


def intersection(n,p,q):
    """Integral on Gr(2,2n+1) of sigma_p sigma_q h^2."""
    f=multiply(multiply(schur(*p),schur(*q)),{(2,0):1,(1,1):2,(0,2):1})
    N=2*n+1
    return f.get((N-2,N-2),0)-f.get((N-1,N-3),0)


def determinant(A):
    # Exact fraction-free elimination (Bareiss).
    A=[list(row) for row in A]
    n=len(A)
    if not n:return 1
    last=1;sgn=1
    for k in range(n-1):
        if A[k][k]==0:
            nxt=next((j for j in range(k+1,n) if A[j][k]),None)
            if nxt is None:return 0
            A[k],A[nxt]=A[nxt],A[k];sgn=-sgn
        p=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=A[i][j]*p-A[i][k]*A[k][j]
                assert numerator%last==0
                A[i][j]=numerator//last
            A[i][k]=0
        last=p
    return sgn*A[-1][-1]


for n in range(2,13):
    M=2*n-1; d=2*M-2;m=M-1
    mids=[(m-i,i) for i in range(n)]
    B=[[intersection(n,p,q) for q in mids] for p in mids]
    expected=[[2 if i==j and i<n-1 else 1 if i==j or abs(i-j)==1 else 0 for j in range(n)] for i in range(n)]
    assert B==expected,(n,B,expected)
    assert determinant(B)==1,(n,determinant(B))
    for r in range(m):
        j=d-r;s=r//2
        alpha=[(M-t,M-2-r+t) for t in range(s+1)]
        beta=[(r-c,c) for c in range(s+1)]
        T=[[intersection(n,p,q) for q in beta] for p in alpha]
        assert all(T[t][c]==0 for t in range(s+1) for c in range(t+1,s+1)),(n,r,T)
        assert all(T[t][t]==1 for t in range(s+1)),(n,r,T)
        assert determinant(T)==1,(n,r,T)
    # degree of Gr(2,2n+1) from the Plucker hyperplane class
    top=comb(2*M,M)-comb(2*M,M-1)
    catalan=comb(2*M,M)//(M+1)
    assert top==catalan
    print('n=%d middle_rank=%d middle_det=1 high_degree_unimodular=OK Plucker_degree=%d'%(n,n,top))
print('ALL_EXACT_SCHUR_PAIRING_CHECKS_OK')
