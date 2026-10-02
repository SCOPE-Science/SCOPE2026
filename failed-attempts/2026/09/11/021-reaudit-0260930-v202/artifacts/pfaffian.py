"""Exact Pfaffian tools: Bareiss determinant + combinatorial matching Pfaffian."""
from itertools import combinations

def bareiss_det(M):
    n=len(M)
    if n==0: return 1
    A=[row[:] for row in M]
    prev=1
    for k in range(n-1):
        # partial pivot (exact): find nonzero
        if A[k][k]==0:
            piv=None
            for i in range(k+1,n):
                if A[i][k]!=0:
                    piv=i; break
            if piv is None: return 0
            A[k],A[piv]=A[piv],A[k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*A[k][k]-A[i][k]*A[k][j])//prev
            A[i][k]=0
        prev=A[k][k]
        if prev==0: return 0
    return A[n-1][n-1]

def skew_from_upper(B):
    n=len(B)
    A=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            A[i][j]=B[i][j]; A[j][i]=-B[i][j]
    return A

def pf_matchings(B):
    """Direct matching-sum Pfaffian of upper-triangular dict/matrix B (n even)."""
    n=len(B)
    if n==0: return 1
    assert n%2==0
    def rec(remaining):
        if not remaining: return 1
        i=remaining[0]
        tot=0
        for k in range(1,len(remaining)):
            j=remaining[k]
            # sign = (-1)^{k-1}? pairing i (first) with k-th next: positions between
            s=1 if (k-1)%2==0 else -1
            rest=remaining[1:k]+remaining[k+1:]
            tot+=s*B[i][j]*rec(rest)
        return tot
    return rec(list(range(n)))

def pf_via_det(B):
    import math
    n=len(B)
    if n==0: return 1
    A=skew_from_upper(B)
    d=bareiss_det(A)
    if d<0: d=-d  # det(A)=Pf^2>=0; bareiss pivot swaps drop sign: use abs
    assert isinstance(d,int), d
    r=math.isqrt(d)
    assert r*r==d, d
    m=pf_matchings(B)
    assert m*m==d, (m,d)
    return m
def numDSASM_entry(i,j):
    from math import comb
    tot=0
    for k in range(0,i+1):
        c=(3-(1 if k==0 else 0))
        tot+=c*(comb(i+j-2*k-1,i-k)-comb(i+j-2*k-1,j-k)) if (i+j-2*k-1)>=0 else 0
    return tot

def BFK_total(n):
    idx=list(range(1 if n%2 else 0, n))
    m=len(idx)
    B=[[0]*m for _ in range(m)]
    for a,i in enumerate(idx):
        for b,j in enumerate(idx):
            if b>a: B[a][b]=numDSASM_entry(i,j)
    return B

for n in range(1,11):
    B=BFK_total(n)
    print(n, "idxsize", len(B), "match-pf", pf_matchings(B))
