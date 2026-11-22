#!/usr/bin/env python3
"""Exhaustive checks of rank-one partial-map commuting clique formulas.

Uses only Python 3 standard library. Adjacency is computed from direct
composition of partial functions, without invoking the proved criterion.
"""
from math import comb
from collections import Counter


def candidates(n):
    return [(mask,head) for head in range(n) for mask in range(1,1<<n)]


def compose(f,g,n):
    # f after g: partial map with domain g.domain if g.head in f.domain
    af,hf=f; ag,hg=g
    return ((ag,hf) if (af>>hg)&1 else (0,-1))


def all_cliques(adj):
    sizes=Counter({0:1})
    def grow(P,d):
        while P:
            b=P&-P; P^=b
            i=b.bit_length()-1
            sizes[d+1]+=1
            grow(P&adj[i],d+1)
    grow((1<<len(adj))-1,0)
    return sizes


def maximal_cliques(adj):
    sizes=Counter()
    def bron(P,X,d):
        if P==0 and X==0:
            sizes[d]+=1
            return
        union=P|X
        if union:
            best=max((u for u in range(len(adj)) if union>>u&1), key=lambda u:(P&adj[u]).bit_count())
            work=P&~adj[best]
        else:
            work=P
        while work:
            b=work&-work;work^=b
            u=b.bit_length()-1
            bron(P&adj[u],X&adj[u],d+1)
            P ^= b
            X |= b
    bron((1<<len(adj))-1,0,0)
    return sizes


def predicted(n):
    coeff=Counter({0:1})
    maxc=Counter()
    for h in range(1,n+1):
        d=n-h
        M=(1<<d)-1
        # F_h=(1+z)^M-1+2^d z
        F=[0]*max(2,M+1)
        for k in range(1,M+1):F[k]=comb(M,k)
        F[1]+=1<<d
        prod=[1]
        for _ in range(h):
            nxt=[0]*(len(prod)+len(F)-1)
            for i,a in enumerate(prod):
                for j,b in enumerate(F):
                    if a and b:nxt[i+j]+=a*b
            prod=nxt
        for k,c in enumerate(prod):
            if c:coeff[k]+=comb(n,h)*c
        maxc[h]+=comb(n,h)*((1<<h)-1)**d
        if d>0:
            for e in range(1,h+1):
                m=e*M+h-e
                maxc[m]+=comb(n,h)*comb(h,e)*2**(d*(h-e))
    return coeff,maxc


def check(n):
    vertices=candidates(n)
    N=len(vertices)
    adj=[0]*N
    for i,f in enumerate(vertices):
        for j,g in enumerate(vertices):
            commute=compose(f,g,n)==compose(g,f,n)
            if i!=j and commute:
                adj[i]|=1<<j
            if i!=j:
                A,a=f;B,b=g
                assert commute==(not(A>>b&1) and not(B>>a&1))
    for i in range(N):
        assert not(adj[i]>>i&1)
        for j in range(N):assert (adj[i]>>j&1)==(adj[j]>>i&1)
    got=all_cliques(adj)
    maximal=maximal_cliques(adj)
    exp,expmax=predicted(n)
    assert got==exp,(n,got,exp)
    assert maximal==expmax,(n,maximal,expmax)
    omega=max(k for k,v in got.items() if v)
    expected_omega=max(n,(1<<(n-1))-1)
    assert omega==expected_omega,(n,omega,expected_omega)
    print('n',n,'vertices',N,'cliques',sum(got.values()),'maximal',sum(maximal.values()),'omega',omega,'PASS')

if __name__=='__main__':
    for n in range(1,5):check(n)
    print('ALL_CHECKS_PASS')
