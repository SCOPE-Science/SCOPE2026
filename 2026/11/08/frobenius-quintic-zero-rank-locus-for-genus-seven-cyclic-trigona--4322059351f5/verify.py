#!/usr/bin/env python3
"""Exact finite-field checks for Cartier ranks of genus-seven cubic Kummer covers.
Only the finite instances below are asserted by the executable tests.
"""
from collections import Counter
from itertools import product

class GF:
    def __init__(self,m,mod):
        self.m=m; self.mod=mod; self.q=1<<m
    def mul(self,a,b):
        z=0
        while b:
            if b&1:z^=a
            b>>=1; a<<=1
            if a&self.q: a^=self.mod
        return z
    def power(self,a,n):
        z=1
        while n:
            if n&1:z=self.mul(z,a)
            a=self.mul(a,a);n>>=1
        return z
    def inv(self,a):
        assert a
        return self.power(a,self.q-2)
    def root(self,a):return self.power(a,self.q//2)
    def fourth(self,a):return self.power(a,4)
    def mulmat(self,A,B):
        n=len(A); r=len(B);m=len(B[0]);C=[[0]*m for _ in range(n)]
        for i in range(n):
            for k in range(r):
                if A[i][k]:
                    for j in range(m):
                        C[i][j]^=self.mul(A[i][k],B[k][j])
        return C
    def rank(self,A):
        A=[row[:] for row in A]; rows=len(A); cols=len(A[0]); r=0
        for c in range(cols):
            pivot=next((k for k in range(r,rows) if A[k][c]),None)
            if pivot is None:continue
            A[r],A[pivot]=A[pivot],A[r]
            v=self.inv(A[r][c]); A[r]=[self.mul(v,x) for x in A[r]]
            for i in range(r+1,rows):
                if A[i][c]:
                    v=A[i][c]
                    A[i]=[x^self.mul(v,y) for x,y in zip(A[i],A[r])]
            r+=1
            if r==rows:break
        return r
    def trim(self,P):
        while len(P)>1 and P[-1]==0:P.pop()
        return P
    def rem(self,P,Q):
        P=self.trim(P[:]);Q=self.trim(Q[:]);d=len(Q)-1
        if d==0:return [0]
        inv=self.inv(Q[-1])
        while len(P)>=len(Q) and P!=[0]:
            a=self.mul(P[-1],inv);off=len(P)-len(Q)
            for i,x in enumerate(Q):P[i+off]^=self.mul(a,x)
            self.trim(P)
        return P
    def squarefree(self,f):
        d=[f[i] if i%2 else 0 for i in range(1,len(f))]
        d=self.trim(d or [0])
        if d==[0]:return False
        a=f[:];b=d
        while b!=[0]:a,b=b,self.rem(a,b)
        return len(a)==1

def cartier_matrix(F, coeff):
    c=coeff+[1];M=[[0]*7 for _ in range(7)]
    M[0][3]=1;M[1][5]=1
    for i in range(4):M[2+i][0]=F.root(c[2*i+1])
    for i in range(5):M[2+i][1]=F.root(c[2*i])
    return M

def ranks(F,M):
    P=[row[:] for row in M]; T=[row[:] for row in M];rr=[F.rank(P)]
    for n in range(2,9):
        T=[[F.root(a) for a in row] for row in T]
        P=F.mulmat(P,T)
        rr.append(F.rank(P))
    return tuple(rr)

def predicted(F,c):
    a3,a2,a7,a6=c[3],c[2],c[7],c[6]
    det=F.mul(a3,a6)^F.mul(a2,a7)
    H=[[a3,a2],[a7,a6]]
    HH=F.mulmat([[F.fourth(x) for x in row] for row in H],H)
    if det:return (4,)*8, 'rank4'
    if all(x==0 for row in H for x in row):return (4,2,0,0,0,0,0,0),'rank0-vertex'
    if all(x==0 for row in HH for x in row):return (4,3,2,1,0,0,0,0),'rank0-nonvertex'
    return (4,3,2,2,2,2,2,2),'rank2'

def go(F, mode):
    totals=Counter(); checked=0
    if mode=='exhaustive':it=product(range(F.q), repeat=8)
    else:
        import random
        rng=random.Random(97519+F.q)
        it=(tuple(rng.randrange(F.q) for _ in range(8)) for i in range(2400))
    for c0 in it:
        c=list(c0)
        if not F.squarefree(c+[1]):continue
        checked+=1
        expected, kind=predicted(F,c)
        found=ranks(F,cartier_matrix(F,c))
        assert found==expected,(F.q,c,expected,found)
        totals[kind]+=1
    assert checked>0 and totals['rank0-nonvertex']>0 and totals['rank2']>0 and totals['rank4']>0
    if F.q>=4:assert totals['rank0-vertex']>0
    print('field',F.q,'mode',mode,'smooth',checked,'counts',dict(sorted(totals.items())))

if __name__=='__main__':
    go(GF(1,0b11),'exhaustive')
    go(GF(2,0b111),'exhaustive')
    go(GF(3,0b1011),'sample')
    print('ALL_CARTIER_CHECKS_PASSED')
