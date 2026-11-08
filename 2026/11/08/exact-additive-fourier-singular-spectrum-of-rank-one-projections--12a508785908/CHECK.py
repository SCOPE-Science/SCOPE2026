#!/usr/bin/env python3
"""Exact cyclotomic check of the rank-one-idempotent Fourier formula.

Usage: python idempotent_fourier_checker.py
Standard-library only. The test cases are finite; the written proof is universal.
"""
from itertools import product
from collections import Counter
from math import cos, pi, isclose

class Field:
    def __init__(self, p, degree=1, poly=None):
        self.p, self.d, self.q = p, degree, p**degree
        self.poly = poly
        self.elements = range(self.q)
        self.add = [[self._add(a,b) for b in self.elements] for a in self.elements]
        self.mul = [[self._mul(a,b) for b in self.elements] for a in self.elements]
        self.neg = [next(b for b in self.elements if self.add[a][b]==0) for a in self.elements]
        self.inv = [None]+[next(b for b in self.elements if self.mul[a][b]==1) for a in range(1,self.q)]
        self.trace = [self._trace(a) for a in self.elements]
    def _add(self,a,b):
        p=self.p
        return sum((((a//(p**i))%p+(b//(p**i))%p)%p)*(p**i) for i in range(self.d))
    def _mul(self,a,b):
        p=self.p
        if self.d==1:return a*b%p
        x,y=a%p,a//p
        u,v=b%p,b//p
        c0,c1=self.poly
        return ((x*u-y*v*c0)%p)+p*((x*v+y*u-y*v*c1)%p)
    def pow(self,a,n):
        z=1
        while n:
            if n&1:z=self.mul[z][a]
            a=self.mul[a][a];n//=2
        return z
    def _trace(self,a):
        x,s=a,0
        for _ in range(self.d):
            s=self.add[s][x]
            x=self.pow(x,self.p)
        assert s<self.p
        return s

def matmul(F,X,Y):
    m,a=F.mul,F.add
    return (a[m[X[0]][Y[0]]][m[X[1]][Y[2]]],
            a[m[X[0]][Y[1]]][m[X[1]][Y[3]]],
            a[m[X[2]][Y[0]]][m[X[3]][Y[2]]],
            a[m[X[2]][Y[1]]][m[X[3]][Y[3]]])

def pairing(F,A,P):
    m,a=F.mul,F.add
    return a[a[m[A[0]][P[0]]][m[A[1]][P[2]]]][a[m[A[2]][P[1]]][m[A[3]][P[3]]]]

def eigenline_exponents(F,A):
    add,mul,inv=F.add,F.mul,F.inv
    out=[]
    for u in [(1,x) for x in F.elements]+[(0,1)]:
        v=(add[mul[A[0]][u[0]]][mul[A[1]][u[1]]],
           add[mul[A[2]][u[0]]][mul[A[3]][u[1]]])
        j=0 if u[0] else 1
        lam=mul[v[j]][inv[u[j]]]
        if all(v[i]==mul[lam][u[i]] for i in range(2)):
            out.append(F.trace[lam])
    return out

def predicted_histogram(F):
    # Exact multiplicities from conjugacy classes and trace-difference fibres.
    q,p=F.q,F.p
    h=Counter()
    h['zero_irreducible']=q*q*(q-1)**2//2
    h['scalar']=q
    h['jordan']=q*(q*q-1)
    if p==2:
        h['zero_split']=q**3*(q+1)//4
        h['split_2q']=q*q*(q+1)*(q-2)//4
    else:
        h['split_2q']=q*q*(q+1)*(q//p-1)//2
        for j in range(1,(p+1)//2):
            h[f'split_phase_{j}']=q**3*(q+1)//p
    assert sum(h.values())==q**4
    return h

def test(F):
    q,p=F.q,F.p
    mats=list(product(F.elements,repeat=4))
    projectors=[P for P in mats if F.add[P[0]][P[3]]==1 and matmul(F,P,P)==P]
    assert len(projectors)==q*(q+1)
    actual=Counter()
    for A in mats:
        bins=[0]*p
        for P in projectors:
            bins[F.trace[pairing(F,A,P)]]+=1
        E=eigenline_exponents(F,A)
        pred=[0]*p
        for z in E:pred[z]+=q
        diffs=[bins[i]-pred[i] for i in range(p)]
        assert len(set(diffs))==1, (F.q,A,bins,pred)
        if not E: key='zero_irreducible'
        elif len(E)==q+1: key='scalar'
        elif len(E)==1: key='jordan'
        else:
            assert len(E)==2
            d=(E[0]-E[1])%p
            if p==2:key='zero_split' if d else 'split_2q'
            elif d==0:key='split_2q'
            else:key=f'split_phase_{min(d,p-d)}'
        actual[key]+=1
        if key.startswith('zero'):
            assert len(set(bins))==1, (F.q,A,bins)
        else:
            assert len(set(bins))>1, (F.q,A,bins)
    expected=predicted_histogram(F)
    assert actual==expected, (actual,expected)
    nonzero=q**4-expected['zero_irreducible']-expected.get('zero_split',0)
    print(f'EXACT_CYCLOTOMIC_OK q={q} p={p} ambient={q**4} projectors={len(projectors)} rank={nonzero} histogram={dict(sorted(actual.items()))}')

if __name__=='__main__':
    for args in [(2,),(3,),(2,2,(1,1)),(5,),(7,),(3,2,(1,0))]:
        test(Field(*args))
    print('ALL_PROJECTOR_FOURIER_CHECKS_OK')
