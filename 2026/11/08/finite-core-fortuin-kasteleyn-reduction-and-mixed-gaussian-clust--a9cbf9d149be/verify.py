#!/usr/bin/env python3
"""Finite-state consistency checks for fixed-hub random-cluster reduction.

All finite enumerations use rational arithmetic. The limiting random-cluster
conditional probability is checked separately; it does not replace the proof.
"""
from fractions import Fraction as F
from itertools import product
from math import exp


def components(n_vertices, pairs):
    p = list(range(n_vertices))
    def root(x):
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x
    for a, b in pairs:
        x, y = root(a), root(b)
        if x != y:
            p[x] = y
    return len({root(x) for x in range(n_vertices)})


def partition_direct(r, n, p, q):
    edges = [(i, r + j) for j in range(n) for i in range(r)]
    z = F(0)
    connected_01 = F(0)
    for bits in product((0, 1), repeat=len(edges)):
        chosen = [e for e, bit in zip(edges, bits) if bit]
        weight = q ** components(r+n, chosen)
        for k, bit in enumerate(bits):
            i = edges[k][0]
            weight *= p[i] if bit else 1-p[i]
        z += weight
        parent = list(range(r+n))
        for a,b in chosen:
            a0=a
            while parent[a0]!=a0: a0=parent[a0]
            b0=b
            while parent[b0]!=b0: b0=parent[b0]
            if a0!=b0: parent[a0]=b0
        def rt(a):
            while parent[a]!=a: a=parent[a]
            return a
        if rt(0)==rt(1): connected_01+=weight
    return z, connected_01


def partition_column(r, n, p, q):
    column = []
    for bits in product((0, 1), repeat=r):
        s = tuple(i for i, b in enumerate(bits) if b)
        w = q if not s else F(1)
        for i, b in enumerate(bits): w *= p[i] if b else 1-p[i]
        column.append((s,w))
    z = F(0)
    connected_01=F(0)
    for cols in product(column, repeat=n):
        pairs = []
        for s,w in cols:
            if len(s)>=2:
                pairs.extend((s[0],i) for i in s[1:])
        c=components(r,pairs)
        wt=q**c
        for _,w in cols: wt*=w
        z+=wt
        if components(r,pairs+[(0,1)])==c: connected_01+=wt
    return z,connected_01


def limiting_probability(q, lam):
    p=1-exp(-lam)
    probs={}
    pairs=[(0,1),(0,2),(1,2)]
    for bits in product((0,1),repeat=3):
        w=q**components(3,[e for e,b in zip(pairs,bits) if b])
        for b in bits: w*=p if b else 1-p
        probs[bits]=w
    z=sum(probs.values())
    return {bits:w/z for bits,w in probs.items()}


def run():
    assertions=0
    for n in (1,2,3):
        for q in (F(2),F(3,2),F(3,4)):
            p=(F(1,5),F(2,7),F(1,3))
            x=partition_direct(3,n,p,q)
            y=partition_column(3,n,p,q)
            assert x==y,(n,q,x,y)
            assertions+=2
    for q in (F(1),F(2),F(3,2),F(3,4)):
        for lam in (0.2,0.9,1.8):
            law=limiting_probability(float(q),lam)
            p=1-exp(-lam)
            v0=p/(p+float(q)*(1-p))
            v1=p
            cond0=sum(v for bits,v in law.items() if bits[0] and bits[1]==0 and bits[2]==0)/sum(v for bits,v in law.items() if bits[1]==0 and bits[2]==0)
            cond1=sum(v for bits,v in law.items() if bits[0] and bits[1]==1 and bits[2]==1)/sum(v for bits,v in law.items() if bits[1]==1 and bits[2]==1)
            assert abs(cond0-v0)<1e-12 and abs(cond1-v1)<1e-12
            assert abs(sum(law.values())-1)<1e-12
            assertions+=4
    print(f'PASS: {assertions} assertions, exact finite-state partition/connectivity and limiting triangle tests')


if __name__=='__main__': run()
