#!/usr/bin/env python3
"""Exact standalone checks for crown-graph controllability and actuator reliability."""
from fractions import Fraction
from itertools import combinations
from math import comb


def laplacian(n):
    A = [[0] * (2 * n) for _ in range(2 * n)]
    for i in range(n):
        A[i][i] = A[n+i][n+i] = n - 1
        for j in range(n):
            if i != j:
                A[i][n+j] = A[n+j][i] = -1
    return A


def matvec(M, x):
    return [sum(a*b for a,b in zip(row,x)) for row in M]


def rank_mod(rows, p=1000000007):
    if not rows: return 0
    B=[[x % p for x in row] for row in rows]
    nr=len(B); nc=len(B[0]); rank=0
    for c in range(nc):
        k=next((r for r in range(rank,nr) if B[r][c]),None)
        if k is None: continue
        B[rank],B[k]=B[k],B[rank]
        q=pow(B[rank][c],-1,p)
        B[rank][c:]=[(x*q)%p for x in B[rank][c:]]
        for r in range(rank+1,nr):
            if B[r][c]:
                q=B[r][c]
                B[r][c:]=[(x-q*y)%p for x,y in zip(B[r][c:],B[rank][c:])]
        rank+=1
        if rank==nr:break
    return rank


def rank_kalman(n, chosen):
    N=2*n
    if not chosen:return 0
    L=laplacian(n)
    columns=[]
    for v in chosen:
        z=[int(i==v) for i in range(N)]
        for _ in range(N):
            columns.append(z)
            z=matvec(L,z)
    return rank_mod([list(x) for x in zip(*columns)])


def covered_indices(n,S):
    return len({i % n for i in S})


def eigbasis(n):
    N=2*n
    one=[1]*n
    minus=[1]*n+[-1]*n
    plus=[1]*(2*n)
    groups={0:[plus],2*n-2:[minus],n:[],n-2:[]}
    for i in range(n-1):
        v=[int(j==i)-int(j==n-1) for j in range(n)]
        groups[n].append(v+v)
        groups[n-2].append(v+[-a for a in v])
    return groups


def reliable(n,S,p):
    # Direct coefficient extraction: probability of 0 or 1 empty pair.
    active=[]
    S=set(S)
    for i in range(n):
        k=int(i in S)+int(n+i in S)
        active.append(1-p**k if k else Fraction(0))
    total=Fraction(1)
    for t in active:total*=t
    for i in range(n):
        term=1-active[i]
        for j in range(n):
            if i!=j: term*=active[j]
        total+=term
    return total


def formula(n,m,p):
    if m<n-1:return Fraction(0)
    s=1-p; r=1-p*p
    if m==n-1:return s**(n-1)
    a=m-n; b=2*n-m
    out=r**a*s**b
    if a:out+=a*p*p*r**(a-1)*s**b
    if b:out+=b*p*r**a*s**(b-1)
    return out


def zero_forces(n,S):
    black=sum(1<<i for i in S)
    nbr=[]
    for i in range(2*n):
        k=i%n
        nbr.append(sum(1<<(j+n if i<n else j) for j in range(n) if j!=k))
    while True:
        extra=0
        for i in range(2*n):
            if black>>i&1:
                w=nbr[i]&~black
                if w and not(w&(w-1)):extra|=w
        if not extra:break
        black|=extra
    return black==(1<<(2*n))-1


def run():
    checks=0; kchecks=0; rchecks=0; fchecks=0; zchecks=0
    for n in range(3,7):
        L=laplacian(n); spaces=eigbasis(n)
        for value,vectors in spaces.items():
            for v in vectors:
                assert matvec(L,v)==[value*t for t in v]
                checks+=1
        for bits in range(1<<(2*n)):
            S=[i for i in range(2*n) if bits>>i&1]
            expected=covered_indices(n,S)>=n-1
            passes=all(rank_mod([[v[i] for v in vecs] for i in S])==len(vecs) for vecs in spaces.values())
            assert expected==passes,(n,S,expected,passes)
            checks+=1
            if n<=4:
                assert (rank_kalman(n,S)==2*n)==expected
                kchecks+=1
            if n<=5:
                for p in [Fraction(1,3),Fraction(1,2),Fraction(3,4)]:
                    # reliability independent of which vertices were picked at an index.
                    a=sum(i in S and n+i in S for i in range(n))
                    b=sum((i in S)!=(n+i in S) for i in range(n))
                    c=n-a-b
                    s=1-p; r=1-p*p
                    if c>=2:val=Fraction(0)
                    elif c==1:val=r**a*s**b
                    else:
                        val=r**a*s**b
                        if a:val+=a*p*p*r**(a-1)*s**b
                        if b:val+=b*p*r**a*s**(b-1)
                    assert reliable(n,S,p)==val,(n,S,p)
                    rchecks+=1
            if n<=4:
                c=sorted(sum(v in S for v in [i,n+i]) for i in range(n))
                for f in range(5):
                    actual=all(covered_indices(n,set(S)-set(F))>=n-1
                               for k in range(min(f,len(S))+1)
                               for F in combinations(S,k))
                    assert actual==(c[0]+c[1]>f)
                    fchecks+=1
            if len(S)<2*n-4:assert not zero_forces(n,S)
            zchecks+=1
        # sharp zero forcing construction
        S=set(range(2*n))-{0,1,n+1,n+2}
        assert len(S)==2*n-4 and zero_forces(n,S)
    for n in range(3,7):
        for m in range(2*n+1):
            for p in (Fraction(1,3),Fraction(1,2),Fraction(3,4)):
                observed=max(reliable(n,[j for j in range(2*n) if mask>>j&1],p)
                             for mask in range(1<<(2*n)) if mask.bit_count()==m)
                assert observed==formula(n,m,p),(n,m,p,observed,formula(n,m,p))
                rchecks+=1
    print('VERIFY_OK eigenspace_checks=%d kalman_checks=%d reliability_checks=%d robust_checks=%d zero_forcing_checks=%d n_range=3..6' % (checks,kchecks,rchecks,fchecks,zchecks))
if __name__=='__main__':run()
