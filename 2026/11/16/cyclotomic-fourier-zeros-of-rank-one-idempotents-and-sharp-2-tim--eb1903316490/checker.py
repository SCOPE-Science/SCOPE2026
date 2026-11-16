#!/usr/bin/env python3
"""Direct finite-field enumeration of rank-one-idempotent orbital character sums.
Python 3 standard library only. No external tables.
"""
import itertools
import cmath
import math
from collections import Counter

class Field:
    def __init__(self,q):
        assert q in (2,3,4,5,7)
        self.q=q
        self.p=2 if q in (2,4) else q
    def add(self,a,b):return (a^b) if self.q==4 else (a+b)%self.q
    def mul(self,a,b):
        if self.q!=4:return a*b%self.q
        raw=0
        for i in range(2):
            if (b>>i)&1:raw^=a<<i
        if raw&8:raw^=0b1110 # reduce x^3 using x(x^2+x+1)
        if raw&4:raw^=0b111
        return raw
    def trace(self,a):return ((a>>1)&1) if self.q==4 else a
    def dot(self,u,v):
        z=0
        for a,b in zip(u,v):z=self.add(z,self.mul(a,b))
        return z
    def smat(self,A,u):return tuple(self.dot(row,u) for row in A)

def hist_fourier_direct(F,n,P,X):
    h=[0]*F.p
    for u in P:
        # P encoded row-major, pairing trace(XP)=sum_i,j X_ij P_ji
        v=0
        for i in range(n):
            for j in range(n):
                v=F.add(v,F.mul(X[i][j],u[j*n+i]))
        h[F.trace(v)]+=1
    return tuple(h)

def hist_fourier_eigen(F,n,X):
    h=[0]*F.p
    for lam in range(F.q):
        count=0
        for u in itertools.product(range(F.q), repeat=n):
            if all(a==0 for a in u):continue
            if F.smat(X,u)==tuple(F.mul(lam,a) for a in u):count+=1
        assert count%(F.q-1)==0
        h[F.trace(lam)]+=F.q**(n-1)*(count//(F.q-1))
    return tuple(h)

def create_orbit(F,n):
    out=set()
    vlist=list(itertools.product(range(F.q),repeat=n))
    for u in vlist:
        if all(x==0 for x in u):continue
        for v in vlist:
            if F.dot(v,u)==1:
                P=tuple(F.mul(u[i],v[j]) for i in range(n) for j in range(n))
                out.add(P)
    assert len(out)==(F.q**n-1)*F.q**(n-1)//(F.q-1)
    return sorted(out)

def norm_formula(q,p):
    if p==2:return (q+1)/2
    return (q+1)/p/math.sin(math.pi/(2*p))

def run(q,n):
    F=Field(q)
    Ps=create_orbit(F,n)
    tested=0
    zeros=0
    abssum=0.
    for raw in itertools.product(range(q),repeat=n*n):
        X=tuple(tuple(raw[i*n:(i+1)*n]) for i in range(n))
        a=hist_fourier_direct(F,n,Ps,X)
        b=hist_fourier_eigen(F,n,X)
        assert len(set(x-y for x,y in zip(a,b)))==1,(q,n,X,a,b)
        # Cyclotomic vanish iff all character coefficients equal.
        zero=len(set(a))==1
        zeros+=zero
        z=sum(c*cmath.exp(2j*math.pi*i/F.p) for i,c in enumerate(a))
        assert (abs(z)<1e-6)==zero,(q,n,X,a)
        abssum+=abs(z)
        tested+=1
    if n==2:
        expected=q*q*(q-1)**2//2
        if F.p==2:expected+=q**3*(q+1)//4
        assert zeros==expected,(q,zeros,expected)
        expected_norm=norm_formula(q,F.p)
        assert abs(abssum/(q**4)-expected_norm)<1e-9,(q,abssum/(q**4),expected_norm)
    print('q',q,'n',n,'orbit',len(Ps),'frequencies',tested,'zeros',zeros,'norm',f'{abssum/(q**(n*n)):.12f}')

if __name__=='__main__':
    for q,n in [(2,2),(3,2),(4,2),(5,2),(7,2),(2,3)]:run(q,n)
    print('RANK_ONE_IDEMPOTENT_ORBIT_FOURIER_EXACT_CHECKS_PASS')
