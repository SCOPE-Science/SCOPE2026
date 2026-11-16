#!/usr/bin/env python3
"""Exact finite checks of connected fixed-cycle-rank spectra on K_(2,n)."""
from math import comb,isqrt
from collections import Counter

def K(r,u,q):
    return sum((-1)**j*comb(u,j)*comb(q-u,r-j) for j in range(max(0,r-(q-u)), min(u,r)+1))

def predicted(n,k,m):
    t=0;u=0;signprod=1
    for j in range(n):
        a = -1 if (m >> (2*j)) & 1 else 1
        b = -1 if (m >> (2*j+1)) & 1 else 1
        if a != b: t+=1
        else:
            if a==-1: u+=1
            signprod*=a
    if t>k+1:return 0
    return (-1)**t * (2**(n-k-1)) * signprod * K(k+1-t,u,n-t)

def brute_indicator(n,k):
    dim=2*n;N=1<<dim
    F=[0]*N
    for m in range(N):
        if m.bit_count()!=n+1+k:continue
        p=list(range(n+2))
        def root(i):
            while p[i]!=i:i=p[i];i=p[i]
            return i
        for j in range(n):
            for side in range(2):
                if (m>>(2*j+side))&1:
                    p[root(side)]=root(j+2)
        F[m]=int(len({root(i) for i in range(n+2)})==1)
    return F

def fwht(a):
    h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x=a[j];y=a[j+h]
                a[j]=x+y;a[j+h]=x-y
        h*=2

def main():
    count=0
    for n in range(2,9):
        for k in range(n):
            v=brute_indicator(n,k)
            assert sum(v)==comb(n,k+1)*(1<<(n-k-1)),(n,k,'count')
            fwht(v)
            pred=[predicted(n,k,m) for m in range(1<<(2*n))]
            assert v==pred,(n,k,[(i,a,b) for i,(a,b) in enumerate(zip(v,pred)) if a!=b][:4])
            nonzero=[abs(x) for x in v if x]
            assert min(nonzero)==2**(n-k-1),(n,k,'min')
            assert max(nonzero)==comb(n,k+1)*2**(n-k-1),(n,k,'max')
            assert sum(x*x for x in v)==(1<<(2*n))*comb(n,k+1)*(1<<(n-k-1)),(n,k,'parseval')
            if k==1:
                rank=(1<<n)*(1+n+comb(n,2))
                if n%2:rank-=2*n*comb(n-1,(n-1)//2)
                r=isqrt(n)
                if r*r==n:rank-=2*comb(n,(n-r)//2)
                assert len(nonzero)==rank,(n,k,'unicyclic',len(nonzero),rank)
            count+=len(v)
            print('n=',n,'k=',k,'N=',sum(1 for x in pred if x),'rank=',len(nonzero))
    print('CONNECTED_FIXED_EXCESS_KRAWTCHOUK_PASS coefficients=',count)
if __name__=='__main__':main()
