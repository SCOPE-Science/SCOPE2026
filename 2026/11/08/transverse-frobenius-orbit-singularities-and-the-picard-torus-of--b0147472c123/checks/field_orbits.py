#!/usr/bin/env python3
"""Exact finite-field replay for the symmetric-Frobenius rational curves.
Pure Python; no external packages or network access needed.
The mathematical proof of the all-q,n result is separate from these finite checks.
"""
from itertools import product
from math import prod
def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

def mobius(n):
    x=n; primes=0; p=2
    while p*p<=x:
        if x%p==0:
            x//=p; primes+=1
            if x%p==0:return 0
        p+=1
    if x>1:primes+=1
    return -1 if primes%2 else 1


def poly_rem(f,g,p):
    f=list(f)
    while len(f)>=len(g):
        a=f[-1]*pow(g[-1],-1,p)%p
        off=len(f)-len(g)
        for i,c in enumerate(g): f[off+i]=(f[off+i]-a*c)%p
        while f and not f[-1]: f.pop()
    return f


def irred(p,m):
    if m==1:return [0,1]
    divs=[]
    for k in range(1,m//2+1):
        divs.extend([list(v)+[1] for v in product(range(p),repeat=k)])
    for v in product(range(p),repeat=m):
        if v[0]==0: continue
        f=list(v)+[1]
        if all(poly_rem(f,g,p) for g in divs): return f
    raise RuntimeError('no irreducible polynomial')

class Field:
    def __init__(self,p,m):
        self.p,self.m,self.size=p,m,p**m
        self.mod=irred(p,m)
        self.digits=[self.unrank(i) for i in range(self.size)]
        self.add_table=None
    def unrank(self,a):
        v=[]
        for _ in range(self.m):v.append(a%self.p);a//=self.p
        return v
    def rank(self,v):
        return sum((a%self.p)*self.p**i for i,a in enumerate(v))
    def add(self,a,b):
        return self.rank([(x+y)%self.p for x,y in zip(self.digits[a],self.digits[b])])
    def neg(self,a):
        return self.rank([(-x)%self.p for x in self.digits[a]])
    def sub(self,a,b):return self.add(a,self.neg(b))
    def mul(self,a,b):
        if a==0 or b==0:return 0
        v=[0]*(2*self.m-1)
        for i,ai in enumerate(self.digits[a]):
            for j,bj in enumerate(self.digits[b]):v[i+j]=(v[i+j]+ai*bj)%self.p
        if self.m>1:
            for j in range(len(v)-1,self.m-1,-1):
                top=v[j]
                if top:
                    for k in range(self.m):v[j-self.m+k]=(v[j-self.m+k]-top*self.mod[k])%self.p
            v=v[:self.m]
        return self.rank(v)
    def power(self,a,e):
        v=1
        while e:
            if e&1:v=self.mul(v,a)
            a=self.mul(a,a);e//=2
        return v
    def inv(self,a):
        if not a:raise ZeroDivisionError
        return self.power(a,self.size-2)
    def pp(self,a,terms):
        c=[1]
        for x in terms:
            new=[0]*(len(c)+1)
            for j,y in enumerate(c):
                new[j]=self.sub(new[j],self.mul(y,x))
                new[j+1]=self.add(new[j+1],y)
            c=new
        return tuple(c)
    def rank_matrix(self,rows):
        a=[list(r) for r in rows]
        if not a:return 0
        pos=0
        for col in range(len(a[0])):
            pivot=next((i for i in range(pos,len(a)) if a[i][col]!=0),None)
            if pivot is None:continue
            a[pos],a[pivot]=a[pivot],a[pos]
            inv=self.inv(a[pos][col]);a[pos]=[self.mul(x,inv) for x in a[pos]]
            for i in range(len(a)):
                if i==pos:continue
                c=a[i][col]
                if c: a[i]=[self.sub(y,self.mul(c,x)) for x,y in zip(a[pos],a[i])]
            pos+=1
            if pos==len(a):break
        return pos

def expected(q,n):
    dcounts={d:sum(int(mobius(e))*q**(d//e) for e in divisors(d))//d for d in divisors(n) if d>1}
    dimension=sum((d-1)*v for d,v in dcounts.items())
    pic_order=prod(((q**d-1)//(q-1))**v for d,v in dcounts.items())
    return dcounts,dimension,pic_order

def verify(p,e,n):
    q=p**e
    F=Field(p,e*n)
    assert F.size==q**n
    reps={}; done=set(); histogram={}; tangent_ranks={}
    for x in range(F.size):
        if x in done:continue
        orbit=[];a=x
        while a not in done:
            orbit.append(a);done.add(a);a=F.power(a,q)
        assert a==x
        d=len(orbit)
        coeffs=[F.pp(0,[F.power(t,q**i) for i in range(n)]) for t in orbit]
        assert len(set(coeffs))==1
        image=coeffs[0]
        assert image not in reps, (q,n,d,image)
        assert all(F.power(c,q)==c for c in image)
        reps[image]=orbit
        vectors=[F.pp(0,[F.power(t,q**i) for i in range(1,n)]) for t in orbit]
        rk=F.rank_matrix(vectors)
        assert rk==d, (q,n,d,rk,vectors)
        tangent_ranks.setdefault(d,set()).add(rk)
        histogram[d]=histogram.get(d,0)+1
    assert len(done)==F.size
    assert len(reps)+1==q+1+sum(expected(q,n)[0].values())
    assert histogram.pop(1)==q
    dcounts,genus,pic=expected(q,n)
    assert histogram==dcounts, (histogram,dcounts)
    assert sum((d-1)*v for d,v in histogram.items())==genus
    assert all(rks=={d} for d,rks in tangent_ranks.items())
    print(f'q={q},n={n},size={F.size},polynomial={F.mod},orbits={dcounts},image_points={len(reps)+1},tangent_ranks={tangent_ranks},p_a={genus},#Pic0(Fq)={pic}')

if __name__=='__main__':
    for p,e,n in [(2,1,2),(2,1,3),(2,1,4),(2,1,5),(3,1,2),(3,1,3),(3,1,4),(2,2,3),(5,1,3)]:
        verify(p,e,n)
    print('ALL_INDEPENDENT_FINITE_CHECKS_PASSED')
