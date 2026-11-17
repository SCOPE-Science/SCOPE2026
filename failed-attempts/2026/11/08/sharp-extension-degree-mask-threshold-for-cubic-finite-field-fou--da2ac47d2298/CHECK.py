#!/usr/bin/env python3
"""Independent exact finite-field incidence tests for polynomial Fourier measurements.
No external packages. Run: python3 CHECK.py
"""
from collections import defaultdict
from itertools import product
from math import isclose, pi
from cmath import exp

CHECKS = 0

def checked(condition, label):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)

class Field:
    def __init__(self,p,m=1):
        self.p,self.m,self.q=p,m,p**m
        if m!=1 and (p,m)!=(5,2): raise ValueError('supported tests: prime fields or F25')
        self.items=range(self.q)
    def add(self,a,b):
        p=self.p
        if self.m==1:return (a+b)%p
        return ((a%p+b%p)%p)+p*((a//p+b//p)%p)
    def neg(self,a):return self.mul(self.p-1,a)
    def sub(self,a,b):return self.add(a,self.neg(b))
    def mul(self,a,b):
        p=self.p
        if self.m==1:return (a*b)%p
        c,d=a%p,a//p;e,f=b%p,b//p
        return ((c*e+3*d*f)%p)+p*((c*f+d*e)%p)
    def sc(self,k,a):
        r=0
        for _ in range(k%self.p):r=self.add(r,a)
        return r
    def sq(self,a):return self.mul(a,a)
    def cube(self,a):return self.mul(self.sq(a),a)
    def invp(self,k):return pow(k,-1,self.p)

def matrix_rank_mod(mat,prime=1000003):
    a=[list(row) for row in mat];height=len(a);width=len(a[0]);r=0
    for j in range(width):
        k=next((i for i in range(r,height) if a[i][j]%prime),None)
        if k is None:continue
        a[r],a[k]=a[k],a[r]
        z=pow(a[r][j]%prime,-1,prime)
        for u in range(j,width):a[r][u]=a[r][u]*z%prime
        for i in range(r+1,height):
            z=a[i][j]
            if z:
                for u in range(j,width):a[i][u]=(a[i][u]-z*a[r][u])%prime
        r+=1
        if r==width:break
    return r

def incidence(F,lambdas,d):
    """Built directly from the polynomial differences, not reflection formula."""
    rows=[]
    inv2=F.invp(2)
    for lam in lambdas:
        groups=defaultdict(list)
        for s in F.items:
            a=F.sc(inv2,F.add(s,d));b=F.sc(inv2,F.sub(s,d))
            v=F.sub(F.add(F.cube(a),F.mul(lam,F.sq(a))),
                    F.add(F.cube(b),F.mul(lam,F.sq(b))))
            groups[v].append(s)
        for e in sorted(groups):
            members=set(groups[e]);rows.append([int(s in members) for s in F.items])
    return rows

def subgroup(F,lambdas):
    H={0};base=lambdas[0]
    for lam in lambdas[1:]:
        delta=F.sub(lam,base)
        H={F.add(h,F.sc(j,delta)) for h in H for j in range(F.p)}
    return H

def test_ranks(p,m,lambdas):
    F=Field(p,m)
    for k in range(1,len(lambdas)+1):
        chosen=lambdas[:k];H=subgroup(F,chosen)
        target=F.q-(F.q//len(H)-1)//2
        for d in F.items:
            if not d:continue
            A=incidence(F,chosen,d)
            r=matrix_rank_mod(A)
            checked(r==target, f'rank q={F.q}, d={d}, lambdas={chosen}, rank={r}, target={target}')
            # Direct root-set reflection validation for all observed fibers.
            for lam in chosen:
                C=F.sc(F.invp(3),F.sc(4,lam))
                R=lambda s:F.sub(F.neg(s),C)
                for s in F.items:
                    a=F.sc(F.invp(2),F.add(s,d));b=F.sc(F.invp(2),F.sub(s,d))
                    z=F.sub(F.add(F.cube(a),F.mul(lam,F.sq(a))),
                            F.add(F.cube(b),F.mul(lam,F.sq(b))))
                    ss=R(s);aa=F.sc(F.invp(2),F.add(ss,d));bb=F.sc(F.invp(2),F.sub(ss,d))
                    zz=F.sub(F.add(F.cube(aa),F.mul(lam,F.sq(aa))),
                             F.add(F.cube(bb),F.mul(lam,F.sq(bb))))
                    checked(z==zz,'reflection preserves cubic difference')
        print(f'FIELD q={F.q}, masks={k}, subgroup={len(H)}, per-d rank={target}, Hermitian rank={1+(F.q-1)*target}')

for p in (5,7,11,13):test_ranks(p,1,[0,1])
test_ranks(5,2,[0,1,5])

# A nonzero explicit Hermitian-kernel fiber for F25 with two masks, broken by the third.
F=Field(5,2);f=[0]*25
for s in F.items:
    v=s//5
    f[s]=1 if v==1 else (-1 if v==4 else 0)
checked(any(f),'nonzero witness')
for lam in (0,1):
    for row in incidence(F,[lam],1):checked(sum(v*w for v,w in zip(row,f))==0,'two-mask kernel witness')
checked(any(sum(v*w for v,w in zip(row,f))!=0 for row in incidence(F,[5],1)),
        'third mask sees kernel witness')

# Check complex Fourier orthogonality against a direct coordinate-space sum for q=5,7.
for p in (5,7):
    F=Field(p);zeta=exp(2j*pi/p)
    # Arbitrary Hermitian test matrix, with nontrivial diagonal and imaginary part.
    M=[[0j]*p for _ in range(p)]
    for a in range(p):
        M[a][a]=complex((a*a+3*a+1)%11,0)
        for b in range(a):
            z=complex((2*a+b+1)%7-3,(a+2*b+3)%7-3)
            M[a][b]=z;M[b][a]=z.conjugate()
    for lam in (0,1):
        # Explicit character phase uses polynomial, not the reflection reduction.
        y=[]
        for x,t in product(range(p),repeat=2):
            z=0j
            for a,b in product(range(p),repeat=2):
                ph=(x*(a-b)+t*(a**3-b**3+lam*(a*a-b*b)))%p
                z+=M[a][b]*(zeta**ph)
            checked(abs(z.imag)<1e-7,'Hermitian measurement is real')
            y.append(z)
        lhs=sum(abs(z)**2 for z in y)/(p*p)
        coeff=defaultdict(complex)
        for a,b in product(range(p),repeat=2):
            d=(a-b)%p;e=(a**3-b**3+lam*(a*a-b*b))%p
            coeff[(d,e)]+=M[a][b]
        rhs=sum(abs(z)**2 for z in coeff.values())
        checked(isclose(lhs,rhs,rel_tol=1e-11,abs_tol=1e-7),'Fourier Parseval and measurement normalization')
print(f'CHECK_OK exact_and_numeric_assertions={CHECKS}')
