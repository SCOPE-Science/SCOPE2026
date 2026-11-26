#!/usr/bin/env python3
"""Exact cyclotomic arithmetic check for Möbius ladder mixing ranks.
This checks finite orders only; the manuscript supplies the all-order proof.
Requires only the Python standard library.
"""
from functools import lru_cache


def trim(a):
    while len(a)>1 and a[-1]==0: a.pop()
    return a


def divide_monic(a,b):
    a=trim(list(a));b=trim(list(b));q=[0]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and a!=[0]:
        d=len(a)-len(b);c=a[-1]
        q[d]=c
        for j,v in enumerate(b):a[d+j]-=c*v
        trim(a)
    return trim(q),a


@lru_cache(None)
def cyclo(n):
    pol=[-1]+[0]*(n-1)+[1]
    for d in range(1,n):
        if n%d==0:
            pol,r=divide_monic(pol,cyclo(d))
            assert r==[0]
    return tuple(pol)


def rem(a,b):
    return tuple(divide_monic(a,b)[1])


def profile(n):
    N=2*n;mod=cyclo(N)
    vals=[]
    for k in range(N):
        poly=[0]*N
        poly[k]+=1;poly[(N-k)%N]+=1;poly[0]+=(-1)**k
        vals.append(rem(poly,mod))
    groups={}
    for k,v in enumerate(vals): groups.setdefault(v,[]).append(k)
    counts=[0]*N
    cross=[]
    for g in groups.values():
        if {k%2 for k in g}=={0,1}:cross.append(tuple(g))
        for k in g:
            for l in g:counts[(k+l)%N]+=1
    rk=sum(int(t>0) for t in counts)
    exp=n+(3 if n%2==1 and n%3==0 else 2 if n%4==2 else 0)
    assert rk==exp,(n,rk,exp,groups)
    assert all(counts[2*j]>0 for j in range(n))
    expected=set(range(0,N,2))
    if n%2==1 and n%3==0:
        expected.update([n//3,n,5*n//3])
    if n%4==2:
        expected.update([n//2,3*n//2])
    assert {q for q,c in enumerate(counts) if c>0}==expected,(n,counts)
    for g in cross:
        assert (n%2==1 and n%3==0 and len(g)==4) or (n%4==2 and len(g)==3)
    return len(groups),len(cross)


def main():
    exceptions=0
    for n in range(3,121):
        g,c=profile(n);exceptions+=int(c>0)
    print('VERIFY_OK exact_cyclotomic_orders=118 graph_vertices=6..240 exceptional_orders=',exceptions)

if __name__=='__main__':main()
