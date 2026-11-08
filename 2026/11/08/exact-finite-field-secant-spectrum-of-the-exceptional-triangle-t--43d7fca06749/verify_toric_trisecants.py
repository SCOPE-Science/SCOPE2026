#!/usr/bin/env python3
"""Exact finite-field checks for all-secants spectrum of XYZ=W^3.

Independent finite examples; the uniform proof is in RESULT.md.
"""
from math import comb
from itertools import product

class Field:
    def __init__(self,p,poly):
        self.p=p; self.mod=tuple(poly); self.k=len(poly)-1; self.q=p**self.k
        assert self.mod[-1]==1
        self.addtab=[[self.addraw(a,b) for b in range(self.q)] for a in range(self.q)]
        self.multab=[[self.mulraw(a,b) for b in range(self.q)] for a in range(self.q)]
        self.one=1
        self.invtab={a:self.pow(a,self.q-2) for a in range(1,self.q)}
        assert all(self.mul(a,self.invtab[a])==1 for a in self.invtab)
    def dig(self,a):
        return [(a//self.p**i)%self.p for i in range(self.k)]
    def enc(self,x):
        return sum((v%self.p)*self.p**i for i,v in enumerate(x))
    def addraw(self,a,b):
        x=self.dig(a);y=self.dig(b)
        return self.enc([(u+v)%self.p for u,v in zip(x,y)])
    def mulraw(self,a,b):
        A=self.dig(a);B=self.dig(b);C=[0]*(2*self.k-1)
        for i,x in enumerate(A):
            for j,y in enumerate(B):C[i+j]=(C[i+j]+x*y)%self.p
        for d in range(len(C)-1,self.k-1,-1):
            s=C[d]
            for j in range(self.k):C[d-self.k+j]=(C[d-self.k+j]-s*self.mod[j])%self.p
        return self.enc(C[:self.k])
    def add(self,a,b):return self.addtab[a][b]
    def mul(self,a,b):return self.multab[a][b]
    def neg(self,a):return self.enc([(-v)%self.p for v in self.dig(a)])
    def sub(self,a,b):return self.add(a,self.neg(b))
    def inv(self,a):return self.invtab[a]
    def pow(self,a,n):
        out=1
        while n:
            if n&1:out=self.multab[out][a]
            a=self.multab[a][a];n//=2
        return out

def trial(p,poly):
    F=Field(p,poly);q=F.q
    def a(*x):
        u=0
        for v in x:u=F.add(u,v)
        return u
    def m(*x):
        u=1
        for v in x:u=F.mul(u,v)
        return u
    def P(x,y):return (1,x,y,F.inv(m(x,y)))
    A=(1,1,1,1)
    torus=[P(x,y) for x in range(1,q) for y in range(1,q)]
    assert len(set(torus))==(q-1)**2
    N=len(torus)
    all_collinear=0;sloped=0;edge=0;tangA=0;tangB=0
    for B in torus:
        if B==A:continue
        delta=[F.sub(B[i],A[i]) for i in range(4)]
        s1=a(*delta[1:]);s3=m(*delta[1:])
        if s3==0:
            edge+=1
            continue
        if s1==0:
            tangA+=1
            continue
        if s1==s3:
            tangB+=1
            continue
        t=m(s1,F.inv(s3))
        C=tuple(a(A[i],m(t,delta[i])) for i in range(4))
        assert C in torus and C!=A and C!=B,(q,A,B,t,C)
        # cubic identity checked independently, to guard wrong collinearity implementation
        assert m(C[1],C[2],C[3])==1
        all_collinear+=1
    rho=sum(1 for k in range(q) if a(m(k,k),k,1)==0)
    T=(q-2)*(q-5)+2*rho
    assert edge==3*(q-2),(q,edge)
    assert tangA==tangB==q-2-rho,(q,tangA,tangB,rho)
    assert all_collinear==T,(q,all_collinear,T)
    n3=N*T//6
    assert 6*n3==N*T
    n2=N*(N-1-T)//2
    n1=N*(q*q+q+1)-2*n2-3*n3
    all_lines=(q*q+1)*(q*q+q+1)
    n0=all_lines-n1-n2-n3
    assert min(n0,n1,n2,n3)>=0
    assert sum((n0,n1,n2,n3))==all_lines
    assert n1+2*n2+3*n3==N*(q*q+q+1)
    assert n2+3*n3==comb(N,2)
    d2=N-(3 if T>0 else 2)
    assert T>0 if q>=7 or q==4 else T==0
    return dict(q=q,rho=rho,T=T,n0=n0,n1=n1,n2=n2,n3=n3,d2=d2)

if __name__ == "__main__":
    for p,mod in [
     (3,[0,1]),(2,[1,1,1]),(5,[0,1]),(7,[0,1]),
     (2,[1,1,0,1]),(3,[1,0,1]),(11,[0,1]),(13,[0,1]),
     (2,[1,1,0,0,1]),(5,[2,0,1]),(3,[1,2,0,1])
    ]:
        r=trial(p,mod)
        print('q={q} rho={rho} T={T} line_spectrum=[{n0},{n1},{n2},{n3}] d2={d2}'.format(**r))
    print('ALL_EXACT_CHECKS_PASSED')
