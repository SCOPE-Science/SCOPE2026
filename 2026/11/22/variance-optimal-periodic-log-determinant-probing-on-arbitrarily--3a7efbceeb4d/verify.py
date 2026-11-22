"""Exact rational checks for positive-resolvent path probing and its interval certificate.
Standard-library only. These finite checks supplement the all-size argument.
"""
from fractions import Fraction as Q
from itertools import product
from math import factorial

def inverse(A):
    n=len(A)
    B=[[Q(A[i][j]) for j in range(n)]+[Q(int(i==j)) for j in range(n)] for i in range(n)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if B[i][j]!=0)
        B[j],B[pivot]=B[pivot],B[j]
        z=B[j][j]
        B[j]=[v/z for v in B[j]]
        for i in range(n):
            if i==j:continue
            z=B[i][j]
            if z:
                B[i]=[a-z*b for a,b in zip(B[i],B[j])]
    return [r[n:] for r in B]

def path(c,q,shift=0):
    n=len(q); A=[[Q(0) for _ in range(n)] for __ in range(n)]
    for i,a in enumerate(q):A[i][i]=Q(a)+Q(shift)
    for i,a in enumerate(c):
        a=Q(a);A[i][i]+=a;A[i+1][i+1]+=a;A[i][i+1]-=a;A[i+1][i]-=a
    return A

def kernel(c,q):
    shifts=(Q(0),Q(2),Q(5))
    weights=(Q(1),Q(3,2),Q(2,3))
    n=len(q); X=[[Q(0) for _ in range(n)] for _ in range(n)]
    for s,w in zip(shifts,weights):
        G=inverse(path(c,q,s))
        for i in range(n):
            for j in range(n):X[i][j]+=w*G[i][j]
    return X

def restricted_growth(n):
    def rec(t,m):
        if len(t)==n:
            yield tuple(t);return
        for a in range(m+2):
            yield from rec(t+[a],max(m,a))
    yield from rec([0],0)

def variance(W,partition):
    n=len(partition)
    return 4*sum((W[i][j] for i in range(n) for j in range(i+1,n) if partition[i]==partition[j]),Q(0))

def run():
    count=0;cases=0
    for n in range(2,9):
        for case in range(2):
            c=[Q(1+((7*i+3*n+case)%4)) for i in range(n-1)]
            q=[Q(1+((5*i+2*n+case)%3)) for i in range(n)]
            K=kernel(c,q)
            W=[[K[i][j]**2 for j in range(n)] for i in range(n)]
            # Check exact nonnegative interval decomposition on the full strict upper triangle.
            D={}
            for a in range(n):
                for b in range(a+1,n):
                    t=W[a][b]
                    if a>0:t-=W[a-1][b]
                    if b+1<n:t-=W[a][b+1]
                    if a>0 and b+1<n:t+=W[a-1][b+1]
                    assert t>0,(n,case,a,b,t)
                    D[(a,b)]=t;count+=1
            for i in range(n):
                for j in range(i+1,n):
                    assert W[i][j]==sum((D[(a,b)] for a in range(i+1) for b in range(j,n)),Q(0))
                    count+=1
            for k in range(1,n+1):
                periodic=tuple(i%k for i in range(n))
                best=variance(W,periodic)
                opt=0
                for parts in restricted_growth(n):
                    if max(parts)+1 !=k:continue
                    val=variance(W,parts)
                    assert val>=best, (n,k,case,parts,val-best)
                    assert (val==best)==(parts==periodic), (n,k,case,parts,val-best)
                    count+=2;opt+=(val==best)
                assert opt==1;count+=1
            cases+=1
    # Sanity check the analytic bilateral-path log coefficients: reconstruct
    # log(spectral symbol) at selected angles from its absolutely convergent Fourier series.
    import math
    mu=Q(1);r=(3-math.sqrt(5))/2
    for theta in (0.0,0.3,1.0,1.7,3.0):
        direct=math.log(3-2*math.cos(theta))
        truncated=-math.log(r)-2*sum(r**d*math.cos(d*theta)/d for d in range(1,130))
        assert abs(direct-truncated)<3e-14
        count+=1
    print(f'PASS {count} exact/Fourier assertions in {cases} rational path cases, n=2..8')
if __name__=='__main__':run()
