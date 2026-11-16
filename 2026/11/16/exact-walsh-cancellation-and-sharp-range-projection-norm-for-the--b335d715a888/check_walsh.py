#!/usr/bin/env python3
"""Exact 512-character Walsh certificate for the 4 by 4 domino family."""
from collections import Counter
from fractions import Fraction

# Vertices r*4+c; edges ordered at each vertex: right, then down.
E=[]
for r in range(4):
    for c in range(4):
        v=4*r+c
        if c<3: E.append((v,v+1))
        if r<3: E.append((v,v+4))
assert len(E)==24

# The edge order defines a spanning tree by Kruskal's rule.
parent=list(range(16))
def find(u):
    while parent[u]!=u:
        u=parent[u]
    return u
C=[]
for j,(u,v) in enumerate(E):
    a,b=find(u),find(v)
    if a==b: C.append(j)
    else: parent[a]=b
assert C==[7,9,11,14,16,18,21,22,23]

inc=[[] for _ in range(16)]
for j,(u,v) in enumerate(E):
    inc[u].append((v,j));inc[v].append((u,j))

def list_matchings():
    out=[]
    def visit(used,mask):
        if used==65535:
            out.append(mask)
            return
        u=next(j for j in range(16) if not (used>>j&1))
        for v,e in inc[u]:
            if not used>>v&1:
                visit(used|(1<<u)|(1<<v), mask|(1<<e))
    visit(0,0)
    return out

matchings=list_matchings()
assert len(matchings)==len(set(matchings))==36
edge_usage=[sum((mask>>e)&1 for mask in matchings) for e in range(24)]
assert dict(Counter(edge_usage))=={6:8,12:8,18:8}
assert {e for e,v in enumerate(edge_usage) if v==18}=={0,1,4,6,15,20,21,23}

# Restriction to nine chords injects on the affine family of perfect matchings.
codes=[sum(((m>>e)&1)<<j for j,e in enumerate(C)) for m in matchings]
assert len(set(codes))==36

def hadamard(a):
    a=list(a)
    k=1
    while k<len(a):
        for p in range(0,len(a),2*k):
            for q in range(k):
                x,y=a[p+q],a[p+q+k]
                a[p+q]=x+y
                a[p+q+k]=x-y
        k*=2
    return a

f=[int(t in set(codes)) for t in range(512)]
W=hadamard(f)
absolute=dict(Counter(abs(x) for x in W))
expected={0:233,4:177,8:72,12:12,16:6,20:2,24:8,32:1,36:1}
assert absolute==expected
assert sum(x*x for x in W)==512*36
assert W[0]==36
assert min(abs(x) for x in W if x)==4
h=[int(x!=0) for x in W]
H=hadamard(h)
assert sum(abs(x) for x in H)==3698
assert Fraction(sum(abs(x) for x in H),512)==Fraction(1849,256)
assert sum(1 for t in range(512) if W[t]==0 and t.bit_count()==1)==2
print('PASS: 36 tilings, 512 exact Walsh sums, 233 zeros, 279 nonzeros, sharp endpoint 1849/256.')
