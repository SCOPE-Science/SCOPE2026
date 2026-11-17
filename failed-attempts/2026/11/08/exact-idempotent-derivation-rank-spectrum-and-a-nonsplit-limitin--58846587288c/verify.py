"""Direct exhaustive small-field check of the finite-field projection-derivation spectrum.

Run: python verify.py
All calculations are exact, and no external packages are needed.
"""
from itertools import product
from collections import Counter
from math import prod


def mul(a,b,q):
    if q==2: return a & b
    assert q==4
    # F_4 = F_2[z]/(z^2+z+1), bit 1 represents 1 and bit 2 represents z
    t=0
    if a&1: t ^= b
    if a&2:
        t ^= ((b<<1)&3) ^ (3 if (b&2) else 0)
    return t


def rank(M,q):
    a=[row[:] for row in M]
    n=len(a); m=len(a[0]) if n else 0
    lead=0
    for j in range(m):
        pivot=next((i for i in range(lead,n) if a[i][j]),None)
        if pivot is None: continue
        a[lead],a[pivot]=a[pivot],a[lead]
        inv=next(x for x in range(1,q) if mul(x,a[lead][j],q)==1)
        a[lead]=[mul(inv,z,q) for z in a[lead]]
        for i in range(n):
            if i!=lead and a[i][j]:
                c=a[i][j]
                a[i]=[v^mul(c,w,q) for v,w in zip(a[i],a[lead])]
        lead+=1
        if lead==n: break
    return lead


def matmul(A,B,q):
    n=len(A)
    return [[__import__('functools').reduce(lambda s,k:s^mul(A[i][k],B[k][j],q),range(n),0) for j in range(n)] for i in range(n)]


def glorder(n,q):
    return prod(q**n-q**i for i in range(n))


def gauss(n,r,q):
    a=1
    for i in range(r):
        a=a*(q**n-q**i)
    return a//prod(q**r-q**i for i in range(r)) if r else 1


def predicted(n,q):
    assert q in (2,4)
    out=Counter()
    for r in range((n-1)//2+1):
        out[2*r*(n-r)]+=gauss(n,r,q)*q**(r*(n-r))
    if n%2==0:
        m=n//2
        out[n*n//2]+=gauss(n,m,q)*q**(m*m)//2
        out[n*n//2]+=glorder(n,q)//glorder(m,q*q)//2
    return out


def brute(n,q):
    out=Counter()
    # Unique representative of A modulo scalar matrices: A[0,0]=0.
    for coeffs in product(range(q),repeat=n*n-1):
        seq=iter(coeffs)
        A=[[0 if (i,j)==(0,0) else next(seq) for j in range(n)] for i in range(n)]
        S=matmul(A,A,q)
        S=[[S[i][j]^A[i][j] for j in range(n)] for i in range(n)]
        if any(S[i][j] != (S[0][0] if i==j else 0) for i in range(n) for j in range(n)):
            continue
        # Evaluate D(E_ab)=AE_ab-E_ab A (addition= subtraction in char 2).
        M=[]
        for a in range(n):
            for b in range(n):
                entries=[]
                for i in range(n):
                    for j in range(n):
                        entries.append((A[i][a] if b==j else 0)^(A[b][j] if a==i else 0))
                M.append(entries)
        # transpose to matrix with basis images in columns
        T=[list(x) for x in zip(*M)]
        # D^2=D independently, without relying on the A^2+A criterion.
        D2=matmul(T,T,q) if n==1 else None
        if n>1:
            size=n*n
            D2=[[0]*size for _ in range(size)]
            for i in range(size):
                for k in range(size):
                    if T[i][k]:
                        for j in range(size):
                            D2[i][j]^=mul(T[i][k],T[k][j],q)
        assert D2==T
        out[rank(T,q)]+=1
    return out

for n,q in [(2,2),(3,2),(4,2),(2,4)]:
    actual=brute(n,q); expect=predicted(n,q)
    assert actual==expect,(n,q,actual,expect)
    print('EXHAUSTIVE_OK',n,q,dict(sorted(actual.items())))
print('VERIFY_OK')
