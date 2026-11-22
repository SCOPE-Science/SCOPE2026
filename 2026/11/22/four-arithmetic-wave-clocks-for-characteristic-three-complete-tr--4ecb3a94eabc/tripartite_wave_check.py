#!/usr/bin/env python3
"""Independent exact rank and polynomial-order checks for ternary tripartite waves.
Science-only reproducibility script; Python 3 plus stdlib, no external packages.
"""
from itertools import combinations_with_replacement

def rank3(M):
    A=[list(map(lambda v:v%3,row)) for row in M]
    n=len(A); m=len(A[0]); r=0
    for c in range(m):
        p=next((j for j in range(r,n) if A[j][c]),None)
        if p is None:continue
        A[r],A[p]=A[p],A[r]
        if A[r][c]==2:A[r]=[(v*2)%3 for v in A[r]]
        for j in range(n):
            if j!=r and A[j][c]:
                w=A[j][c];A[j]=[(x-w*y)%3 for x,y in zip(A[j],A[r])]
        r+=1
        if r==n:break
    return r

def matmul(A,B):
    n=len(A);m=len(B[0]);t=len(B)
    return [[sum(A[i][s]*B[s][j] for s in range(t))%3 for j in range(m)] for i in range(n)]

def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]

def mulpow(A,k):
    n=len(A);Q=eye(n)
    while k:
        if k&1:Q=matmul(Q,A)
        A=matmul(A,A);k//=2
    return Q

def wave(ns):
    N=sum(ns); A=[[0]*N for _ in range(N)];indices=[];s=0
    for n in ns: indices.append(list(range(s,s+n)));s+=n
    for x in range(3):
      for y in range(x+1,3):
       for i in indices[x]:
        for j in indices[y]:A[i][j]=A[j][i]=1
    T=[[0]*(2*N) for _ in range(2*N)]
    for i in range(N):
      for j in range(N):T[i][j]=A[i][j]
      T[i][N+i]=2;T[N+i][i]=1
    return T

def fixed_dim_formula(ns,k):
    N=sum(ns); v=1; t=k
    while t%3==0:t//=3;v*=3
    A=sorted(n%3 for n in ns); r=3-A.count(0)
    h=int(k%4==0)
    if r==0:return h*(2*(N-6)+6*min(2,v))
    if r==1:return h*(2*(N-5)+2*min(2,v)+2*min(3,v))
    if r==2:
        c=h*(2*(N-4)+2*min(2,v))
        ab=A[1]*A[2]%3
        if ab==1:return c+min(2,v)*(1+int(k%2==0))
        return c+4*int(k%8==0)
    c=h*2*(N-3)
    if A==[1,1,1]:return c+min(4,v)+min(2,v)
    if A==[2,2,2]:return c+int(k%2==0)*(min(4,v)+min(2,v))
    if A==[1,1,2]:return c+min(2,v)+4*int(k%10==0)
    if A==[1,2,2]:return c+int(k%2==0)*min(2,v)+4*int(k%5==0)
    raise AssertionError(A)

def period_formula(ns):
    a=sorted(n%3 for n in ns);r=3-a.count(0)
    if r<=1:return 12
    if r==2:return 12 if a[1]*a[2]%3==1 else 24
    if a==[1,1,1] and sum(ns)==3:return 9
    if a==[1,1,1] or a==[2,2,2]:return 36
    return 60

def main():
    tests=0
    for ns in combinations_with_replacement(range(1,7),3):
        T=wave(ns);n=len(T)
        for k in [1,2,3,4,5,6,8,9,10,12,18,20,24,30,36,40,45,48,60,72,90,120]:
            K=mulpow(T,k)
            for i in range(n):K[i][i]=(K[i][i]-1)%3
            dim=n-rank3(K)
            want=fixed_dim_formula(ns,k)
            assert dim==want,(ns,k,dim,want)
            tests+=1
        p=period_formula(ns)
        assert fixed_dim_formula(ns,p)==n,(ns,p)
        for d in range(1,p):
            if p%d==0:assert fixed_dim_formula(ns,d)<n,(ns,p,d)
    print('PASS:',tests,'independent direct matrix-rank vs formula checks; 56 size triples; exact order divisors verified.')
if __name__=='__main__':main()
