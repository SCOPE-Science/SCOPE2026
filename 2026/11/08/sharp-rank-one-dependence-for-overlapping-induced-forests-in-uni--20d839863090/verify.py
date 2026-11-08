#!/usr/bin/env python3
"""Exact, independent checks of overlapping induced-edge counts in uniform labelled trees.

Uses Pruefer enumeration, not the spanning-tree determinant derivation.
Python standard library only. Output VERIFY_OK if every assertion succeeds.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial

CHECKS=0

def check(cond, msg=''):
    global CHECKS
    CHECKS+=1
    if not cond: raise AssertionError(msg)

def pmf_bin(m,p):
    return [Fraction(comb(m,j))*p**j*(1-p)**(m-j) for j in range(m+1)]

def prufer_edges(code,n):
    degrees=[1]*n
    for v in code: degrees[v]+=1
    edges=[]
    for v in code:
        u=next(i for i in range(n) if degrees[i]==1)
        edges.append((min(u,v),max(u,v)))
        degrees[u]-=1; degrees[v]-=1
    x,y=[i for i in range(n) if degrees[i]==1]
    edges.append((min(x,y),max(x,y)))
    return edges

def convolve2(F,G,H):
    # H is 2-by-2 probability distribution of paired Bernoullis
    ret=Counter()
    for i,fi in enumerate(F):
        for j,gj in enumerate(G):
            for x in range(2):
                for y in range(2):
                    ret[(i+x,j+y)]+=fi*gj*H[x][y]
    return ret

def predicted(n,a,b):
    p=Fraction(a,n); r=Fraction(b,n)
    h11=Fraction(a+b-1,n*n)
    H=[[1-p-r+h11,r-h11],[p-h11,h11]]
    F=pmf_bin(a-2,p); G=pmf_bin(b-2,r)
    return convolve2(F,G,H), F,G,H

def mass(c,k,l):return c.get((k,l),Fraction(0))

for n in range(3,8):
    # enumerate trees once for each n and collect all a,b with one shared vertex
    configs=[(a,b) for a in range(2,n+1) for b in range(2,n+1) if a+b-1<=n]
    obs={ab:Counter() for ab in configs}
    for code in product(range(n),repeat=n-2):
        edges=prufer_edges(code,n)
        for a,b in configs:
            A=set(range(a))
            B={0}|set(range(a,a+b-1))
            x=sum(u in A and v in A for u,v in edges)
            y=sum(u in B and v in B for u,v in edges)
            obs[a,b][x,y]+=1
    total=n**(n-2)
    for a,b in configs:
        model,F,G,H=predicted(n,a,b)
        check(sum(obs[a,b].values())==total,f'n={n}, a={a}, b={b}, count')
        for k in range(a):
            for l in range(b):
                check(Fraction(obs[a,b][k,l],total)==mass(model,k,l),f'joint n={n}, a={a}, b={b}, {k},{l}')
        p=Fraction(a,n); r=Fraction(b,n)
        Fa=pmf_bin(a-1,p); Gb=pmf_bin(b-1,r)
        sig=Fraction((a-1)*(b-1),n*n)
        for k in range(a):
            check(sum(mass(model,k,l) for l in range(b))==Fa[k],'marginal A')
        for l in range(b):
            check(sum(mass(model,k,l) for k in range(a))==Gb[l],'marginal B')
        check(sum(sum(row) for row in H)==1 and all(v>=0 for row in H for v in row),'table')
        mean_a=sum(k*Fa[k] for k in range(a))
        mean_b=sum(l*Gb[l] for l in range(b))
        covariance=sum((k-mean_a)*(l-mean_b)*mass(model,k,l) for k in range(a) for l in range(b))
        check(covariance==-sig,'covariance')
        d_tv=sum(abs(mass(model,k,l)-Fa[k]*Gb[l]) for k in range(a) for l in range(b))/2
        check(d_tv==2*sig*max(F)*max(G),'TV')
        for s in range(1,a):
            for t in range(1,b):
                tail_joint=sum(mass(model,k,l) for k in range(s,a) for l in range(t,b))
                tail_prod=sum(Fa[k] for k in range(s,a))*sum(Gb[l] for l in range(t,b))
                check(tail_joint-tail_prod==-sig*F[s-1]*G[t-1],'quadrant')
print('VERIFY_OK',CHECKS,'exact assertions; exhaustive Pruefer n=3..7')
