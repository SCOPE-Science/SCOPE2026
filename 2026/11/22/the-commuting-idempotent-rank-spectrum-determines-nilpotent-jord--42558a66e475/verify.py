#!/usr/bin/env python3
"""Finite checks for the nilpotent commuting-idempotent rank spectrum."""
from itertools import product
from functools import lru_cache
from collections import Counter

@lru_cache(None)
def gaussian(n,k,q):
    if not 0<=k<=n:return 0
    if k==0 or k==n:return 1
    return gaussian(n-1,k,q)+q**(n-k)*gaussian(n-1,k-1,q)

def partitions(n,minimum=1):
    if n==0:
        yield ();return
    for j in range(minimum,n+1):
        for tail in partitions(n-j,j):yield (j,)+tail

def formula(part,q):
    m=Counter(part); lengths=sorted(m)
    out=[0]*(sum(part)+1)
    for v in product(*(range(m[j]+1) for j in lengths)):
        a=dict(zip(lengths,v)); b={j:m[j]-a[j] for j in lengths}
        cross=sum(a[i]*b[j]*min(i,j) for i in lengths for j in lengths)
        exponent=2*cross-sum(a[j]*b[j] for j in lengths)
        count=q**exponent
        for j in lengths:count*=gaussian(m[j],a[j],q)
        out[sum(j*a[j] for j in lengths)]+=count
    return tuple(out)

def reconstruct(poly,q):
    n=len(poly)-1
    if n==0:return ()
    assert poly[0]==poly[n]==1
    d=next(i for i in range(1,n+1) if poly[i])
    c=poly[d]
    exponent=0
    while q**(exponent+1)<=c: exponent+=1
    assert exponent%(2*d)==0
    B=1+exponent//(2*d)
    m={}
    for j in range(1,n+1):
        # Contributions from image modules with all summands strictly shorter than j.
        older=sorted(m)
        total=sum(m.values())
        known=0
        for v in product(*(range(m[i]+1) for i in older)):
            a=dict(zip(older,v))
            if sum(i*a[i] for i in older)!=j:continue
            b={i:m[i]-a[i] for i in older}
            exponent_old=2*sum(a[i]*(sum(b[l]*min(i,l) for l in older)+i*(B-total)) for i in older)-sum(a[i]*b[i] for i in older)
            coeff=q**exponent_old
            for i in older:coeff*=gaussian(m[i],a[i],q)
            known+=coeff
        residual=poly[j]-known
        assert residual>=0,(j,residual)
        if residual==0: continue
        exponent_new=2*(sum(i*m[i] for i in older)+j*(B-total-1))
        assert exponent_new>=0
        x=q**exponent_new
        summation=0; count=0
        while summation<residual:
            assert x>0 and x==int(x)
            summation+=x
            count+=1
            x//=q
            assert count<=B
        assert summation==residual, (j,residual,exponent_new)
        m[j]=count
    out=tuple(j for j in sorted(m) for _ in range(m[j]))
    assert sum(out)==n
    return out

def matrix_mul(A,B,q):
    n=len(A)
    return tuple(tuple(sum(A[i][j]*B[j][k] for j in range(n))%q for k in range(n)) for i in range(n))
def rank(A,q):
    a=[list(row) for row in A];n=len(a)
    r=0
    for c in range(n):
        pivot=next((i for i in range(r,n) if a[i][c]%q),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        u=pow(a[r][c],-1,q)
        a[r]=[(v*u)%q for v in a[r]]
        for i in range(r+1,n):
            f=a[i][c]%q
            a[i]=[(a[i][j]-f*a[r][j])%q for j in range(n)]
        r+=1
    return r

def jordan(part):
    n=sum(part); A=[[0]*n for _ in range(n)]
    k=0
    for size in part:
        for i in range(size-1):A[k+i][k+i+1]=1
        k+=size
    return tuple(map(tuple,A))

def exhaustive(part,q):
    N=jordan(part);n=sum(part);counts=[0]*(n+1)
    for entries in product(range(q),repeat=n*n):
        E=tuple(tuple(entries[i*n:(i+1)*n]) for i in range(n))
        if matrix_mul(E,E,q)!=E:continue
        if matrix_mul(N,E,q)!=matrix_mul(E,N,q):continue
        counts[rank(E,q)]+=1
    return tuple(counts)

if __name__=='__main__':
    for q,max_n in ((2,4),(3,3)):
        for n in range(1,max_n+1):
            for p in partitions(n):
                actual=exhaustive(p,q)
                expected=formula(p,q)
                assert actual==expected,(q,p,actual,expected)
                assert reconstruct(expected,q)==p,(q,p)
            print('BRUTE',q,n,'PASS')
    for q in (2,3,4,5):
        for n in range(1,23):
            polys={}
            for p in partitions(n):
                P=formula(p,q)
                assert reconstruct(P,q)==p,(q,n,p)
                assert P not in polys,('COLLISION',q,n,p,polys.get(P))
                polys[P]=p
        print('PARTITION_RECONSTRUCTION',q,'through n=22 PASS')
    print('JORDAN_IDEMPOTENT_RECONSTRUCTION_VERIFIED')
