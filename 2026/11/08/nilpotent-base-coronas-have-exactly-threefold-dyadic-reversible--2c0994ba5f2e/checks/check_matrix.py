#!/usr/bin/env python3
"""Independent GF(2) rank verification for graph-corona reversible waves.
Usage: python check_matrix.py
"""
from itertools import combinations
from math import ceil, log2

def ident(n): return [1<<i for i in range(n)]
def zeros(n): return [0]*n
def mul(A,B):
    out=[]
    for row in A:
        accum=0
        while row:
            low=row & -row
            accum ^= B[low.bit_length()-1]
            row ^= low
        out.append(accum)
    return out

def powmat(A,k):
    acc=ident(len(A))
    while k:
        if k&1: acc=mul(acc,A)
        A=mul(A,A);k>>=1
    return acc

def add(A,B):return [a^b for a,b in zip(A,B)]
def rank(A):
    A=list(A); n=len(A); r=0
    for col in range(n):
        pivot=next((i for i in range(r,n) if A[i]>>col&1),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        for i in range(n):
            if i!=r and A[i]>>col&1:A[i]^=A[r]
        r+=1
    return r

def path(n):
    A=zeros(n)
    for i in range(n-1):A[i]^=1<<(i+1);A[i+1]^=1<<i
    return A

def cycle(n):
    A=path(n)
    A[0]^=1<<(n-1);A[-1]^=1
    return A

def cube(d):
    n=1<<d; A=zeros(n)
    for i in range(n):
        for j in range(d): A[i]^=1<<(i^(1<<j))
    return A

def blocks(B):
    n=len(B);powr=ident(n); ker=[0]
    for i in range(1,n+1):
        powr=mul(powr,B)
        ker.append(n-rank(powr))
        if ker[-1]==n:break
    if ker[-1]!=n:return None
    levels=[ker[i]-ker[i-1] for i in range(1,len(ker))]+[0]
    return [s for s in range(1,len(levels)) for _ in range(levels[s-1]-levels[s])]

def corona(B):
    n=len(B);A=zeros(2*n)
    for i in range(n):A[i]=B[i] | 1<<(n+i);A[n+i]=1<<i
    return A

def wave(A):
    n=len(A);T=zeros(2*n)
    for i in range(n):T[i]=A[i]|1<<(n+i);T[n+i]=1<<i
    return T

def expect_fixed(bs,t):
    if t%3:return 0
    low=t & -t
    return 2*sum(min(2*s,low) for s in bs)

def check(B):
    bs=blocks(B)
    if bs is None:
        T=wave(corona(B))
        for r in range(1,7):
            assert powmat(T,3*(1<<r))!=ident(len(T)),('unexpected threefold-power order',len(B),r)
        return False
    A=corona(B);T=wave(A);r=max((2*s-1).bit_length() for s in bs)
    assert rank(A)==len(A)
    order=3*(1<<r)
    assert powmat(T,order)==ident(len(T)),(len(B),bs,order)
    assert powmat(T,order//2)!=ident(len(T))
    for t in [1,2,3,4,6,12,24,48,96]:
        f=len(T)-rank(add(powmat(T,t),ident(len(T))))
        expected=expect_fixed(bs,t)
        assert f==expected,(len(B),bs,t,f,expected)
    return True

if __name__=='__main__':
    total=0; good=0; by_order={}
    for n in range(1,6):
        edges=list(combinations(range(n),2))
        for mask in range(1<<len(edges)):
            B=zeros(n)
            for j,(u,v) in enumerate(edges):
                if mask>>j&1:B[u]^=1<<v;B[v]^=1<<u
            total+=1
            if check(B):
                good+=1
                bs=blocks(B);order=3*(1<<max((2*s-1).bit_length() for s in bs))
                by_order[order]=by_order.get(order,0)+1
    print('all labelled simple graphs on 1..5 vertices:',total)
    print('nilpotent-base graphs checked:',good)
    print('operator order distribution:',dict(sorted(by_order.items())))
    for name,B in [('P3',path(3)),('P7',path(7)),('P15',path(15)),('C4',cycle(4)),('Q4',cube(4))]:
        bs=blocks(B); assert bs is not None
        assert check(B)
        print(name,'base-Jordan',bs,'order',3*(1<<max((2*s-1).bit_length() for s in bs)))
    print('PASS')
