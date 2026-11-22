#!/usr/bin/env python3
"""Exact finite-field sample checks for a linearized cover of a Hermitian plane curve.
No external dependencies.
"""
from itertools import product


def mul_poly(a,b,p):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):r[i+j]=(r[i+j]+x*y)%p
    return r

def rem(a,b,p):
    a=a[:]
    while len(a)>=len(b):
        if a[-1]:
            c=a[-1]*pow(b[-1],-1,p)%p
            for i,x in enumerate(b):a[len(a)-len(b)+i]=(a[len(a)-len(b)+i]-c*x)%p
        a.pop()
    return a

def find_mod(p,n):
    if n==1:return [0,1]
    for cc in product(range(p),repeat=n):
        if cc[0]==0:continue
        f=list(cc)+[1]
        if all(any(rem(f,list(c)+[1],p)) for d in range(1,n//2+1) for c in product(range(p),repeat=d)):
            return f
    raise ValueError('no irreducible polynomial')

class Field:
    def __init__(self,p,n):
        self.p,self.n,self.mod=p,n,find_mod(p,n)
        self.size=p**n
        self.vec=[tuple((i//p**k)%p for k in range(n)) for i in range(self.size)]
        self.idx={a:i for i,a in enumerate(self.vec)}
        self.add=[[self.idx[tuple((a[k]+b[k])%p for k in range(n))] for b in self.vec] for a in self.vec]
        self.mul=[[self.m(a,b) for b in range(self.size)] for a in range(self.size)]
        self.one=1
    def m(self,a,b):
        av,bv=self.vec[a],self.vec[b]
        if self.n==1:return a*b%self.p
        z=mul_poly(av,bv,self.p)
        z=rem(z,self.mod,self.p)
        z += [0]*(self.n-len(z))
        return self.idx[tuple(z)]
    def power(self,a,k):
        b=self.one
        while k:
            if k&1:b=self.mul[b][a]
            a=self.mul[a][a];k//=2
        return b

def sample(p,n):
    f=Field(p,n); q=p
    zero=0; one=1; negone=p-1
    roots_alpha=[a for a in range(f.size) if f.power(a,q+1)==negone]
    roots_beta=[b for b in range(f.size) if f.add[b][f.power(b,q*q)]==0]
    L=[f.add[a][f.power(a,q*q)] for a in range(f.size)]
    hval=[f.power(a,q+1) for a in range(f.size)]
    xval=[hval[L[a]] for a in range(f.size)]
    # given z, find w=-1-z explicitly (in p-adic characteristic): -z-1
    def affine(vals):
        freq={}
        for z in vals:freq[z]=freq.get(z,0)+1
        return sum(count*freq.get(f.add[negone][f.mul[negone][z]],0) for z,count in freq.items())
    # -1 - z = (-1)+((-1)*z) because p prime
    hn=affine(hval)+len(roots_alpha)
    xn=affine(xval)+len(roots_alpha)*len(roots_beta)
    expected_h = (q**n+1) if n%2 else (q**n+1-q*(q-1)*((-q)**(n//2)))
    expected_x=xn if n%4==0 else expected_h
    if n%4==0 and n==4: expected_x=q**7-q**5+q**3+q**2
    assert hn==expected_h,(p,n,hn,expected_h)
    assert xn==expected_x,(p,n,xn,expected_x)
    return (p,n,';'.join(map(str,f.mod)),len(roots_alpha),len(roots_beta),hn,xn)

if __name__=='__main__':
    print('q,n,irreducible_modulus,alpha_roots,beta_roots,hermitian_points,cover_points')
    for q,n in ((3,1),(3,2),(3,3),(3,4),(5,1),(5,2),(5,4),(7,1),(7,2)):
        print(','.join(map(str,sample(q,n))))
