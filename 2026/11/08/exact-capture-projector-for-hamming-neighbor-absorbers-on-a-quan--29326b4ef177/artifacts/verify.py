#!/usr/bin/env python3
"""Exact finite tests of the Hamming-shell capture projector."""
from fractions import Fraction as F
from math import comb


def choose(n,r):
    return comb(n,r) if 0<=r<=n else 0


def K(d,j,k):
    return sum((-1)**s*choose(k,s)*choose(d-k,j-s) for s in range(j+1))


def prediction_B(d):
    return d*d-d+2-int(d%2==0)


def kernel(d,x,y):
    k=x.bit_count();ell=y.bit_count();v=F(0)
    if k==ell:
        v+=F(1,choose(d,k))
        if 1<=k<=d-1:
            intersection=(x&y).bit_count()
            v+=F(d*(d-1),choose(d,k)*k*(d-k))*(intersection-F(k*k,d))
    if d%2==0:
        q=d//2
        v-=F(K(d,q,k)*K(d,q,ell),2**d*choose(d,q))
    return v


def spectral_kernel(d,x,y):
    # Separate spectral Gram pseudoinverse of P_j restricted to all traps.
    total=F(0)
    for j in range(d+1):
        scale=2**d
        diag=F(choose(d,j),scale)
        off=F(K(d,j,2),scale)
        std=diag-off;triv=diag+(d-1)*off
        vx=[F(K(d,j,(x^(1<<i)).bit_count()),scale) for i in range(d)]
        vy=[F(K(d,j,(y^(1<<i)).bit_count()),scale) for i in range(d)]
        sx=sum(vx);sy=sum(vy)
        if triv:total+=sx*sy/(d*triv)
        if std:total+=(sum(a*b for a,b in zip(vx,vy))-sx*sy/d)/std
    return total


def rank_mod_prime(rows,p):
    a=[[x%p for x in r] for r in rows]
    h=len(a);w=len(a[0]);rank=0
    for col in range(w):
        piv=next((i for i in range(rank,h) if a[i][col]),None)
        if piv is None:continue
        a[rank],a[piv]=a[piv],a[rank]
        inv=pow(a[rank][col],-1,p)
        a[rank]=[v*inv%p for v in a[rank]]
        for i in range(rank+1,h):
            if a[i][col]:
                c=a[i][col]; a[i]=[(a[i][q]-c*a[rank][q])%p for q in range(w)]
        rank+=1
        if rank==h:break
    return rank


def krylov_rank(d):
    n=1<<d;cols=[]
    for bit in range(d):
        v=[int(x==(1<<bit)) for x in range(n)]
        for power in range(d+1):
            cols.append(v)
            v=[sum(v[x^(1<<q)] for q in range(d)) for x in range(n)]
    return rank_mod_prime([[col[x] for col in cols] for x in range(n)],1000003)


def main():
    checked=0;rank_checks=0
    for d in range(2,8):
        n=1<<d
        for x in range(n):
            for y in range(n):
                actual=spectral_kernel(d,x,y)
                expect=kernel(d,x,y)
                assert actual==expect,(d,x,y,actual,expect)
                checked+=1
        assert sum(kernel(d,x,x) for x in range(n))==prediction_B(d)
        assert krylov_rank(d)==prediction_B(d)
        rank_checks+=1
    print('VERIFY_OK exact_projector_entries=%d modular_krylov=%d'%(checked,rank_checks))

if __name__=='__main__':main()
