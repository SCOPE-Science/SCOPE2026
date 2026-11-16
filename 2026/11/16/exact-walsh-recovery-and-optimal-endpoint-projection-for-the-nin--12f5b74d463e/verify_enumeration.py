"""Exact finite Walsh census from edge-subset enumeration; Python 3 standard library."""
from itertools import combinations
from collections import Counter
from math import gcd

V=[(r,c) for r in range(3) for c in range(3)]
E=[]
for r in range(3):
    for c in range(3):
        if c<2:E.append(((r,c),(r,c+1)))
        if r<2:E.append(((r,c),(r+1,c)))
assert len(V)==9 and len(E)==12
index={v:i for i,v in enumerate(V)}
ends=[(index[u],index[v]) for u,v in E]

def is_tree(C):
    parent=list(range(9))
    def root(x):
        while x != parent[x]:x=parent[x]
        return x
    for e in C:
        a,b=ends[e];a,b=root(a),root(b)
        if a==b:return False
        parent[a]=b
    return len({root(i) for i in range(9)})==1

trees=[sum(1<<e for e in C) for C in combinations(range(12),8) if is_tree(C)]
assert len(trees)==192
edge_degrees=[sum((t>>e)&1 for t in trees) for e in range(12)]
assert Counter(edge_degrees)==Counter({136:8,112:4})
F=[0]*4096
for t in trees:F[t]+=1

def fwht(a):
    h=1
    while h<len(a):
        for start in range(0,len(a),2*h):
            for k in range(start,start+h):
                x,y=a[k],a[k+h];a[k],a[k+h]=x+y,x-y
        h*=2
    return a
fwht(F)
EXPECT={0:1186,4:1536,8:496,12:320,16:176,20:64,24:48,28:64,32:68,36:64,40:16,64:24,72:16,80:16,192:2}
assert Counter(map(abs,F))==EXPECT
assert all(x%4==0 for x in F)
assert F[116]==4 and F[47]==0
assert min(abs(x) for x in F if x)==4
support=[int(x!=0) for x in F]
fwht(support)
assert sum(map(abs,support))==40976
assert support[0]==2910
print('PASS edge enumeration / integer Walsh / 15-value histogram / projection norm',sum(map(abs,support)),'/4096')
