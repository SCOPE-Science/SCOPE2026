#!/usr/bin/env python3
"""Exact finite calculations for signed perfect matching convolution on GP(10,3).
Python 3 standard library only. Assertions are mathematical test conditions.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations

def gp_edges():
    n=10
    return sorted({tuple(sorted((i,(i+1)%n))) for i in range(n)}
                  | {tuple(sorted((10+i,10+(i+3)%n))) for i in range(n)}
                  | {(i,10+i) for i in range(n)})

def h52_edges():
    pairs=list(combinations(range(5),2))
    triples=list(combinations(range(5),3))
    return [(i,10+j) for i,p in enumerate(pairs)
            for j,t in enumerate(triples) if set(p).issubset(t)]

def enumerate_gp(E):
    adj=[[] for _ in range(20)]
    for j,(u,v) in enumerate(E):
        adj[u].append((v,j));adj[v].append((u,j))
    ans=[]
    def recur(available,edges):
        if not available:
            ans.append(edges);return
        u=(available & -available).bit_length()-1
        remain=available ^ (1<<u)
        for v,j in adj[u]:
            if (remain >> v)&1:
                recur(remain ^ (1<<v), edges | (1<<j))
    recur((1<<20)-1,0)
    return ans

def enumerate_bipartite(E):
    adj=[[] for _ in range(10)]
    for j,(u,v) in enumerate(E):
        assert 0<=u<10<=v<20
        adj[u].append((v-10,j))
    ans=[]
    def recur(row,chosen,edges):
        if row==10:
            ans.append(edges);return
        for col,j in adj[row]:
            if not (chosen>>col)&1:
                recur(row+1,chosen | (1<<col),edges | (1<<j))
    recur(0,0,0)
    return ans

def cotree(E):
    parent=list(range(20))
    def root(x):
        while parent[x]!=x:
            x=parent[x]
        return x
    skipped=[]
    for j,(u,v) in enumerate(E):
        a,b=root(u),root(v)
        if a!=b:parent[a]=b
        else:skipped.append(j)
    assert len(skipped)==11
    return skipped

def hadamard(data):
    a=data[:];p=1
    while p<len(a):
        for i in range(0,len(a),2*p):
            for j in range(i,i+p):
                a[j],a[j+p]=a[j]+a[j+p],a[j]-a[j+p]
        p*=2
    return a

def quotient_spectrum(E,matchings):
    C=cotree(E)
    hist=[0]*2048
    for m in matchings:
        q=sum((1<<k) for k,j in enumerate(C) if m>>j&1)
        hist[q]+=1
    W=hadamard(hist)
    return C,W

def count_moments(E,matchings):
    assert len(matchings)==60
    first=Counter(i for m in matchings for i in range(30) if m>>i&1)
    second=Counter((a,b) for m in matchings for a,b in combinations((j for j in range(30) if m>>j&1),2))
    assert len(first)==30 and set(first.values())=={20}
    assert all(v%2==0 for v in second.values())
    assert Counter(second.values())=={10:120,6:120,4:75,8:60}
    return first,second

def main():
    E=gp_edges(); E2=h52_edges()
    assert len(E)==len(E2)==30
    M=enumerate_gp(E)
    M2=enumerate_bipartite(E2)
    assert len(M)==len(M2)==60 and len(set(M))==len(set(M2))==60
    count_moments(E,M);count_moments(E2,M2)
    C,W=quotient_spectrum(E,M)
    C2,W2=quotient_spectrum(E2,M2)
    expected={4:1551,12:406,20:90,60:1}
    assert Counter(map(abs,W))==Counter(map(abs,W2))==expected
    assert all(x%8==4 for x in W+W2)
    assert 0 not in W and min(map(abs,W))==4 and max(map(abs,W))==60
    # Direct permanent checks for 2,048 Kruskal-gauge sign assignments,
    # independent of Walsh transform of the matching-incidence histogram.
    for mask in range(2048):
        selected=sum((1<<e) for k,e in enumerate(C2) if mask>>k&1)
        signed=sum((-1 if (m & selected).bit_count()%2 else 1) for m in M2)
        assert signed==W2[mask]
    # For an inverse convolution kernel, switchings at graph vertices
    # force its support to the 2^11 all-odd-degree edge subsets.
    inverse_integer=hadamard([60//w for w in W])
    L1=Fraction(sum(map(abs,inverse_integer)),60*2048)
    assert L1==Fraction(68,15)
    assert sum(bool(x) for x in inverse_integer)==1343
    assert sum(map(abs,inverse_integer))==557056
    # Certified inverse spectral multiplier satisfies W*(60/W)=60.
    assert all(w*(60//w)==60 for w in W)
    print('PASS: 60 perfect matchings in two independent graph models')
    print('PASS: 30 single-edge counts 20; pair-extension histogram',dict(sorted(Counter(Counter((a,b) for m in M for a,b in combinations((j for j in range(30) if m>>j&1),2)).values()).items())))
    print('PASS: 2048 signed permanents (H(5,2)) equal the independent GP(10,3) absolute spectrum')
    print('abs multiplier histogram',dict(sorted(expected.items())))
    print('all signed multipliers congruent to 4 modulo 8; minimum 4, maximum 60')
    print('inverse endpoint norm:',L1,'nonzero inverse entries',1343,'of 2048 possible')
    print('rank:',2**30,'Hilbert condition:',15)
if __name__=='__main__':main()
