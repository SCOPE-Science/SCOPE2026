#!/usr/bin/env python3
"""Exact low-degree character classification for complete-graph Hamilton tours."""
from itertools import combinations
from math import comb, factorial

E = list(combinations(range(8), 2))
EXPECTED = {
  0: {(0,0,0,0): 'empty'},
  1: {(1,0,0,0): 'edge'},
  2: {(2,1,0,0): 'path of length two', (2,2,0,0): 'two disjoint edges'},
  3: {(3,3,0,0): 'triangle or three-star',
      (3,4,1,0): 'path of length three',
      (3,5,2,0): 'two-path plus disjoint edge',
      (3,6,4,0): 'three disjoint edges'},
  4: {(4,6,0,0): 'four-star',
      (4,7,2,0): 'triangle with pendant edge',
      (4,8,4,0): 'four-cycle or five-vertex T tree',
      (4,9,6,0): 'triangle and disjoint edge OR three-star and disjoint edge',
      (4,9,6,1): 'five-vertex path',
      (4,10,9,2): 'four-vertex path and disjoint edge',
      (4,10,8,2): 'two three-vertex paths',
      (4,11,12,4): 'three-vertex path and two edges',
      (4,12,16,8): 'four disjoint edges'}
}

def component_path_weight(sub):
    if not sub: return 0
    d = [0]*8; p=list(range(8))
    def root(x):
        while p[x]!=x: x=p[x]
        return x
    for u,v in sub:
        d[u]+=1; d[v]+=1
        if d[u]>2 or d[v]>2: return 0
        ru,rv = root(u),root(v)
        if ru==rv: return 0
        p[ru]=rv
    comps=len(set(root(v) for v in range(8) if d[v]))
    return 1 << (comps-1)

def signature(edges):
    c=[0,0,0,0]
    for k in range(1,len(edges)+1):
        c[k-1]=sum(component_path_weight(s) for s in combinations(edges,k))
    return tuple(c)

def value(n,c):
    assert n>=6
    w=factorial(n-1)//2
    for j, v in enumerate(c,1):
        if v: w+=((-2)**j)*v*factorial(n-j-1)
    return w

seen={}
for k in range(5):
    got=set(); counts={}
    for edges in combinations(E,k):
        sig=signature(edges);got.add(sig)
        counts[sig]=counts.get(sig,0)+1
    assert got==set(EXPECTED[k]), (k,got^set(EXPECTED[k]))
    assert sum(counts.values())==comb(28,k)
    seen[k]=counts
    print('support',k,'signature types',len(got),'K8 frequency count',sum(counts.values()))
zeros=[]
for n in range(6,18):
    for k in range(5):
        for c in EXPECTED[k]:
            if value(n,c)==0: zeros.append((n,k,c))
assert zeros==[(9,4,(4,9,6,0)),(10,3,(3,3,0,0))], zeros
# n >= 18: W >= ((n-1)!/2)*(1-4k/(n-1))>0 for k<=4.
assert 6300 == comb(9,3)*comb(6,2) + 9*comb(8,3)*comb(5,2)
assert 960 == comb(10,3) + 10*comb(9,3)
print('ALL ZERO CLASSES:',zeros)
print('n9 zero four-edge masks = 6300; n10 zero three-edge masks = 960')
for n in (6,7,8):
    mod=8 if n==6 else 16
    assert (factorial(n-1)//2)%mod==mod//2
    for j in range(1,min(3,n-1)+1):
        # If a path forest with j edges has b components, count is 2^(b-1)*(n-j-1)!.
        for b in range(1,j+1):
            assert ((-2)**j)*(1<<(b-1))*factorial(n-j-1)%mod==0
    print('n',n,'every Walsh coefficient congruent',mod//2,'mod',mod)
print('PASS')
