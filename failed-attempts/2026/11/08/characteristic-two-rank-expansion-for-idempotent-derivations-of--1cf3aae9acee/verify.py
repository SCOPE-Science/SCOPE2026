"""Independent enumeration of idempotent derivation ranks of free class-two Lie algebras.

Standard-library-only.  All arithmetic uses prime fields; the proof applies to all finite fields.
"""
from itertools import product
from math import comb
from collections import Counter

def matmul(A,B,p):
    rows=len(A); mid=len(B); cols=len(B[0]);
    return [[sum(A[i][k]*B[k][j] for k in range(mid))%p for j in range(cols)] for i in range(rows)]

def gauss(n,r,q):
    if r<0 or r>n:return 0
    num=den=1
    for i in range(r):num*=q**(n-i)-1;den*=q**(r-i)-1
    return num//den

def predicted(n,q):
    P=Counter({0:1})
    for r in range(1,n+1):
        s=n-r
        E=r*(comb(r,2)+comb(s,2))+s*r*s
        if q%2:
            if r>1:continue
            E=comb(n-1,2)+(n-1)**2
            rank=n
        else:rank=r*(s+1)
        P[rank]+=gauss(n,r,q)*q**(r*s+E)
    return P

def enumerate_all(n,q):
    pairs=list(__import__('itertools').combinations(range(n),2)); N=len(pairs)
    M=n+N
    P=Counter()
    ids=[(i,j) for i in range(n) for j in range(n)]
    for values in product(range(q),repeat=n*n):
        A=[[values[i*n+j] for j in range(n)] for i in range(n)]
        C=[[0]*N for _ in range(N)]
        for col,(i,j) in enumerate(pairs):
            for row,(u,v) in enumerate(pairs):
                C[row][col]=(A[u][i]*(v==j)-A[v][i]*(u==j)+A[v][j]*(u==i)-A[u][j]*(v==i))%q
        # independent direct bracket test for the induced central matrix
        for bc in product(range(q),repeat=n*N):
            B=[list(bc[t*n:(t+1)*n]) for t in range(N)]
            D=[]
            for i in range(n):D.append(A[i]+[0]*N)
            for i in range(N):D.append(B[i]+C[i])
            if matmul(D,D,q)!=D:continue
            # compute rank by elimination, without using the theorem's block-rank formula
            E=[row[:] for row in D];rank=0
            for col in range(M):
                piv=next((i for i in range(rank,M) if E[i][col]%q),None)
                if piv is None:continue
                E[piv],E[rank]=E[rank],E[piv]
                inv=pow(E[rank][col],-1,q)
                E[rank]=[(t*inv)%q for t in E[rank]]
                for i in range(M):
                    if i!=rank and E[i][col]:
                        z=E[i][col]
                        E[i]=[(a-z*b)%q for a,b in zip(E[i],E[rank])]
                rank+=1
            P[rank]+=1
    return P

if __name__=='__main__':
    for n,q in ((2,2),(2,3),(2,5),(3,2)):
        actual=enumerate_all(n,q);expect=predicted(n,q)
        assert actual==expect,(n,q,actual,expect)
        print('n=',n,'field=',q,'rank_histogram=',dict(sorted(actual.items())))
    print('VERIFY_OK')
