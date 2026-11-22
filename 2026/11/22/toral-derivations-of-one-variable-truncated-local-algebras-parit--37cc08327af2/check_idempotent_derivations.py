#!/usr/bin/env python3
"""Finite, exhaustive tests of projection derivations of k[t]/(t^N).
Uses original derivation matrices and composition identities, not only the normal form.
No external dependencies.
"""
from itertools import product
from collections import Counter

class Field:
    def __init__(self,q):
        assert q in (2,3,4,5)
        self.q=q
        self.p=2 if q==4 else q
    def add(self,a,b): return a^b if self.q==4 else (a+b)%self.q
    def neg(self,a): return a if self.q==4 else (-a)%self.q
    def mul(self,a,b):
        if self.q!=4:return a*b%self.q
        z=0
        for i in range(2):
            if (b>>i)&1:z^=a<<i
        if z&4:z^=0b111
        return z
    def pow(self,a,e):
        z=1
        for _ in range(e):z=self.mul(z,a)
        return z
    def inv(self,a):
        assert a
        return next(x for x in range(1,self.q) if self.mul(a,x)==1)

def mm(A,B,F):
    n=len(A)
    return [[sum_product([ (A[i][k],B[k][j]) for k in range(n)],F) for j in range(n)] for i in range(n)]
def sum_product(terms,F):
    a=0
    for x,y in terms:a=F.add(a,F.mul(x,y))
    return a

def derivation(f,N,F):
    # columns: D(t^j)=j t^(j-1) f mod t^N
    out=[[0]*N for i in range(N)]
    for j in range(1,N):
        for i in range(N-j+1):
            out[i+j-1][j]=F.mul(j%F.p,f[i])
    return out

def rank(A,F):
    B=[row[:] for row in A]; n=len(B); m=len(B[0]); r=0
    for c in range(m):
        piv=next((j for j in range(r,n) if B[j][c]),None)
        if piv is None: continue
        B[r],B[piv]=B[piv],B[r]
        inv=F.inv(B[r][c]);B[r]=[F.mul(x,inv) for x in B[r]]
        for j in range(n):
            if j!=r and B[j][c]:
                a=B[j][c]
                B[j]=[F.add(B[j][k],F.neg(F.mul(a,B[r][k]))) for k in range(m)]
        r+=1
    return r

def check(q,N):
    F=Field(q)
    frequency=Counter(); predicted=Counter(); n_good=0
    for f in product(range(q),repeat=N):
        valid_derivation=((N%F.p)==0 or f[0]==0)
        if not valid_derivation:continue
        A=derivation(f,N,F)
        # Directly verify derivation on all monomial pairs
        for i in range(N):
            for j in range(N):
                u=[0]*N
                if i+j<N:u=[A[k][i+j] for k in range(N)]
                v=[0]*N
                for k in range(N):
                    if k+j<N:v[k+j]=F.add(v[k+j],A[k][i])
                    if k+i<N:v[k+i]=F.add(v[k+i],A[k][j])
                assert u==v,(q,N,f,i,j)
        good=(mm(A,A,F)==A)
        if good:
            n_good+=1;frequency[rank(A,F)]+=1
        h=N//2
        expected=(all(x==0 for x in f) or (
            F.p==2 and f[1]==1 and all(f[j]==0 for j in range(3,N,2))
            and (N%2==0 or f[0]==0)))
        assert good==expected,(q,N,f,good,expected)
    if F.p==2:
        predicted=Counter({0:1,h:q**h})
    else:predicted=Counter({0:1})
    assert frequency==predicted,(q,N,frequency,predicted)
    print('PASS',q,N,'count',n_good,'ranks',dict(sorted(frequency.items())))

if __name__=='__main__':
    for q,Ns in [(2,(3,4,5,6,7,8,9)),(4,(3,4,5,6)),(3,(3,4,5)),(5,(3,4))]:
        for N in Ns:check(q,N)
    print('IDEMPOTENT_TRUNCATED_DERIVATIONS_VERIFIED')
