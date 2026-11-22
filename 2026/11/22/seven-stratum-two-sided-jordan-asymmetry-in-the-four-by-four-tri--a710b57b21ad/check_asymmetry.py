#!/usr/bin/env python3
"""Direct verification of a two-sided Jordan discrepancy law for T_4(k)."""
from collections import Counter
from itertools import product

BASIS=[(i,j) for i in range(4) for j in range(i,4)]
I={v:k for k,v in enumerate(BASIS)}
N=len(BASIS)
COORDS=[(0,1),(1,2),(2,3),(0,2),(1,3),(0,3)]


def matmul(A,B,p):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n))%p for j in range(n)] for i in range(n)]


def rank_mod_p(mat,p):
    M=[list(row) for row in mat]
    n=len(M)
    row=0
    for col in range(n):
        pivot=next((j for j in range(row,n) if M[j][col]%p),None)
        if pivot is None:continue
        M[row],M[pivot]=M[pivot],M[row]
        inv=pow(M[row][col],-1,p)
        M[row]=[inv*v%p for v in M[row]]
        for k in range(row+1,n):
            f=M[k][col]
            if f:M[k]=[(M[k][j]-f*M[row][j])%p for j in range(n)]
        row+=1
        if row==n:break
    return row


def left_right(coords,p):
    L=[[0]*N for _ in range(N)]
    R=[[0]*N for _ in range(N)]
    for a,v in zip(COORDS,coords):
        if not v: continue
        for j,b in enumerate(BASIS):
            if a[1]==b[0]: L[I[a[0],b[1]]][j]=(L[I[a[0],b[1]]][j]+v)%p
            if b[1]==a[0]: R[I[b[0],a[1]]][j]=(R[I[b[0],a[1]]][j]+v)%p
    return L,R


def jordan(mat,p):
    M=mat
    ranks=[N]
    for k in range(1,5):
        ranks.append(rank_mod_p(M,p))
        if k!=4:M=matmul(M,mat,p)
    assert ranks[-1]==0
    return tuple(ranks[k-1]-2*ranks[k]+ranks[k+1] for k in range(1,4))+(ranks[3],)


def signature_from_support(coords):
    a,b,c,d,e,_=coords
    A,B,C,D,E=map(lambda x:int(bool(x)),(a,b,c,d,e))
    delta3=B*(A-C)
    delta2=A+int(bool(A or B or D))-A*B-(C+int(bool(B or C or E))-B*C)
    return (delta3,delta2)


def expected(q):
    return {(-1,0):q**3*(q-1)**2,(1,0):q**3*(q-1)**2,
            (0,-2):q**2*(q-1),(0,2):q**2*(q-1),
            (0,-1):q*(q-1)*(q*q-q+1),
            (0,1):q*(q-1)*(q*q-q+1),
            (0,0):q*(q**5-2*q**4+2*q**3-2*q+2)}


def test(p):
    C=Counter()
    for v in product(range(p),repeat=6):
        L,R=left_right(v,p)
        jL=jordan(L,p);jR=jordan(R,p)
        assert sum((k+1)*jL[k] for k in range(4))==N
        assert sum((k+1)*jR[k] for k in range(4))==N
        assert jL[3]==jR[3]
        diff=(jL[2]-jR[2],jL[1]-jR[1])
        assert diff==signature_from_support(v),(v,jL,jR,diff)
        C[diff]+=1
    E=expected(p)
    assert C==E,(C,E)
    assert sum(C.values())==p**6
    print(f'GF({p}): {p**6} algebra elements, seven signatures, exact counts verified')
    print(' ',sorted(C.items()))

if __name__=='__main__':
    for p in [2,3,5]: test(p)
    print('ALL CHECKS PASSED')
