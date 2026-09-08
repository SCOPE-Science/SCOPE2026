"""Exact verification toolkit: weights, enumerator, MacWilliams, Griesmer, SS-deletion check."""
from itertools import combinations

def weights_of_cols(cols,k):
    from collections import Counter
    c=Counter()
    for u in range(1<<k):
        w=sum(bin(u&cc).count('1')&1 for cc in cols)
        c[w]+=1
    return dict(c)

def minweight(cols,k):
    return min(w for u,w in ((u,sum(bin(u&cc).count('1')&1 for cc in cols)) for u in range(1,1<<k)))

def dual_cols(cols,k):
    # nullspace basis over GF2 of k x n matrix given by columns (k-bit ints)
    n=len(cols)
    # rows: row r has bit j if cols[j] has bit r
    import copy
    M=[[ (cols[j]>>r)&1 for j in range(n)] for r in range(k)]
    # nullspace of M (k x n): solve Mx=0
    # row-reduce
    A=[row[:] for row in M]; piv=[]
    r=0
    where=[-1]*n
    for j in range(n):
        f=None
        for i in range(r,k):
            if A[i][j]: f=i; break
        if f is None: continue
        A[r],A[f]=A[f],A[r]; where[j]=r; r+=1
        for i in range(k):
            if i!=r-1 and A[i][j]:
                for t in range(j,n): A[i][t]^=A[r-1][t]
    basis=[]
    for j in range(n):
        if where[j]==-1:
            v=[0]*n; v[j]=1
            for i in range(k):
                # row i pivot col p: A[i][p]=1; x_p = sum_{free} A[i][f] x_f
                pass
            # reconstruct: for each pivot col p with where[p]=i: v[p]=A[i][j]
            for p in range(n):
                if where[p]!=-1: v[p]=A[where[p]][j]
            basis.append(v)
    return basis  # list of n-bit vectors spanning dual

def dual_weights(cols,k):
    from collections import Counter
    B=dual_cols(cols,k); r=len(B); n=len(cols)
    c=Counter()
    for m in range(1<<r):
        v=[0]*n
        for i in range(r):
            if (m>>i)&1:
                for j in range(n): v[j]^=B[i][j]
        c[sum(v)]+=1
    return dict(c)

def macwilliams_check(A,B,n,k):
    # B'_j = 2^-k sum_i A_i K_j(i); compare with B
    from math import comb
    def K(j,i):
        return sum(((-1)**t)*comb(i,t)*comb(n-i,j-t) for t in range(j+1) if t<=i and j-t<=n-i)
    ok=True; detail={}
    for j in range(n+1):
        pred=sum(A.get(i,0)*K(j,i) for i in range(n+1))/(2**k)
        detail[j]=pred
        if abs(pred-B.get(j,0))>1e-6: ok=False
    return ok,detail

def gries(k,d): return sum((d+(1<<i)-1)//(1<<i) for i in range(k))
def gmax(k,n):
    dm=0
    for d in range(1,n+2):
        if gries(k,d)<=n: dm=d
    return dm
def defect(n,k,d): return n-gries(k,d)

def ss_params(k):
    # all multisets of subspace dims u_i>=1 with total deleted pts < 2^k-1
    res=[]
    maxpts=(1<<k)-1
    def rec(umin,used,ds):
        pts=sum((1<<u)-1 for u in ds)
        if ds: res.append((tuple(ds),maxpts-pts,(1<<(k-1))-sum(1<<(u-1) for u in ds)))
        for u in range(umin, k):
            p=(1<<u)-1
            if used+p<maxpts:
                ds.append(u); rec(u,used+p,ds); ds.pop()
    rec(1,0,[])
    return res
