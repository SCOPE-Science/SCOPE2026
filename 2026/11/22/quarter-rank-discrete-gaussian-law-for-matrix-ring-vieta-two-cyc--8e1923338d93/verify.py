"""Independent finite-field Vieta 2-cycle rank enumeration and coefficient limits.
No external packages; exhaustive ordered-pair iteration only for small matrices.
"""
from math import prod
from collections import Counter

def qbinom(n,r,q):
    if r<0 or r>n:return 0
    k=min(r,n-r)
    v=1
    for j in range(k):
        num=q**(n-j)-1
        den=q**(k-j)-1
        v=v*num//den if (v*num)%den==0 else None
        if v is None:
            # Fall back to safe integer numerator/denominator product
            return prod(q**(n-i)-1 for i in range(k))//prod(q**(k-i)-1 for i in range(k))
    return v

def coefficient(n,r,q):
    GL=prod(q**r-q**j for j in range(r))
    return qbinom(n,r,q)*qbinom(n-r,r,q)*GL*q**(n*(n-r))

def pred(n,q):return sum(coefficient(n,r,q) for r in range(1,n//2+1))//2

def mat_prod(x,y,n,q):
    return tuple(sum(x[i*n+k]*y[k*n+j] for k in range(n))%q for i in range(n) for j in range(n))

def rank(M,n,q):
    a=[list(M[i*n:(i+1)*n]) for i in range(n)]
    piv=0
    for j in range(n):
        p=next((i for i in range(piv,n) if a[i][j]),None)
        if p is None:continue
        a[piv],a[p]=a[p],a[piv]
        inv=pow(a[piv][j],-1,q)
        for k in range(j,n):a[piv][k]=a[piv][k]*inv%q
        for i in range(piv+1,n):
            c=a[i][j]
            for k in range(j,n):a[i][k]=(a[i][k]-c*a[piv][k])%q
        piv+=1
    return piv

def verify(n,q,full=True):
    from itertools import product
    E=list(product(range(q),repeat=n*n))
    zero=(0,)*(n*n)
    sq=Counter()
    cycles=Counter()
    for B in E:
        if mat_prod(B,B,n,q)==zero:
            sq[rank(B,n,q)]+=1
    for r in range(1,n//2+1):
        expected=qbinom(n,r,q)*qbinom(n-r,r,q)*prod(q**r-q**j for j in range(r))
        assert sq[r]==expected,(n,q,r,sq[r],expected)
        if full:
            for B in E:
                if mat_prod(B,B,n,q)!=zero or rank(B,n,q)!=r:continue
                for A in E:
                    AB=mat_prod(A,B,n,q)
                    # direct dynamics T^2 on pair, independent of classification formula
                    C=tuple((A[j]+B[j])%q for j in range(n*n))
                    D=AB
                    CC=tuple((C[j]+D[j])%q for j in range(n*n))
                    DD=mat_prod(C,D,n,q)
                    if CC==A and DD==B and (C,D)!=(A,B):cycles[r]+=1
            assert cycles[r]==coefficient(n,r,q),(n,q,r,cycles[r],coefficient(n,r,q))
    if full:assert sum(cycles.values())//2==pred(n,q)
    return len(E),sq,cycles

for n,q,full in ((2,2,True),(2,3,True),(3,2,True),(4,2,False)):
    print('MATRIX_CASE',n,q,verify(n,q,full)[1])

# Four residue classes: log-exact integer ratios approach discrete Gaussian
for q in (2,3):
    for s in range(4):
        n=4*16+s
        vals=[coefficient(n,r,q) for r in range(1,n//2+1)]
        mid=16
        p=vals[mid-1]/sum(vals)
        # limiting theta center mass at r=floor(n/4)
        theta=sum(q**(-2*(k-s/4)**2) for k in range(-12,13))
        tgt=q**(-2*(s/4)**2)/theta
        assert abs(p-tgt)<0.0002,(n,q,p,tgt)
print('MATRIX_VIETA2_OK')
