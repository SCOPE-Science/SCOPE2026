#!/usr/bin/env python3
"""Independent checks for the quadratic Veronese Fourier projector."""
from itertools import product
from fractions import Fraction
from math import prod, sqrt, pi
from cmath import exp

def gaussian_binomial(q,n,r):
    return int(prod(Fraction(q**(n-i)-1,q**(r-i)-1) for i in range(r)))
def nonsingular(q,r):
    s=Fraction(q**(r*(r+1)//2))
    for j in range(1,(r+1)//2+1):s*=Fraction(q**(2*j-1)-1,q**(2*j-1))
    assert s.denominator==1
    return int(s)
def rank_count(q,n,r):return gaussian_binomial(q,n,r)*nonsingular(q,r)
def formula_norm(q,n):
    total=0.0
    for r in range(n+1):
        N=rank_count(q,n,r)
        if r%2==0:
            s=r//2
            total+=N*(q**(n-s)+q**(-s))
        elif q%4==1:
            total+=N*q**(n-r/2)
        else:
            total+=N*sqrt(1+q**(2*n-r))
    return total/(2*q**(n*(n+1)//2))

def rank_mod(a,p):
    mat=[row[:] for row in a];n=len(a);r=0
    for j in range(n):
        pivot=next((i for i in range(r,n) if mat[i][j]%p),None)
        if pivot is None:continue
        mat[r],mat[pivot]=mat[pivot],mat[r]
        inv=pow(mat[r][j]%p,-1,p)
        for i in range(r+1,n):
            z=(mat[i][j]*inv)%p
            for k in range(j,n):mat[i][k]=(mat[i][k]-z*mat[r][k])%p
        r+=1
    return r

def check(p,n):
    cone=set()
    for v in product(range(p),repeat=n):
        cone.add(tuple(v[i]*v[j]%p for i in range(n) for j in range(i,n)))
    assert len(cone)==(p**n+1)//2
    roots=[exp(2j*pi*k/p) for k in range(p)]
    counts=[0]*(n+1)
    abs_sum=0.0;square_sum=0.0
    for c in product(range(p),repeat=n*(n+1)//2):
        a=[[0]*n for _ in range(n)];ix=0
        for i in range(n):
            for j in range(i,n):
                a[i][j]=a[j][i]=c[ix];ix+=1
        r=rank_mod(a,p)
        counts[r]+=1
        val=0j
        for b in cone:
            ix=0;dot=0
            for i in range(n):
                for j in range(i,n):
                    dot+=(1 if i==j else 2)*c[ix]*b[ix];ix+=1
            val+=roots[dot%p]
        mag=abs(val)
        if r%2==1 and p%4==3:
            expmag=sqrt(1+p**(2*n-r))/2
            assert abs(mag-expmag)<1e-8,(p,n,r,mag,expmag)
        else:
            x=p**(n-r/2)
            opts=((x+1)/2,abs(x-1)/2)
            assert min(abs(mag-y) for y in opts)<1e-8,(p,n,r,mag,opts)
        abs_sum+=mag;square_sum+=mag*mag
    for r,v in enumerate(counts):assert v==rank_count(p,n,r)
    full=p**(n*(n+1)//2)
    exact=formula_norm(p,n)
    assert abs(abs_sum/full-exact)<1e-8,(p,n,abs_sum/full,exact)
    assert abs(square_sum/full-len(cone))<1e-7
    print('p',p,'n',n,'sample',full,'cone',len(cone),'norm',exact,'PASS')

if __name__=='__main__':
    for p,n in ((3,1),(3,2),(3,3),(5,1),(5,2)):
        check(p,n)
    print('QUADRATIC_VERONESE_FOURIER_PASS')
