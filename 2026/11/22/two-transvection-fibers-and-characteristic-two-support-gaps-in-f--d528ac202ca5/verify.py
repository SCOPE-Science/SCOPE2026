#!/usr/bin/env python3
"""Finite-field direct multiplication cross-check for prescribed two-transvection fibers.

Uses only the Python standard library. Runs prime and quadratic extension fields.
Counts all ordered nonidentity symplectic-transvection pairs, compares each output
with an independently reconstructed rank/Wall-quadratic classification, and checks
closed-form support and multiplicity data. This is a finite stress test, not a
proof of the universal formulas.
"""
from collections import Counter
from itertools import product

class Field:
    def __init__(self,p,d=1):
        self.p,self.d,self.q=p,d,p**d
        if d==2:
            # u^2 = -u-1 for p=2; u^2=-1 for p=3; u^2=-2 for p=5
            self.coeffs={2:(1,1),3:(1,0),5:(2,0)}[p]
        elif d!=1:raise ValueError
        def mul(a,b):
            if d==1:return (a*b)%p
            a0,a1=a%p,a//p;b0,b1=b%p,b//p
            c0,c1=self.coeffs
            return ((a0*b0-c0*a1*b1)%p)+p*((a0*b1+a1*b0-c1*a1*b1)%p)
        self.M=[[mul(a,b) for b in range(self.q)] for a in range(self.q)]
        self.N=[(-a)%p+ p*((-(a//p))%p) for a in range(self.q)]
        self.I=[0]*self.q
        for a in range(1,self.q):self.I[a]=next(b for b in range(1,self.q) if mul(a,b)==1)
    def plus(self,a,b):
        if self.d==1:return (a+b)%self.p
        p=self.p;return (a%p+b%p)%p+p*((a//p+b//p)%p)
    def minus(self,a,b):return self.plus(a,self.N[b])
    def mul(self,a,b):return self.M[a][b]
    def lin(self,a,b,c):return self.plus(self.mul(a,b),c)

def lines(k,F):
    for i in range(k):
        for tail in product(range(F.q),repeat=k-i-1):yield tuple([0]*i+[1]+list(tail))

def rank_rows(A,F):
    if not A:return 0
    A=[list(row) for row in A];m=len(A);n=len(A[0]);r=0
    for j in range(n):
        pivot=next((i for i in range(r,m) if A[i][j]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        a=F.I[A[r][j]]
        A[r]=[F.mul(a,x) for x in A[r]]
        for i in range(m):
            if i!=r and A[i][j]:
                a=A[i][j]
                A[i]=[F.minus(x,F.mul(a,y)) for x,y in zip(A[i],A[r])]
        r+=1
        if r==m:break
    return r

def run(p,d,m):
    F=Field(p,d);q=F.q;n=2*m
    J=[[0]*n for _ in range(n)]
    for k in range(m):J[2*k][2*k+1]=1;J[2*k+1][2*k]=F.N[1]
    eye=tuple(tuple(int(i==j) for j in range(n)) for i in range(n))
    def mv(A,v):
        return tuple(sumfield(F.mul(a,b) for a,b in zip(row,v)) for row in A)
    def sumfield(xs):
        x=0
        for z in xs:x=F.plus(x,z)
        return x
    def bil(u,v):return sumfield(F.mul(u[i],x) for i,x in enumerate(mv(J,v)))
    T=[]
    for v in lines(n,F):
        jv=mv(J,v)
        for a in range(1,q):
            A=tuple(tuple(F.plus(eye[i][j],F.mul(a,F.mul(v[i],jv[j]))) for j in range(n)) for i in range(n))
            T.append(A)
    assert len(T)==q**n-1
    def multiply(A,B):
        return tuple(tuple(sumfield(F.mul(A[i][k],B[k][j]) for k in range(n)) for j in range(n)) for i in range(n))
    fibers=Counter(multiply(A,B) for A in T for B in T)
    def classify(P):
        if P==eye:return q**n-1,'id'
        N=[[F.minus(P[i][j],eye[i][j]) for j in range(n)] for i in range(n)]
        r=rank_rows(N,F)
        if r==1:return q-2,'transvection'
        if r!=2:return 0,'rank-other'
        cols=[tuple(N[i][j] for i in range(n)) for j in range(n)]; W=[]
        for v in cols:
            if rank_rows(W+[v],F)>len(W):W.append(v)
        u,v=W
        if bil(u,v):
            eig=0
            for a,b in lines(2,F):
                z=tuple(F.plus(F.mul(a,u[i]),F.mul(b,v[i])) for i in range(n))
                if rank_rows([z,mv(P,z)],F)==1:eig+=1
            return q+1-eig,'nondeg'
        pre=[]
        for j in range(n):
            e=tuple(int(i==j) for i in range(n))
            if rank_rows([mv(N,z) for z in pre+[e]],F)>len(pre):pre.append(e)
            if len(pre)==2:break
        c=0
        for a,b in lines(2,F):
            z=tuple(F.plus(F.mul(a,pre[0][i]),F.mul(b,pre[1][i])) for i in range(n))
            if bil(mv(N,z),z):c+=1
        return c,'isotropic'
    bad=[];hist=Counter()
    for P,c in fibers.items():
        expected,kind=classify(P)
        hist[(kind,c)]+=1
        if expected!=c:bad.append((kind,c,expected))
    assert not bad,bad[:5]
    D=q**(2*m-2)*(q**(2*m)-1)//(q*q-1)
    I=(q**(2*m)-1)*(q**(2*m-2)-1)//((q-1)*(q*q-1))
    pred=Counter({'id':1})
    if q>2:pred['transvection']=q**(2*m)-1
    if p%2:
        pred['nondeg']=D*(q**3-q*q-q-1)
        pred['isotropic']=I*q*q*(q-1)
    else:
        pred['nondeg']=D*(q**3-q*q-q)
        pred['isotropic']=I*(q-1)*(q*q-1)
    actual=Counter()
    for (t,c),z in hist.items():actual[t]+=z
    assert all(actual.get(k,0)==v for k,v in pred.items()),(actual,pred)
    assert sum(pred.values())==len(fibers)
    assert sum(c*z for (_,c),z in hist.items())==len(T)**2
    print('PASS',f'GF({q})','dimension',n,'transvections',len(T), 'pairs',len(T)**2,'image',len(fibers),'type_histogram',dict(actual),'fiber_histogram',dict(sorted(hist.items())))
    return fibers

if __name__=='__main__':
    for args in [(2,1,1),(3,1,1),(5,1,1),(7,1,1),(2,2,1),(3,2,1),
                 (2,1,2),(3,1,2),(2,2,2),(2,1,3)]:
        run(*args)
    print('ALL FINITE CHECKS PASSED')
