#!/usr/bin/env python3
"""Reproducible checks for modular dihedral-quandle idempotents.

Requires Python 3 standard library only.  Finite checks do not prove the
all-prime assertion; the proof is the truncated logarithm argument.
"""
from itertools import product

def mul(a, b, p):
    out=[0]*p
    for i,ai in enumerate(a):
        if ai:
            for j,bj in enumerate(b):
                if bj and i+j<p: out[i+j]=(out[i+j]+ai*bj)%p
    return out

def powpoly(a,n,p):
    out=[1]+[0]*(p-1)
    while n:
        if n&1: out=mul(out,a,p)
        a=mul(a,a,p); n//=2
    return out

def substitute(a,c,p):
    # The group-algebra parameter is t=1+u, so t^c-1 is substituted for u.
    z=powpoly([1,1]+[0]*(p-2),c%p,p)
    z[0]=(z[0]-1)%p
    out=[0]*p; power=[1]+[0]*(p-1)
    for aj in a:
        for i,x in enumerate(power): out[i]=(out[i]+aj*x)%p
        power=mul(power,z,p)
    return out

def rank_nullbasis(m,p):
    A=[row[:] for row in m]; n=len(A); piv=[]; r=0
    for j in range(n):
        ip=next((i for i in range(r,n) if A[i][j]%p),None)
        if ip is None: continue
        A[r],A[ip]=A[ip],A[r]
        t=pow(A[r][j],-1,p)
        A[r]=[(x*t)%p for x in A[r]]
        for i in range(n):
            if i!=r and A[i][j]:
                t=A[i][j]
                A[i]=[(x-t*y)%p for x,y in zip(A[i],A[r])]
        piv.append(j); r+=1
    free=[j for j in range(n) if j not in piv]
    bs=[]
    for j in free:
        x=[0]*n; x[j]=1
        for i,k in enumerate(piv): x[k]=(-A[i][j])%p
        bs.append(x)
    return bs

def exp_poly(a,p):
    out=[1]+[0]*(p-1); x=[1]+[0]*(p-1); fact=1
    for j in range(1,p):
        x=mul(x,a,p); fact=fact*j%p
        inv=pow(fact,-1,p)
        out=[(v+inv*w)%p for v,w in zip(out,x)]
    return out

def operator_kernel(p):
    M=[]
    for j in range(1,p):
        x=[0]*p; x[j]=1
        sm=substitute(x,p-1,p); sp=substitute(x,2,p)
        M.append([(x[i]-sm[i]-sp[i])%p for i in range(1,p)])
    rows=list(map(list,zip(*M)))
    return rank_nullbasis(rows,p)

def direct_idempotent(v,p):
    # coefficients in the original basis t^i, not the u=t-1 basis.
    x=[0]*p
    for i,a in enumerate(v):
        if a:
            for j,b in enumerate(v): x[(2*j-i)%p]=(x[(2*j-i)%p]+a*b)%p
    return x==list(v)

def order2(p):
    o=1; x=2%p
    while x!=1:
        x=x*2%p; o+=1
    return o

def binom(n,k,p):
    from math import comb
    return comb(n,k)%p

def to_t_coeffs(uc,p):
    # u^j=(t-1)^j modulo t^p-1.
    v=[0]*p
    for j,a in enumerate(uc):
        for i in range(j+1):
            v[i]=(v[i]+a*binom(j,i,p)*(-1)**(j-i))%p
    return v

def main():
    for p in [3,5,7,11,13,17,19,31,127]:
        basis=operator_kernel(p)
        ell=order2(p); L=ell if ell%2==0 else 2*ell
        d=1+(p-2)//L
        assert len(basis)==d,(p,len(basis),d)
        if p<=31:
            for b in basis:
                h=[0]+b
                assert substitute(h,p-1,p)==[(-x)%p for x in h]
                assert substitute(h,2,p)==[(2*x)%p for x in h]
            for b in basis:
                f=exp_poly([0]+b,p)
                assert direct_idempotent(to_t_coeffs(f,p),p),p
            if len(basis)>1:
                f=exp_poly([0]+[(basis[0][i]+3*basis[1][i])%p for i in range(p-1)],p)
                assert direct_idempotent(to_t_coeffs(f,p),p),p
                u=[0]+basis[0]
                v=[0]+basis[1]
                x=exp_poly(u,p); y=exp_poly(v,p)
                xy=mul(substitute(x,p-1,p),substitute(y,2,p),p)
                wanted=exp_poly([(2*bb-aa)%p for aa,bb in zip(u,v)],p)
                assert xy==wanted,p
        print(f'p={p}: order_2={ell}, d={d}, q=p count={p**d+1}')
    for p in [3,5]:
        count=sum(direct_idempotent(v,p) for v in product(range(p),repeat=p))
        d=len(operator_kernel(p))
        assert count==p**d+1,(p,count,p**d+1)
        print(f'exhaustive p={p}: {count} idempotents')
    print('VERIFY_OK')
if __name__=='__main__': main()
