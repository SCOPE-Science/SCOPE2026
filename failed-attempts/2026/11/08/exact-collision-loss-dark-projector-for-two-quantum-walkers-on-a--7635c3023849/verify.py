#!/usr/bin/env python3
"""Exact finite checks for collision-loss dark projectors on finite rings.
This verifies projector identities in integer arithmetic and independently
computes the reachable Krylov dimension modulo two large primes.
"""
from collections import deque


def construct(n):
    N=n*n
    ix=lambda x,y:(x%n)*n+(y%n)
    H=[[0]*N for _ in range(N)]
    for x in range(n):
        for y in range(n):
            i=ix(x,y)
            for a,b in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                H[i][ix(a,b)]+=1
    # M = 2n times the proposed orthogonal dark projector.
    M=[[0]*N for _ in range(N)]
    for x in range(n):
        for y in range(n):
            i=ix(x,y)
            M[i][i]+=n
            M[i][ix(y,x)]-=n
            if n%2==0:
                for t in range(n):
                    c=(-1)**t
                    M[i][ix(x+t,y+t)]+=c
                    M[i][ix(y+t,x+t)]+=c
    if n%2==0:
        for x in range(n):
            for y in range(n):
                M[ix(x,x)][ix(y,y)]-=2*(-1)**(x+y)
    return H,M


def products(A,B):
    n=len(A)
    C=[[0]*n for _ in range(n)]
    for i in range(n):
        for k,a in enumerate(A[i]):
            if a:
                for j,b in enumerate(B[k]):
                    C[i][j]+=a*b
    return C


def krylov_rank(H,n,prime):
    N=n*n
    piv={}
    Q=deque()
    for x in range(n):
        v=[0]*N
        v[x*n+x]=1
        Q.append(v)
    while Q:
        v=Q.popleft()
        for p,b in sorted(piv.items()):
            scale=v[p]
            if scale:
                for j in range(p,N):
                    v[j]=(v[j]-scale*b[j])%prime
        p=next((i for i,a in enumerate(v) if a),None)
        if p is None:
            continue
        inv=pow(v[p],-1,prime)
        v=[(a*inv)%prime for a in v]
        piv[p]=v
        # Only independent vectors need to generate descendants.
        nxt=[sum(H[i][j]*v[j] for j in range(N))%prime for i in range(N)]
        Q.append(nxt)
    return len(piv)


def go():
    all_cases=[]
    for n in range(3,11):
        H,M=construct(n)
        N=n*n
        # Exact symmetry, Hermitian projection, commuting Hamiltonian, and
        # the support restriction on every collision location.
        assert all(M[i][j]==M[j][i] for i in range(N) for j in range(N))
        for x in range(n):
            assert all(M[x*n+x][j]==0 for j in range(N))
        assert products(M,M)==[[2*n*v for v in row] for row in M]
        assert products(H,M)==products(M,H)
        f=2 if (n%4==0) else 0
        d=N//2-n//2 if n%2 else (n*(n-1))//2+(n+f)//2-1
        # Since M is a projector, its rank equals trace(M)/(2n).
        assert sum(M[i][i] for i in range(N))==2*n*d
        # Independent Krylov construction: vectors generated from collision
        # basis under H, without using the proposed projection formula.
        for prime in (1000003,1000033):
            assert krylov_rank(H,n,prime)==N-d,(n,prime)
        for x in range(n):
            for y in range(n):
                if x==y:
                    assert M[x*n+y][x*n+y]==0
                    continue
                i=x*n+y
                j=y*n+x
                # 2n times bosonic survival, evaluated on the normalized
                # symmetrized unordered pair.
                bos2n=(M[i][i]+M[j][j]+2*M[i][j])//2
                expected=0 if n%2 else 2*(1+((-1)**(n//2) if (x-y)%n==n//2 else 0))
                assert (M[i][i]+M[j][j]+2*M[i][j])%2==0
                assert bos2n==expected,(n,x,y,bos2n,expected)
        all_cases.append((n,N,d,N-d))
    print('VERIFY_OK n dimension dark_rank bright_rank')
    for row in all_cases:
        print(*row)

if __name__=='__main__':
    go()
