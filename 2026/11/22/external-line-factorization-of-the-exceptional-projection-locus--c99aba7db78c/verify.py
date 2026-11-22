#!/usr/bin/env python3
"""Exact finite-field checks for the external-line exceptional-center identity.
Requires only the Python standard library. Exhaustive for indicated small fields;
the general theorem is proved separately by a degree-and-divisibility argument.
"""
from itertools import product, combinations
from collections import Counter

class Field:
    def __init__(self, q):
        assert q in (2, 3, 4, 5, 7, 8)
        self.q=q
        self.binary=q in (2,4,8)
        self.mod={2:0b11,4:0b111,8:0b1011}.get(q)
    def add(self,a,b):return (a^b) if self.binary else (a+b)%self.q
    def neg(self,a):return a if self.binary else (-a)%self.q
    def sub(self,a,b):return self.add(a,self.neg(b))
    def mul(self,a,b):
        if not self.binary:return (a*b)%self.q
        out=0
        while b:
            if b&1:out^=a
            a<<=1
            if a&self.q:a^=self.mod
            b>>=1
        return out
    def pow(self,a,n):
        out=1
        while n:
            if n&1:out=self.mul(out,a)
            a=self.mul(a,a); n>>=1
        return out
    def inv(self,a):
        assert a
        return self.pow(a,self.q-2)
    def sum(self,arr):
        z=0
        for x in arr:z=self.add(z,x)
        return z
    def dot(self,a,b):return self.sum(self.mul(x,y) for x,y in zip(a,b))
    def det(self,u,v,w):
        F=self
        a=F.sub(F.mul(v[1],w[2]), F.mul(v[2],w[1]))
        b=F.sub(F.mul(v[2],w[0]), F.mul(v[0],w[2]))
        c=F.sub(F.mul(v[0],w[1]), F.mul(v[1],w[0]))
        return F.dot(u,(a,b,c))
    def cross(self,v,w):
        F=self
        return (F.sub(F.mul(v[1],w[2]),F.mul(v[2],w[1])),
                F.sub(F.mul(v[2],w[0]),F.mul(v[0],w[2])),
                F.sub(F.mul(v[0],w[1]),F.mul(v[1],w[0])))
    def normalize(self,v):
        k=next(a for a in v if a)
        return tuple(self.mul(a,self.inv(k)) for a in v)

ZERO=(0,0,0)
ONE={(0,0,0):1}

def poly_add(A,B,F):
    R=dict(A)
    for m,c in B.items():
        R[m]=F.add(R.get(m,0),c)
        if not R[m]:del R[m]
    return R

def poly_mul(A,B,F):
    R={}
    for i,a in A.items():
        for j,b in B.items():
            ij=tuple(x+y for x,y in zip(i,j))
            R[ij]=F.add(R.get(ij,0),F.mul(a,b))
            if not R[ij]:del R[ij]
    return R

def linear(h):return {tuple(1 if i==j else 0 for i in range(3)):a for j,a in enumerate(h) if a}

def scalar(A,c,F):return {m:F.mul(a,c) for m,a in A.items() if F.mul(a,c)}

def data(q):
    F=Field(q)
    V=[(1,t,F.mul(t,t)) for t in range(q)]+[(0,0,1)]
    assert len(set(V))==q+1
    U=sorted({F.normalize(v) for v in product(range(q),repeat=3) if any(v)})
    ext=[h for h in U if all(F.dot(h,v)!=0 for v in V)]
    assert len(ext)==q*(q-1)//2,(q,len(ext))
    # The projectivized bad-center polynomial, computed from the augmented
    # degree-(q-1) Vandermonde evaluation determinant.
    pairs={ij:linear(F.cross(V[ij[0]],V[ij[1]])) for ij in combinations(range(q+1),2)}
    D={}
    for i in range(q+1):
        term=ONE
        for (j,k),Lin in pairs.items():
            if i not in (j,k):term=poly_mul(term,Lin,F)
        if i%2==0:term=scalar(term,F.neg(1),F)
        D=poly_add(D,term,F)
    E=ONE
    for h in ext:E=poly_mul(E,linear(h),F)
    assert D and E
    pivot=next(iter(D))
    assert pivot in E
    ratio=F.mul(D[pivot],F.inv(E[pivot]))
    assert D==scalar(E,ratio,F),(q,D,E)
    # Check the complete geometric intersection profile: all line pairs
    # meet in rational points because all lines are rational.
    hist=Counter(sum(F.dot(h,u)==0 for h in ext) for u in U)
    if q%2:
        target=Counter({0:q+1,(q-1)//2:q*(q+1)//2,(q+1)//2:q*(q-1)//2})
    else:
        target=Counter({0:q+2,q//2:q*q-1})
    # Multiplicities 0 and 1 can coincide in the special q=2,3 cases.
    counts=Counter()
    if q%2:
        for r,c in [(0,q+1),((q-1)//2,q*(q+1)//2),((q+1)//2,q*(q-1)//2)]:counts[r]+=c
    else:
        for r,c in [(0,q+2),(q//2,q*q-1)]:counts[r]+=c
    assert hist==counts,(q,hist,counts)
    print(f'GF({q}): {len(V)} conic directions, {len(ext)} external lines, '
          f'factorization degree {len(ext)}, intersection histogram {dict(sorted(hist.items()))}, PASS')

if __name__=='__main__':
    for q in [2,3,4,5,7,8]:data(q)
