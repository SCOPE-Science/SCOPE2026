#!/usr/bin/env python3
"""Exact enumeration of idempotents of finite perfect evolution algebras.
No assumptions about analytical variance formula are used in enumeration.
"""
from collections import Counter
from fractions import Fraction
from itertools import product

class Field:
    def __init__(self,p,mod=None):
        self.p=p; self.mod=mod; self.m=(len(mod)-1 if mod else 1)
        self.q=p**self.m
        self.digits=[tuple((v//(p**i))%p for i in range(self.m)) for v in range(self.q)]
        self.add=[[self.encode(tuple((a+b)%p for a,b in zip(x,y))) for y in self.digits] for x in self.digits]
        self.mul=[[self.multiply(x,y) for y in self.digits] for x in self.digits]
        self.inv=[None]*self.q
        for x in range(1,self.q):
            self.inv[x]=next(y for y in range(1,self.q) if self.mul[x][y]==1)
        self.sq=[self.mul[x][x] for x in range(self.q)]
    def encode(self,cs):return sum(v*self.p**i for i,v in enumerate(cs))
    def multiply(self,x,y):
        p=self.p; m=self.m
        if m==1:return (x[0]*y[0])%p
        a=[0]*(2*m-1)
        for i,v in enumerate(x):
            for j,w in enumerate(y):a[i+j]=(a[i+j]+v*w)%p
        for k in range(2*m-2,m-1,-1):
            f=a[k]
            for i in range(m):a[k-m+i]=(a[k-m+i]-f*self.mod[i])%p
        return self.encode(a[:m])

def is_invertible(matrix,n,F):
    a=[list(matrix[i*n:(i+1)*n]) for i in range(n)]
    for col in range(n):
        pivot=next((i for i in range(col,n) if a[i][col]),None)
        if pivot is None:return False
        a[col],a[pivot]=a[pivot],a[col]
        z=F.inv[a[col][col]]
        for j in range(col,n):a[col][j]=F.mul[z][a[col][j]]
        for i in range(col+1,n):
            z=a[i][col]
            if z:
                for j in range(col,n):a[i][j]=F.add[a[i][j]][F.mul[F.p-1][F.mul[z][a[col][j]]]] if F.p>2 else F.add[a[i][j]][F.mul[z][a[col][j]]]
    return True

def check(p,n,mod=None):
    F=Field(p,mod);q=F.q; vecs=list(product(range(q),repeat=n));xs=vecs[1:]
    h=Counter(); gl=0
    for a in product(range(q),repeat=n*n):
        if not is_invertible(a,n,F):continue
        gl+=1
        fixed=0
        for x in xs:
            sx=[F.sq[z] for z in x]
            if all(fold_sum(F,[F.mul[a[i*n+j]][sx[j]] for j in range(n)])==x[i] for i in range(n)):
                fixed+=1
        h[fixed]+=1
    expected_gl=1
    for j in range(n):expected_gl*=q**n-q**j
    assert gl==expected_gl, (p,n,q,gl,expected_gl)
    mu=Fraction(sum(k*v for k,v in h.items()),gl)
    variance=Fraction(sum((k-1)**2*v for k,v in h.items()),gl)
    B=0 if p==2 else Fraction(q-1,2)*((2*q-1)**n-2*q**n+1)
    predicted=1-Fraction(B,(q**n-1)*(q**n-q))
    assert mu==1 and variance==predicted,(p,n,mu,variance,predicted)
    # Directly count the exceptional pairs with independent vectors but
    # proportional coordinatewise squares, using only field arithmetic.
    if q**n <= 81:
        bad=0
        for x in xs:
            xx=tuple(F.sq[v] for v in x)
            for y in xs:
                if y==x: continue
                # Do not test all ratios: determine each rank by a minor.
                independent=any(F.mul[x[i]][y[j]]!=F.mul[x[j]][y[i]]
                                for i in range(n) for j in range(i+1,n))
                dependent_squares=all(F.mul[xx[i]][F.sq[y[j]]]==
                                      F.mul[xx[j]][F.sq[y[i]]]
                                      for i in range(n) for j in range(i+1,n))
                bad+=independent and dependent_squares
        assert bad==B,(q,n,bad,B)
    print(f'q={q} n={n} GL={gl} mean={mu} variance={variance} histogram={sorted(h.items())}')

def fold_sum(F,arr):
    z=0
    for v in arr:z=F.add[z][v]
    return z

if __name__=='__main__':
    for p,n,mod in [(2,2,None),(3,2,None),(5,2,None),(7,2,None),
                    (2,2,[1,1,1]),(2,2,[1,1,0,1]),(3,2,[1,0,1]),
                    (2,3,None),(3,3,None),(2,4,None)]:
        check(p,n,mod)
    print('VERIFY_OK')
